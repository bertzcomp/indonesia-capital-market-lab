from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import polars as pl
from fae_polars.io import read_table


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--path", default="data/features/fundamental_signal_panel.parquet")
    ap.add_argument("--as-of-date", default=None)
    ap.add_argument("--cols", nargs="*", default=[
        "pe_ttm", "pbv", "ps_ttm", "ev_ebitda", "earnings_yield", "roe_ttm", "roa_ttm",
        "debt_to_equity", "current_ratio", "dividend_yield", "payout_ratio", "keystats_snapshot_date",
    ])
    args = ap.parse_args()
    root = Path(args.root)
    df = read_table(root / args.path)
    if df.is_empty():
        print("Empty dataframe:", root / args.path)
        return
    if args.as_of_date and "as_of_date" in df.columns:
        target = pl.lit(args.as_of_date).str.strptime(pl.Date, format="%Y-%m-%d", strict=False)
        df = df.filter(pl.col("as_of_date") <= target)
        latest = df.select(pl.col("as_of_date").max()).item()
        df = df.filter(pl.col("as_of_date") == latest)
        print("latest_panel_date <= requested:", latest)
    else:
        print("rows:", df.height)
    rows = []
    for c in args.cols:
        if c not in df.columns:
            rows.append({"column": c, "exists": False, "nonnull": None, "coverage": None})
            continue
        nonnull = df.select(pl.col(c).is_not_null().sum()).item()
        rows.append({"column": c, "exists": True, "nonnull": int(nonnull), "coverage": float(nonnull / max(df.height, 1))})
    print(pl.DataFrame(rows))


if __name__ == "__main__":
    main()
