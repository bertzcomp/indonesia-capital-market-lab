from __future__ import annotations
from pathlib import Path
from datetime import datetime
import json, joblib, random
import numpy as np
import polars as pl
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import roc_auc_score, average_precision_score, precision_score, recall_score, f1_score
from alpha_research.core.io import write_json, safe_write_parquet
from alpha_research.features.contract import get_feature_cols
from alpha_research.training.wrappers import RegimeSpecialistHGB, RankHGB

FAMILIES = {
    "multi_strategy_time": {"targets": ["label_scalp", "label_swing", "label_position"]},
    "sm_tracker": {"targets": ["label_brok_cont"]},
    "ara_predictor": {"targets": ["label_ara_tomorrow", "label_near_ara_tomorrow"]},
    "market_maker_accumulation": {"targets": ["label_silent_accum_breakout", "label_big_runner_30d"]},
    "momentum_ranker": {"targets": ["label_momentum_5d", "label_momentum_10d", "label_momentum_20d"]},
}

DEFAULT_PARAMS = {
    "hgb": {"max_iter": 220, "learning_rate": 0.05, "max_leaf_nodes": 31, "l2_regularization": 0.03, "min_samples_leaf": 25},
    "regime_hgb": {"max_iter": 220, "learning_rate": 0.05, "max_leaf_nodes": 31, "l2_regularization": 0.05, "min_samples_leaf": 25},
    "rank_hgb": {"max_iter": 240, "learning_rate": 0.04, "max_leaf_nodes": 31, "l2_regularization": 0.03, "min_samples_leaf": 20},
    "lgb": {"n_estimators": 350, "learning_rate": 0.03, "num_leaves": 31, "subsample": 0.85, "colsample_bytree": 0.85},
    "xgb": {"n_estimators": 350, "learning_rate": 0.03, "max_depth": 4, "subsample": 0.85, "colsample_bytree": 0.85},
}

SEARCH_SPACE = {
    "hgb": {
        "max_iter": [120, 180, 240, 320],
        "learning_rate": [0.025, 0.04, 0.06, 0.08],
        "max_leaf_nodes": [15, 31, 63],
        "l2_regularization": [0.0, 0.01, 0.03, 0.08],
        "min_samples_leaf": [15, 25, 40, 60],
    },
    "regime_hgb": {
        "max_iter": [140, 220, 320],
        "learning_rate": [0.025, 0.04, 0.06],
        "max_leaf_nodes": [15, 31, 63],
        "l2_regularization": [0.01, 0.05, 0.10],
        "min_samples_leaf": [20, 40, 60],
    },
    "rank_hgb": {
        "max_iter": [160, 240, 360],
        "learning_rate": [0.02, 0.035, 0.05, 0.07],
        "max_leaf_nodes": [15, 31, 63],
        "l2_regularization": [0.0, 0.02, 0.05],
        "min_samples_leaf": [15, 25, 50],
    },
    "lgb": {
        "n_estimators": [200, 350, 550],
        "learning_rate": [0.015, 0.03, 0.05],
        "num_leaves": [15, 31, 63],
        "subsample": [0.75, 0.85, 1.0],
        "colsample_bytree": [0.7, 0.85, 1.0],
    },
    "xgb": {
        "n_estimators": [200, 350, 550],
        "learning_rate": [0.015, 0.03, 0.05],
        "max_depth": [3, 4, 5],
        "subsample": [0.75, 0.85, 1.0],
        "colsample_bytree": [0.7, 0.85, 1.0],
    },
}


def _sample_params(algo: str, rng: random.Random) -> dict:
    space = SEARCH_SPACE.get(algo, {})
    base = dict(DEFAULT_PARAMS.get(algo, {}))
    for k, vals in space.items():
        base[k] = rng.choice(vals)
    return base


def _model(algo, seed, params=None):
    params = dict(params or DEFAULT_PARAMS.get(algo, {}))
    if algo == "hgb":
        return HistGradientBoostingClassifier(random_state=seed, **params)
    if algo == "regime_hgb":
        return RegimeSpecialistHGB(random_state=seed, **params)
    if algo == "rank_hgb":
        return RankHGB(random_state=seed, **params)
    if algo == "lgb":
        try:
            from lightgbm import LGBMClassifier
            return LGBMClassifier(random_state=seed, n_jobs=-1, class_weight="balanced", verbose=-1, **params)
        except Exception as e:
            raise ImportError(f"lightgbm unavailable: {e}")
    if algo == "xgb":
        try:
            from xgboost import XGBClassifier
            return XGBClassifier(random_state=seed, eval_metric="logloss", n_jobs=-1, **params)
        except Exception as e:
            raise ImportError(f"xgboost unavailable: {e}")
    raise ValueError(algo)


def _daily_precision_at_k(y, p, dates, k=5):
    if dates is None or len(y) == 0:
        return None
    import pandas as pd
    d = pd.DataFrame({"y": y, "p": p, "date": dates})
    vals = []
    for _, g in d.groupby("date"):
        if len(g) == 0:
            continue
        top = g.sort_values("p", ascending=False).head(k)
        if len(top):
            vals.append(float(top["y"].mean()))
    return float(np.mean(vals)) if vals else None


def _metrics(y, p, dates=None, threshold=0.5):
    pred = (p >= threshold).astype(int)
    out = {"n": float(len(y)), "positive_rate": float(np.mean(y)) if len(y) else None, "threshold": threshold}
    try: out["roc_auc"] = float(roc_auc_score(y, p))
    except Exception: out["roc_auc"] = None
    try: out["avg_precision"] = float(average_precision_score(y, p))
    except Exception: out["avg_precision"] = None
    for name, fn in [("precision", precision_score), ("recall", recall_score), ("f1", f1_score)]:
        try: out[name] = float(fn(y, pred, zero_division=0))
        except Exception: out[name] = None
    for k in [5, 10, 20, 50, 100, 200]:
        if len(y) >= k:
            out[f"precision_at_{k}"] = float(np.mean(y[np.argsort(-p)[:k]]))
        dp = _daily_precision_at_k(y, p, dates, k=k if k <= 20 else 20)
        if dp is not None and k <= 20:
            out[f"daily_precision_at_{k}_mean"] = dp
    return out


def _score_for_selection(metrics: dict, target: str):
    # Rank/event targets should prioritize daily top-k/average precision over 0.5 threshold metrics.
    if target in {"label_ara_tomorrow", "label_near_ara_tomorrow", "label_momentum_5d", "label_momentum_10d", "label_momentum_20d"}:
        return metrics.get("daily_precision_at_5_mean") or metrics.get("avg_precision") or -1
    return metrics.get("daily_precision_at_5_mean") or metrics.get("avg_precision") or metrics.get("roc_auc") or -1


def _fit_best_trial(algo, Xtr, ytr, Xv, yv, dates, seed, target, tune_trials=0):
    rng = random.Random(seed)
    trials = []
    if tune_trials and tune_trials > 0:
        for t in range(tune_trials):
            trials.append({"trial": t, "params": _sample_params(algo, rng)})
    else:
        trials.append({"trial": 0, "params": dict(DEFAULT_PARAMS.get(algo, {}))})
    best = None
    errors = []
    for tr in trials:
        try:
            m = _model(algo, seed + tr["trial"], tr["params"])
            m.fit(Xtr, ytr)
            p = m.predict_proba(Xv)[:, 1]
            met = _metrics(yv, p, dates)
            score = _score_for_selection(met, target)
            cand = {"model": m, "pred": p, "metrics": met, "params": tr["params"], "trial": tr["trial"], "selection_score": score}
            if best is None or score > best["selection_score"]:
                best = cand
        except Exception as e:
            errors.append({"trial": tr["trial"], "params": tr["params"], "error": str(e)})
    if best is None:
        raise RuntimeError(f"all trials failed for algo={algo}: {errors[:3]}")
    best["trial_errors"] = errors
    return best


def train_models(root, fold_set="quarterly", families=None, algos=None, seed=42, tune_trials=0):
    root = Path(root)
    families = families or list(FAMILIES)
    algos = algos or ["hgb"]
    fold_dir = root / "data/datasets/folds" / fold_set
    if not fold_dir.exists():
        raise FileNotFoundError(fold_dir)
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_run = root / "models/runs" / run_id
    out_run.mkdir(parents=True, exist_ok=True)
    pred_root = root / "data/validation/predictions" / run_id
    summary = []
    i = 1
    while (fold_dir / f"fold_{i:02d}_train.parquet").exists():
        tr = pl.read_parquet(fold_dir / f"fold_{i:02d}_train.parquet")
        va = pl.read_parquet(fold_dir / f"fold_{i:02d}_val.parquet")
        feature_cols = get_feature_cols(tr)
        for fam in families:
            if fam not in FAMILIES:
                summary.append({"fold": i, "family": fam, "status": "failed", "error": "unknown family"})
                continue
            for target in FAMILIES[fam]["targets"]:
                if target not in tr.columns or target not in va.columns:
                    summary.append({"fold": i, "family": fam, "target": target, "status": "skipped", "reason": "missing target"})
                    continue
                train = tr.filter(pl.col(target).is_not_null())
                val = va.filter(pl.col(target).is_not_null())
                if train.height < 100 or val.height < 20:
                    summary.append({"fold": i, "family": fam, "target": target, "status": "skipped", "reason": "too few rows", "train": train.height, "val": val.height})
                    continue
                ytr = train[target].to_numpy().astype(int)
                yv = val[target].to_numpy().astype(int)
                if len(np.unique(ytr)) < 2 or len(np.unique(yv)) < 2:
                    summary.append({"fold": i, "family": fam, "target": target, "status": "skipped", "reason": "single class"})
                    continue
                Xtr = train.select(feature_cols).fill_null(0).to_numpy()
                Xv = val.select(feature_cols).fill_null(0).to_numpy()
                dates = val["date"].to_list() if "date" in val.columns else None
                for algo in algos:
                    try:
                        best = _fit_best_trial(algo, Xtr, ytr, Xv, yv, dates, seed + i * 1000, target, tune_trials=tune_trials)
                    except Exception as e:
                        summary.append({"fold": i, "family": fam, "target": target, "algo": algo, "status": "failed", "error": str(e)})
                        continue
                    od = out_run / fam / algo / target / f"fold_{i:02d}"
                    od.mkdir(parents=True, exist_ok=True)
                    joblib.dump(best["model"], od / "model.pkl")
                    meta = {
                        "run_id": run_id,
                        "fold_set": fold_set,
                        "fold": i,
                        "family": fam,
                        "algo": algo,
                        "target": target,
                        "feature_cols": feature_cols,
                        "params": best["params"],
                        "tune_trials": tune_trials,
                        "selected_trial": best["trial"],
                        "selection_score": best["selection_score"],
                        "trial_errors": best.get("trial_errors", []),
                        "metrics": best["metrics"],
                    }
                    write_json(od / "meta.json", meta)
                    # Save OOF validation predictions for signal-panel/backtest/forward-test.
                    pr = val.select(["date", "ticker", target]).with_columns([
                        pl.Series("score", best["pred"]),
                        pl.lit(run_id).alias("run_id"),
                        pl.lit(fam).alias("family"),
                        pl.lit(algo).alias("algo"),
                        pl.lit(target).alias("target"),
                        pl.lit(i).alias("fold"),
                    ])
                    pred_path = pred_root / fam / algo / target / f"fold_{i:02d}.parquet"
                    pred_path.parent.mkdir(parents=True, exist_ok=True)
                    safe_write_parquet(pr, pred_path)
                    summary.append({"fold": i, "family": fam, "target": target, "algo": algo, "status": "ok", "params": best["params"], **best["metrics"]})
        i += 1
    write_json(out_run / "training_summary.json", {"run_id": run_id, "fold_set": fold_set, "families": families, "algos": algos, "tune_trials": tune_trials, "summary": summary})
    return {"run_id": run_id, "path": str(out_run), "prediction_path": str(pred_root), "n_records": len(summary)}
