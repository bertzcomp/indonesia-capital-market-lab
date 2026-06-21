from __future__ import annotations
from pathlib import Path
import json, shutil
import polars as pl
import pandas as pd

def read_table(path: str | Path) -> pl.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(p)
    suf = p.suffix.lower()
    if suf == ".parquet":
        return pl.read_parquet(p)
    if suf == ".csv":
        return pl.read_csv(p, infer_schema_length=10000, ignore_errors=True, try_parse_dates=False)
    if suf in {".xlsx", ".xls"}:
        pdf = pd.read_excel(p)
        return pl.from_pandas(pdf)
    raise ValueError(f"Unsupported table: {p}")

def write_json(path, obj):
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2, default=str), encoding="utf-8")

def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def safe_write_parquet(df: pl.DataFrame, path: str | Path) -> None:
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    if tmp.exists(): tmp.unlink()
    df.write_parquet(tmp)
    # validate
    _ = pl.read_parquet(tmp, n_rows=5)
    tmp.replace(p)

def safe_publish_dir(src_tmp: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.move(str(src_tmp), str(dst))
