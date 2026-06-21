from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.config import load_config
from fae_polars.labels import build_forward_labels, build_training_panel


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--config", default="configs/default_config.json")
    ap.add_argument("--ohlcv", required=True)
    ap.add_argument("--sector", default=None)
    ap.add_argument("--bad-drawdown-threshold", type=float, default=None)
    ap.add_argument("--takeprofit-threshold", type=float, default=None)
    args = ap.parse_args()
    root = Path(args.root)
    cfg = load_config(root / args.config)
    print("[1/2] Building forward labels with Polars...")
    build_forward_labels(
        root / args.ohlcv,
        root / "data/labels/forward_return_labels.parquet",
        cfg.get("label_horizons_days", [20, 60, 120]),
        threshold=float(cfg.get("outperform_threshold", 0.05)),
        sector_path=(root / args.sector) if args.sector else None,
        bad_drawdown_threshold=float(args.bad_drawdown_threshold if args.bad_drawdown_threshold is not None else cfg.get("bad_drawdown_threshold", 0.15)),
        takeprofit_threshold=float(args.takeprofit_threshold if args.takeprofit_threshold is not None else cfg.get("takeprofit_threshold", 0.20)),
    )
    print("[2/2] Building training panel with Polars...")
    build_training_panel(
        root / "data/features/fundamental_signal_panel.parquet",
        root / "data/labels/forward_return_labels.parquet",
        root / "data/features/fundamental_training_panel.parquet",
    )
    print("Done. Output:", root / "data/features/fundamental_training_panel.parquet")


if __name__ == "__main__":
    main()
