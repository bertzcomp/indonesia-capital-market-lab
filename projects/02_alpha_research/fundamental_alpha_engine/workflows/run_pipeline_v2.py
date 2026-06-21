from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print("\n$", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="End-to-end v5 model-redesign pipeline.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--as-of-date", required=True)
    ap.add_argument("--ohlcv", required=True)
    ap.add_argument("--sector", default=None)
    ap.add_argument("--horizon", type=int, default=60)
    ap.add_argument("--model-dir", default="models/fundamental_model_v2")
    ap.add_argument("--score-mode", choices=["scorecard", "model", "hybrid"], default="hybrid")
    ap.add_argument("--mode", choices=["research_all", "tradable", "liquid", "strict_liquid"], default="research_all")
    ap.add_argument("--top-n", type=int, default=50)
    ap.add_argument("--min-score", type=float, default=55.0)
    ap.add_argument("--walkforward", action="store_true")
    ap.add_argument("--purge-days", type=int, default=60)
    ap.add_argument("--skip-clean", action="store_true")
    ap.add_argument("--skip-train", action="store_true")
    args = ap.parse_args()
    root = Path(args.root)
    py = sys.executable

    if not args.skip_clean:
        run([py, "workflows/01_clean_fundamental_data.py", "--root", str(root), "--as-of-date", args.as_of_date])
    cmd2 = [py, "workflows/02_build_features.py", "--root", str(root), "--ohlcv", args.ohlcv]
    if args.sector:
        cmd2 += ["--sector", args.sector]
    run(cmd2)
    cmd3 = [py, "workflows/03_build_labels.py", "--root", str(root), "--ohlcv", args.ohlcv]
    if args.sector:
        cmd3 += ["--sector", args.sector]
    run(cmd3)
    if not args.skip_train:
        cmd4 = [py, "workflows/04_train_model_v2.py", "--root", str(root), "--horizon", str(args.horizon), "--model-dir", args.model_dir]
        if args.walkforward:
            cmd4 += ["--walkforward", "--purge-days", str(args.purge_days)]
        run(cmd4)
    cmd5 = [
        py, "workflows/05_generate_signals_v2.py", "--root", str(root), "--as-of-date", args.as_of_date,
        "--model-dir", args.model_dir, "--score-mode", args.score_mode, "--mode", args.mode,
        "--top-n", str(args.top_n), "--min-score", str(args.min_score), "--save-named-copy",
    ]
    run(cmd5)


if __name__ == "__main__":
    main()
