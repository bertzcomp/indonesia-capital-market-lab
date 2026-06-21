from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

import polars as pl


def ensure_dir(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def _read_csv_text(fp: Path) -> pl.DataFrame:
    # Raw exports are intentionally read as text first. This prevents mixed int/string columns
    # such as insider price from failing during ingestion. Numeric conversion happens explicitly.
    return pl.read_csv(
        fp,
        infer_schema=False,
        ignore_errors=True,
        null_values=["", "-", "--", "nan", "NaN", "None", "null", "NULL"],
    ).with_columns(pl.lit(fp.name).alias("_source_file"))


def read_csv_many(paths: str | Path | Iterable[str | Path], recursive: bool = True) -> pl.DataFrame:
    if isinstance(paths, (str, Path)):
        p = Path(paths)
        if p.is_dir():
            files = sorted(p.rglob("*.csv") if recursive else p.glob("*.csv"))
        else:
            files = [p]
    else:
        files = []
        for x in paths:
            p = Path(x)
            if p.is_dir():
                files.extend(sorted(p.rglob("*.csv") if recursive else p.glob("*.csv")))
            else:
                files.append(p)
    frames: list[pl.DataFrame] = []
    for fp in files:
        if fp.exists() and fp.suffix.lower() == ".csv":
            try:
                frames.append(_read_csv_text(fp))
            except Exception as exc:  # keep pipeline running but make the bad file visible
                raise RuntimeError(f"Failed to read CSV file {fp}: {exc}") from exc
    if not frames:
        return pl.DataFrame()
    return pl.concat(frames, how="diagonal_relaxed")


def list_table_files(path: str | Path, recursive: bool = True) -> list[Path]:
    p = Path(path)
    if not p.exists():
        return []
    if p.is_file():
        return [p] if p.suffix.lower() in {".csv", ".parquet", ".json"} else []
    patterns = ["*.csv", "*.parquet", "*.json"]
    files: list[Path] = []
    for pat in patterns:
        files.extend(sorted(p.rglob(pat) if recursive else p.glob(pat)))
    return sorted(set(files))


def read_table(path: str | Path) -> pl.DataFrame:
    p = Path(path)
    if not p.exists() and p.suffix.lower() == ".parquet" and p.with_suffix(".csv").exists():
        p = p.with_suffix(".csv")
    if not p.exists():
        return pl.DataFrame()
    suffix = p.suffix.lower()
    if suffix == ".parquet":
        return pl.read_parquet(p)
    if suffix == ".csv":
        return pl.read_csv(p, infer_schema_length=10000, ignore_errors=True)
    if suffix == ".json":
        with open(p, "r", encoding="utf-8") as f:
            obj = json.load(f)
        if isinstance(obj, dict) and isinstance(obj.get("data"), list):
            return pl.from_dicts(obj["data"], infer_schema_length=10000)
        if isinstance(obj, list):
            return pl.from_dicts(obj, infer_schema_length=10000)
        if isinstance(obj, dict):
            return pl.from_dicts([obj], infer_schema_length=10000)
    raise ValueError(f"Unsupported table format: {p}")


def write_table(df: pl.DataFrame, path: str | Path, csv_copy: bool = False) -> Path:
    p = Path(path)
    ensure_dir(p.parent)
    if p.suffix.lower() == ".csv":
        df.write_csv(p)
        return p
    # Polars has strict schema before writing, which is useful for catching data issues earlier.
    df.write_parquet(p)
    if csv_copy:
        df.write_csv(p.with_suffix(".csv"))
    return p


def write_json(obj: object, path: str | Path) -> Path:
    p = Path(path)
    ensure_dir(p.parent)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, default=str)
    return p
