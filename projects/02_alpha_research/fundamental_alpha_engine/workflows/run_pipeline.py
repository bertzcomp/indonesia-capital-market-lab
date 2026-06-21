from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print("\n$", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--as-of-date", required=True)
    ap.add_argument("--ohlcv", default=None)
    ap.add_argument("--sector", default=None)
    ap.add_argument("--train", action="store_true")
    ap.add_argument("--target", default="label_outperform_sector_60d")
    ap.add_argument("--top-n", type=int, default=50)
    ap.add_argument("--min-score", type=float, default=55.0)
    ap.add_argument("--include-avoid", action="store_true")
    ap.add_argument("--current-keystats-overlay", action="store_true", help="For current inference only: overlay latest keystats snapshot <= --as-of-date onto latest OHLCV row when OHLCV lags the snapshot date.")
    args = ap.parse_args()
    root = Path(args.root)
    py = sys.executable

    run([py, "workflows/01_clean_fundamental_data.py", "--root", str(root), "--as-of-date", args.as_of_date])
    cmd2 = [py, "workflows/02_build_features.py", "--root", str(root), "--as-of-date", args.as_of_date]
    if args.ohlcv:
        cmd2 += ["--ohlcv", args.ohlcv]
    if args.sector:
        cmd2 += ["--sector", args.sector]
    if args.current_keystats_overlay:
        cmd2 += ["--current-keystats-overlay"]
    run(cmd2)
    if args.ohlcv:
        cmd3 = [py, "workflows/03_build_labels.py", "--root", str(root), "--ohlcv", args.ohlcv]
        if args.sector:
            cmd3 += ["--sector", args.sector]
        run(cmd3)
    if args.train:
        if not args.ohlcv:
            raise SystemExit("--train requires --ohlcv because labels must be built first.")
        run([py, "workflows/04_train_model.py", "--root", str(root), "--target", args.target])
    cmd5 = [py, "workflows/05_generate_signals.py", "--root", str(root), "--as-of-date", args.as_of_date, "--top-n", str(args.top_n), "--min-score", str(args.min_score)]
    if args.include_avoid:
        cmd5 += ["--include-avoid"]
    if args.train:
        cmd5 += ["--model-dir", "models/fundamental_model"]
    run(cmd5)


if __name__ == "__main__":
    main()
