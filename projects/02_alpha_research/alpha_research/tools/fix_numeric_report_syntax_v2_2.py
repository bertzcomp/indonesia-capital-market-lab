#!/usr/bin/env python3
from __future__ import annotations

import argparse
import py_compile
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    args = ap.parse_args()

    root = Path(args.root).resolve()
    path = root / 'src' / 'alpha_research' / 'inference' / 'numeric_trade_report.py'
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding='utf-8')
    backup = path.with_suffix(path.suffix + '.bak_v2_2')
    backup.write_text(text, encoding='utf-8')

    # Fix the exact broken pattern introduced by v2.1:
    # f"... resistance_20d {_fmt_float(resistance_20, 0)}.""
    text2 = text.replace(
        'resistance_20d {_fmt_float(resistance_20, 0)}.""',
        'resistance_20d {_fmt_float(resistance_20, 0)}."',
    )

    # Additional defensive fixes for the same class of accidental trailing double quote.
    text2 = text2.replace(').""\n', ')."\n')
    text2 = text2.replace('}.""\n', '}."\n')
    text2 = text2.replace('}.""\r\n', '}."\r\n')

    changed = text2 != text
    path.write_text(text2, encoding='utf-8')

    try:
        py_compile.compile(str(path), doraise=True)
        compiled = True
        compile_error = None
    except Exception as e:
        compiled = False
        compile_error = repr(e)

    print({
        'path': str(path),
        'backup': str(backup),
        'changed': changed,
        'compiled': compiled,
        'compile_error': compile_error,
    })

    if not compiled:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
