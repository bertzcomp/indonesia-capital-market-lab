#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from alpha_research.features.store import build_feature_store


def default_continual_output_dir(root: Path, start_date: str, end_date: str) -> Path:
    safe_start = str(start_date).replace('-', '_')
    safe_end = str(end_date).replace('-', '_')
    return root / 'data' / 'features' / 'continual' / f'{safe_start}_to_{safe_end}'


def main() -> None:
    p = argparse.ArgumentParser(
        description='Build contract-enforced feature store for history, live, or continual/challenger training.'
    )
    p.add_argument('--root', default='.', help='Project root')
    p.add_argument('--scope', required=True, choices=['history', 'live', 'continual'])
    p.add_argument('--start-date', required=True)
    p.add_argument('--end-date', required=True)
    p.add_argument('--output-dir', default=None, help='Optional explicit output directory. Recommended for continual scope.')
    p.add_argument('--no-macro', action='store_true', help='Do not auto-build macro if missing')
    args = p.parse_args()

    root = Path(args.root).resolve()

    output_dir = args.output_dir
    if args.scope == 'continual' and output_dir is None:
        output_dir = str(default_continual_output_dir(root, args.start_date, args.end_date))

    if args.scope == 'live' and args.output_dir:
        print('WARN: --output-dir is ignored for --scope live; live feature store is written to data/features/live/<end-date> and latest/.')

    meta = build_feature_store(
        root,
        args.start_date,
        args.end_date,
        args.scope,
        output_dir,
        build_macro_if_missing=not args.no_macro,
    )
    print(json.dumps(meta, indent=2, default=str))


if __name__ == '__main__':
    main()
