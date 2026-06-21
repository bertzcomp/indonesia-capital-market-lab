from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.modeling import apply_model
from fae_polars.scorecard import score_panel
from fae_polars.signals import generate_signals


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--as-of-date", required=True)
    ap.add_argument("--top-n", type=int, default=50)
    ap.add_argument("--min-score", type=float, default=55.0)
    ap.add_argument("--include-avoid", action="store_true")
    ap.add_argument("--model-dir", default=None)
    args = ap.parse_args()
    root = Path(args.root)
    print("[1/3] Scoring panel with Polars scorecard...")
    score_panel(root / "data/features/fundamental_signal_panel.parquet", root / "data/features/fundamental_scorecard_panel.parquet")
    model_scored = None
    if args.model_dir:
        print("[2/3] Applying trained model...")
        model_scored = root / "data/features/fundamental_model_scored_panel.parquet"
        apply_model(root / "data/features/fundamental_scorecard_panel.parquet", root / args.model_dir, model_scored)
    else:
        print("[2/3] Skipping ML model; using scorecard only.")
    print("[3/3] Generating final signal file...")
    out = generate_signals(
        root / "data/features/fundamental_scorecard_panel.parquet",
        root / "data/signals/fundamental_signals.parquet",
        as_of_date=args.as_of_date,
        top_n=args.top_n,
        min_score=args.min_score,
        include_avoid=args.include_avoid,
        model_scored_path=model_scored,
    )
    print("Done. Signals rows:", out.height)
    print("Output:", root / "data/signals/fundamental_signals.parquet")
    print("CSV copy:", root / "data/signals/fundamental_signals.csv")


if __name__ == "__main__":
    main()
