from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.cleaning import (
    build_data_quality_report,
    clean_financials,
    clean_insider_activity,
    clean_keystats_dividends,
    clean_keystats_quarterly,
    clean_keystats_ratios,
)
from fae_polars.config import load_config


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--config", default="configs/default_config.json")
    ap.add_argument("--as-of-date", required=True)
    ap.add_argument("--financials", default="data/raw/financials")
    ap.add_argument("--keystats-ratios", default="data/raw/keystats/ratios")
    ap.add_argument("--keystats-quarterly", default="data/raw/keystats/quarterly")
    ap.add_argument("--keystats-dividends", default="data/raw/keystats/dividends")
    ap.add_argument("--insider", default="data/raw/insider_activity")
    args = ap.parse_args()
    root = Path(args.root)
    cfg = load_config(root / args.config)
    paths = {
        "financials": root / "data/interim/financials_clean.parquet",
        "keystats_ratios": root / "data/interim/keystats_ratios_clean.parquet",
        "keystats_quarterly": root / "data/interim/keystats_quarterly_clean.parquet",
        "keystats_dividends": root / "data/interim/keystats_dividends_clean.parquet",
        "insider_activity": root / "data/interim/insider_activity_clean.parquet",
    }
    print("[1/5] Cleaning financials with Polars...")
    clean_financials(root / args.financials, paths["financials"], cfg)
    print("[2/5] Cleaning keystats ratios with Polars...")
    clean_keystats_ratios(root / args.keystats_ratios, paths["keystats_ratios"], args.as_of_date)
    print("[3/5] Cleaning keystats quarterly with Polars...")
    clean_keystats_quarterly(root / args.keystats_quarterly, paths["keystats_quarterly"], args.as_of_date)
    print("[4/5] Cleaning keystats dividends with Polars...")
    clean_keystats_dividends(root / args.keystats_dividends, paths["keystats_dividends"])
    print("[5/5] Cleaning insider activity with Polars...")
    clean_insider_activity(root / args.insider, paths["insider_activity"])
    report = build_data_quality_report(paths, root / "reports/data_quality_report.json")
    print("Done. Data quality report:", root / "reports/data_quality_report.json")
    for k, v in report.items():
        print(f"  - {k}: rows={v.get('rows')} tickers={v.get('tickers')}")


if __name__ == "__main__":
    main()
