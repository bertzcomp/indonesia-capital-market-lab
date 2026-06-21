from __future__ import annotations

import csv
import json
import math
import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import polars as pl


# ---------------------------------------------------------------------------
# General helpers
# ---------------------------------------------------------------------------

MONTH_ABBR = {
    1: "jan", 2: "feb", 3: "mar", 4: "apr", 5: "may", 6: "jun",
    7: "jul", 8: "aug", 9: "sep", 10: "oct", 11: "nov", 12: "dec",
}


def _read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _safe_float(x: Any, default: Optional[float] = None) -> Optional[float]:
    if x is None:
        return default
    try:
        if isinstance(x, str) and x.strip() == "":
            return default
        v = float(x)
        if math.isnan(v) or math.isinf(v):
            return default
        return v
    except Exception:
        return default


def _safe_int(x: Any, default: int = 0) -> int:
    try:
        if x is None:
            return default
        if isinstance(x, str) and x.strip() == "":
            return default
        return int(float(x))
    except Exception:
        return default


def _fmt_float(x: Any, digits: int = 2, na: str = "n/a") -> str:
    v = _safe_float(x)
    if v is None:
        return na
    if digits <= 0:
        return f"{v:,.0f}"
    return f"{v:,.{digits}f}"


def _fmt_pct(x: Any, digits: int = 2, na: str = "n/a") -> str:
    v = _safe_float(x)
    if v is None:
        return na
    return f"{v*100:.{digits}f}%"


def _fmt_rr(x: Any, na: str = "n/a") -> str:
    v = _safe_float(x)
    if v is None:
        return na
    return f"{v:.2f}R"


def _idx_tick(price: float) -> int:
    # IDX-style tick approximation. It is intentionally conservative and
    # adequate for report rounding, not for order-routing.
    p = float(price)
    if p < 200:
        return 1
    if p < 500:
        return 2
    if p < 2000:
        return 5
    if p < 5000:
        return 10
    return 25


def _round_to_tick(value: float, mode: str = "nearest") -> float:
    if value is None or math.isnan(value) or math.isinf(value):
        return float("nan")
    tick = _idx_tick(value)
    if mode == "up":
        return math.ceil(value / tick) * tick
    if mode == "down":
        return math.floor(value / tick) * tick
    return round(value / tick) * tick


def _to_date_str(d: Any) -> str:
    if d is None:
        return ""
    if isinstance(d, date):
        return d.isoformat()
    s = str(d)
    if " " in s:
        s = s.split(" ")[0]
    return s


def _parse_target_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def _signal_dir_from_target(root: Path, target_date: str) -> Path:
    d = _parse_target_date(target_date)
    candidates = [
        root / "signals" / "daily" / f"signal_{d.day:02d}_{MONTH_ABBR[d.month]}_{d.year}",
        root / "signals" / "daily" / f"signal_{d.day}_{MONTH_ABBR[d.month]}_{d.year}",
        root / "signals" / "daily" / f"signal_{d.isoformat()}",
    ]
    for c in candidates:
        if c.exists():
            return c
    # fallback: search by year/month/day tokens
    base = root / "signals" / "daily"
    if base.exists():
        tokens = [str(d.year), MONTH_ABBR[d.month], str(d.day)]
        for p in sorted(base.glob("signal_*")):
            low = p.name.lower()
            if all(t in low for t in tokens):
                return p
    return candidates[0]


def _load_signal_frame(signal_dir: Path, source_file: str) -> pl.DataFrame:
    path = signal_dir / source_file
    fallbacks = [
        source_file,
        "all_strategy_watchlist.csv",
        "all_strategy_candidates.csv",
        "signals_main.csv",
        "execution_shortlist.csv",
    ]
    seen = set()
    for name in fallbacks:
        if name in seen:
            continue
        seen.add(name)
        p = signal_dir / name
        if p.exists():
            return pl.read_csv(p, infer_schema_length=10000)
    raise FileNotFoundError(
        f"Could not find source signal file in {signal_dir}. Tried: {fallbacks}"
    )


def _normalize_ticker_col(df: pl.DataFrame) -> pl.DataFrame:
    if "ticker" not in df.columns:
        raise ValueError("Signal file must contain a ticker column")
    return df.with_columns(pl.col("ticker").cast(pl.Utf8).str.to_uppercase().alias("ticker"))


def _extract_policy_strategies(policy: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    if not policy:
        return {}
    if isinstance(policy.get("strategies"), dict):
        return policy["strategies"]
    # Backward-compatible formats
    out: Dict[str, Dict[str, Any]] = {}
    for group in ["core_execution", "aggressive_challenger", "watchlist_only"]:
        items = policy.get(group, [])
        if isinstance(items, list):
            for obj in items:
                if isinstance(obj, dict) and "name" in obj:
                    out[obj["name"]] = obj
    if isinstance(policy.get("champion_strategies"), dict):
        out.update(policy["champion_strategies"])
    return out


def _guess_strategy_key(row: Dict[str, Any], strategies: Dict[str, Dict[str, Any]]) -> str:
    for col in ["strategy_key", "strategy_name", "strategy", "strategy_tag", "strategy_id"]:
        v = row.get(col)
        if v is not None and str(v).strip():
            s = str(v).strip()
            if s in strategies:
                return s
            # try normalized contains
            for k in strategies:
                if k.lower() == s.lower():
                    return k
            return s

    # infer from score_col if available
    score_col = str(row.get("score_col") or "")
    if score_col:
        for k, spec in strategies.items():
            if spec.get("score_col") == score_col:
                return k

    # infer from non-null score columns
    for k, spec in strategies.items():
        sc = spec.get("score_col")
        if sc and row.get(sc) is not None:
            return k
    return "unknown_strategy"


def _get_score(row: Dict[str, Any], strategy_key: str, strategy_spec: Dict[str, Any]) -> Optional[float]:
    score_col = strategy_spec.get("score_col")
    if score_col and score_col in row:
        v = _safe_float(row.get(score_col))
        if v is not None:
            return v
    for c in ["score", "selected_score", "policy_score", "model_score"]:
        if c in row:
            v = _safe_float(row.get(c))
            if v is not None:
                return v
    # fallback: any score-like column for strategy
    for c, x in row.items():
        if isinstance(c, str) and c.startswith("score_"):
            v = _safe_float(x)
            if v is not None:
                return v
    return None


def _load_ohlcv(root: Path) -> pl.DataFrame:
    p = root / "data" / "raw_canonical" / "ohlcv.parquet"
    if not p.exists():
        raise FileNotFoundError(f"Missing canonical OHLCV: {p}")
    df = pl.read_parquet(p)
    if "date" not in df.columns or "ticker" not in df.columns:
        raise ValueError(f"OHLCV must contain date/ticker columns: {p}")
    return (
        df.with_columns([
            pl.col("date").cast(pl.Date),
            pl.col("ticker").cast(pl.Utf8).str.to_uppercase(),
        ])
        .sort(["ticker", "date"])
    )


def _load_live_features(root: Path) -> Optional[pl.DataFrame]:
    p = root / "data" / "features" / "live" / "latest" / "base_features.parquet"
    if not p.exists():
        return None
    try:
        return (
            pl.read_parquet(p)
            .with_columns([
                pl.col("date").cast(pl.Date),
                pl.col("ticker").cast(pl.Utf8).str.to_uppercase(),
            ])
        )
    except Exception:
        return None


def _determine_signal_date(signals: pl.DataFrame, live_df: Optional[pl.DataFrame], ohlcv: pl.DataFrame, target_date: Optional[str]) -> date:
    if "date" in signals.columns:
        try:
            mx = signals.select(pl.col("date").cast(pl.Date).max()).item()
            if mx:
                return mx
        except Exception:
            pass
    if live_df is not None and not live_df.is_empty():
        mx = live_df.select(pl.col("date").max()).item()
        if mx:
            return mx
    if target_date:
        td = _parse_target_date(target_date)
        # signal source is usually previous market date
        candidates = ohlcv.filter(pl.col("date") < td)
        if not candidates.is_empty():
            return candidates.select(pl.col("date").max()).item()
    return ohlcv.select(pl.col("date").max()).item()


# ---------------------------------------------------------------------------
# Market structure engine
# ---------------------------------------------------------------------------

@dataclass
class Structure:
    ticker: str
    signal_date: date
    close: float
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    volume: Optional[float]
    value: Optional[float]
    atr14: float
    support_5: Optional[float]
    support_10: Optional[float]
    support_20: Optional[float]
    resistance_5: Optional[float]
    resistance_10: Optional[float]
    resistance_20: Optional[float]
    resistance_60: Optional[float]
    volume_ma20: Optional[float]
    volume_ratio_20d: Optional[float]
    ret_5d: Optional[float]
    ret_20d: Optional[float]


def _true_range_rows(rows: List[Dict[str, Any]]) -> List[float]:
    trs: List[float] = []
    prev_close: Optional[float] = None
    for r in rows:
        h = _safe_float(r.get("high"))
        l = _safe_float(r.get("low"))
        c = _safe_float(r.get("close"))
        if h is None or l is None or c is None:
            prev_close = c
            continue
        if prev_close is None:
            tr = h - l
        else:
            tr = max(h - l, abs(h - prev_close), abs(l - prev_close))
        if tr >= 0:
            trs.append(tr)
        prev_close = c
    return trs


def _build_structures(ohlcv: pl.DataFrame, tickers: List[str], signal_date: date) -> Dict[str, Structure]:
    out: Dict[str, Structure] = {}
    subset = (
        ohlcv
        .filter((pl.col("ticker").is_in(tickers)) & (pl.col("date") <= signal_date))
        .sort(["ticker", "date"])
    )
    if subset.is_empty():
        return out

    for t in tickers:
        h = subset.filter(pl.col("ticker") == t).tail(90)
        if h.is_empty():
            continue
        rows = h.to_dicts()
        last = rows[-1]
        close = _safe_float(last.get("close"))
        if close is None or close <= 0:
            continue

        def lows(n: int) -> List[float]:
            return [v for v in (_safe_float(r.get("low")) for r in rows[-n:]) if v is not None and v > 0]

        def highs(n: int) -> List[float]:
            return [v for v in (_safe_float(r.get("high")) for r in rows[-n:]) if v is not None and v > 0]

        def closes(n: int) -> List[float]:
            return [v for v in (_safe_float(r.get("close")) for r in rows[-n:]) if v is not None and v > 0]

        trs = _true_range_rows(rows[-20:])
        atr14 = sum(trs[-14:]) / max(1, len(trs[-14:])) if trs else max(close * 0.025, _idx_tick(close))

        vols20 = [v for v in (_safe_float(r.get("volume")) for r in rows[-20:]) if v is not None]
        vol_ma20 = sum(vols20) / len(vols20) if vols20 else None
        vol = _safe_float(last.get("volume"))
        vol_ratio = (vol / vol_ma20) if vol is not None and vol_ma20 and vol_ma20 > 0 else None

        c5 = closes(6)
        c20 = closes(21)
        ret5 = (c5[-1] / c5[0] - 1.0) if len(c5) >= 2 and c5[0] else None
        ret20 = (c20[-1] / c20[0] - 1.0) if len(c20) >= 2 and c20[0] else None

        out[t] = Structure(
            ticker=t,
            signal_date=signal_date,
            close=close,
            open=_safe_float(last.get("open")),
            high=_safe_float(last.get("high")),
            low=_safe_float(last.get("low")),
            volume=vol,
            value=_safe_float(last.get("value")),
            atr14=atr14 if atr14 > 0 else max(close * 0.025, _idx_tick(close)),
            support_5=min(lows(5)) if lows(5) else None,
            support_10=min(lows(10)) if lows(10) else None,
            support_20=min(lows(20)) if lows(20) else None,
            resistance_5=max(highs(5)) if highs(5) else None,
            resistance_10=max(highs(10)) if highs(10) else None,
            resistance_20=max(highs(20)) if highs(20) else None,
            resistance_60=max(highs(60)) if highs(60) else None,
            volume_ma20=vol_ma20,
            volume_ratio_20d=vol_ratio,
            ret_5d=ret5,
            ret_20d=ret20,
        )
    return out


# ---------------------------------------------------------------------------
# Strategy-aware numeric plan
# ---------------------------------------------------------------------------

DEFAULT_NUMERIC_POLICY: Dict[str, Any] = {
    "version": "numeric_report_policy_v3",
    "source": "desk_grade_strategy_aware_numeric_report",
    "global": {
        "max_risk_pct_default": 0.08,
        "min_volume_ratio_for_execution": 0.60,
        "minimum_tick_risk": 2,
        "default_min_score": 0.50,
        "include_watchlist_below_threshold": True,
    },
    "strategy_rules": {
        "ara_candidate": {
            "entry_style": "breakout_confirmation",
            "max_entry_distance_pct": 0.12,
            "stop_atr_mult": 1.10,
            "max_risk_pct": 0.10,
            "target_atr_mults": [1.0, 2.0, 3.2],
            "min_rr_execution": 1.30,
            "risk_note": "high drawdown tactical setup; confirmation is mandatory",
        },
        "market_maker_silent_accum_defensive": {
            "entry_style": "retest_or_controlled_breakout",
            "max_entry_distance_pct": 0.08,
            "stop_atr_mult": 1.20,
            "max_risk_pct": 0.075,
            "target_atr_mults": [1.0, 1.8, 2.5],
            "min_rr_execution": 1.25,
            "risk_note": "defensive accumulation setup; prefer controlled pullback/retest",
        },
        "momentum_5d_hgb_defensive": {
            "entry_style": "controlled_momentum_breakout",
            "max_entry_distance_pct": 0.08,
            "stop_atr_mult": 1.15,
            "max_risk_pct": 0.07,
            "target_atr_mults": [1.0, 1.7, 2.6],
            "min_rr_execution": 1.25,
            "risk_note": "selective high-liquidity 5D momentum",
        },
        "momentum_10d_hgb_aggressive": {
            "entry_style": "momentum_breakout",
            "max_entry_distance_pct": 0.15,
            "stop_atr_mult": 1.30,
            "max_risk_pct": 0.10,
            "target_atr_mults": [1.3, 2.3, 3.5],
            "min_rr_execution": 1.40,
            "risk_note": "aggressive momentum; avoid chasing extended triggers",
        },
        "scalping_rank_hgb": {
            "entry_style": "tight_breakout_or_retest",
            "max_entry_distance_pct": 0.05,
            "stop_atr_mult": 0.90,
            "max_risk_pct": 0.045,
            "target_atr_mults": [0.75, 1.15, 1.60],
            "min_rr_execution": 1.10,
            "risk_note": "top-1 short-horizon scalp; invalidation must be quick",
        },
        "swing_hgb_defensive": {
            "entry_style": "pullback_retest",
            "max_entry_distance_pct": 0.08,
            "stop_atr_mult": 1.20,
            "max_risk_pct": 0.075,
            "target_atr_mults": [1.0, 1.8, 2.5],
            "min_rr_execution": 1.25,
            "risk_note": "core defensive swing; do not chase far from close",
        },
        "position_xgb": {
            "entry_style": "structured_pullback_or_breakout",
            "max_entry_distance_pct": 0.10,
            "stop_atr_mult": 1.40,
            "max_risk_pct": 0.09,
            "target_atr_mults": [1.4, 2.4, 3.8],
            "min_rr_execution": 1.35,
            "risk_note": "moderate position sleeve; target can be wider but must be staged",
        },
        "default": {
            "entry_style": "hybrid",
            "max_entry_distance_pct": 0.08,
            "stop_atr_mult": 1.20,
            "max_risk_pct": 0.08,
            "target_atr_mults": [1.0, 1.8, 2.5],
            "min_rr_execution": 1.25,
            "risk_note": "generic strategy rule",
        },
    },
}


def _merge_dict(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(a)
    for k, v in (b or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _merge_dict(out[k], v)
        else:
            out[k] = v
    return out


def _get_strategy_rule(cfg: Dict[str, Any], strategy_key: str) -> Dict[str, Any]:
    rules = cfg.get("strategy_rules", {})
    default = rules.get("default", DEFAULT_NUMERIC_POLICY["strategy_rules"]["default"])
    return _merge_dict(default, rules.get(strategy_key, {}))


def _nearest_resistance_above(entry: float, values: Iterable[Optional[float]], min_gap: float) -> Optional[float]:
    candidates = []
    for v in values:
        x = _safe_float(v)
        if x is not None and x > entry + min_gap:
            candidates.append(x)
    return min(candidates) if candidates else None


def _compute_entry(struct: Structure, strategy_key: str, rule: Dict[str, Any]) -> Tuple[float, float, float, str]:
    close = struct.close
    atr = struct.atr14
    tick = _idx_tick(close)
    style = str(rule.get("entry_style", "hybrid"))

    if style in {"pullback_retest", "structured_pullback_or_breakout"}:
        zone_low = _round_to_tick(max(close - 0.45 * atr, close * 0.92), "down")
        zone_high = _round_to_tick(close + 0.10 * atr, "up")
        trigger = zone_high
        basis = (
            f"Entry is a controlled pullback/retest plan around close {_fmt_float(close,0)}: "
            f"zone {_fmt_float(zone_low,0)}–{_fmt_float(zone_high,0)} uses ATR14 {_fmt_float(atr,1)} "
            f"so the trade avoids chasing a far breakout."
        )
        return trigger, zone_low, zone_high, basis

    if style in {"tight_breakout_or_retest", "breakout_confirmation", "controlled_momentum_breakout", "momentum_breakout"}:
        lookback_res = struct.resistance_5 if style == "tight_breakout_or_retest" else struct.resistance_10
        if lookback_res is None:
            lookback_res = struct.resistance_5 or struct.resistance_20 or close
        trigger = _round_to_tick(max(close + tick, lookback_res + tick), "up")
        # buy zone below trigger, not above it
        zone_low = _round_to_tick(max(close - 0.20 * atr, close * 0.92), "down")
        zone_high = trigger
        basis = (
            f"Entry trigger {_fmt_float(trigger,0)} is set above recent resistance "
            f"{_fmt_float(lookback_res,0)} plus one IDX tick. This requires confirmation instead of buying blindly at close "
            f"{_fmt_float(close,0)}."
        )
        return trigger, zone_low, zone_high, basis

    # hybrid fallback
    zone_low = _round_to_tick(close - 0.35 * atr, "down")
    trigger = _round_to_tick(close + 0.20 * atr, "up")
    zone_high = trigger
    basis = (
        f"Hybrid entry uses close {_fmt_float(close,0)} and ATR14 {_fmt_float(atr,1)}: "
        f"buy zone {_fmt_float(zone_low,0)}–{_fmt_float(zone_high,0)}."
    )
    return trigger, zone_low, zone_high, basis


def _compute_stop(struct: Structure, entry: float, rule: Dict[str, Any]) -> Tuple[float, str]:
    atr = struct.atr14
    tick = _idx_tick(entry)
    stop_atr_mult = float(rule.get("stop_atr_mult", 1.2))
    max_risk_pct = float(rule.get("max_risk_pct", 0.08))

    structural_candidates = [
        x for x in [struct.support_10, struct.support_20]
        if x is not None and x < entry
    ]
    structural_stop = None
    if structural_candidates:
        structural_stop = _round_to_tick(max(structural_candidates) - tick, "down")

    atr_stop = _round_to_tick(entry - stop_atr_mult * atr, "down")
    max_risk_stop = _round_to_tick(entry * (1 - max_risk_pct), "down")

    # Prefer structure if it is not too far. If structure is too deep, cap with ATR/max-risk.
    candidates = [x for x in [structural_stop, atr_stop, max_risk_stop] if x is not None and x < entry]
    if not candidates:
        stop = _round_to_tick(entry - max(2 * tick, 0.03 * entry), "down")
        reason = (
            f"Stop {_fmt_float(stop,0)} is fallback because no reliable support/ATR stop was available. "
            f"Setup invalidates if price loses this emergency risk level."
        )
        return stop, reason

    # Higher stop = smaller risk, but it must still be below entry. It acts as capped structural invalidation.
    stop = max(candidates)
    if structural_stop is not None and stop == structural_stop:
        reason = (
            f"Stop {_fmt_float(stop,0)} is placed below support structure "
            f"({_fmt_float(struct.support_10,0)} / {_fmt_float(struct.support_20,0)}). "
            f"A breakdown below this area invalidates the thesis because support/retest behaviour fails."
        )
    elif stop == atr_stop:
        reason = (
            f"Stop {_fmt_float(stop,0)} uses {stop_atr_mult:.2f}×ATR14 volatility cap. "
            f"Thesis invalidates if the move reverses beyond normal volatility."
        )
    else:
        reason = (
            f"Stop {_fmt_float(stop,0)} is capped by max risk {max_risk_pct*100:.1f}% from entry. "
            f"This prevents a structurally attractive setup from becoming oversized risk."
        )
    return stop, reason


def _compute_targets(struct: Structure, entry: float, stop: float, hold_days: int, rule: Dict[str, Any]) -> Tuple[List[float], str]:
    risk = max(entry - stop, _idx_tick(entry))
    atr = struct.atr14
    mults = rule.get("target_atr_mults", [1.0, 1.8, 2.5])
    if not isinstance(mults, list) or len(mults) < 3:
        mults = [1.0, 1.8, 2.5]
    sqrt_hold = math.sqrt(max(1, hold_days))

    resistances = [struct.resistance_5, struct.resistance_10, struct.resistance_20, struct.resistance_60]
    nearest = _nearest_resistance_above(entry, resistances, min_gap=max(0.25 * atr, _idx_tick(entry)))

    targets: List[float] = []
    rationale_parts = []

    for i, mult in enumerate(mults[:3]):
        atr_cap = entry + float(mult) * atr * sqrt_hold
        rr_floor = entry + [1.0, 1.7, 2.4][i] * risk
        raw = max(rr_floor, entry + 0.5 * atr)
        if nearest is not None and nearest <= atr_cap * 1.05:
            # If structure is within realistic ATR envelope, respect it.
            raw = max(raw, nearest if i == 0 else min(atr_cap, max(nearest, rr_floor)))
        else:
            raw = min(raw, atr_cap)
        target = _round_to_tick(max(raw, entry + _idx_tick(entry)), "up")
        # enforce monotonic targets
        if targets and target <= targets[-1]:
            target = _round_to_tick(targets[-1] + max(_idx_tick(targets[-1]), 0.50 * risk), "up")
        # do not exceed the ATR cap wildly
        max_target = _round_to_tick(atr_cap, "up")
        if target > max_target and i < 2:
            target = max_target
        targets.append(target)

    rationale_parts.append(
        f"Targets are ATR/structure capped for hold_days={hold_days}. "
        f"ATR14={_fmt_float(atr,1)}, resistance_5/10/20/60="
        f"{_fmt_float(struct.resistance_5,0)}/{_fmt_float(struct.resistance_10,0)}/"
        f"{_fmt_float(struct.resistance_20,0)}/{_fmt_float(struct.resistance_60,0)}."
    )
    rationale_parts.append(
        "TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case."
    )
    return targets, " ".join(rationale_parts)


def _quality_and_reasons(
    *,
    score: Optional[float],
    min_score: float,
    execution_enabled: bool,
    entry_distance_pct: float,
    risk_pct: float,
    rr1: Optional[float],
    volume_ratio: Optional[float],
    rule: Dict[str, Any],
    row: Dict[str, Any],
) -> Tuple[str, List[str], List[str]]:
    hard: List[str] = []
    soft: List[str] = []

    max_entry_distance = float(rule.get("max_entry_distance_pct", 0.08))
    max_risk_pct = float(rule.get("max_risk_pct", 0.08))
    min_rr = float(rule.get("min_rr_execution", 1.25))

    if not execution_enabled:
        hard.append("strategy policy has execution_enabled=false")
    if score is None:
        soft.append("model score unavailable")
    elif score < min_score:
        soft.append(f"score {_fmt_float(score,3)} below policy min_score {_fmt_float(min_score,2)}")
    if entry_distance_pct > max_entry_distance:
        hard.append(
            f"entry trigger is too far from latest close: {_fmt_pct(entry_distance_pct)} > max {_fmt_pct(max_entry_distance)}"
        )
    if risk_pct > max_risk_pct:
        hard.append(
            f"entry-to-stop risk {_fmt_pct(risk_pct)} exceeds max strategy risk {_fmt_pct(max_risk_pct)}"
        )
    if rr1 is not None and rr1 < min_rr:
        soft.append(f"TP1 reward/risk {_fmt_rr(rr1)} is below strategy minimum {_fmt_rr(min_rr)}")
    min_vol = _safe_float(rule.get("min_volume_ratio_for_execution"))
    if min_vol is None:
        min_vol = None
    if volume_ratio is not None and min_vol is not None and volume_ratio < min_vol:
        soft.append(f"volume ratio {_fmt_float(volume_ratio,2)} below required {_fmt_float(min_vol,2)}")
    risk_flags = str(row.get("risk_flags") or "")
    if "DOMINANT_RANK1_BUYER" in risk_flags:
        soft.append("dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow")

    if hard:
        status = "NO_TRADE"
    elif soft:
        status = "CONDITIONAL"
    else:
        status = "ACTIONABLE"

    return status, hard, soft


def _calc_trade_plan(
    row: Dict[str, Any],
    struct: Structure,
    signal_policy: Dict[str, Any],
    numeric_cfg: Dict[str, Any],
) -> Dict[str, Any]:
    strategies = _extract_policy_strategies(signal_policy)
    strategy_key = _guess_strategy_key(row, strategies)
    strategy_spec = strategies.get(strategy_key, {})

    rule = _get_strategy_rule(numeric_cfg, strategy_key)
    # inherit global min volume threshold unless strategy rule overrides
    if "min_volume_ratio_for_execution" not in rule:
        rule["min_volume_ratio_for_execution"] = numeric_cfg.get("global", {}).get("min_volume_ratio_for_execution", 0.60)

    score = _get_score(row, strategy_key, strategy_spec)
    min_score = _safe_float(strategy_spec.get("min_score"), numeric_cfg.get("global", {}).get("default_min_score", 0.5))
    hold_days = _safe_int(strategy_spec.get("hold_days"), 1)
    execution_enabled = bool(strategy_spec.get("execution_enabled", True))

    entry, zone_low, zone_high, entry_reason = _compute_entry(struct, strategy_key, rule)
    stop, stop_reason = _compute_stop(struct, entry, rule)
    risk_points = max(entry - stop, _idx_tick(entry))
    risk_pct = risk_points / entry if entry else None
    targets, target_reason = _compute_targets(struct, entry, stop, hold_days, rule)

    rr = [((t - entry) / risk_points if risk_points > 0 else None) for t in targets]
    entry_distance_pct = max(0.0, (entry - struct.close) / struct.close)

    status, hard_reasons, soft_reasons = _quality_and_reasons(
        score=score,
        min_score=float(min_score or 0.5),
        execution_enabled=execution_enabled,
        entry_distance_pct=entry_distance_pct,
        risk_pct=float(risk_pct or 0),
        rr1=rr[0],
        volume_ratio=struct.volume_ratio_20d,
        rule=rule,
        row=row,
    )

    if score is not None and score < float(min_score or 0.5) and status == "CONDITIONAL":
        plan_quality = "WATCHLIST_ONLY"
    else:
        plan_quality = status

    ticker = str(row.get("ticker", struct.ticker)).upper()

    why_entry = (
        f"{entry_reason} Entry is valid only if price can trade/hold around "
        f"{_fmt_float(entry,0)} without immediate rejection. If price gaps far above trigger, wait for retest."
    )
    why_stop = (
        f"{stop_reason} This stop is not a random number; it is the invalidation level for the structure/volatility thesis."
    )
    why_targets = (
        f"TP1 {_fmt_float(targets[0],0)} ({_fmt_rr(rr[0])}), "
        f"TP2 {_fmt_float(targets[1],0)} ({_fmt_rr(rr[1])}), "
        f"TP3 {_fmt_float(targets[2],0)} ({_fmt_rr(rr[2])}). {target_reason}"
    )

    no_trade_reasons = hard_reasons + soft_reasons
    if not no_trade_reasons:
        no_trade_reasons = [
            "No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation."
        ]

    return {
        "ticker": ticker,
        "signal_date": _to_date_str(struct.signal_date),
        "strategy": strategy_key,
        "role": strategy_spec.get("role", ""),
        "risk_profile": strategy_spec.get("risk_profile", ""),
        "score": score,
        "min_score": min_score,
        "execution_enabled": execution_enabled,
        "plan_quality": plan_quality,
        "latest_close": struct.close,
        "atr14": struct.atr14,
        "volume_ratio_20d": struct.volume_ratio_20d,
        "ret_5d": struct.ret_5d,
        "ret_20d": struct.ret_20d,
        "support_5d": struct.support_5,
        "support_10d": struct.support_10,
        "support_20d": struct.support_20,
        "resistance_5d": struct.resistance_5,
        "resistance_10d": struct.resistance_10,
        "resistance_20d": struct.resistance_20,
        "resistance_60d": struct.resistance_60,
        "entry_zone_low": zone_low,
        "entry_zone_high": zone_high,
        "entry_trigger": entry,
        "entry_distance_pct": entry_distance_pct,
        "stop_loss": stop,
        "risk_points": risk_points,
        "risk_pct": risk_pct,
        "target_1": targets[0],
        "target_2": targets[1],
        "target_3": targets[2],
        "rr_1": rr[0],
        "rr_2": rr[1],
        "rr_3": rr[2],
        "recommended_rr": rr[1],
        "hold_days": hold_days,
        "why_entry": why_entry,
        "why_stop": why_stop,
        "why_targets": why_targets,
        "no_trade_reasons": "; ".join(no_trade_reasons),
        "risk_note": rule.get("risk_note", ""),
        "rank1_buyer": row.get("rank1_buyer", ""),
        "risk_flags": row.get("risk_flags", ""),
        "source_score_col": strategy_spec.get("score_col", ""),
    }


def _write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    keys: List[str] = []
    seen = set()
    for r in rows:
        for k in r:
            if k not in seen:
                seen.add(k)
                keys.append(k)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in keys})


def _json_safe(obj: Any) -> Any:
    if isinstance(obj, (date, datetime)):
        return obj.isoformat()
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
    if isinstance(obj, dict):
        return {k: _json_safe(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_json_safe(v) for v in obj]
    return obj


def _build_markdown(plans: List[Dict[str, Any]], signal_dir: Path, target_date: Optional[str]) -> str:
    lines: List[str] = []
    title_date = target_date or (plans[0].get("signal_date") if plans else "unknown")
    lines.append(f"# Numeric Trading Desk Report — {title_date}")
    lines.append("")
    lines.append("This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.")
    lines.append("")
    if not plans:
        lines.append("No signals available.")
        return "\n".join(lines)

    counts: Dict[str, int] = {}
    for p in plans:
        counts[p["plan_quality"]] = counts.get(p["plan_quality"], 0) + 1
    lines.append("## Summary")
    lines.append("")
    lines.append("| Plan quality | Count |")
    lines.append("|---|---:|")
    for k in ["ACTIONABLE", "CONDITIONAL", "WATCHLIST_ONLY", "NO_TRADE"]:
        if k in counts:
            lines.append(f"| {k} | {counts[k]} |")
    lines.append("")

    # Sort by plan quality then score
    order = {"ACTIONABLE": 0, "CONDITIONAL": 1, "WATCHLIST_ONLY": 2, "NO_TRADE": 3}
    plans_sorted = sorted(plans, key=lambda x: (order.get(x.get("plan_quality"), 9), -(_safe_float(x.get("score"), -1) or -1)))

    for p in plans_sorted:
        lines.append(f"## {p['ticker']} — {p['strategy']} — {p['plan_quality']}")
        lines.append("")
        lines.append(
            f"**Score:** {_fmt_float(p.get('score'),3)} vs policy min {_fmt_float(p.get('min_score'),2)} · "
            f"**Close:** {_fmt_float(p.get('latest_close'),0)} · **ATR14:** {_fmt_float(p.get('atr14'),1)} · "
            f"**Volume ratio 20D:** {_fmt_float(p.get('volume_ratio_20d'),2)} · **Hold:** {p.get('hold_days')} day(s)"
        )
        lines.append("")
        lines.append(
            f"**Execution numbers:** Buy zone {_fmt_float(p.get('entry_zone_low'),0)}–{_fmt_float(p.get('entry_zone_high'),0)}, "
            f"entry trigger **{_fmt_float(p.get('entry_trigger'),0)}**, stop **{_fmt_float(p.get('stop_loss'),0)}**, "
            f"risk {_fmt_float(p.get('risk_points'),0)} points ({_fmt_pct(p.get('risk_pct'))})."
        )
        lines.append("")
        lines.append(
            f"**Targets:** TP1 **{_fmt_float(p.get('target_1'),0)}** ({_fmt_rr(p.get('rr_1'))}), "
            f"TP2 **{_fmt_float(p.get('target_2'),0)}** ({_fmt_rr(p.get('rr_2'))}), "
            f"TP3 **{_fmt_float(p.get('target_3'),0)}** ({_fmt_rr(p.get('rr_3'))}). "
            f"Recommended base-case RR: **{_fmt_rr(p.get('recommended_rr'))}**."
        )
        lines.append("")
        lines.append(f"**Why entry:** {p.get('why_entry','')}")
        lines.append("")
        lines.append(f"**Why stop:** {p.get('why_stop','')}")
        lines.append("")
        lines.append(f"**Why targets:** {p.get('why_targets','')}")
        lines.append("")
        lines.append(f"**No-trade / caution condition:** {p.get('no_trade_reasons','')}")
        if p.get("risk_flags"):
            lines.append("")
            lines.append(f"**Risk flags:** {p.get('risk_flags')}")
        if p.get("risk_note"):
            lines.append("")
            lines.append(f"**Strategy risk note:** {p.get('risk_note')}")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def build_numeric_trade_report(
    root: str | Path,
    signal_dir: str | Path | None = None,
    target_date: str | None = None,
    policy: str | Path | None = None,
    source_file: str = "all_strategy_watchlist.csv",
    signal_policy: str | Path | None = None,
) -> Dict[str, Any]:
    root = Path(root)
    if signal_dir is None:
        if target_date is None:
            raise ValueError("Either signal_dir or target_date must be provided")
        signal_dir_path = _signal_dir_from_target(root, target_date)
    else:
        signal_dir_path = Path(signal_dir)
        if not signal_dir_path.is_absolute():
            signal_dir_path = root / signal_dir_path

    if not signal_dir_path.exists():
        raise FileNotFoundError(f"Signal directory not found: {signal_dir_path}")

    policy_path = Path(policy) if policy else root / "configs" / "numeric_report_policy.json"
    if not policy_path.is_absolute():
        policy_path = root / policy_path
    user_numeric_cfg = _read_json(policy_path, {})
    numeric_cfg = _merge_dict(DEFAULT_NUMERIC_POLICY, user_numeric_cfg)

    signal_policy_path = Path(signal_policy) if signal_policy else root / "configs" / "signal_policy.json"
    if not signal_policy_path.is_absolute():
        signal_policy_path = root / signal_policy_path
    signal_policy_cfg = _read_json(signal_policy_path, {})

    signals = _normalize_ticker_col(_load_signal_frame(signal_dir_path, source_file))
    ohlcv = _load_ohlcv(root)
    live_features = _load_live_features(root)
    sig_date = _determine_signal_date(signals, live_features, ohlcv, target_date)

    tickers = [str(x).upper() for x in signals.select("ticker").unique().to_series().to_list()]
    structures = _build_structures(ohlcv, tickers, sig_date)

    plans: List[Dict[str, Any]] = []
    for row in signals.to_dicts():
        t = str(row.get("ticker", "")).upper()
        st = structures.get(t)
        if st is None:
            continue
        try:
            plans.append(_calc_trade_plan(row, st, signal_policy_cfg, numeric_cfg))
        except Exception as e:
            plans.append({
                "ticker": t,
                "signal_date": _to_date_str(sig_date),
                "strategy": str(row.get("strategy_name") or row.get("strategy") or "unknown_strategy"),
                "plan_quality": "ERROR",
                "error": str(e),
            })

    # Stable ordering for review: actionable first, then conditional/watchlist, then score desc.
    order = {"ACTIONABLE": 0, "CONDITIONAL": 1, "WATCHLIST_ONLY": 2, "NO_TRADE": 3, "ERROR": 9}
    plans.sort(key=lambda x: (order.get(x.get("plan_quality"), 8), -(_safe_float(x.get("score"), -1) or -1), x.get("ticker","")))

    csv_path = signal_dir_path / "numeric_trade_plan.csv"
    json_path = signal_dir_path / "numeric_trade_plan.json"
    md_path = signal_dir_path / "numeric_trading_report.md"

    _write_csv(csv_path, plans)
    json_path.write_text(json.dumps(_json_safe(plans), indent=2, ensure_ascii=False), encoding="utf-8")
    md_path.write_text(_build_markdown(plans, signal_dir_path, target_date), encoding="utf-8")

    meta = {
        "signal_dir": str(signal_dir_path),
        "source_file": source_file,
        "signal_date": _to_date_str(sig_date),
        "target_date": target_date,
        "rows": len(plans),
        "csv": str(csv_path),
        "json": str(json_path),
        "markdown": str(md_path),
        "numeric_policy": str(policy_path),
        "signal_policy": str(signal_policy_path),
        "plan_quality_counts": {},
    }
    for p in plans:
        q = p.get("plan_quality", "UNKNOWN")
        meta["plan_quality_counts"][q] = meta["plan_quality_counts"].get(q, 0) + 1

    (signal_dir_path / "numeric_trade_report_meta.json").write_text(
        json.dumps(_json_safe(meta), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return meta
