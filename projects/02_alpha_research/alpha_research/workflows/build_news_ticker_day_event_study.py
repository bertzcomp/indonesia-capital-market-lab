#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT_GUESS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_GUESS / "src"))

from alpha_research.news.event_study_polars import build_ticker_day_event_study


def main() -> None:
    ap = argparse.ArgumentParser(description="Build event study reports using ticker-day aggregate news features.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--input", default="data/news/event_intelligence/aggregates/ticker_day_news_features.parquet")
    ap.add_argument("--output-dir", default="data/news/event_intelligence/aggregates/report")
    ap.add_argument("--min-rows", type=int, default=30)
    args = ap.parse_args()
    root = Path(args.root)
    build_ticker_day_event_study(root / args.input, root / args.output_dir, min_rows=args.min_rows)
    print(f"Saved ticker-day event study to {root / args.output_dir}")


if __name__ == "__main__":
    main()
