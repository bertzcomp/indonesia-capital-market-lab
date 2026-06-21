#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    args = ap.parse_args()
    root = Path(args.root).resolve()
    p = root / 'dashboards' / 'local_research_dashboard.py'
    if not p.exists():
        raise FileNotFoundError(p)

    text = p.read_text(encoding='utf-8')
    original = text

    old1 = 'st.dataframe(num["risk_flags"].fillna("OK").value_counts().reset_index().rename(columns={"index": "risk_flags", "risk_flags": "count"}), hide_index=True, width="stretch")'
    new1 = 'st.dataframe(num["risk_flags"].fillna("OK").value_counts().rename_axis("risk_flags").reset_index(name="count"), hide_index=True, width="stretch")'

    old2 = 'st.dataframe(num["rank1_buyer"].fillna("UNKNOWN").value_counts().head(15).reset_index().rename(columns={"index": "rank1_buyer", "rank1_buyer": "count"}), hide_index=True, width="stretch")'
    new2 = 'st.dataframe(num["rank1_buyer"].fillna("UNKNOWN").value_counts().head(15).rename_axis("rank1_buyer").reset_index(name="count"), hide_index=True, width="stretch")'

    text = text.replace(old1, new1).replace(old2, new2)

    if text == original:
        # Fallback for minor formatting differences: insert a helper and replace by simpler line fragments if found.
        text = text.replace(
            'num["risk_flags"].fillna("OK").value_counts().reset_index().rename(columns={"index": "risk_flags", "risk_flags": "count"})',
            'num["risk_flags"].fillna("OK").value_counts().rename_axis("risk_flags").reset_index(name="count")'
        ).replace(
            'num["rank1_buyer"].fillna("UNKNOWN").value_counts().head(15).reset_index().rename(columns={"index": "rank1_buyer", "rank1_buyer": "count"})',
            'num["rank1_buyer"].fillna("UNKNOWN").value_counts().head(15).rename_axis("rank1_buyer").reset_index(name="count")'
        )

    changed = text != original
    if changed:
        backup = p.with_suffix(p.suffix + '.bak_v3_2_1')
        if not backup.exists():
            backup.write_text(original, encoding='utf-8')
        p.write_text(text, encoding='utf-8')

    print({
        'target': str(p),
        'backup': str(p.with_suffix(p.suffix + '.bak_v3_2_1')),
        'changed': changed,
    })


if __name__ == '__main__':
    main()
