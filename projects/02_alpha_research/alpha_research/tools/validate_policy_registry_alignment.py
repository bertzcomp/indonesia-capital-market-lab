#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from alpha_research.inference.policy_engine import collect_policy_score_cols, collect_registry_score_cols, load_json


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--registry", required=True)
    ap.add_argument("--policy", required=True)
    args = ap.parse_args()

    root = Path(args.root)
    registry_path = Path(args.registry)
    if not registry_path.is_absolute():
        registry_path = root / registry_path
    policy_path = Path(args.policy)
    if not policy_path.is_absolute():
        policy_path = root / policy_path

    registry = load_json(registry_path)
    policy = load_json(policy_path)
    policy_scores = collect_policy_score_cols(policy)
    registry_scores = collect_registry_score_cols(registry)
    missing = [c for c in policy_scores if c not in registry_scores]

    print(json.dumps({
        "policy_score_count": len(policy_scores),
        "registry_component_count": len(registry_scores),
        "policy_scores": policy_scores,
        "registry_scores": registry_scores,
        "missing_from_registry": missing,
    }, indent=2))


if __name__ == "__main__":
    main()
