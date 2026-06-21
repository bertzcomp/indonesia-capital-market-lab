from __future__ import annotations
from pathlib import Path
from alpha_research.core.io import write_json

PREF = {
    "score_sm": ("sm_tracker", ["regime_hgb", "rank_hgb", "hgb", "lgb", "xgb"], "label_brok_cont"),
    "score_ara": ("ara_predictor", ["rank_hgb", "regime_hgb", "hgb", "lgb", "xgb"], "label_ara_tomorrow"),
    "score_scalp": ("multi_strategy_time", ["rank_hgb", "hgb", "regime_hgb", "lgb", "xgb"], "label_scalp"),
    "score_swing": ("multi_strategy_time", ["rank_hgb", "hgb", "regime_hgb", "lgb", "xgb"], "label_swing"),
    "score_position": ("multi_strategy_time", ["rank_hgb", "hgb", "regime_hgb", "lgb", "xgb"], "label_position"),
    "score_mm_silent": ("market_maker_accumulation", ["rank_hgb", "regime_hgb", "hgb", "lgb", "xgb"], "label_silent_accum_breakout"),
    "score_mm_big": ("market_maker_accumulation", ["rank_hgb", "regime_hgb", "hgb", "lgb", "xgb"], "label_big_runner_30d"),
    "score_momentum_5d": ("momentum_ranker", ["rank_hgb", "hgb", "regime_hgb", "lgb", "xgb"], "label_momentum_5d"),
    "score_momentum_10d": ("momentum_ranker", ["rank_hgb", "hgb", "regime_hgb", "lgb", "xgb"], "label_momentum_10d"),
    "score_momentum_20d": ("momentum_ranker", ["rank_hgb", "hgb", "regime_hgb", "lgb", "xgb"], "label_momentum_20d"),
}


def latest_run(root):
    runs = sorted((Path(root) / "models/runs").glob("*"))
    if not runs:
        raise FileNotFoundError("No model runs")
    return runs[-1].name


def build_registry(root, run_id="latest", output="configs/model_registry.json"):
    root = Path(root)
    run_id = latest_run(root) if run_id == "latest" else run_id
    comps = {}
    skipped = {}
    for score, (fam, algos, target) in PREF.items():
        found = False
        for a in algos:
            path = root / "models/runs" / run_id / fam / a / target
            if path.exists() and list(path.glob("fold_*/model.pkl")):
                comps[score] = {"enabled": True, "run_id": run_id, "family": fam, "algo": a, "target": target}
                found = True
                break
        if not found:
            skipped[score] = {"family": fam, "target": target, "tried_algos": algos}
    reg = {"version": "4.0", "run_id": run_id, "components": comps, "skipped_components": skipped}
    write_json(root / output, reg)
    return reg
