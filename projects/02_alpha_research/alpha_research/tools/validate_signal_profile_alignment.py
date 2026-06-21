#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--registry", required=True)
    ap.add_argument("--policy", required=True)
    args = ap.parse_args()
    root = Path(args.root)
    reg = json.load(open(root / args.registry))
    pol = json.load(open(root / args.policy))
    comps = reg.get("components", {})
    enabled_comps = {k: v for k, v in comps.items() if v.get("enabled", True)}
    score_cols = []
    for name, s in pol.get("strategies", {}).items():
        if s.get("enabled", True):
            score_cols.append((name, s.get("score_col")))
    missing = [(name, score) for name, score in score_cols if score not in enabled_comps]
    print(json.dumps({
        "registry": args.registry,
        "policy": args.policy,
        "enabled_registry_components": list(enabled_comps.keys()),
        "enabled_policy_scores": score_cols,
        "missing_policy_scores_from_registry": missing,
        "ok": len(missing) == 0,
    }, indent=2))
    if missing:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
