#!/usr/bin/env python3
"""
Hotfix v2.1: Fix invalid conditional f-string format specifiers in
src/alpha_research/inference/numeric_trade_report.py.

Problem example:
    f"support_10d {support_10:.0f if support_10 else float('nan')}"

Python does not allow conditional logic inside the format specifier.
This patch adds a safe _fmt_float() helper and replaces known invalid
patterns with helper calls.

Run from project root:
    python3 tools/fix_numeric_report_format_v2_1.py --root .
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

HELPER = '''

# -----------------------------------------------------------------------------
# Numeric report formatting helpers
# -----------------------------------------------------------------------------
def _fmt_float(value, digits: int = 0, default: str = "n/a") -> str:
    """Format optional numeric values safely for narrative reports."""
    try:
        if value is None:
            return default
        # Handles numpy/pandas/polars NaN without importing numpy.
        v = float(value)
        if v != v or v == float("inf") or v == float("-inf"):
            return default
        return f"{v:.{int(digits)}f}"
    except Exception:
        return default


def _fmt_pct(value, digits: int = 2, default: str = "n/a") -> str:
    """Format optional decimal values as percent safely."""
    try:
        if value is None:
            return default
        v = float(value)
        if v != v or v == float("inf") or v == float("-inf"):
            return default
        return f"{v * 100:.{int(digits)}f}%"
    except Exception:
        return default
'''


def insert_helper(text: str) -> str:
    if "def _fmt_float(" in text:
        return text

    # Prefer inserting before the first internal helper/function used in report calc.
    markers = [
        "def _calc_trade_plan(",
        "def _safe_float(",
        "def _load_json(",
        "def build_numeric_trade_report(",
    ]
    for marker in markers:
        idx = text.find(marker)
        if idx != -1:
            return text[:idx] + HELPER + "\n" + text[idx:]

    # Fallback: append near top after imports by placing after last import block line.
    lines = text.splitlines(True)
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("import ") or line.startswith("from ") or line.strip() == "":
            insert_at = i + 1
        elif insert_at:
            break
    return "".join(lines[:insert_at]) + HELPER + "\n" + "".join(lines[insert_at:])


def replace_invalid_format_specs(text: str) -> str:
    # Exact known problematic fragment from the traceback.
    exact = (
        'f"latest close {close:.0f}, ATR14 {atr:.1f}, '
        "support_10d {support_10:.0f if support_10 else float('nan')}, "
        "resistance_20d {resistance_20:.0f if resistance_20 else float('nan')}."
    )
    fixed = (
        'f"latest close {_fmt_float(close, 0)}, ATR14 {_fmt_float(atr, 1)}, '
        'support_10d {_fmt_float(support_10, 0)}, '
        'resistance_20d {_fmt_float(resistance_20, 0)}."'
    )
    text = text.replace(exact, fixed)

    # Broader regex for cases like:
    # {support_10:.0f if support_10 else float('nan')}
    # {resistance_20:.1f if resistance_20 else float('nan')}
    pattern_same_var = re.compile(
        r"\{([A-Za-z_][A-Za-z0-9_]*):\.([0-9]+)f\s+if\s+\1\s+else\s+float\(['\"]nan['\"]\)\}"
    )
    text = pattern_same_var.sub(lambda m: f"{{_fmt_float({m.group(1)}, {m.group(2)})}}", text)

    # Also catch conditional expressions with 'is not None'.
    pattern_not_none = re.compile(
        r"\{([A-Za-z_][A-Za-z0-9_]*):\.([0-9]+)f\s+if\s+\1\s+is\s+not\s+None\s+else\s+[^\}]+\}"
    )
    text = pattern_not_none.sub(lambda m: f"{{_fmt_float({m.group(1)}, {m.group(2)})}}", text)

    # Make the simple close/atr formatting robust if the known sentence exists.
    text = text.replace("{close:.0f}", "{_fmt_float(close, 0)}")
    text = text.replace("{atr:.1f}", "{_fmt_float(atr, 1)}")
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    path = root / "src" / "alpha_research" / "inference" / "numeric_trade_report.py"
    if not path.exists():
        raise FileNotFoundError(path)

    original = path.read_text(encoding="utf-8")
    text = insert_helper(original)
    text = replace_invalid_format_specs(text)

    backup = path.with_suffix(path.suffix + ".bak_v2_1")
    backup.write_text(original, encoding="utf-8")

    changed = text != original
    if changed:
        path.write_text(text, encoding="utf-8")

    print({"path": str(path), "backup": str(backup), "changed": changed})


if __name__ == "__main__":
    main()
