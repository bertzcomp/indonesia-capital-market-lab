#!/usr/bin/env python3
"""
Build Alpha Research news-event impact dataset.

This workflow intentionally replaces generic sentiment labeling with event-aware rows:
  article + ticker/scope + event_type + event_side + optional future OHLCV outcomes.

Example:
  python3 workflows/build_news_event_impact_dataset.py \
    --root . \
    --news-path data/news/kabarbursa_market.json \
    --news-path data/news/idxchannel_market.json \
    --emiten-path data/raw/listed_companies.json \
    --ohlcv-path data/raw_canonical/ohlcv.parquet
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from alpha_research.news.event_impact import BuildConfig, build_news_event_impact_dataset


def _resolve(root: Path, value: str | None) -> Path | None:
    if value is None:
        return None
    p = Path(value).expanduser()
    return p if p.is_absolute() else root / p


def _resolve_many(root: Path, values: list[str]) -> list[Path]:
    out = []
    for v in values:
        p = Path(v).expanduser()
        out.append(p if p.is_absolute() else root / p)
    return out


def _autodiscover_news(root: Path) -> list[Path]:
    candidates = []
    for base in [root / "data" / "news", root / "data" / "raw" / "news", root / "data" / "pure_raw" / "news"]:
        if base.exists():
            candidates.extend(sorted(base.glob("*.json")))
    return candidates


def _autodiscover_emiten(root: Path) -> Path | None:
    patterns = [
        "data/raw/listed_companies.json",
        "data/raw/emiten.json",
        "data/pure_raw/listed_companies.json",
        "data/raw_canonical/listed_companies.json",
        "data/raw/listed_companies.parquet",
    ]
    for pat in patterns:
        p = root / pat
        if p.exists():
            return p
    return None


def _autodiscover_ohlcv(root: Path) -> Path | None:
    patterns = [
        "data/raw_canonical/ohlcv.parquet",
        "data/raw_canonical/ohlcv.csv",
        "data/raw/ohlcv.parquet",
        "data/raw/ohlcv.csv",
        "data/features/history/base_features.parquet",
    ]
    for pat in patterns:
        p = root / pat
        if p.exists():
            return p
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description="Build event-aware news impact dataset for Alpha Research.")
    ap.add_argument("--root", default=".", help="Alpha Research project root")
    ap.add_argument("--news-path", action="append", default=[], help="News JSON file. Can be passed multiple times.")
    ap.add_argument("--emiten-path", default=None, help="IDX/listed-company metadata JSON. Auto-discovered if omitted.")
    ap.add_argument("--ohlcv-path", default=None, help="OHLCV parquet/csv. Auto-discovered if omitted unless --no-ohlcv.")
    ap.add_argument("--no-ohlcv", action="store_true", help="Build event store only; do not attach future return/volatility outcomes.")
    ap.add_argument("--output-dir", default=None, help="Output directory. Default: data/news/event_impact")
    ap.add_argument("--alpha-threshold", type=float, default=0.01, help="Bullish/bearish threshold for alpha label.")
    ap.add_argument("--vol-shock-threshold", type=float, default=1.50, help="Volatility shock label threshold.")
    args = ap.parse_args()

    root = Path(args.root).expanduser().resolve()
    news_paths = _resolve_many(root, args.news_path) if args.news_path else _autodiscover_news(root)
    if not news_paths:
        raise FileNotFoundError("No news JSON files found. Pass --news-path or place files under data/news/*.json")

    emiten_path = _resolve(root, args.emiten_path) if args.emiten_path else _autodiscover_emiten(root)
    if emiten_path is None:
        print("WARN: no emiten metadata found. Ticker extraction will be limited.")

    ohlcv_path = None
    if not args.no_ohlcv:
        ohlcv_path = _resolve(root, args.ohlcv_path) if args.ohlcv_path else _autodiscover_ohlcv(root)
        if ohlcv_path is None:
            print("WARN: no OHLCV found. Building event rows only; future outcomes will not be attached.")

    config = BuildConfig(
        root=root,
        news_paths=news_paths,
        emiten_path=emiten_path,
        ohlcv_path=ohlcv_path,
        output_dir=_resolve(root, args.output_dir) if args.output_dir else None,
        alpha_threshold=args.alpha_threshold,
        vol_shock_threshold=args.vol_shock_threshold,
    )
    meta = build_news_event_impact_dataset(config)
    print(json.dumps(meta, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
