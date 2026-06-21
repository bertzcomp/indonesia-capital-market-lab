from __future__ import annotations
from pathlib import Path

def root_path(root) -> Path:
    return Path(root).expanduser().resolve()

def ensure_dirs(root):
    root = root_path(root)
    dirs = [
        "data/pure_raw", "data/raw", "data/raw_canonical", "data/features/history",
        "data/features/live", "data/features/macro", "data/datasets/training", "data/datasets/folds",
        "data/datasets/continual", "models/runs", "models/continual_runs", "signals/live",
        "signals/daily", "reports", "configs"
    ]
    for d in dirs:
        (root / d).mkdir(parents=True, exist_ok=True)
    return root
