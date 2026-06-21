from __future__ import annotations

import argparse
import sys
from pathlib import Path

import polars as pl

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.io import list_table_files


def preview_file(fp: Path) -> dict:
    out = {"file": str(fp), "suffix": fp.suffix.lower(), "size_bytes": fp.stat().st_size if fp.exists() else None}
    try:
        if fp.suffix.lower() == ".csv":
            df = pl.read_csv(fp, infer_schema=False, n_rows=3, ignore_errors=True)
            out["columns"] = df.columns
            out["preview_rows"] = df.height
        elif fp.suffix.lower() == ".parquet":
            df = pl.read_parquet(fp, n_rows=3)
            out["columns"] = df.columns
            out["preview_rows"] = df.height
        elif fp.suffix.lower() == ".json":
            out["columns"] = ["json_file"]
    except Exception as exc:
        out["error"] = str(exc)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--financials", default="data/raw/financials")
    ap.add_argument("--keystats-ratios", default="data/raw/keystats/ratios")
    ap.add_argument("--keystats-quarterly", default="data/raw/keystats/quarterly")
    ap.add_argument("--keystats-dividends", default="data/raw/keystats/dividends")
    ap.add_argument("--insider", default="data/raw/insider_activity")
    args = ap.parse_args()
    root = Path(args.root)
    groups = {
        "financials": args.financials,
        "keystats_ratios": args.keystats_ratios,
        "keystats_quarterly": args.keystats_quarterly,
        "keystats_dividends": args.keystats_dividends,
        "insider_activity": args.insider,
    }
    for name, rel in groups.items():
        path = root / rel
        files = list_table_files(path, recursive=True)
        print(f"\n[{name}] {path}")
        print(f"exists={path.exists()} files={len(files)}")
        for fp in files[:10]:
            info = preview_file(fp)
            print(f"- {fp} | size={info.get('size_bytes')} | cols={info.get('columns')}")
        if len(files) > 10:
            print(f"... {len(files)-10} more files")


if __name__ == "__main__":
    main()
