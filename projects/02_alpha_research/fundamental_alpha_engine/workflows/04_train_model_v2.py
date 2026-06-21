from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.modeling import train_redesigned_models
from fae_polars.scorecard import score_panel


def main() -> None:
    ap = argparse.ArgumentParser(description="Train v5 redesigned multi-model alpha stack: return ranker, outperform classifier, downside-risk classifier.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--horizon", type=int, default=60)
    ap.add_argument("--rank-target", default=None)
    ap.add_argument("--classifier-target", default=None)
    ap.add_argument("--risk-target", default=None)
    ap.add_argument("--model-dir", default="models/fundamental_model_v2")
    ap.add_argument("--walkforward", action="store_true")
    ap.add_argument("--purge-days", type=int, default=60)
    args = ap.parse_args()
    root = Path(args.root)
    print("[1/2] Building scorecard components for training panel...")
    score_panel(root / "data/features/fundamental_training_panel.parquet", root / "data/features/fundamental_training_scorecard_panel.parquet")
    print("[2/2] Training redesigned model stack...")
    metrics = train_redesigned_models(
        root / "data/features/fundamental_training_scorecard_panel.parquet",
        root / args.model_dir,
        horizon=args.horizon,
        rank_target=args.rank_target,
        classifier_target=args.classifier_target,
        risk_target=args.risk_target,
        walkforward=args.walkforward,
        purge_days=args.purge_days,
    )
    print("Done. Model stack saved to:", root / args.model_dir)
    print("Feature count:", metrics.get("feature_count"))
    print("Keystats included:", metrics.get("keystats_included"))
    print("Score components included:", metrics.get("score_components_included"))
    print("Model diagnostics:", metrics.get("models"))


if __name__ == "__main__":
    main()
