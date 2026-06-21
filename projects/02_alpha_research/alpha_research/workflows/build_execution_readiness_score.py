#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

GENERIC_SCORE_COLS = [
    "score_ara",
    "score_momentum_5d",
    "score_momentum_10d",
    "score_momentum_20d",
    "score_scalp",
    "score_swing",
    "score_position",
    "score_mm_silent",
    "score_sm",
]


def _to_float(x: Any, default: float | None = None) -> float | None:
    if x is None:
        return default
    if isinstance(x, (int, float)):
        if math.isnan(x):
            return default
        return float(x)
    s = str(x).strip()
    if s == "" or s.lower() in {"nan", "none", "null"}:
        return default
    try:
        return float(s)
    except Exception:
        return default


def _to_int(x: Any, default: int = 0) -> int:
    f = _to_float(x, None)
    return default if f is None else int(f)


def _truthy(x: Any) -> bool:
    if isinstance(x, bool):
        return x
    s = str(x).strip().lower()
    return s in {"1", "true", "yes", "y"}


def _read_csv(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields: list[str] = []
    for row in rows:
        for k in row:
            if k not in fields:
                fields.append(k)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def _load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _percentile_rank(value: float | None, universe_values: list[float]) -> float:
    if value is None or not universe_values:
        return 0.0
    vals = sorted(v for v in universe_values if v is not None and not math.isnan(v))
    if not vals:
        return 0.0
    # fraction <= value
    import bisect
    return bisect.bisect_right(vals, value) / len(vals)


def _clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def _tick_size(price: float | None) -> int | None:
    if price is None:
        return None
    if price < 200:
        return 1
    if price < 500:
        return 2
    if price < 2000:
        return 5
    if price < 5000:
        return 10
    return 25


def _tier(score: float) -> str:
    if score >= 75:
        return "A_READY_WNS"
    if score >= 60:
        return "B_WATCH_CONFIRM"
    if score >= 45:
        return "C_CONDITIONAL"
    return "D_LOW_PRIORITY"


def _entry_style(row: dict[str, Any], strategy_names: list[str]) -> str:
    hold = _to_int(row.get("hold_days") or row.get("suggested_hold_days"), 1)
    risk_profile = str(row.get("risk_profile") or "").lower()
    vol = _to_float(row.get("volatility_20d"), 0.0) or 0.0
    ret5 = _to_float(row.get("ret_5d"), 0.0) or 0.0
    names = " ".join(strategy_names).lower()
    if "ara" in names or "high" in risk_profile:
        return "intraday_trigger_reclaim_only; small size; avoid chase; fast invalidation if trigger fails"
    if hold >= 5 or "position" in names:
        return "position_setup; prefer daily close confirmation or clean trigger retest; avoid opening spike"
    if "scalp" in names:
        return "scalp_setup; entry only on breakout acceptance + shallow retest; partial/fast exit"
    if vol >= 0.08 or ret5 <= -0.25:
        return "volatile_rebound; wait for liquidity sweep/reclaim or trigger retest"
    return "standard_trigger_retest_confirmation"


def _setup_type(row: dict[str, Any], n_strat: int) -> str:
    ret5 = _to_float(row.get("ret_5d"), 0.0) or 0.0
    ret20 = _to_float(row.get("ret_20d"), 0.0) or 0.0
    vol_ratio = _to_float(row.get("volume_ratio_20d"), None)
    if ret5 <= -0.25 and ret20 <= -0.30:
        return "distressed_rebound"
    if n_strat >= 4:
        return "multi_strategy_confluence"
    if vol_ratio is not None and vol_ratio >= 3:
        return "high_volume_event"
    return "single_or_mixed_signal"


def _score_components(
    base_row: dict[str, Any],
    strategy_rows: list[dict[str, Any]],
    plan_rows: list[dict[str, Any]],
    universe_stats: dict[str, list[float]],
    policy: dict[str, Any],
) -> dict[str, Any]:
    th = policy.get("thresholds", {})

    strategies = sorted({str(r.get("strategy_name") or r.get("strategy") or "") for r in strategy_rows if str(r.get("strategy_name") or r.get("strategy") or "").strip()})
    n_strat = len(strategies)
    strat_scores = [_to_float(r.get("strategy_score"), None) for r in strategy_rows]
    strat_scores = [s for s in strat_scores if s is not None]
    max_strategy_score = max(strat_scores) if strat_scores else None
    mean_strategy_score = mean(strat_scores) if strat_scores else None

    # Score breadth from generic score columns available on the base/watchlist row.
    generic_vals = []
    for c in GENERIC_SCORE_COLS:
        v = _to_float(base_row.get(c), None)
        if v is not None:
            generic_vals.append(v)
    max_generic_score = max(generic_vals) if generic_vals else max_strategy_score
    score_breadth = sum(1 for v in generic_vals if v >= th.get("score_breadth_threshold", 0.30))
    score_strong_count = sum(1 for v in generic_vals if v >= th.get("score_strong_threshold", 0.50))
    pct = _percentile_rank(max_generic_score, universe_stats.get("max_generic_score", []))
    passes = [_truthy(r.get("passes_execution_threshold")) for r in strategy_rows]
    pass_rate = sum(passes) / len(passes) if passes else 0.0

    model_edge = 0.0
    model_edge += 10.0 * _clamp(n_strat / 6.0)
    model_edge += 8.0 * pct
    model_edge += 5.0 * _clamp(score_breadth / 5.0)
    model_edge += 2.0 * pass_rate

    # Numeric plan: use the plan with best recommended_rr then closest trigger distance.
    chosen_plan = {}
    if plan_rows:
        chosen_plan = sorted(
            plan_rows,
            key=lambda r: (
                _to_float(r.get("recommended_rr"), -999) or -999,
                -abs(_to_float(r.get("entry_distance_pct"), 999) or 999),
            ),
            reverse=True,
        )[0]

    entry_dist = _to_float(chosen_plan.get("entry_distance_pct"), _to_float(base_row.get("entry_distance_pct"), None))
    risk_pct = _to_float(chosen_plan.get("risk_pct"), _to_float(base_row.get("risk_pct"), None))
    rr = _to_float(chosen_plan.get("recommended_rr"), _to_float(chosen_plan.get("rr_1"), None))
    plan_quality = str(chosen_plan.get("plan_quality") or "").upper()
    no_trade_reasons = str(chosen_plan.get("no_trade_reasons") or "").strip()

    execution = 0.0
    if entry_dist is not None:
        if entry_dist <= th.get("ideal_entry_distance_pct", 0.04):
            execution += 8
        elif entry_dist <= 0.07:
            execution += 5
        elif entry_dist <= th.get("max_entry_distance_pct", 0.12):
            execution += 2
    if risk_pct is not None:
        if risk_pct <= th.get("ideal_risk_pct", 0.065):
            execution += 7
        elif risk_pct <= 0.08:
            execution += 4
        elif risk_pct <= th.get("max_risk_pct", 0.10):
            execution += 1
    if rr is not None:
        if rr >= 2.0:
            execution += 7
        elif rr >= th.get("good_recommended_rr", 1.75):
            execution += 5
        elif rr >= th.get("min_recommended_rr", 1.25):
            execution += 3
    if "ACTIONABLE" in plan_quality:
        execution += 4
    elif "CONDITIONAL" in plan_quality:
        execution += 2
    if no_trade_reasons and no_trade_reasons.lower() not in {"none", "nan", "null"}:
        execution -= 4
    execution = max(0.0, min(30.0, execution))

    tv = _to_float(base_row.get("traded_value_proxy"), _to_float(base_row.get("value"), None))
    vol_ratio = _to_float(base_row.get("volume_ratio_20d"), _to_float(base_row.get("volume_ratio"), None))
    has_broksum = _truthy(base_row.get("has_broksum"))
    anomaly = _truthy(base_row.get("broker_value_anomaly_flag"))
    buyer_share = _to_float(base_row.get("rank1_buyer_daily_share"), None)
    has_bdm = _truthy(base_row.get("has_bdm_any")) or _truthy(base_row.get("has_bdm_market_maker")) or _truthy(base_row.get("has_bdm_non_retail"))

    liquidity = 0.0
    if tv is not None:
        if tv >= 100_000_000_000:
            liquidity += 5
        elif tv >= th.get("min_traded_value_core", 50_000_000_000):
            liquidity += 4
        elif tv >= 10_000_000_000:
            liquidity += 3
        elif tv >= th.get("min_traded_value_floor", 500_000_000):
            liquidity += 1
    if vol_ratio is not None:
        if th.get("volume_ratio_good", 1.0) <= vol_ratio <= th.get("volume_ratio_hot", 3.0):
            liquidity += 5
        elif th.get("volume_ratio_min", 0.7) <= vol_ratio <= 5.0:
            liquidity += 3
        elif vol_ratio > 5.0:
            liquidity += 1
    if has_broksum:
        liquidity += 3
    if has_bdm:
        liquidity += 2
    if buyer_share is not None:
        if buyer_share <= 0.20:
            liquidity += 3
        elif buyer_share <= 0.40:
            liquidity += 2
        elif buyer_share <= th.get("buyer_share_overcrowded", 0.50):
            liquidity += 1
    if anomaly:
        liquidity -= 4
    liquidity = max(0.0, min(20.0, liquidity))

    ret5 = _to_float(base_row.get("ret_5d"), None)
    ret20 = _to_float(base_row.get("ret_20d"), None)
    close_vs_ma20 = _to_float(base_row.get("close_vs_ma20"), None)
    vol20 = _to_float(base_row.get("volatility_20d"), None)
    market_regime = str(base_row.get("market_regime") or "").lower()

    structure = 0.0
    if ret5 is not None and ret20 is not None:
        if -0.40 <= ret5 <= -0.05 and -0.60 <= ret20 <= -0.10:
            structure += 5
        elif ret5 <= -0.40 or ret20 <= -0.65:
            structure += 2
        elif ret5 > 0 and ret20 > 0:
            structure += 3
    if close_vs_ma20 is not None:
        if close_vs_ma20 >= 0:
            structure += 3
        elif close_vs_ma20 >= -0.10:
            structure += 3
        elif close_vs_ma20 >= -0.25:
            structure += 2
        else:
            structure += 1
    if vol20 is not None:
        if vol20 <= 0.05:
            structure += 3
        elif vol20 <= th.get("volatility_high", 0.08):
            structure += 2
        elif vol20 <= 0.15:
            structure += 1
    if market_regime and market_regime != "risk_off":
        structure += 2
    elif market_regime == "risk_off":
        structure += 1
    structure = max(0.0, min(15.0, structure))

    net_flow = _to_float(base_row.get("net_flow_ratio"), None)
    streak = _to_int(base_row.get("rank1_same_buyer_streak"), 0)
    buyer_dom = _to_float(base_row.get("buyer_dominance_ratio"), None)

    broker = 0.0
    if net_flow is not None:
        if net_flow >= 0.02:
            broker += 3
        elif net_flow >= 0:
            broker += 2
        elif net_flow >= -0.02:
            broker += 1
    if 2 <= streak <= 6:
        broker += 3
    elif streak == 1:
        broker += 1
    elif streak > 6:
        broker += 1
    if buyer_dom is not None:
        if 0.15 <= buyer_dom <= 0.45:
            broker += 2
        elif 0.05 <= buyer_dom < 0.15:
            broker += 1
    if has_bdm:
        broker += 2
    broker = max(0.0, min(10.0, broker))

    total = model_edge + execution + liquidity + structure + broker
    total = max(0.0, min(100.0, total))

    trigger = _to_float(chosen_plan.get("entry_trigger"), None)
    latest_close = _to_float(chosen_plan.get("latest_close"), _to_float(base_row.get("close"), None))
    tick = _tick_size(latest_close or trigger)
    stop = _to_float(chosen_plan.get("stop_loss"), None)

    warnings: list[str] = []
    if no_trade_reasons and no_trade_reasons.lower() not in {"none", "nan", "null"}:
        warnings.append("numeric_no_trade_reason_present")
    if risk_pct is not None and risk_pct > th.get("ideal_risk_pct", 0.065):
        warnings.append("risk_above_ideal")
    if entry_dist is not None and entry_dist > th.get("ideal_entry_distance_pct", 0.04):
        warnings.append("trigger_not_close")
    if vol_ratio is not None and vol_ratio < th.get("volume_ratio_min", 0.7):
        warnings.append("volume_ratio_weak")
    if anomaly:
        warnings.append("broker_value_anomaly")
    if buyer_share is not None and buyer_share > th.get("buyer_share_overcrowded", 0.50):
        warnings.append("rank1_buyer_overcrowded")
    if close_vs_ma20 is not None and close_vs_ma20 < -0.20:
        warnings.append("still_far_below_ma20")

    return {
        "ticker": base_row.get("ticker"),
        "date": base_row.get("date") or chosen_plan.get("signal_date"),
        "readiness_score": round(total, 2),
        "readiness_tier": _tier(total),
        "setup_type": _setup_type(base_row, n_strat),
        "entry_style": _entry_style({**base_row, **chosen_plan}, strategies),
        "n_strategies": n_strat,
        "strategies": ";".join(strategies),
        "model_edge_score": round(model_edge, 2),
        "execution_geometry_score": round(execution, 2),
        "liquidity_behavior_score": round(liquidity, 2),
        "price_structure_score": round(structure, 2),
        "broker_flow_score": round(broker, 2),
        "max_strategy_score": None if max_strategy_score is None else round(max_strategy_score, 6),
        "mean_strategy_score": None if mean_strategy_score is None else round(mean_strategy_score, 6),
        "max_generic_score": None if max_generic_score is None else round(max_generic_score, 6),
        "max_generic_score_universe_pct": round(pct, 4),
        "score_breadth_ge_030": score_breadth,
        "score_strong_ge_050": score_strong_count,
        "entry_trigger": trigger,
        "entry_zone_low": _to_float(chosen_plan.get("entry_zone_low"), None),
        "entry_zone_high": _to_float(chosen_plan.get("entry_zone_high"), None),
        "stop_loss": stop,
        "target_1": _to_float(chosen_plan.get("target_1"), None),
        "target_2": _to_float(chosen_plan.get("target_2"), None),
        "target_3": _to_float(chosen_plan.get("target_3"), None),
        "latest_close": latest_close,
        "tick_size": tick,
        "trigger_tick_area": _trigger_area(trigger, tick),
        "entry_distance_pct": None if entry_dist is None else round(entry_dist, 6),
        "risk_pct": None if risk_pct is None else round(risk_pct, 6),
        "recommended_rr": None if rr is None else round(rr, 6),
        "plan_quality": plan_quality,
        "no_trade_reasons": no_trade_reasons,
        "traded_value_proxy": tv,
        "volume_ratio_20d": None if vol_ratio is None else round(vol_ratio, 6),
        "has_broksum": int(has_broksum),
        "broker_value_anomaly_flag": int(anomaly),
        "rank1_buyer": base_row.get("rank1_buyer"),
        "rank1_seller": base_row.get("rank1_seller"),
        "rank1_same_buyer_streak": streak,
        "rank1_buyer_daily_share": None if buyer_share is None else round(buyer_share, 6),
        "net_flow_ratio": None if net_flow is None else round(net_flow, 6),
        "buyer_dominance_ratio": None if buyer_dom is None else round(buyer_dom, 6),
        "has_bdm_any": int(has_bdm),
        "ret_5d": None if ret5 is None else round(ret5, 6),
        "ret_20d": None if ret20 is None else round(ret20, 6),
        "close_vs_ma20": None if close_vs_ma20 is None else round(close_vs_ma20, 6),
        "volatility_20d": None if vol20 is None else round(vol20, 6),
        "market_regime": base_row.get("market_regime"),
        "warnings": ";".join(warnings),
    }


def _trigger_area(trigger: float | None, tick: int | None) -> str:
    if trigger is None or tick is None:
        return ""
    lo = trigger - tick
    hi = trigger + tick
    return f"{int(lo) if lo.is_integer() else lo}-{int(hi) if hi.is_integer() else hi}"


def _build_universe_stats(all_scores: list[dict[str, Any]]) -> dict[str, list[float]]:
    vals: list[float] = []
    for r in all_scores:
        row_vals = []
        for c in GENERIC_SCORE_COLS:
            v = _to_float(r.get(c), None)
            if v is not None:
                row_vals.append(v)
        if row_vals:
            vals.append(max(row_vals))
    return {"max_generic_score": vals}


def _render_report(rows: list[dict[str, Any]], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Execution Readiness Score Report")
    lines.append("")
    lines.append("This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.")
    lines.append("")
    if not rows:
        lines.append("No rows generated.")
        out_path.write_text("\n".join(lines), encoding="utf-8")
        return
    tier_counts = defaultdict(int)
    for r in rows:
        tier_counts[r["readiness_tier"]] += 1
    lines.append("## Tier counts")
    lines.append("")
    for t in ["A_READY_WNS", "B_WATCH_CONFIRM", "C_CONDITIONAL", "D_LOW_PRIORITY"]:
        lines.append(f"- {t}: {tier_counts[t]}")
    lines.append("")
    lines.append("## Top candidates")
    lines.append("")
    lines.append("| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |")
    lines.append("|---:|---|---:|---|---|---:|---:|---:|---:|---|")
    for i, r in enumerate(rows[:20], 1):
        lines.append(
            f"| {i} | {r.get('ticker')} | {r.get('readiness_score')} | {r.get('readiness_tier')} | {r.get('setup_type')} | {r.get('n_strategies')} | {r.get('entry_trigger')} | {r.get('stop_loss')} | {r.get('recommended_rr')} | {r.get('warnings','')} |"
        )
    lines.append("")
    lines.append("## Execution notes")
    lines.append("")
    lines.append("- A tier means priority WNS, not automatic buy.")
    lines.append("- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.")
    lines.append("- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.")
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="Build Execution Readiness Score from daily signal watchlist + numeric trade plan + all_scores universe.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--signal-dir", default=None, help="Signal profile dir, e.g. signals/daily/signal_26_may_2026/continual_model")
    ap.add_argument("--watchlist", default=None, help="Optional explicit all_strategy_watchlist.csv path")
    ap.add_argument("--numeric-plan", default=None, help="Optional explicit numeric_trade_plan.json path")
    ap.add_argument("--all-scores", default=None, help="Optional explicit all_scores.csv path for universe percentiles")
    ap.add_argument("--policy", default="configs/execution_readiness_policy.json")
    ap.add_argument("--output-dir", default=None)
    ap.add_argument("--top-n", type=int, default=12)
    args = ap.parse_args()

    root = Path(args.root).resolve()
    signal_dir = (root / args.signal_dir).resolve() if args.signal_dir else None
    watchlist_path = Path(args.watchlist).resolve() if args.watchlist else (signal_dir / "all_strategy_watchlist.csv" if signal_dir else None)
    numeric_path = Path(args.numeric_plan).resolve() if args.numeric_plan else (signal_dir / "numeric_trade_plan.json" if signal_dir else None)
    all_scores_path = Path(args.all_scores).resolve() if args.all_scores else (signal_dir / "all_scores.csv" if signal_dir else None)
    policy = _load_json(root / args.policy, {})

    if watchlist_path is None or not watchlist_path.exists():
        raise SystemExit(f"Watchlist file not found: {watchlist_path}")

    output_dir = Path(args.output_dir).resolve() if args.output_dir else (signal_dir if signal_dir else watchlist_path.parent)
    output_dir.mkdir(parents=True, exist_ok=True)

    watchlist = _read_csv(watchlist_path)
    all_scores = _read_csv(all_scores_path) if all_scores_path and all_scores_path.exists() else []
    numeric = _load_json(numeric_path, []) if numeric_path and numeric_path.exists() else []
    if isinstance(numeric, dict):
        numeric = numeric.get("plans") or numeric.get("rows") or []

    universe_stats = _build_universe_stats(all_scores if all_scores else watchlist)

    grouped_strategy: dict[str, list[dict[str, Any]]] = defaultdict(list)
    base_by_ticker: dict[str, dict[str, Any]] = {}
    for r in watchlist:
        t = str(r.get("ticker") or "").strip()
        if not t:
            continue
        grouped_strategy[t].append(r)
        # Prefer row with highest strategy_score as representative base row.
        if t not in base_by_ticker or (_to_float(r.get("strategy_score"), -1) or -1) > (_to_float(base_by_ticker[t].get("strategy_score"), -1) or -1):
            base_by_ticker[t] = r

    plans_by_ticker: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in numeric or []:
        t = str(r.get("ticker") or "").strip()
        if t:
            plans_by_ticker[t].append(r)

    rows: list[dict[str, Any]] = []
    for ticker, srows in grouped_strategy.items():
        row = _score_components(base_by_ticker[ticker], srows, plans_by_ticker.get(ticker, []), universe_stats, policy)
        rows.append(row)
    rows.sort(key=lambda r: (r.get("readiness_score") or 0, r.get("n_strategies") or 0, r.get("max_generic_score") or 0), reverse=True)

    out_cfg = policy.get("output", {})
    csv_path = output_dir / out_cfg.get("readiness_csv", "execution_readiness.csv")
    json_path = output_dir / out_cfg.get("readiness_json", "execution_readiness.json")
    short_path = output_dir / out_cfg.get("priority_shortlist_csv", "execution_priority_shortlist.csv")
    report_path = output_dir / out_cfg.get("report_md", "execution_readiness_report.md")

    _write_csv(csv_path, rows)
    json_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    _write_csv(short_path, rows[: args.top_n])
    _render_report(rows, report_path)

    print(json.dumps({
        "watchlist": str(watchlist_path),
        "numeric_plan": str(numeric_path) if numeric_path else None,
        "all_scores": str(all_scores_path) if all_scores_path else None,
        "rows": len(rows),
        "output_dir": str(output_dir),
        "readiness_csv": str(csv_path),
        "priority_shortlist_csv": str(short_path),
        "report_md": str(report_path),
        "tier_counts": {t: sum(1 for r in rows if r.get("readiness_tier") == t) for t in ["A_READY_WNS", "B_WATCH_CONFIRM", "C_CONDITIONAL", "D_LOW_PRIORITY"]},
    }, indent=2))


if __name__ == "__main__":
    main()
