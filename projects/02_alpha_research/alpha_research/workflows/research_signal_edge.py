#!/usr/bin/env python3
"""Signal / feature edge research workflow.

Standalone hypothesis-testing workflow for IDX alpha research datasets.
It can analyse:
  1) model score edge from validation panels / all_score-like panels that include fwd_ret_* columns
  2) raw feature edge from full_labeled.parquet

Outputs quantile lift, top-k daily portfolio metrics, IC/spearman, and a markdown report.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np
import pandas as pd

try:
    import polars as pl
except Exception as exc:  # pragma: no cover
    raise SystemExit("polars is required. Install with: pip install polars") from exc


FWD_TARGETS = [
    "fwd_ret_1d", "fwd_ret_2d", "fwd_ret_3d", "fwd_ret_5d", "fwd_ret_10d", "fwd_ret_20d", "fwd_ret_30d", "fwd_ret_60d",
]
LABEL_TARGETS = [
    "label_scalp", "label_swing", "label_position", "label_ara_tomorrow", "label_near_ara_tomorrow",
    "label_brok_cont", "label_silent_accum_breakout", "label_big_runner_30d", "label_multibagger_60d",
    "label_momentum_5d", "label_momentum_10d", "label_momentum_20d",
]
TARGETS = FWD_TARGETS + LABEL_TARGETS

PRESET_FEATURES = {
    "momentum_ranker": [
        "ret_1d", "ret_5d", "ret_10d", "ret_20d", "close_vs_ma20", "volume_ratio_20d", "volatility_20d",
        "cs_rank_ret_5d", "cs_rank_ret_10d", "cs_rank_ret_20d", "cs_rank_volume_ratio_20d",
        "market_ret_1d", "market_ret_5d", "market_ret_20d", "market_volatility_20d", "macro_risk_score",
        "ihsg_ret_5d", "ihsg_ret_10d", "ihsg_ret_20d", "has_bdm_any", "has_bdm_non_retail",
    ],
    "multi_strategy_time": [
        "ret_1d", "ret_5d", "ret_10d", "ret_20d", "close_vs_ma20", "volume_ratio_20d", "volatility_20d",
        "traded_value_proxy", "has_broksum", "net_flow_ratio", "net_buy_flag", "buyer_dominance_ratio",
        "seller_dominance_ratio", "rank1_same_buyer_streak", "rank1_buyer_daily_share",
        "rank1_buyer_overcrowded_flag", "broker_value_anomaly_flag",
        "cs_rank_net_flow_ratio", "cs_rank_rank1_same_buyer_streak", "cs_rank_buyer_dominance_ratio",
        "rank1_buy_val", "rank1_buy_lot", "rank1_buy_freq", "has_bdm_market_maker", "has_bdm_non_retail",
    ],
    "ara_predictor": [
        "ret_1d", "ret_5d", "ret_10d", "ret_20d", "volume_ratio_20d", "volatility_20d", "close_vs_ma20",
        "traded_value_proxy", "net_flow_ratio", "net_buy_flag", "buyer_dominance_ratio", "rank1_same_buyer_streak",
        "broker_value_anomaly_flag", "rank1_buyer_overcrowded_flag", "cs_rank_volume_ratio_20d", "cs_rank_net_flow_ratio",
        "market_ret_1d", "market_ret_5d", "macro_risk_score", "has_bdm_any",
    ],
}

FAMILY_SCORE_PATTERNS = {
    "ara_predictor": ["score_ara"],
    "momentum_ranker": ["score_momentum"],
    "multi_strategy_time": ["score_scalp", "score_swing", "score_position"],
    "all": ["score_"],
}

FAMILY_TARGETS = {
    "ara_predictor": ["fwd_ret_1d", "fwd_ret_2d", "label_ara_tomorrow", "label_near_ara_tomorrow"],
    "momentum_ranker": ["fwd_ret_3d", "fwd_ret_5d", "fwd_ret_10d", "fwd_ret_20d", "label_momentum_5d", "label_momentum_10d", "label_momentum_20d"],
    "multi_strategy_time": ["fwd_ret_1d", "fwd_ret_2d", "fwd_ret_3d", "fwd_ret_5d", "fwd_ret_10d", "fwd_ret_20d", "label_scalp", "label_swing", "label_position"],
    "all": FWD_TARGETS + LABEL_TARGETS,
}


def _split_csv(s: str | None) -> list[str]:
    if not s:
        return []
    return [x.strip() for x in s.split(",") if x.strip()]


def _resolve(root: Path, p: str | None) -> Path | None:
    if not p:
        return None
    path = Path(p)
    return path if path.is_absolute() else root / path


def _read_columns(path: Path) -> list[str]:
    if path.suffix.lower() == ".parquet":
        return pl.scan_parquet(str(path)).collect_schema().names()
    if path.suffix.lower() in {".csv", ".txt"}:
        return list(pd.read_csv(path, nrows=1).columns)
    raise ValueError(f"Unsupported file type: {path}")


def _read_frame(path: Path, columns: list[str] | None = None) -> pl.DataFrame:
    if path.suffix.lower() == ".parquet":
        lf = pl.scan_parquet(str(path))
        if columns:
            existing = set(lf.collect_schema().names())
            columns = [c for c in columns if c in existing]
            lf = lf.select(columns)
        return lf.collect()
    if path.suffix.lower() in {".csv", ".txt"}:
        return pl.from_pandas(pd.read_csv(path, usecols=columns if columns else None))
    raise ValueError(f"Unsupported file type: {path}")


def _ensure_date(df: pl.DataFrame) -> pl.DataFrame:
    if "date" not in df.columns:
        return df
    dtype = df.schema.get("date")
    if dtype == pl.Date:
        return df
    if dtype == pl.Datetime:
        return df.with_columns(pl.col("date").dt.date())
    return df.with_columns(pl.col("date").cast(pl.Utf8).str.strptime(pl.Date, strict=False))


def _filter_frame(
    df: pl.DataFrame,
    start_date: str | None,
    end_date: str | None,
    min_traded_value: float | None,
    price_min: float | None,
    price_max: float | None,
    require_broksum: bool,
    exclude_broker_value_anomaly: bool,
) -> pl.DataFrame:
    df = _ensure_date(df)
    filters = []
    if start_date and "date" in df.columns:
        filters.append(pl.col("date") >= pl.lit(start_date).str.strptime(pl.Date))
    if end_date and "date" in df.columns:
        filters.append(pl.col("date") <= pl.lit(end_date).str.strptime(pl.Date))
    if min_traded_value is not None and "traded_value_proxy" in df.columns:
        filters.append(pl.col("traded_value_proxy") >= float(min_traded_value))
    if price_min is not None and "close" in df.columns:
        filters.append(pl.col("close") >= float(price_min))
    if price_max is not None and "close" in df.columns:
        filters.append(pl.col("close") <= float(price_max))
    if require_broksum and "has_broksum" in df.columns:
        filters.append(pl.col("has_broksum").fill_null(0) == 1)
    if exclude_broker_value_anomaly and "broker_value_anomaly_flag" in df.columns:
        filters.append(pl.col("broker_value_anomaly_flag").fill_null(0) == 0)
    for f in filters:
        df = df.filter(f)
    return df


def _infer_score_cols(columns: list[str], family: str) -> list[str]:
    patterns = FAMILY_SCORE_PATTERNS.get(family, FAMILY_SCORE_PATTERNS["all"])
    out = []
    for c in columns:
        if any(c.startswith(p) or p in c for p in patterns):
            # Avoid duplicated aggregate alias when specific score exists? Keep both; report will show all.
            out.append(c)
    return sorted(set(out))


def _infer_feature_cols(columns: list[str], family: str, max_features: int = 80) -> list[str]:
    preset = [c for c in PRESET_FEATURES.get(family, []) if c in columns]
    if preset:
        return preset
    bad_prefix = ("fwd_ret_", "target_", "label_", "score_")
    bad = {"date", "ticker", "rank1_buyer", "rank1_seller", "rank1_buyer_type", "rank1_seller_type", "market_regime"}
    candidates = [c for c in columns if c not in bad and not c.startswith(bad_prefix)]
    return candidates[:max_features]


def _safe_spearman(x: pd.Series, y: pd.Series) -> float | None:
    m = x.notna() & y.notna()
    if int(m.sum()) < 30:
        return None
    xr = x[m].rank(method="average")
    yr = y[m].rank(method="average")
    v = xr.corr(yr)
    if pd.isna(v):
        return None
    return float(v)


def _is_label(col: str) -> bool:
    return col.startswith("label_")


def _quantile_table(pdf: pd.DataFrame, signal_col: str, target_col: str, q: int) -> pd.DataFrame:
    sub = pdf[[signal_col, target_col]].replace([np.inf, -np.inf], np.nan).dropna()
    if len(sub) < max(50, q * 5) or sub[signal_col].nunique(dropna=True) < 3:
        return pd.DataFrame()
    # Use duplicates='drop' because many tree scores/features can be tied.
    try:
        sub["bucket"] = pd.qcut(sub[signal_col], q=q, labels=False, duplicates="drop") + 1
    except ValueError:
        return pd.DataFrame()
    if sub["bucket"].nunique() < 2:
        return pd.DataFrame()
    g = sub.groupby("bucket", observed=True)
    out = g.agg(
        n=(target_col, "size"),
        signal_min=(signal_col, "min"),
        signal_mean=(signal_col, "mean"),
        signal_max=(signal_col, "max"),
        target_mean=(target_col, "mean"),
        target_median=(target_col, "median"),
        win_rate=(target_col, lambda s: float((s > 0).mean())),
    ).reset_index()
    out.insert(0, "target_col", target_col)
    out.insert(0, "signal_col", signal_col)
    return out


def _top_bucket_summary(qtab: pd.DataFrame) -> dict[str, Any]:
    if qtab.empty:
        return {}
    top = qtab.sort_values("bucket").iloc[-1]
    base_mean = float(np.average(qtab["target_mean"], weights=qtab["n"])) if qtab["n"].sum() else None
    base_wr = float(np.average(qtab["win_rate"], weights=qtab["n"])) if qtab["n"].sum() else None
    return {
        "top_bucket": int(top["bucket"]),
        "top_n": int(top["n"]),
        "top_target_mean": float(top["target_mean"]),
        "base_target_mean": base_mean,
        "target_mean_lift": (float(top["target_mean"]) - base_mean) if base_mean is not None else None,
        "top_win_rate": float(top["win_rate"]),
        "base_win_rate": base_wr,
        "win_rate_lift": (float(top["win_rate"]) - base_wr) if base_wr is not None else None,
    }


def _topk_table(pdf: pd.DataFrame, signal_col: str, target_col: str, topks: list[int]) -> pd.DataFrame:
    needed = ["date", "ticker", signal_col, target_col]
    if not set(needed).issubset(pdf.columns):
        return pd.DataFrame()
    sub = pdf[needed].replace([np.inf, -np.inf], np.nan).dropna(subset=["date", signal_col, target_col])
    if len(sub) < 50:
        return pd.DataFrame()
    rows = []
    dates = sub["date"].nunique()
    base_ret = float(sub[target_col].mean()) if not _is_label(target_col) else None
    for k in topks:
        sel = sub.sort_values(["date", signal_col], ascending=[True, False]).groupby("date", observed=True).head(k)
        if sel.empty:
            continue
        daily = sel.groupby("date", observed=True)[target_col].mean()
        daily_mean = float(daily.mean())
        daily_std = float(daily.std(ddof=1)) if len(daily) > 1 else 0.0
        daily_sharpe = (daily_mean / daily_std * math.sqrt(252)) if daily_std and not _is_label(target_col) else None
        rows.append({
            "signal_col": signal_col,
            "target_col": target_col,
            "top_k": int(k),
            "n_trades": int(len(sel)),
            "n_days": int(dates),
            "avg_trades_per_day": float(len(sel) / max(dates, 1)),
            "mean_target": float(sel[target_col].mean()),
            "median_target": float(sel[target_col].median()),
            "win_rate": float((sel[target_col] > 0).mean()),
            "daily_mean_target": daily_mean,
            "daily_sharpe_like": daily_sharpe,
            "base_mean_target": base_ret,
            "lift_vs_base_mean": (float(sel[target_col].mean()) - base_ret) if base_ret is not None else None,
        })
    return pd.DataFrame(rows)


def _analyse_signals(pdf: pd.DataFrame, signal_cols: list[str], target_cols: list[str], quantiles: int, topks: list[int]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    qtabs = []
    topks_tabs = []
    summary_rows = []
    for s in signal_cols:
        if s not in pdf.columns:
            continue
        for t in target_cols:
            if t not in pdf.columns:
                continue
            ic = _safe_spearman(pdf[s], pdf[t])
            qtab = _quantile_table(pdf, s, t, quantiles)
            if not qtab.empty:
                qtabs.append(qtab)
            ts = _top_bucket_summary(qtab)
            topk = _topk_table(pdf, s, t, topks)
            if not topk.empty:
                topks_tabs.append(topk)
                best = topk.sort_values(["mean_target", "win_rate"], ascending=False).iloc[0].to_dict()
            else:
                best = {}
            summary_rows.append({
                "signal_col": s,
                "target_col": t,
                "n_non_null_pairs": int((pdf[s].notna() & pdf[t].notna()).sum()),
                "spearman_ic": ic,
                **{f"quantile_{k}": v for k, v in ts.items()},
                "best_top_k": int(best.get("top_k")) if best else None,
                "best_topk_mean_target": float(best.get("mean_target")) if best else None,
                "best_topk_win_rate": float(best.get("win_rate")) if best else None,
                "best_topk_n_trades": int(best.get("n_trades")) if best else None,
            })
    return (
        pd.concat(qtabs, ignore_index=True) if qtabs else pd.DataFrame(),
        pd.concat(topks_tabs, ignore_index=True) if topks_tabs else pd.DataFrame(),
        pd.DataFrame(summary_rows),
    )


def _write_report(out_dir: Path, meta: dict[str, Any], summary: pd.DataFrame, qtab: pd.DataFrame, topk: pd.DataFrame) -> None:
    lines = []
    lines.append("# Signal / Feature Edge Research Report\n")
    lines.append("## Run metadata\n")
    lines.append("```json\n" + json.dumps(meta, indent=2, default=str) + "\n```\n")
    if summary.empty:
        lines.append("No edge summary rows were produced. Check selected columns and filters.\n")
    else:
        lines.append("## Best summary rows\n")
        sort_cols = [c for c in ["quantile_target_mean_lift", "best_topk_mean_target", "spearman_ic"] if c in summary.columns]
        view = summary.copy()
        if sort_cols:
            view["rank_score"] = 0.0
            if "quantile_target_mean_lift" in view.columns:
                view["rank_score"] += view["quantile_target_mean_lift"].fillna(0)
            if "best_topk_mean_target" in view.columns:
                view["rank_score"] += view["best_topk_mean_target"].fillna(0)
            view = view.sort_values("rank_score", ascending=False)
        cols = [c for c in ["signal_col", "target_col", "n_non_null_pairs", "spearman_ic", "quantile_top_target_mean", "quantile_base_target_mean", "quantile_target_mean_lift", "quantile_top_win_rate", "quantile_win_rate_lift", "best_top_k", "best_topk_mean_target", "best_topk_win_rate", "best_topk_n_trades"] if c in view.columns]
        lines.append(view[cols].head(30).to_markdown(index=False))
        lines.append("\n")
        lines.append("## Interpretation rules\n")
        lines.append("- Positive Spearman IC means higher score/feature tends to align with higher future return or label rate.\n")
        lines.append("- Quantile lift is the difference between the top bucket and the population average.\n")
        lines.append("- Top-k metrics simulate taking the top ranked names per day. Prefer stable positive mean, non-trivial n_trades, and acceptable win rate.\n")
        lines.append("- For labels, `mean_target` is the positive rate. For returns, it is average forward return.\n")
    out_dir.joinpath("edge_research_report.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--dataset", default=None, help="full_labeled.parquet/csv for raw feature edge research")
    ap.add_argument("--score-panel", default=None, help="validation/all_scores panel containing score_* and fwd_ret/label columns")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--family", default="all", choices=["all", "ara_predictor", "momentum_ranker", "multi_strategy_time"])
    ap.add_argument("--score-cols", default=None, help="Comma-separated score columns. If omitted, inferred from family.")
    ap.add_argument("--feature-cols", default=None, help="Comma-separated feature columns for dataset analysis. If omitted, preset features are used.")
    ap.add_argument("--targets", default=None, help="Comma-separated target columns. If omitted, family preset targets are used.")
    ap.add_argument("--start-date", default=None)
    ap.add_argument("--end-date", default=None)
    ap.add_argument("--forward-start", default=None, help="Alias for --start-date when testing a forward window.")
    ap.add_argument("--quantiles", type=int, default=10)
    ap.add_argument("--top-ks", default="1,3,5,7,10,15")
    ap.add_argument("--min-traded-value", type=float, default=None)
    ap.add_argument("--price-min", type=float, default=None)
    ap.add_argument("--price-max", type=float, default=None)
    ap.add_argument("--require-broksum", action="store_true")
    ap.add_argument("--exclude-broker-value-anomaly", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    out_dir = _resolve(root, args.out_dir) or Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    source_path = _resolve(root, args.score_panel) or _resolve(root, args.dataset)
    source_kind = "score_panel" if args.score_panel else "dataset"
    if source_path is None or not source_path.exists():
        raise SystemExit(f"Source file not found: {source_path}")

    columns = _read_columns(source_path)
    explicit_scores = _split_csv(args.score_cols)
    explicit_features = _split_csv(args.feature_cols)
    targets = _split_csv(args.targets) or [t for t in FAMILY_TARGETS.get(args.family, TARGETS) if t in columns]

    if source_kind == "score_panel":
        signal_cols = [c for c in (explicit_scores or _infer_score_cols(columns, args.family)) if c in columns]
    else:
        signal_cols = [c for c in (explicit_features or _infer_feature_cols(columns, args.family)) if c in columns]

    base_cols = ["date", "ticker", "close", "traded_value_proxy", "has_broksum", "broker_value_anomaly_flag", "market_regime"]
    needed_cols = sorted(set([c for c in base_cols + signal_cols + targets if c in columns]))
    df = _read_frame(source_path, needed_cols)
    start_date = args.forward_start or args.start_date
    df = _filter_frame(
        df,
        start_date=start_date,
        end_date=args.end_date,
        min_traded_value=args.min_traded_value,
        price_min=args.price_min,
        price_max=args.price_max,
        require_broksum=args.require_broksum,
        exclude_broker_value_anomaly=args.exclude_broker_value_anomaly,
    )

    # Convert to pandas for qcut/rank/groupby. Keep only selected columns to control memory.
    pdf = df.to_pandas()
    if "date" in pdf.columns:
        pdf["date"] = pd.to_datetime(pdf["date"]).dt.date

    topks = [int(x) for x in _split_csv(args.top_ks)]
    qtab, topk, summary = _analyse_signals(pdf, signal_cols, targets, args.quantiles, topks)

    qtab_path = out_dir / "quantile_edge.csv"
    topk_path = out_dir / "topk_edge.csv"
    summary_path = out_dir / "edge_summary.csv"
    meta_path = out_dir / "edge_research_meta.json"

    if not qtab.empty:
        qtab.to_csv(qtab_path, index=False)
    else:
        pd.DataFrame().to_csv(qtab_path, index=False)
    if not topk.empty:
        topk.to_csv(topk_path, index=False)
    else:
        pd.DataFrame().to_csv(topk_path, index=False)
    if not summary.empty:
        summary.to_csv(summary_path, index=False)
    else:
        pd.DataFrame().to_csv(summary_path, index=False)

    meta = {
        "source_kind": source_kind,
        "source_path": str(source_path),
        "out_dir": str(out_dir),
        "family": args.family,
        "rows_after_filters": int(len(pdf)),
        "signal_cols": signal_cols,
        "target_cols": targets,
        "filters": {
            "start_date": start_date,
            "end_date": args.end_date,
            "min_traded_value": args.min_traded_value,
            "price_min": args.price_min,
            "price_max": args.price_max,
            "require_broksum": args.require_broksum,
            "exclude_broker_value_anomaly": args.exclude_broker_value_anomaly,
        },
        "outputs": {
            "summary": str(summary_path),
            "quantile_edge": str(qtab_path),
            "topk_edge": str(topk_path),
            "report": str(out_dir / "edge_research_report.md"),
        },
    }
    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    _write_report(out_dir, meta, summary, qtab, topk)
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
