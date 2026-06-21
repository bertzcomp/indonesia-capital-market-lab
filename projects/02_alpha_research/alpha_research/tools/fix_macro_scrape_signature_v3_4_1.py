#!/usr/bin/env python3
"""
Hotfix v3.4.1 for alpha_research macro builder.

Fixes a signature mismatch where _scrape_macro() is defined with root/start/end
but build_macro_features() calls it as _scrape_macro(start_date, end_date, ...).

Run from project root:
  python3 tools/fix_macro_scrape_signature_v3_4_1.py --root .
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
from datetime import datetime


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    p = root / "src" / "alpha_research" / "macro" / "builder.py"
    if not p.exists():
        raise FileNotFoundError(f"Cannot find macro builder: {p}")

    text = p.read_text(encoding="utf-8")
    original = text

    # Main expected broken call from v3.4:
    old = "_scrape_macro(start_date, end_date, coal_fill_method=coal_fill_method, bi_rate_path=bi_rate_path)"
    new = "_scrape_macro(root, start_date, end_date, coal_fill_method=coal_fill_method, bi_rate_path=bi_rate_path)"
    text = text.replace(old, new)

    # More tolerant regex fallback for minor spacing/line-wrap variants.
    pattern = re.compile(
        r"_scrape_macro\(\s*start_date\s*,\s*end_date\s*,\s*coal_fill_method\s*=\s*coal_fill_method\s*,\s*bi_rate_path\s*=\s*bi_rate_path\s*\)",
        flags=re.MULTILINE,
    )
    text = pattern.sub(new, text)

    # If the function definition accidentally lacks root but the internals expect it,
    # leave it alone; the observed error indicates the definition already has root.
    # This script intentionally avoids broad rewrites.

    if text == original:
        # Diagnose helpful snippets.
        hits = [line for line in text.splitlines() if "_scrape_macro" in line]
        print("No exact replacement was made. _scrape_macro occurrences:")
        for h in hits[:20]:
            print("  ", h)
        raise RuntimeError(
            "Could not apply hotfix automatically. Please inspect the occurrences above."
        )

    backup = p.with_suffix(p.suffix + f".bak_v3_4_1_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    shutil.copy2(p, backup)
    p.write_text(text, encoding="utf-8")
    print(f"Patched: {p}")
    print(f"Backup : {backup}")


if __name__ == "__main__":
    main()
