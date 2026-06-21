#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT_GUESS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_GUESS / "src"))

from alpha_research.news.aggregation_polars import build_news_event_aggregates


def main() -> None:
    ap = argparse.ArgumentParser(description="Build event cluster, ticker-day, and market-day aggregate news features.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--input", default="data/news/event_intelligence/news_event_intelligence_dataset.parquet")
    ap.add_argument("--output-dir", default="data/news/event_intelligence/aggregates")
    args = ap.parse_args()
    root = Path(args.root)
    result = build_news_event_aggregates(root / args.input, root / args.output_dir)
    print(json.dumps(result.__dict__, indent=2))


if __name__ == "__main__":
    main()
