#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import polars as pl


def bootstrap_src(root: Path) -> None:
    src = root / "src"
    if src.exists() and str(src) not in sys.path:
        sys.path.insert(0, str(src))


def main() -> None:
    parser = argparse.ArgumentParser(description="Build event study report from news_event_intelligence_dataset.parquet")
    parser.add_argument("--root", default=".")
    parser.add_argument("--dataset", default="data/news/event_intelligence/news_event_intelligence_dataset.parquet")
    parser.add_argument("--output-dir", default="data/news/event_intelligence/report")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    bootstrap_src(root)
    from alpha_research.news.intelligence_polars import build_event_study

    dataset = root / args.dataset
    if dataset.suffix.lower() == ".parquet":
        df = pl.read_parquet(dataset)
    elif dataset.suffix.lower() == ".csv":
        df = pl.read_csv(dataset, try_parse_dates=True)
    else:
        raise ValueError(f"Unsupported dataset format: {dataset}")

    out_dir = root / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    study = build_event_study(df)
    out_path = out_dir / "event_study_by_event_type.csv"
    study.write_csv(out_path)
    print(json.dumps({"rows": study.height, "output": str(out_path)}, indent=2))


if __name__ == "__main__":
    main()
