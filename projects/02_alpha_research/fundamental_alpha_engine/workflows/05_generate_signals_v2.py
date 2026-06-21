from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fae_polars.modeling import apply_redesigned_models
from fae_polars.scorecard import score_panel
from fae_polars.signals import generate_signals


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate v5 redesigned alpha signals using scorecard/model/hybrid scoring.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--as-of-date", required=True)
    ap.add_argument("--model-dir", default="models/fundamental_model_v2")
    ap.add_argument("--score-mode", choices=["scorecard", "model", "hybrid"], default="hybrid")
    ap.add_argument("--mode", choices=["research_all", "tradable", "liquid", "strict_liquid"], default="research_all")
    ap.add_argument("--min-avg-value-20d", type=float, default=None)
    ap.add_argument("--min-price", type=float, default=None)
    ap.add_argument("--max-volatility-20d", type=float, default=None)
    ap.add_argument("--top-n", type=int, default=50)
    ap.add_argument("--min-score", type=float, default=55.0)
    ap.add_argument("--include-avoid", action="store_true")
    ap.add_argument("--save-named-copy", action="store_true", help="Also save CSV/parquet copies with score mode and universe mode in the filename.")
    args = ap.parse_args()
    root = Path(args.root)
    print("[1/4] Scoring latest panel with scorecard components...")
    score_panel(root / "data/features/fundamental_signal_panel.parquet", root / "data/features/fundamental_scorecard_panel.parquet")
    print("[2/4] Applying redesigned model stack...")
    model_scored = root / "data/features/fundamental_model_v2_scored_panel.parquet"
    apply_redesigned_models(root / "data/features/fundamental_scorecard_panel.parquet", root / args.model_dir, model_scored)
    print("[3/4] Generating final signal file...")
    out_path = root / "data/signals/fundamental_signals_v2.parquet"
    out = generate_signals(
        root / "data/features/fundamental_scorecard_panel.parquet",
        out_path,
        as_of_date=args.as_of_date,
        top_n=args.top_n,
        min_score=args.min_score,
        include_avoid=args.include_avoid,
        model_scored_path=model_scored,
        mode=args.mode,
        min_avg_value_20d=args.min_avg_value_20d,
        score_mode=args.score_mode,
        min_price=args.min_price,
        max_volatility_20d=args.max_volatility_20d,
    )
    print("[4/4] Done. Signals rows:", out.height)
    print("Output:", out_path)
    print("CSV copy:", out_path.with_suffix(".csv"))
    if args.save_named_copy:
        suffix = f"_{args.score_mode}_{args.mode}_{args.as_of_date}"
        csv_src = out_path.with_suffix(".csv")
        pq_dest = root / f"data/signals/fundamental_signals_v2{suffix}.parquet"
        csv_dest = root / f"data/signals/fundamental_signals_v2{suffix}.csv"
        shutil.copyfile(out_path, pq_dest)
        if csv_src.exists():
            shutil.copyfile(csv_src, csv_dest)
        print("Named copies:", pq_dest, csv_dest)


if __name__ == "__main__":
    main()
