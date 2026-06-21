#!/usr/bin/env python3
"""
Build labeled training / continual datasets from a feature store.

This workflow is intentionally path-aware so continual/challenger datasets do not
overwrite the baseline training dataset.

Legacy usage remains supported:
  python3 workflows/build_training_dataset.py --root . --feature-scope history --start-date ... --end-date ...

Continual usage:
  python3 workflows/build_training_dataset.py \
    --root . \
    --feature-path data/features/continual/q3_2024_to_2026_05_20/base_features.parquet \
    --output-dir data/datasets/continual/q3_2024_to_2026_04_30 \
    --start-date 2024-07-01 \
    --end-date 2026-04-30 \
    --as-of-date 2026-05-20 \
    --drop-unmatured-labels
"""
from __future__ import annotations

import argparse
import json
from datetime import date, datetime
from pathlib import Path
from typing import Any

import polars as pl


TARGETS = [
    "label_scalp",
    "label_swing",
    "label_position",
    "label_brok_cont",
    "label_ara_tomorrow",
    "label_silent_accum_breakout",
    "label_big_runner_30d",
    "label_momentum_5d",
    "label_momentum_10d",
    "label_momentum_20d",
]

HELPER_COLS = [
    "fwd_ret_1d",
    "fwd_ret_5d",
    "fwd_ret_10d",
    "fwd_ret_20d",
    "fwd_ret_30d",
    "fwd_rank_1d_pct",
    "fwd_rank_5d_pct",
    "fwd_rank_10d_pct",
    "fwd_rank_20d_pct",
]


def _parse_date(x: str | date | datetime | None) -> date | None:
    if x is None:
        return None
    if isinstance(x, datetime):
        return x.date()
    if isinstance(x, date):
        return x
    return date.fromisoformat(str(x)[:10])


def _resolve_feature_path(root: Path, feature_scope: str, feature_path: str | None) -> Path:
    if feature_path:
        p = Path(feature_path)
        return p if p.is_absolute() else root / p
    if feature_scope == "history":
        return root / "data" / "features" / "history" / "base_features.parquet"
    if feature_scope == "live":
        return root / "data" / "features" / "live" / "latest" / "base_features.parquet"
    # For custom/continual scope, force explicit feature path so we never guess wrong.
    raise ValueError("For feature_scope other than history/live, pass --feature-path explicitly.")


def _resolve_output_dir(root: Path, output_dir: str | None, feature_scope: str) -> Path:
    if output_dir:
        p = Path(output_dir)
        return p if p.is_absolute() else root / p
    if feature_scope == "history":
        return root / "data" / "datasets" / "training"
    if feature_scope == "live":
        return root / "data" / "datasets" / "live_training_debug"
    return root / "data" / "datasets" / feature_scope


def _normalize_keys(df: pl.DataFrame) -> pl.DataFrame:
    if "date" not in df.columns or "ticker" not in df.columns:
        raise ValueError("Feature store must contain date and ticker columns")
    return df.with_columns([
        pl.col("date").cast(pl.Date).alias("date"),
        pl.col("ticker").cast(pl.Utf8).str.strip_chars().str.to_uppercase().alias("ticker"),
    ]).sort(["ticker", "date"])


def _add_forward_returns(df: pl.DataFrame) -> pl.DataFrame:
    # Computed per ticker; if insufficient future observations exist, result remains null.
    exprs = []
    for h in [1, 5, 10, 20, 30]:
        exprs.append(((pl.col("close").shift(-h).over("ticker") / pl.col("close")) - 1.0).alias(f"fwd_ret_{h}d"))
    return df.with_columns(exprs)


def _add_rank_pct(df: pl.DataFrame) -> pl.DataFrame:
    exprs = []
    for h in [1, 5, 10, 20]:
        c = f"fwd_ret_{h}d"
        # descending rank / count. Lower pct means stronger forward return rank.
        exprs.append((pl.col(c).rank(method="average", descending=True).over("date") / pl.len().over("date")).alias(f"fwd_rank_{h}d_pct"))
    return df.with_columns(exprs)


def _label_from_rank(ret_col: str, rank_col: str, threshold: float = 0.20) -> pl.Expr:
    return (
        pl.when(pl.col(ret_col).is_null())
        .then(None)
        .when((pl.col(ret_col) > 0) & (pl.col(rank_col) <= threshold))
        .then(1)
        .otherwise(0)
        .cast(pl.Int8)
    )


def _add_labels(df: pl.DataFrame) -> pl.DataFrame:
    # Cross-sectional labels are used because these models are primarily rankers / daily selection engines.
    exprs = [
        _label_from_rank("fwd_ret_1d", "fwd_rank_1d_pct", 0.20).alias("label_scalp"),
        _label_from_rank("fwd_ret_5d", "fwd_rank_5d_pct", 0.20).alias("label_swing"),
        _label_from_rank("fwd_ret_20d", "fwd_rank_20d_pct", 0.20).alias("label_position"),
        _label_from_rank("fwd_ret_5d", "fwd_rank_5d_pct", 0.20).alias("label_momentum_5d"),
        _label_from_rank("fwd_ret_10d", "fwd_rank_10d_pct", 0.20).alias("label_momentum_10d"),
        _label_from_rank("fwd_ret_20d", "fwd_rank_20d_pct", 0.20).alias("label_momentum_20d"),
        (
            pl.when(pl.col("fwd_ret_1d").is_null())
            .then(None)
            .when(pl.col("fwd_ret_1d") >= 0.08)
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("label_ara_tomorrow")
        ),
        (
            pl.when(pl.col("fwd_ret_5d").is_null())
            .then(None)
            .when(
                (pl.col("fwd_ret_5d") > 0.02)
                & (pl.col("has_broksum").fill_null(0) == 1)
                & (pl.col("net_flow_ratio").fill_null(0) > 0)
            )
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("label_brok_cont")
        ),
        (
            pl.when(pl.col("fwd_ret_20d").is_null())
            .then(None)
            .when(
                (pl.col("fwd_ret_20d") >= 0.10)
                & (pl.col("has_broksum").fill_null(0) == 1)
                & (pl.col("rank1_same_buyer_streak").fill_null(0) >= 2)
            )
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("label_silent_accum_breakout")
        ),
        (
            pl.when(pl.col("fwd_ret_30d").is_null())
            .then(None)
            .when(pl.col("fwd_ret_30d") >= 0.20)
            .then(1)
            .otherwise(0)
            .cast(pl.Int8)
            .alias("label_big_runner_30d")
        ),
    ]
    return df.with_columns(exprs)


def _sanitize_numeric(df: pl.DataFrame) -> pl.DataFrame:
    exprs = []
    for c, dt in zip(df.columns, df.dtypes):
        if dt in (pl.Float32, pl.Float64):
            exprs.append(
                pl.when(pl.col(c).is_nan() | pl.col(c).is_infinite())
                .then(None)
                .otherwise(pl.col(c))
                .alias(c)
            )
    return df.with_columns(exprs) if exprs else df


def _target_stats(df: pl.DataFrame) -> dict[str, Any]:
    stats: dict[str, Any] = {}
    for c in TARGETS:
        if c not in df.columns:
            stats[c] = {"exists": False}
            continue
        s = df.select([
            pl.len().alias("rows"),
            pl.col(c).is_null().sum().alias("nulls"),
            (pl.col(c) == 0).sum().alias("zeros"),
            (pl.col(c) == 1).sum().alias("ones"),
        ]).to_dicts()[0]
        non_null = int(s["rows"] - s["nulls"])
        ones = int(s["ones"])
        s["positive_rate_non_null"] = (ones / non_null) if non_null else None
        stats[c] = {"exists": True, **s}
    return stats


def build_training_dataset(
    root: str | Path,
    feature_scope: str = "history",
    feature_path: str | None = None,
    output_dir: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    as_of_date: str | None = None,
    drop_unmatured_labels: bool = False,
    keep_helper_cols: bool = False,
) -> dict[str, Any]:
    root = Path(root).resolve()
    feature_file = _resolve_feature_path(root, feature_scope, feature_path)
    out_dir = _resolve_output_dir(root, output_dir, feature_scope)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not feature_file.exists():
        raise FileNotFoundError(feature_file)

    df = pl.read_parquet(feature_file)
    df = _normalize_keys(df)

    sdt = _parse_date(start_date) if start_date else None
    edt = _parse_date(end_date) if end_date else None
    if sdt:
        df = df.filter(pl.col("date") >= pl.lit(sdt))
    if edt:
        df = df.filter(pl.col("date") <= pl.lit(edt))

    if df.is_empty():
        raise ValueError(f"No feature rows after filtering. feature_file={feature_file}, start={start_date}, end={end_date}")

    df = _sanitize_numeric(df)
    df = _add_forward_returns(df)
    df = _add_rank_pct(df)
    df = _add_labels(df)

    if drop_unmatured_labels:
        # Drop only rows where every target is null. Per-target training should still drop nulls label-by-label.
        present_targets = [c for c in TARGETS if c in df.columns]
        if present_targets:
            any_label_present = None
            for c in present_targets:
                expr = pl.col(c).is_not_null()
                any_label_present = expr if any_label_present is None else (any_label_present | expr)
            df = df.filter(any_label_present)

    # Preserve helper columns by default? No: helper columns are label-construction artifacts and can leak future returns.
    if not keep_helper_cols:
        drop_cols = [c for c in HELPER_COLS if c in df.columns]
        if drop_cols:
            df = df.drop(drop_cols)

    out_path = out_dir / "full_labeled.parquet"
    df.write_parquet(out_path)

    feature_cols = [c for c in df.columns if c not in {"date", "ticker"} and not c.startswith("label_")]
    registry = {
        "feature_count": len(feature_cols),
        "feature_cols": feature_cols,
        "target_cols": [c for c in TARGETS if c in df.columns],
    }
    (out_dir / "feature_registry.json").write_text(json.dumps(registry, indent=2, default=str))

    meta = {
        "root": str(root),
        "feature_scope": feature_scope,
        "feature_path": str(feature_file),
        "output_dir": str(out_dir),
        "path": str(out_path),
        "start_date": str(start_date),
        "end_date": str(end_date),
        "as_of_date": str(as_of_date) if as_of_date else None,
        "drop_unmatured_labels": drop_unmatured_labels,
        "rows": df.height,
        "cols": df.width,
        "min_date": str(df.select(pl.col("date").min()).item()),
        "max_date": str(df.select(pl.col("date").max()).item()),
        "duplicate_ticker_date": int(df.select(pl.struct(["date", "ticker"]).is_duplicated().sum()).item()),
        "feature_count": len(feature_cols),
        "target_stats": _target_stats(df),
        "label_definitions_note": "Continual/challenger dataset labels are generated from forward close returns and cross-sectional ranks; rows lacking future observations remain null per target.",
    }
    (out_dir / "dataset_meta.json").write_text(json.dumps(meta, indent=2, default=str))
    return meta


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--feature-scope", default="history")
    ap.add_argument("--feature-path", default=None)
    ap.add_argument("--output-dir", default=None)
    ap.add_argument("--start-date", default=None)
    ap.add_argument("--end-date", default=None)
    ap.add_argument("--as-of-date", default=None)
    ap.add_argument("--drop-unmatured-labels", action="store_true")
    ap.add_argument("--keep-helper-cols", action="store_true")
    args = ap.parse_args()

    meta = build_training_dataset(
        root=args.root,
        feature_scope=args.feature_scope,
        feature_path=args.feature_path,
        output_dir=args.output_dir,
        start_date=args.start_date,
        end_date=args.end_date,
        as_of_date=args.as_of_date,
        drop_unmatured_labels=args.drop_unmatured_labels,
        keep_helper_cols=args.keep_helper_cols,
    )
    print(json.dumps(meta, indent=2, default=str))


if __name__ == "__main__":
    main()
