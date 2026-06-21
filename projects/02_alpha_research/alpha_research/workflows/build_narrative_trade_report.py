#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from alpha_research.inference.narrative_report import build_narrative_trading_report


def main() -> None:
    p = argparse.ArgumentParser(description="Build narrative trading intelligence report from daily signal outputs.")
    p.add_argument("--root", default=".")
    p.add_argument("--signal-dir", default=None, help="Path to signals/daily/signal_<date> directory. If omitted, latest daily signal dir is used.")
    p.add_argument("--target-date", default=None, help="Optional target date, e.g. 2026-05-20, used to locate signal directory.")
    p.add_argument("--policy", default=None, help="Optional narrative policy JSON. Defaults to configs/narrative_policy.json if present.")
    args = p.parse_args()

    meta = build_narrative_trading_report(
        root=Path(args.root),
        signal_dir=args.signal_dir,
        target_date=args.target_date,
        policy_path=args.policy,
    )
    print(json.dumps(meta, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
