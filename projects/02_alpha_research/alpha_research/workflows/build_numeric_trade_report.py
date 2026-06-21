#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from alpha_research.inference.numeric_trade_report import build_numeric_trade_report


def main() -> None:
    ap = argparse.ArgumentParser(description="Build strategy-aware numeric trading desk report")
    ap.add_argument("--root", default=".")
    ap.add_argument("--signal-dir", default=None)
    ap.add_argument("--target-date", default=None)
    ap.add_argument("--policy", default="configs/numeric_report_policy.json")
    ap.add_argument("--signal-policy", default="configs/signal_policy.json")
    ap.add_argument("--source-file", default="all_strategy_watchlist.csv")
    args = ap.parse_args()

    meta = build_numeric_trade_report(
        root=args.root,
        signal_dir=args.signal_dir,
        target_date=args.target_date,
        policy=args.policy,
        signal_policy=args.signal_policy,
        source_file=args.source_file,
    )
    print(json.dumps(meta, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
