from __future__ import annotations

import json
from pathlib import Path
from typing import Optional, Sequence

import numpy as np
import pandas as pd


def _read_dataset(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() == ".parquet":
        return pd.read_parquet(path)
    return pd.read_csv(path)


def _safe_rate(s: pd.Series) -> float:
    s = pd.to_numeric(s, errors="coerce")
    if s.notna().sum() == 0:
        return float("nan")
    return float(s.mean())


def build_event_study_report(
    dataset_path: str | Path,
    output_dir: str | Path,
    group_cols: Sequence[str] = ("event_scope", "event_type", "event_side", "impact_channel"),
) -> dict:
    df = _read_dataset(dataset_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    if df.empty:
        empty = pd.DataFrame()
        empty.to_csv(output_dir / "event_study_by_event_type.csv", index=False)
        return {"rows": 0, "outputs": [str(output_dir / "event_study_by_event_type.csv")]}
    for col in group_cols:
        if col not in df.columns:
            df[col] = "UNKNOWN"
    # numeric coercion
    metrics = [
        "fwd_ret_1d", "fwd_ret_3d", "fwd_ret_5d", "fwd_ret_7d", "fwd_ret_14d", "fwd_ret_30d",
        "market_alpha_5d", "sector_alpha_5d", "volatility_shock_5d", "mae_5d", "mfe_5d",
        "sentiment_trap_label_5d", "sell_the_news_label_5d", "delayed_reaction_label_5d",
        "acceleration_trigger_label_5d", "confirmed_positive_label_5d", "confirmed_negative_label_5d",
    ]
    for m in metrics:
        if m in df.columns:
            df[m] = pd.to_numeric(df[m], errors="coerce")
    def agg(g: pd.DataFrame) -> pd.Series:
        alpha = pd.to_numeric(g.get("sector_alpha_5d"), errors="coerce") if "sector_alpha_5d" in g else pd.Series(dtype=float)
        vol = pd.to_numeric(g.get("volatility_shock_5d"), errors="coerce") if "volatility_shock_5d" in g else pd.Series(dtype=float)
        mae = pd.to_numeric(g.get("mae_5d"), errors="coerce") if "mae_5d" in g else pd.Series(dtype=float)
        return pd.Series({
            "n_events": len(g),
            "n_articles": g["article_id"].nunique() if "article_id" in g else np.nan,
            "n_tickers": g["ticker"].nunique(dropna=True) if "ticker" in g else np.nan,
            "hit_rate_sector_alpha_5d_gt_0": float((alpha > 0).mean()) if alpha.notna().any() else np.nan,
            "hit_rate_sector_alpha_5d_gt_1pct": float((alpha > 0.01).mean()) if alpha.notna().any() else np.nan,
            "avg_sector_alpha_5d": float(alpha.mean()) if alpha.notna().any() else np.nan,
            "median_sector_alpha_5d": float(alpha.median()) if alpha.notna().any() else np.nan,
            "avg_fwd_ret_5d": float(pd.to_numeric(g.get("fwd_ret_5d"), errors="coerce").mean()) if "fwd_ret_5d" in g else np.nan,
            "avg_volatility_shock_5d": float(vol.mean()) if vol.notna().any() else np.nan,
            "volatility_shock_rate_5d_gt_1_5": float((vol > 1.5).mean()) if vol.notna().any() else np.nan,
            "avg_mae_5d": float(mae.mean()) if mae.notna().any() else np.nan,
            "avg_mfe_5d": float(pd.to_numeric(g.get("mfe_5d"), errors="coerce").mean()) if "mfe_5d" in g else np.nan,
            "sentiment_trap_rate_5d": _safe_rate(g.get("sentiment_trap_label_5d", pd.Series(dtype=float))),
            "sell_the_news_rate_5d": _safe_rate(g.get("sell_the_news_label_5d", pd.Series(dtype=float))),
            "delayed_reaction_rate_5d": _safe_rate(g.get("delayed_reaction_label_5d", pd.Series(dtype=float))),
            "acceleration_trigger_rate_5d": _safe_rate(g.get("acceleration_trigger_label_5d", pd.Series(dtype=float))),
        })
    report = df.groupby(list(group_cols), dropna=False).apply(agg).reset_index().sort_values(["n_events", "avg_sector_alpha_5d"], ascending=[False, False])
    path1 = output_dir / "event_study_by_event_type.csv"
    report.to_csv(path1, index=False)
    outputs = [str(path1)]
    # If regime proxy exists, create event x regime report.
    if "volatility_regime_proxy" in df.columns:
        cols = list(group_cols) + ["volatility_regime_proxy"]
        report2 = df.groupby(cols, dropna=False).apply(agg).reset_index().sort_values(["n_events", "avg_sector_alpha_5d"], ascending=[False, False])
        path2 = output_dir / "event_study_by_event_type_x_vol_regime.csv"
        report2.to_csv(path2, index=False)
        outputs.append(str(path2))
    meta = {"rows": int(len(df)), "groups": int(len(report)), "outputs": outputs}
    (output_dir / "event_study_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return meta
