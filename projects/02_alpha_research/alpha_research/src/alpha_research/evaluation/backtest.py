from __future__ import annotations

from pathlib import Path
import json
import random
import re
from collections import defaultdict
from typing import Iterable

import numpy as np
import polars as pl
from alpha_research.core.io import write_json

TARGET_TO_SCORE = {
    "label_brok_cont": "score_sm",
    "label_ara_tomorrow": "score_ara",
    "label_near_ara_tomorrow": "score_ara_near",
    "label_scalp": "score_scalp",
    "label_swing": "score_swing",
    "label_position": "score_position",
    "label_silent_accum_breakout": "score_mm_silent",
    "label_big_runner_30d": "score_mm_big",
    "label_momentum_5d": "score_momentum_5d",
    "label_momentum_10d": "score_momentum_10d",
    "label_momentum_20d": "score_momentum_20d",
}

# When more than one algo/model produces the same logical score, a primary alias
# is created from the best validation component so downstream scripts can keep
# using score_sm, score_ara, etc. These suffix columns remain available for audit.
COMPONENT_SCORE_RE = re.compile(r"^score_.+")


def _parse_run_ids(run_id: str | Iterable[str]) -> list[str]:
    if isinstance(run_id, (list, tuple, set)):
        raw = []
        for x in run_id:
            raw.extend(str(x).split(","))
    else:
        raw = str(run_id).split(",")
    out = [x.strip() for x in raw if x and x.strip()]
    if not out:
        raise ValueError("At least one run_id is required")
    return list(dict.fromkeys(out))


def _sanitize_name(x: str) -> str:
    x = str(x).strip().lower()
    x = re.sub(r"[^a-z0-9]+", "_", x)
    x = re.sub(r"_+", "_", x).strip("_")
    return x or "unknown"


def _prediction_files(root: Path, run_ids: list[str]) -> list[Path]:
    files: list[Path] = []
    for rid in run_ids:
        pred_root = root / "data/validation/predictions" / rid
        if pred_root.exists():
            files.extend(sorted(pred_root.glob("*/*/*/fold_*.parquet")))
    return sorted(files)


def _infer_meta_from_path(path: Path, run_id: str) -> dict:
    # Expected: data/validation/predictions/<run_id>/<family>/<algo>/<target>/fold_01.parquet
    parts = path.parts
    try:
        idx = parts.index(run_id)
        family, algo, target = parts[idx + 1], parts[idx + 2], parts[idx + 3]
    except Exception:
        # Fallback from tail.
        family, algo, target = path.parts[-4], path.parts[-3], path.parts[-2]
    return {"run_id": run_id, "family": family, "algo": algo, "target": target}


def _first_scalar(df: pl.DataFrame, col: str, default=None):
    if col in df.columns and df.height:
        val = df[col][0]
        return default if val is None else val
    return default


def _model_meta_path(root: Path, run_id: str, family: str, algo: str, target: str, fold_name: str) -> Path:
    return root / "models/runs" / run_id / family / algo / target / fold_name / "meta.json"


def _safe_float(x, default=None):
    try:
        if x is None:
            return default
        v = float(x)
        if np.isnan(v) or np.isinf(v):
            return default
        return v
    except Exception:
        return default


def _component_selection_score(root: Path, run_id: str, family: str, algo: str, target: str) -> float | None:
    model_dir = root / "models/runs" / run_id / family / algo / target
    vals: list[float] = []
    if model_dir.exists():
        for meta_path in sorted(model_dir.glob("fold_*/meta.json")):
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                score = _safe_float(meta.get("selection_score"))
                if score is None:
                    metrics = meta.get("metrics", {}) or {}
                    score = (
                        _safe_float(metrics.get("daily_precision_at_5_mean"))
                        or _safe_float(metrics.get("avg_precision"))
                        or _safe_float(metrics.get("roc_auc"))
                    )
                if score is not None:
                    vals.append(score)
            except Exception:
                continue
    return float(np.mean(vals)) if vals else None


def _build_component_names(records: list[dict]) -> dict[tuple, str]:
    # A component is a unique run/family/algo/target/base_score combination.
    by_base: dict[str, list[tuple]] = defaultdict(list)
    for r in records:
        key = r["component_key"]
        if key not in by_base[r["base_score"]]:
            by_base[r["base_score"]].append(key)

    raw_names: dict[tuple, str] = {}
    for base, keys in by_base.items():
        if len(keys) == 1:
            raw_names[keys[0]] = base
            continue
        for key in keys:
            _, family, algo, target, _ = key
            # Include target to avoid collisions such as score_ara vs near ARA if mapping changes.
            suffix = "__".join([_sanitize_name(family), _sanitize_name(algo), _sanitize_name(target.replace("label_", ""))])
            raw_names[key] = f"{base}__{suffix}"

    # If two different run_ids still collide, append run id.
    counts: dict[str, int] = defaultdict(int)
    for name in raw_names.values():
        counts[name] += 1
    final: dict[tuple, str] = {}
    for key, name in raw_names.items():
        if counts[name] > 1:
            final[key] = f"{name}__run_{_sanitize_name(key[0])}"
        else:
            final[key] = name
    return final


def _normalise_prediction_df(df: pl.DataFrame, score_col: str) -> pl.DataFrame:
    out = df.select(["date", "ticker", "score"]).rename({"score": score_col})
    out = out.with_columns([
        pl.col("date").cast(pl.Date, strict=False).alias("date"),
        pl.col("ticker").cast(pl.Utf8).str.to_uppercase().alias("ticker"),
        pl.col(score_col).cast(pl.Float64, strict=False).alias(score_col),
    ])
    return out.drop_nulls(["date", "ticker"]).unique(["date", "ticker"], keep="last")


def build_validation_signal_panel(root, run_id, output=None):
    """Build an out-of-fold validation signal panel.

    This function is intentionally multi-run and multi-algo safe.

    Previous behavior joined every fold prediction independently. If several
    folds/algos shared the same logical score name (for example many
    sm_tracker algos all mapping to score_sm), Polars repeatedly generated
    score_sm_right and crashed. The correct approach is:

    1. Vertically concatenate all folds for the same component.
    2. Give each component a deterministic unique score column.
    3. Join components wide by date,ticker.
    4. Create canonical aliases such as score_sm from the best component.
    """
    root = Path(root)
    run_ids = _parse_run_ids(run_id)
    files = _prediction_files(root, run_ids)
    if not files:
        tried = [str(root / "data/validation/predictions" / rid) for rid in run_ids]
        raise FileNotFoundError(f"No prediction files found. Tried: {tried}")

    records: list[dict] = []
    for p in files:
        # Find run id in path.
        rid = next((x for x in run_ids if x in p.parts), run_ids[0])
        try:
            df0 = pl.read_parquet(p, n_rows=1)
        except TypeError:
            df0 = pl.read_parquet(p).head(1)
        inferred = _infer_meta_from_path(p, rid)
        family = str(_first_scalar(df0, "family", inferred["family"]))
        algo = str(_first_scalar(df0, "algo", inferred["algo"]))
        target = str(_first_scalar(df0, "target", inferred["target"]))
        base_score = TARGET_TO_SCORE.get(target, f"score_{target.replace('label_', '')}")
        component_key = (rid, family, algo, target, base_score)
        records.append({
            "path": p,
            "run_id": rid,
            "family": family,
            "algo": algo,
            "target": target,
            "base_score": base_score,
            "component_key": component_key,
        })

    name_map = _build_component_names(records)

    component_frames: dict[tuple, list[pl.DataFrame]] = defaultdict(list)
    component_meta: dict[tuple, dict] = {}
    for r in records:
        key = r["component_key"]
        score_col = name_map[key]
        df = pl.read_parquet(r["path"])
        component_frames[key].append(_normalise_prediction_df(df, score_col))
        if key not in component_meta:
            sel = _component_selection_score(root, r["run_id"], r["family"], r["algo"], r["target"])
            component_meta[key] = {**{k: r[k] for k in ["run_id", "family", "algo", "target", "base_score"]}, "score_col": score_col, "selection_score_mean": sel}

    wide_frames: list[pl.DataFrame] = []
    for key, parts in component_frames.items():
        score_col = name_map[key]
        comp = pl.concat(parts, how="diagonal_relaxed").unique(["date", "ticker"], keep="last").sort(["date", "ticker"])
        # Defensive: only keep keys + one score column.
        comp = comp.select(["date", "ticker", score_col])
        wide_frames.append(comp)

    panel = wide_frames[0]
    for i, f in enumerate(wide_frames[1:], start=1):
        # Component score columns are unique by construction, but suffix is still set
        # defensively to avoid Polars default _right collisions if a future column leaks in.
        panel = panel.join(f, on=["date", "ticker"], how="outer", coalesce=True, suffix=f"__dup_{i}")

    # Create canonical aliases (score_sm, score_ara, ...) from best component if multiple components exist.
    by_base: dict[str, list[dict]] = defaultdict(list)
    for meta in component_meta.values():
        by_base[meta["base_score"]].append(meta)
    primary_aliases: dict[str, str] = {}
    for base, metas in by_base.items():
        if base in panel.columns:
            primary_aliases[base] = base
            continue
        # Prefer highest average selection score. If unavailable, deterministic lexical fallback.
        metas_sorted = sorted(
            metas,
            key=lambda m: ((m.get("selection_score_mean") is not None), m.get("selection_score_mean") if m.get("selection_score_mean") is not None else -1e18, m["score_col"]),
            reverse=True,
        )
        chosen = metas_sorted[0]["score_col"]
        panel = panel.with_columns(pl.col(chosen).alias(base))
        primary_aliases[base] = chosen

    # Attach realized returns and filters.
    labeled_path = root / "data/datasets/training/full_labeled.parquet"
    if labeled_path.exists():
        labeled = pl.read_parquet(labeled_path).with_columns([
            pl.col("date").cast(pl.Date, strict=False).alias("date"),
            pl.col("ticker").cast(pl.Utf8).str.to_uppercase().alias("ticker"),
        ])
        keep = [c for c in [
            "date", "ticker", "close", "traded_value_proxy", "has_broksum", "broker_value_anomaly_flag",
            "rank1_buyer", "fwd_ret_1d", "fwd_ret_2d", "fwd_ret_3d", "fwd_ret_5d", "fwd_ret_10d", "fwd_ret_20d", "fwd_ret_30d",
        ] if c in labeled.columns]
        lab = labeled.select(keep).unique(["date", "ticker"], keep="last")
        panel = panel.join(lab, on=["date", "ticker"], how="left", suffix="__label_dup")

    panel = panel.unique(["date", "ticker"], keep="last").sort(["date", "ticker"])
    out = Path(output) if output else root / "signals/validation/validation_signal_panel.parquet"
    out.parent.mkdir(parents=True, exist_ok=True)
    panel.write_parquet(out)

    component_list = sorted(component_meta.values(), key=lambda x: (x["base_score"], x["run_id"], x["family"], x["algo"], x["target"]))
    meta = {
        "run_ids": run_ids,
        "rows": panel.height,
        "cols": panel.width,
        "output": str(out),
        "score_cols": [c for c in panel.columns if c.startswith("score_")],
        "primary_aliases": primary_aliases,
        "components": component_list,
        "n_prediction_files": len(files),
    }
    write_json(out.with_suffix(".json"), meta)
    return meta


def _choose_ret_col(hold_days: int) -> str:
    available = [1, 2, 3, 5, 10, 20, 30]
    h = min(available, key=lambda x: abs(x - hold_days))
    return f"fwd_ret_{h}d"


def run_signal_backtest(panel_path, output_dir, score_col="score_sm", top_k=5, hold_days=5, min_score=None,
                        price_min=100, price_max=1000, min_traded_value=500_000_000, require_broksum=True,
                        exclude_broker_value_anomaly=False):
    panel_path = Path(panel_path)
    outdir = Path(output_dir); outdir.mkdir(parents=True, exist_ok=True)
    df = pl.read_parquet(panel_path).with_columns(pl.col("date").cast(pl.Date, strict=False))
    if score_col not in df.columns:
        available = [c for c in df.columns if c.startswith("score_")]
        raise ValueError(f"score_col not found: {score_col}. Available score columns: {available}")
    ret_col = _choose_ret_col(hold_days)
    if ret_col not in df.columns:
        raise ValueError(f"return column not found: {ret_col}")
    filt = (
        pl.col(score_col).is_not_null() &
        pl.col(ret_col).is_not_null() &
        (pl.col("close") >= price_min) & (pl.col("close") <= price_max) &
        (pl.col("traded_value_proxy").fill_null(0) >= min_traded_value)
    )
    if require_broksum and "has_broksum" in df.columns:
        filt = filt & (pl.col("has_broksum").fill_null(0) == 1)
    if exclude_broker_value_anomaly and "broker_value_anomaly_flag" in df.columns:
        filt = filt & (pl.col("broker_value_anomaly_flag").fill_null(0) == 0)
    if min_score is not None:
        filt = filt & (pl.col(score_col) >= float(min_score))
    cand = df.filter(filt)
    if cand.is_empty():
        trades = pl.DataFrame()
        metrics = {"n_trades": 0, "score_col": score_col}
    else:
        trades = cand.sort(["date", score_col], descending=[False, True]).group_by("date", maintain_order=True).head(top_k)
        trades = trades.with_columns(pl.col(ret_col).alias("trade_ret"))
        daily = trades.group_by("date").agg(pl.col("trade_ret").mean().alias("daily_ret")).sort("date")
        rets = trades["trade_ret"].drop_nulls().to_numpy()
        d = daily["daily_ret"].drop_nulls().to_numpy()
        pos = rets[rets > 0].sum() if len(rets) else 0
        neg = -rets[rets < 0].sum() if len(rets) else 0
        eq = np.cumprod(1 + d) if len(d) else np.array([])
        dd = (eq / np.maximum.accumulate(eq) - 1).min() if len(eq) else None
        metrics = {
            "n_trades": int(len(rets)),
            "n_days": int(len(d)),
            "avg_trades_per_day": float(len(rets) / len(d)) if len(d) else 0.0,
            "win_rate": float((rets > 0).mean()) if len(rets) else None,
            "avg_trade_ret": float(np.mean(rets)) if len(rets) else None,
            "median_trade_ret": float(np.median(rets)) if len(rets) else None,
            "profit_factor": float(pos / neg) if neg > 0 else None,
            "daily_total_return": float(eq[-1] - 1) if len(eq) else None,
            "daily_max_drawdown": float(dd) if dd is not None else None,
            "daily_sharpe": float(np.mean(d) / (np.std(d) + 1e-12) * np.sqrt(252)) if len(d) > 2 else None,
            "score_col": score_col,
            "top_k": top_k,
            "hold_days": hold_days,
            "return_col": ret_col,
            "min_score": min_score,
            "price_min": price_min,
            "price_max": price_max,
            "min_traded_value": min_traded_value,
            "require_broksum": require_broksum,
            "exclude_broker_value_anomaly": exclude_broker_value_anomaly,
        }
    if trades.width:
        trades.write_parquet(outdir / "trades.parquet")
        trades.write_csv(outdir / "trades.csv")
    write_json(outdir / "metrics.json", metrics)
    return metrics


def randomized_backtest_search(panel_path, output_dir, n_iter=100, seed=42):
    rng = random.Random(seed)
    df = pl.read_parquet(panel_path)
    # Include canonical aliases and component-specific scores such as score_sm__regime_hgb.
    score_cols = [c for c in df.columns if c.startswith("score_")]
    # Avoid duplicate backtests of diagnostic duplicate columns if any leaked in.
    score_cols = [c for c in score_cols if "__dup_" not in c]
    if not score_cols:
        raise ValueError("No score columns in panel")
    outdir = Path(output_dir); outdir.mkdir(parents=True, exist_ok=True)
    results = []
    for i in range(n_iter):
        params = {
            "score_col": rng.choice(score_cols),
            "top_k": rng.choice([1, 2, 3, 5, 7, 10, 15]),
            "hold_days": rng.choice([1, 2, 3, 5, 7, 10, 15, 20]),
            "min_score": rng.choice([None, 0.50, 0.55, 0.60, 0.65, 0.70]),
            "min_traded_value": rng.choice([500_000_000, 1_000_000_000, 2_000_000_000, 5_000_000_000]),
            "require_broksum": rng.choice([True, True, False]),
            "exclude_broker_value_anomaly": rng.choice([False, True]),
        }
        try:
            m = run_signal_backtest(panel_path, outdir / f"trial_{i:03d}", **params)
            results.append({**params, **m})
        except Exception as e:
            results.append({**params, "error": str(e)})
    write_json(outdir / "random_search_summary.json", results)
    return {"output_dir": str(outdir), "n_iter": n_iter, "results_path": str(outdir / "random_search_summary.json"), "score_cols": score_cols}


def forward_test(panel_path, output_dir, forward_start, **kwargs):
    df = pl.read_parquet(panel_path).with_columns(pl.col("date").cast(pl.Date, strict=False))
    from alpha_research.core.dates import parse_date_any
    fs = parse_date_any(forward_start)
    fwd = df.filter(pl.col("date") >= pl.lit(fs))
    outdir = Path(output_dir); outdir.mkdir(parents=True, exist_ok=True)
    tmp = outdir / "forward_panel.parquet"
    fwd.write_parquet(tmp)
    return run_signal_backtest(tmp, outdir, **kwargs)


def monte_carlo_from_trades(trades_path, output_dir, n_iter=5000, seed=42):
    rng = np.random.default_rng(seed)
    outdir = Path(output_dir); outdir.mkdir(parents=True, exist_ok=True)
    trades = pl.read_parquet(trades_path) if str(trades_path).endswith(".parquet") else pl.read_csv(trades_path)
    if "trade_ret" not in trades.columns:
        raise ValueError("trade_ret column is required")
    rets = trades["trade_ret"].drop_nulls().to_numpy()
    if len(rets) == 0:
        raise ValueError("no returns")
    finals = []
    maxdds = []
    for _ in range(n_iter):
        sample = rng.choice(rets, size=len(rets), replace=True)
        eq = np.cumprod(1 + sample)
        finals.append(float(eq[-1] - 1))
        maxdds.append(float((eq / np.maximum.accumulate(eq) - 1).min()))
    summary = {
        "n_iter": n_iter,
        "n_trades": int(len(rets)),
        "final_return_p05": float(np.quantile(finals, 0.05)),
        "final_return_p50": float(np.quantile(finals, 0.50)),
        "final_return_p95": float(np.quantile(finals, 0.95)),
        "max_drawdown_p05": float(np.quantile(maxdds, 0.05)),
        "max_drawdown_p50": float(np.quantile(maxdds, 0.50)),
        "max_drawdown_p95": float(np.quantile(maxdds, 0.95)),
        "prob_positive_return": float(np.mean(np.array(finals) > 0)),
    }
    write_json(outdir / "monte_carlo_summary.json", summary)
    return summary