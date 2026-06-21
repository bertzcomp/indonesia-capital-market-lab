#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT_GUESS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_GUESS / "src"))

from alpha_research.news.intelligence_polars import build_news_event_intelligence_dataset, DEFAULT_WINDOWS


def parse_windows(s: str) -> list[int]:
    if not s:
        return DEFAULT_WINDOWS
    return [int(x.strip()) for x in s.split(",") if x.strip()]


def main() -> None:
    ap = argparse.ArgumentParser(description="Build News Event Intelligence Dataset from raw/pure_raw news using Polars.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--engine", default="polars", choices=["polars"])
    ap.add_argument("--news-source", default="raw", choices=["raw", "pure_raw"])
    ap.add_argument("--refresh-raw-news", action="store_true")
    ap.add_argument("--merge-existing-raw-news", action="store_true", default=False)
    ap.add_argument("--emiten-path", default="data/raw/emiten/listed_companies.json")
    ap.add_argument("--ohlcv-path", default=None)
    ap.add_argument("--no-ohlcv", action="store_true")
    ap.add_argument("--windows", default="1,3,5,7,14,30")
    ap.add_argument("--output-dir", default="data/news/event_intelligence")
    ap.add_argument("--build-report", action="store_true")
    ap.add_argument("--write-full-csv", action="store_true")
    args = ap.parse_args()

    result = build_news_event_intelligence_dataset(
        root=args.root,
        news_source=args.news_source,
        refresh_raw_news=args.refresh_raw_news,
        merge_existing_raw_news=args.merge_existing_raw_news,
        emiten_path=args.emiten_path,
        ohlcv_path=None if args.no_ohlcv else args.ohlcv_path,
        windows=parse_windows(args.windows),
        output_dir=args.output_dir,
        build_report=args.build_report,
        write_full_csv=args.write_full_csv,
    )
    print(json.dumps(result.__dict__, indent=2))


if __name__ == "__main__":
    main()
