#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


def replace_in_function(text: str, func_name: str, old: str, new: str) -> str:
    pattern = rf"(^def {re.escape(func_name)}\([^\n]*\):\n)(.*?)(?=^def |\Z)"
    m = re.search(pattern, text, flags=re.M | re.S)
    if not m:
        return text
    head, body = m.group(1), m.group(2)
    body2 = body.replace(old, new)
    return text[:m.start()] + head + body2 + text[m.end():]


def patch_dashboard(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    original = text

    # 1) Make filter_numeric key-safe.
    text = re.sub(r"def\s+filter_numeric\(df\):", 'def filter_numeric(df, key_prefix="num"):', text)
    text = text.replace('key="num_search"', 'key=f"{key_prefix}_search"')
    text = text.replace('key="num_strategy"', 'key=f"{key_prefix}_strategy"')
    text = text.replace('key="num_quality"', 'key=f"{key_prefix}_quality"')
    text = text.replace('key="num_risk"', 'key=f"{key_prefix}_risk"')

    # 2) Ensure each page passes a unique prefix. Streamlit renders all tabs eagerly,
    # so widgets in different tabs still need unique keys.
    text = replace_in_function(
        text,
        "page_trade_plan",
        "filter_numeric(df)",
        'filter_numeric(df, "trade_plan")',
    )
    text = replace_in_function(
        text,
        "page_playbooks",
        "filter_numeric(df)",
        'filter_numeric(df, "playbooks")',
    )

    # 3) Make choose_ticker robust too if it has repeated generic keys.
    # Existing calls already often pass explicit keys, but these replacements are safe.
    text = text.replace('key="selected_ticker"', 'key="selected_ticker_main"')

    # 4) Silence Streamlit deprecation warnings where possible.
    text = text.replace('use_container_width=True', 'width="stretch"')
    text = text.replace('use_container_width=False', 'width="content"')

    # 5) Syntax check before writing.
    compile(text, str(path), "exec")

    changed = text != original
    if changed:
        backup = path.with_suffix(path.suffix + ".bak_v3_1_1")
        if not backup.exists():
            backup.write_text(original, encoding="utf-8")
        path.write_text(text, encoding="utf-8")
    return {"path": str(path), "changed": changed, "backup": str(path.with_suffix(path.suffix + ".bak_v3_1_1"))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    path = root / "dashboards" / "local_research_dashboard.py"
    if not path.exists():
        raise FileNotFoundError(path)
    print(patch_dashboard(path))


if __name__ == "__main__":
    main()
