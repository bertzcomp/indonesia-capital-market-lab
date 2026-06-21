from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DEFAULT_CONFIG: dict[str, Any] = {
    "engine": "polars",
    "available_date_lag_days": {"Quarterly": 60, "Annual": 120, "TTM": 7, "LTM": 7, "Interim YTD": 60},
    "insider_windows_days": [7, 14, 30, 60, 90, 180],
    "label_horizons_days": [20, 60, 120],
    "outperform_threshold": 0.05,
    "top_n_default": 50,
    "score_weights": {
        "quality": 0.20,
        "growth": 0.20,
        "valuation": 0.20,
        "insider": 0.15,
        "balance_sheet": 0.15,
        "dividend": 0.05,
        "liquidity": 0.05,
    },
}


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    if path:
        p = Path(path)
        if p.exists():
            with open(p, "r", encoding="utf-8") as f:
                user_cfg = json.load(f)
            # shallow merge with nested dict merge for common config blocks
            for k, v in user_cfg.items():
                if isinstance(v, dict) and isinstance(cfg.get(k), dict):
                    cfg[k].update(v)
                else:
                    cfg[k] = v
    return cfg
