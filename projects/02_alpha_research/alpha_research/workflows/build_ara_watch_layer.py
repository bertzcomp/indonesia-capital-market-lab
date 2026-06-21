#!/usr/bin/env python3
"""Build ARA opening watch annotations for a daily signal folder.

This implements the v3 two-lane ARA hypothesis as a post-signal layer:
- model lane: score_ara top-k per day
- behavioral ignition lane: ara_signature_score_v1 top-k per day

The layer is deliberately non-destructive by default. It writes new files such as:
- all_scores_with_ara_watch.csv/parquet
- all_strategy_watchlist_with_ara_watch.csv
- ara_opening_shortlist.csv
- ara_opening_radar.csv
- ara_watch_summary.json
- ara_watch_report.md
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _safe_float(x: Any) -> float | None:
    try:
        if pd.isna(x):
            return None
        return float(x)
    except Exception:
        return None


def _fmt_num(x: Any, digits: int = 3) -> str:
    v = _safe_float(x)
    if v is None or not math.isfinite(v):
        return ""
    return f"{v:.{digits}f}"


def _fmt_pct(x: Any, digits: int = 2) -> str:
    v = _safe_float(x)
    if v is None or not math.isfinite(v):
        return ""
    return f"{v*100:.{digits}f}%"


def _normalize_date_series(s: pd.Series) -> pd.Series:
    dt = pd.to_datetime(s, errors="coerce")
    # Keep YYYY-MM-DD strings for stable merging/reporting.
    return dt.dt.strftime("%Y-%m-%d").fillna(s.astype(str))


def _find_score_ara_col(df: pd.DataFrame, requested: str = "score_ara") -> str | None:
    if requested in df.columns:
        return requested
    # Prefer exact generic-ish ARA score, then fallback to any score column containing ara.
    candidates = [c for c in df.columns if c.startswith("score_") and "ara" in c.lower()]
    if not candidates:
        return None
    # Prefer columns without many double-underscore components if present.
    candidates = sorted(candidates, key=lambda c: (c.count("__"), len(c)))
    return candidates[0]


def _compute_signature(df: pd.DataFrame, policy: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    out = df.copy()
    out["date"] = _normalize_date_series(out["date"])

    weights = policy["behavioral_ignition_lane"].get("weights", {})
    fill_rank = float(policy["behavioral_ignition_lane"].get("missing_feature_fill_rank", 0.5))
    used_weights: dict[str, float] = {}
    missing_features: list[str] = []

    weighted_sum = pd.Series(0.0, index=out.index, dtype="float64")
    total_weight = 0.0

    for feature, weight in weights.items():
        weight = float(weight)
        rank_col = f"ara_sig_rank_{feature}"
        if feature not in out.columns:
            missing_features.append(feature)
            continue
        vals = pd.to_numeric(out[feature], errors="coerce")
        out[feature] = vals
        # Higher feature value is assumed better for this v3 hypothesis.
        out[rank_col] = vals.groupby(out["date"]).rank(method="average", pct=True, ascending=True)
        weighted_sum = weighted_sum + weight * out[rank_col].fillna(fill_rank)
        total_weight += weight
        used_weights[feature] = weight

    if total_weight > 0:
        out["ara_signature_score_v1"] = weighted_sum / total_weight
    else:
        out["ara_signature_score_v1"] = np.nan

    out["daily_rank_ara_signature_score_v1"] = out.groupby("date")["ara_signature_score_v1"].rank(
        method="first", ascending=False
    )
    out["daily_pct_ara_signature_score_v1"] = out.groupby("date")["ara_signature_score_v1"].rank(
        method="average", pct=True, ascending=True
    )

    return out, {
        "used_weights": used_weights,
        "missing_features": missing_features,
        "total_weight": total_weight,
        "fill_rank": fill_rank,
    }


def _apply_two_lane_policy(df: pd.DataFrame, policy: dict[str, Any]) -> tuple[pd.DataFrame, dict[str, Any]]:
    out = df.copy()
    model_req = policy["model_lane"].get("score_col", "score_ara")
    score_ara_col = _find_score_ara_col(out, model_req)
    if score_ara_col is not None:
        out["ara_model_score"] = pd.to_numeric(out[score_ara_col], errors="coerce")
        out["daily_rank_score_ara"] = out.groupby("date")["ara_model_score"].rank(method="first", ascending=False)
        out["daily_pct_score_ara"] = out.groupby("date")["ara_model_score"].rank(method="average", pct=True, ascending=True)
        # Keep/overwrite generic score_ara for consistent downstream output if needed.
        if "score_ara" not in out.columns:
            out["score_ara"] = out["ara_model_score"]
    else:
        out["ara_model_score"] = np.nan
        out["daily_rank_score_ara"] = np.nan
        out["daily_pct_score_ara"] = np.nan

    model_top_k = int(policy["model_lane"].get("shortlist_top_k", 1))
    sig_top_k = int(policy["behavioral_ignition_lane"].get("shortlist_top_k", 3))
    radar_model_top_k = int(policy["model_lane"].get("radar_top_k", model_top_k))
    radar_sig_top_k = int(policy["behavioral_ignition_lane"].get("radar_top_k", max(sig_top_k, 15)))

    out["ara_model_lane_flag"] = out["daily_rank_score_ara"].le(model_top_k).fillna(False).astype(int)
    out["behavioral_ignition_lane_flag"] = out["daily_rank_ara_signature_score_v1"].le(sig_top_k).fillna(False).astype(int)
    out["dual_confirm_flag"] = ((out["ara_model_lane_flag"] == 1) & (out["behavioral_ignition_lane_flag"] == 1)).astype(int)
    out["ara_shortlist_flag"] = ((out["ara_model_lane_flag"] == 1) | (out["behavioral_ignition_lane_flag"] == 1)).astype(int)

    out["ara_model_radar_flag"] = out["daily_rank_score_ara"].le(radar_model_top_k).fillna(False).astype(int)
    out["behavioral_ignition_radar_flag"] = out["daily_rank_ara_signature_score_v1"].le(radar_sig_top_k).fillna(False).astype(int)
    out["ara_radar_flag"] = ((out["ara_model_radar_flag"] == 1) | (out["behavioral_ignition_radar_flag"] == 1)).astype(int)

    def lane(row: pd.Series) -> str:
        if row["dual_confirm_flag"] == 1:
            return "dual_confirm"
        if row["ara_model_lane_flag"] == 1:
            return "ara_model_lane"
        if row["behavioral_ignition_lane_flag"] == 1:
            return "behavioral_ignition_lane"
        if row["ara_model_radar_flag"] == 1:
            return "ara_model_radar"
        if row["behavioral_ignition_radar_flag"] == 1:
            return "behavioral_ignition_radar"
        return "none"

    out["ara_watch_lane"] = out.apply(lane, axis=1)

    # Human-readable compact explanation tags.
    tags = []
    for _, row in out.iterrows():
        t = []
        if row.get("ara_model_lane_flag", 0) == 1:
            t.append(f"score_ara_rank<={model_top_k}")
        if row.get("behavioral_ignition_lane_flag", 0) == 1:
            t.append(f"signature_rank<={sig_top_k}")
        if row.get("dual_confirm_flag", 0) == 1:
            t.append("dual_confirm")
        if not t and row.get("behavioral_ignition_radar_flag", 0) == 1:
            t.append(f"signature_radar<={radar_sig_top_k}")
        tags.append(";".join(t) if t else "")
    out["ara_watch_reason"] = tags

    return out, {
        "score_ara_col_used": score_ara_col,
        "model_top_k": model_top_k,
        "signature_top_k": sig_top_k,
        "radar_model_top_k": radar_model_top_k,
        "radar_signature_top_k": radar_sig_top_k,
    }


def _sort_watch(df: pd.DataFrame) -> pd.DataFrame:
    sort_cols = [c for c in [
        "date",
        "dual_confirm_flag",
        "ara_shortlist_flag",
        "behavioral_ignition_lane_flag",
        "ara_model_lane_flag",
        "daily_rank_score_ara",
        "daily_rank_ara_signature_score_v1",
        "ticker",
    ] if c in df.columns]
    ascending = []
    for c in sort_cols:
        ascending.append(False if c in {"dual_confirm_flag", "ara_shortlist_flag", "behavioral_ignition_lane_flag", "ara_model_lane_flag"} else True)
    return df.sort_values(sort_cols, ascending=ascending) if sort_cols else df


def _selected_cols(df: pd.DataFrame) -> list[str]:
    preferred = [
        "date", "ticker", "ara_watch_lane", "ara_shortlist_flag", "ara_radar_flag",
        "ara_model_lane_flag", "behavioral_ignition_lane_flag", "dual_confirm_flag", "ara_watch_reason",
        "daily_rank_score_ara", "score_ara", "ara_model_score",
        "daily_rank_ara_signature_score_v1", "ara_signature_score_v1",
        "close", "volume_ratio_20d", "ret_1d", "ret_5d", "close_vs_ma20", "volatility_20d",
        "buyer_dominance_ratio", "net_flow_ratio", "rank1_same_buyer_streak", "rank1_buyer",
        "traded_value_proxy", "has_broksum", "broker_value_anomaly_flag",
        "strategy", "strategy_group", "score_col", "score_value", "status"
    ]
    cols = [c for c in preferred if c in df.columns]
    extra = [c for c in df.columns if c.startswith("score_") and c not in cols]
    return cols + extra[:10]


def _merge_watchlist(signal_dir: Path, enriched: pd.DataFrame, out_name: str) -> dict[str, Any]:
    watchlist_path = signal_dir / "all_strategy_watchlist.csv"
    if not watchlist_path.exists():
        return {"watchlist_found": False}
    w = pd.read_csv(watchlist_path)
    if "date" not in w.columns or "ticker" not in w.columns:
        return {"watchlist_found": True, "merged": False, "reason": "missing date/ticker columns"}
    w = w.copy()
    w["date"] = _normalize_date_series(w["date"])
    w["ticker"] = w["ticker"].astype(str)
    ann_cols = [
        "date", "ticker", "ara_watch_lane", "ara_shortlist_flag", "ara_radar_flag",
        "ara_model_lane_flag", "behavioral_ignition_lane_flag", "dual_confirm_flag", "ara_watch_reason",
        "daily_rank_score_ara", "daily_rank_ara_signature_score_v1", "ara_signature_score_v1", "ara_model_score",
    ]
    ann_cols = [c for c in ann_cols if c in enriched.columns]
    ann = enriched[ann_cols].copy()
    ann["date"] = _normalize_date_series(ann["date"])
    ann["ticker"] = ann["ticker"].astype(str)
    merged = w.merge(ann, on=["date", "ticker"], how="left")
    for c in ["ara_shortlist_flag", "ara_radar_flag", "ara_model_lane_flag", "behavioral_ignition_lane_flag", "dual_confirm_flag"]:
        if c in merged.columns:
            merged[c] = merged[c].fillna(0).astype(int)
    if "ara_watch_lane" in merged.columns:
        merged["ara_watch_lane"] = merged["ara_watch_lane"].fillna("none")
    merged.to_csv(signal_dir / out_name, index=False)
    return {"watchlist_found": True, "merged": True, "rows": int(len(merged)), "output": out_name}


def _write_report(signal_dir: Path, enriched: pd.DataFrame, shortlist: pd.DataFrame, radar: pd.DataFrame, summary: dict[str, Any], report_name: str, max_shortlist: int, max_radar: int) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], max_rows: int) -> str:
        if df.empty:
            return "_No candidates._\n"
        use = df[[c for c in cols if c in df.columns]].head(max_rows).copy()
        # Format a few numeric columns.
        for c in ["score_ara", "ara_model_score", "ara_signature_score_v1", "volume_ratio_20d", "ret_1d", "ret_5d", "close_vs_ma20", "volatility_20d", "buyer_dominance_ratio", "net_flow_ratio"]:
            if c in use.columns:
                if c in {"ret_1d", "ret_5d", "close_vs_ma20", "volatility_20d", "net_flow_ratio"}:
                    use[c] = use[c].map(lambda x: _fmt_pct(x, 2))
                else:
                    use[c] = use[c].map(lambda x: _fmt_num(x, 3))
        for c in ["daily_rank_score_ara", "daily_rank_ara_signature_score_v1"]:
            if c in use.columns:
                use[c] = use[c].map(lambda x: "" if pd.isna(x) else str(int(x)))
        return use.to_markdown(index=False) + "\n"

    lane_counts = enriched["ara_watch_lane"].value_counts(dropna=False).to_dict() if "ara_watch_lane" in enriched.columns else {}
    lines = []
    lines.append("# ARA Opening Watch Layer\n")
    lines.append("> Research annotation only. This is not an automatic execution rule.\n")
    lines.append("## Policy\n")
    lines.append(f"- Model lane: `score_ara` top {summary['policy'].get('model_top_k')} per day\n")
    lines.append(f"- Behavioral ignition lane: `ara_signature_score_v1` top {summary['policy'].get('signature_top_k')} per day\n")
    lines.append(f"- Broad radar: `score_ara` top {summary['policy'].get('radar_model_top_k')} OR signature top {summary['policy'].get('radar_signature_top_k')}\n")
    lines.append("## Summary\n")
    lines.append(f"- Rows in all_scores: {summary.get('rows')}\n")
    lines.append(f"- Unique tickers: {summary.get('unique_tickers')}\n")
    lines.append(f"- Shortlist candidates: {summary.get('shortlist_rows')}\n")
    lines.append(f"- Radar candidates: {summary.get('radar_rows')}\n")
    lines.append(f"- Lane counts: `{json.dumps(lane_counts, ensure_ascii=False)}`\n")
    lines.append("\n## ARA Shortlist\n")
    lines.append(md_table(shortlist, _selected_cols(shortlist), max_shortlist))
    lines.append("\n## Broad ARA Radar\n")
    lines.append(md_table(radar, _selected_cols(radar), max_radar))
    lines.append("\n## Signature score v1 formula\n")
    for k, v in summary.get("signature", {}).get("used_weights", {}).items():
        lines.append(f"- `{k}`: {v}\n")
    if summary.get("signature", {}).get("missing_features"):
        lines.append("\nMissing features: " + ", ".join(summary["signature"]["missing_features"]) + "\n")
    lines.append("\n## Warning\n")
    lines.append(summary.get("research_warning", "Treat as research annotation, not production proof.") + "\n")
    (signal_dir / report_name).write_text("".join(lines), encoding="utf-8")


def build(signal_dir: Path, policy_path: Path, all_scores_file: str = "all_scores.csv") -> dict[str, Any]:
    if not signal_dir.exists():
        raise FileNotFoundError(f"signal_dir not found: {signal_dir}")
    policy = _read_json(policy_path)
    out_cfg = policy.get("output", {})
    all_scores_path = signal_dir / all_scores_file
    if not all_scores_path.exists():
        raise FileNotFoundError(f"all_scores file not found: {all_scores_path}")

    df = pd.read_csv(all_scores_path)
    if "date" not in df.columns or "ticker" not in df.columns:
        raise ValueError("all_scores must contain date and ticker columns")
    df["date"] = _normalize_date_series(df["date"])
    df["ticker"] = df["ticker"].astype(str)

    enriched, sig_meta = _compute_signature(df, policy)
    enriched, pol_meta = _apply_two_lane_policy(enriched, policy)
    enriched = _sort_watch(enriched)

    shortlist = _sort_watch(enriched[enriched["ara_shortlist_flag"] == 1].copy())
    radar = _sort_watch(enriched[enriched["ara_radar_flag"] == 1].copy())

    # Outputs.
    enriched_csv = out_cfg.get("all_scores_enriched_csv", "all_scores_with_ara_watch.csv")
    enriched_parquet = out_cfg.get("all_scores_enriched_parquet", "all_scores_with_ara_watch.parquet")
    shortlist_csv = out_cfg.get("shortlist_csv", "ara_opening_shortlist.csv")
    radar_csv = out_cfg.get("radar_csv", "ara_opening_radar.csv")
    summary_json = out_cfg.get("summary_json", "ara_watch_summary.json")
    report_md = out_cfg.get("report_md", "ara_watch_report.md")
    enriched.to_csv(signal_dir / enriched_csv, index=False)
    try:
        enriched.to_parquet(signal_dir / enriched_parquet, index=False)
    except Exception:
        # Parquet is convenient but not required if pyarrow/fastparquet is missing.
        enriched_parquet = None
    shortlist[_selected_cols(shortlist)].to_csv(signal_dir / shortlist_csv, index=False)
    radar[_selected_cols(radar)].to_csv(signal_dir / radar_csv, index=False)

    merge_meta = _merge_watchlist(signal_dir, enriched, out_cfg.get("strategy_watchlist_enriched_csv", "all_strategy_watchlist_with_ara_watch.csv"))

    summary = {
        "version": policy.get("version"),
        "signal_dir": str(signal_dir),
        "policy_path": str(policy_path),
        "all_scores_file": all_scores_file,
        "rows": int(len(enriched)),
        "unique_dates": int(enriched["date"].nunique()),
        "unique_tickers": int(enriched["ticker"].nunique()),
        "shortlist_rows": int(len(shortlist)),
        "radar_rows": int(len(radar)),
        "lane_counts": enriched["ara_watch_lane"].value_counts(dropna=False).to_dict(),
        "shortlist_lane_counts": shortlist["ara_watch_lane"].value_counts(dropna=False).to_dict() if not shortlist.empty else {},
        "policy": pol_meta,
        "signature": sig_meta,
        "outputs": {
            "all_scores_enriched_csv": enriched_csv,
            "all_scores_enriched_parquet": enriched_parquet,
            "shortlist_csv": shortlist_csv,
            "radar_csv": radar_csv,
            "summary_json": summary_json,
            "report_md": report_md,
            "watchlist_merge": merge_meta,
        },
        "research_warning": policy.get("research_warning"),
    }
    (signal_dir / summary_json).write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str), encoding="utf-8")

    _write_report(
        signal_dir=signal_dir,
        enriched=enriched,
        shortlist=shortlist,
        radar=radar,
        summary=summary,
        report_name=report_md,
        max_shortlist=int(policy.get("report", {}).get("max_rows_shortlist", 50)),
        max_radar=int(policy.get("report", {}).get("max_rows_radar", 100)),
    )
    return summary


def main() -> None:
    ap = argparse.ArgumentParser(description="Build ARA opening watch research annotations for a daily signal folder.")
    ap.add_argument("--signal-dir", required=True, help="Daily signal profile directory, e.g. signals/daily/signal_22_may_2026/continual_model")
    ap.add_argument("--policy", default="configs/ara_watch_policy.v3.json")
    ap.add_argument("--all-scores-file", default="all_scores.csv")
    args = ap.parse_args()

    signal_dir = Path(args.signal_dir)
    policy_path = Path(args.policy)
    if not policy_path.exists() and not policy_path.is_absolute():
        # Allow running from a project root while passing the default relative policy path.
        policy_path = Path.cwd() / args.policy
    summary = build(signal_dir=signal_dir, policy_path=policy_path, all_scores_file=args.all_scores_file)
    print(json.dumps(summary, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
