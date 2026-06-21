from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.modeling import train_model


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--target", default="label_outperform_sector_60d")
    ap.add_argument("--model-dir", default="models/fundamental_model")
    args = ap.parse_args()
    root = Path(args.root)
    metrics = train_model(root / "data/features/fundamental_training_panel.parquet", root / args.model_dir, args.target)
    print("Done. Model saved to:", root / args.model_dir)
    print("Metrics:", metrics)


if __name__ == "__main__":
    main()
