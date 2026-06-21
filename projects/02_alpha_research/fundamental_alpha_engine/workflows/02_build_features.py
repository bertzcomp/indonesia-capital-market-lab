from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.config import load_config
from fae_polars.features_financials import build_financial_features
from fae_polars.features_insider import build_insider_features
from fae_polars.features_keystats import build_keystats_features
from fae_polars.panel import build_signal_panel


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--config", default="configs/default_config.json")
    ap.add_argument("--as-of-date", default=None, help="Optional: make insider features for a single inference date.")
    ap.add_argument("--ohlcv", default=None)
    ap.add_argument("--sector", default=None)
    ap.add_argument("--current-keystats-overlay", action="store_true", help="For current inference only: overlay latest keystats snapshot <= --as-of-date onto latest OHLCV row when OHLCV lags the snapshot date.")
    args = ap.parse_args()
    root = Path(args.root)
    cfg = load_config(root / args.config)
    print("[1/4] Building financial features with Polars...")
    build_financial_features(root / "data/interim/financials_clean.parquet", root / "data/features/financial_features.parquet")
    print("[2/4] Building keystats features with Polars...")
    build_keystats_features(
        root / "data/interim/keystats_ratios_clean.parquet",
        root / "data/interim/keystats_quarterly_clean.parquet",
        root / "data/interim/keystats_dividends_clean.parquet",
        root / "data/features/keystats_features.parquet",
    )
    print("[3/4] Building insider features with Polars...")
    build_insider_features(
        root / "data/interim/insider_activity_clean.parquet",
        root / "data/features/insider_features.parquet",
        cfg.get("insider_windows_days", [7, 14, 30, 60, 90, 180]),
        as_of_date=args.as_of_date,
    )
    print("[4/4] Building signal panel with Polars...")
    build_signal_panel(
        root / "data/features/financial_features.parquet",
        root / "data/features/keystats_features.parquet",
        root / "data/features/insider_features.parquet",
        root / "data/features/fundamental_signal_panel.parquet",
        ohlcv_path=(root / args.ohlcv) if args.ohlcv else None,
        sector_path=(root / args.sector) if args.sector else None,
        inference_as_of_date=args.as_of_date,
        current_keystats_overlay=args.current_keystats_overlay,
    )
    print("Done. Output:", root / "data/features/fundamental_signal_panel.parquet")


if __name__ == "__main__":
    main()
