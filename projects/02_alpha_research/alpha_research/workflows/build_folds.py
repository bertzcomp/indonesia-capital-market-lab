#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import polars as pl

try:
    # Legacy/default project builder. Used when --dataset / --output-dir are not supplied.
    from alpha_research.validation.folds import build_folds as _legacy_build_folds
except Exception:  # pragma: no cover
    _legacy_build_folds = None


def _parse_date(x: str | date | datetime | None) -> date | None:
    if x is None:
        return None
    if isinstance(x, datetime):
        return x.date()
    if isinstance(x, date):
        return x
    return datetime.strptime(str(x)[:10], "%Y-%m-%d").date()


def _quarter_ranges(year: int) -> list[tuple[date, date, str]]:
    return [
        (date(year, 1, 1), date(year, 3, 31), f"{year}Q1"),
        (date(year, 4, 1), date(year, 6, 30), f"{year}Q2"),
        (date(year, 7, 1), date(year, 9, 30), f"{year}Q3"),
        (date(year, 10, 1), date(year, 12, 31), f"{year}Q4"),
    ]


def _year_ranges(year: int) -> list[tuple[date, date, str]]:
    return [(date(year, 1, 1), date(year, 12, 31), str(year))]


def _month_ranges(year: int) -> list[tuple[date, date, str]]:
    out: list[tuple[date, date, str]] = []
    for m in range(1, 13):
        start = date(year, m, 1)
        if m == 12:
            end = date(year, 12, 31)
        else:
            end = date(year, m + 1, 1) - timedelta(days=1)
        out.append((start, end, f"{year}-{m:02d}"))
    return out


def _periods(freq: str, first_year: int, last_year: int) -> list[tuple[date, date, str]]:
    periods: list[tuple[date, date, str]] = []
    for y in range(first_year, last_year + 1):
        if freq == "quarter":
            periods.extend(_quarter_ranges(y))
        elif freq == "year":
            periods.extend(_year_ranges(y))
        elif freq == "month":
            periods.extend(_month_ranges(y))
        else:
            raise ValueError(f"Unsupported freq={freq!r}; use year, quarter, or month.")
    return periods


def _ensure_date(df: pl.DataFrame) -> pl.DataFrame:
    if "date" not in df.columns:
        raise ValueError("Dataset must contain a 'date' column.")
    if df.schema["date"] == pl.Date:
        return df
    if df.schema["date"] in (pl.Datetime, pl.Datetime("ms"), pl.Datetime("us"), pl.Datetime("ns")):
        return df.with_columns(pl.col("date").dt.date().alias("date"))
    return df.with_columns(pl.col("date").cast(pl.Utf8).str.slice(0, 10).str.to_date("%Y-%m-%d", strict=False).alias("date"))


def _write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")


def build_custom_folds(
    dataset: str | Path,
    output_dir: str | Path,
    freq: str,
    fold_set: str,
    first_val_year: int,
    last_val_year: int,
    train_start: str | None,
    purge_days: int,
    embargo_days: int,
    min_train_rows: int = 1000,
    min_val_rows: int = 100,
) -> dict[str, Any]:
    dataset = Path(dataset).expanduser().resolve()
    output_dir = Path(output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    df = _ensure_date(pl.read_parquet(dataset))
    if "ticker" not in df.columns:
        raise ValueError("Dataset must contain a 'ticker' column.")

    # stable sort for deterministic folds
    df = df.sort(["date", "ticker"])

    ds_min = df.select(pl.col("date").min()).item()
    ds_max = df.select(pl.col("date").max()).item()
    train_start_date = _parse_date(train_start) or ds_min

    dup = df.select(pl.struct(["date", "ticker"]).is_duplicated().sum()).item()
    if dup:
        raise ValueError(f"Dataset is not unique on ['date','ticker']; duplicate rows={dup}")

    folds: list[dict[str, Any]] = []
    periods = _periods(freq, first_val_year, last_val_year)

    for val_start, val_end, period_label in periods:
        # Clip validation to available dataset date range.
        val_start_eff = max(val_start, ds_min)
        val_end_eff = min(val_end, ds_max)
        if val_start_eff > val_end_eff:
            continue

        train_end_eff = val_start_eff - timedelta(days=purge_days + 1)
        if train_start_date > train_end_eff:
            continue

        train = df.filter((pl.col("date") >= pl.lit(train_start_date)) & (pl.col("date") <= pl.lit(train_end_eff)))
        val = df.filter((pl.col("date") >= pl.lit(val_start_eff)) & (pl.col("date") <= pl.lit(val_end_eff)))

        if train.height < min_train_rows or val.height < min_val_rows:
            continue

        fold_no = len(folds) + 1
        fold_id = f"fold_{fold_no:02d}_{period_label}"
        train_path = output_dir / f"{fold_id}_train.parquet"
        val_path = output_dir / f"{fold_id}_val.parquet"

        train.write_parquet(train_path)
        val.write_parquet(val_path)

        fold_meta = {
            "fold": fold_no,
            "fold_id": fold_id,
            "period": period_label,
            "freq": freq,
            "train_start": train.select(pl.col("date").min()).item(),
            "train_end": train.select(pl.col("date").max()).item(),
            "val_start": val.select(pl.col("date").min()).item(),
            "val_end": val.select(pl.col("date").max()).item(),
            "raw_val_start": val_start,
            "raw_val_end": val_end,
            "purge_days": purge_days,
            "embargo_days": embargo_days,
            "train_rows": train.height,
            "val_rows": val.height,
            "train_path": str(train_path),
            "val_path": str(val_path),
        }
        _write_json(output_dir / f"{fold_id}.json", fold_meta)
        folds.append(fold_meta)

    manifest = {
        "fold_set": fold_set,
        "freq": freq,
        "dataset": str(dataset),
        "output_dir": str(output_dir),
        "dataset_min_date": ds_min,
        "dataset_max_date": ds_max,
        "train_start": train_start_date,
        "first_val_year": first_val_year,
        "last_val_year": last_val_year,
        "purge_days": purge_days,
        "embargo_days": embargo_days,
        "n_folds": len(folds),
        "folds": folds,
    }

    _write_json(output_dir / "fold_manifest.json", manifest)
    _write_json(output_dir / f"fold_meta_{fold_set}.json", manifest)
    return manifest


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--freq", default="year", choices=["year", "quarter", "month"])
    ap.add_argument("--fold-set", default="yearly")
    ap.add_argument("--first-val-year", type=int, required=True)
    ap.add_argument("--last-val-year", type=int, required=True)
    ap.add_argument("--train-start", default=None)
    ap.add_argument("--purge-days", type=int, default=30)
    ap.add_argument("--embargo-days", type=int, default=5)

    # Continual/custom dataset support.
    ap.add_argument("--dataset", default=None, help="Custom labeled dataset parquet. Use this for continual/challenger folds.")
    ap.add_argument("--output-dir", default=None, help="Fold output directory. Required with --dataset.")
    ap.add_argument("--min-train-rows", type=int, default=1000)
    ap.add_argument("--min-val-rows", type=int, default=100)

    a = ap.parse_args()

    root = Path(a.root).resolve()

    if a.dataset or a.output_dir:
        if not a.dataset or not a.output_dir:
            raise SystemExit("--dataset and --output-dir must be supplied together.")
        meta = build_custom_folds(
            dataset=(root / a.dataset) if not Path(a.dataset).is_absolute() else Path(a.dataset),
            output_dir=(root / a.output_dir) if not Path(a.output_dir).is_absolute() else Path(a.output_dir),
            freq=a.freq,
            fold_set=a.fold_set,
            first_val_year=a.first_val_year,
            last_val_year=a.last_val_year,
            train_start=a.train_start,
            purge_days=a.purge_days,
            embargo_days=a.embargo_days,
            min_train_rows=a.min_train_rows,
            min_val_rows=a.min_val_rows,
        )
        print(json.dumps(meta, indent=2, default=str))
        return

    if _legacy_build_folds is None:
        raise SystemExit("Legacy alpha_research.validation.folds.build_folds is unavailable. Use --dataset and --output-dir.")

    # Preserve legacy behavior for baseline datasets.
    print(json.dumps(
        _legacy_build_folds(
            a.root,
            a.freq,
            a.fold_set,
            a.first_val_year,
            a.last_val_year,
            a.train_start or "2016-01-01",
            a.purge_days,
            a.embargo_days,
        ),
        indent=2,
        default=str,
    ))


if __name__ == "__main__":
    main()
