from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import pandas as pd


DEFAULT_POLICY: Dict[str, Any] = {
    "max_report_signals": 30,
    "include_watchlist_when_no_execution": True,
    "default_min_traded_value": 500_000_000,
    "liquidity_strong_value": 2_000_000_000,
    "risk": {
        "dominant_rank1_buyer_share": 0.30,
        "high_volatility_20d": 0.08,
        "low_volume_ratio": 0.70,
        "high_volume_ratio": 1.50,
        "max_broker_value_anomaly_flag": 0,
    },
    "strategy_profiles": {
        "ara": {
            "style": "tactical event / watchlist",
            "default_entry_mode": "Only after strong opening confirmation; avoid chasing failed gap-up moves.",
            "holding_bias": "intraday to 1 day",
            "risk_level": "high",
        },
        "market_maker": {
            "style": "silent accumulation / liquidity behaviour",
            "default_entry_mode": "Prefer retest or stable bid support after accumulation confirmation.",
            "holding_bias": "1-3 days",
            "risk_level": "medium-high",
        },
        "momentum": {
            "style": "cross-sectional momentum continuation",
            "default_entry_mode": "Enter only if price holds above prior close or reclaims intraday VWAP/support.",
            "holding_bias": "1-2 days",
            "risk_level": "medium",
        },
        "scalp": {
            "style": "short-time momentum execution",
            "default_entry_mode": "Needs intraday confirmation; do not enter if opening liquidity fades.",
            "holding_bias": "intraday to 1 day",
            "risk_level": "medium-high",
        },
        "swing": {
            "style": "defensive swing continuation",
            "default_entry_mode": "Prefer confirmation above prior close or controlled pullback/retest.",
            "holding_bias": "1-5 days",
            "risk_level": "medium",
        },
        "position": {
            "style": "position continuation / structural setup",
            "default_entry_mode": "Prefer close confirmation and stable liquidity rather than intraday spike.",
            "holding_bias": "multi-day",
            "risk_level": "medium",
        },
    },
}


def _read_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _safe_float(v: Any) -> Optional[float]:
    if v is None:
        return None
    try:
        if pd.isna(v):
            return None
    except Exception:
        pass
    try:
        x = float(v)
    except Exception:
        return None
    if math.isnan(x) or math.isinf(x):
        return None
    return x


def _safe_int(v: Any) -> Optional[int]:
    x = _safe_float(v)
    if x is None:
        return None
    return int(round(x))


def _fmt_num(v: Any, digits: int = 3) -> str:
    x = _safe_float(v)
    if x is None:
        return "n/a"
    return f"{x:.{digits}f}"


def _fmt_pct(v: Any, digits: int = 2) -> str:
    x = _safe_float(v)
    if x is None:
        return "n/a"
    return f"{x * 100:.{digits}f}%"


def _fmt_money(v: Any) -> str:
    x = _safe_float(v)
    if x is None:
        return "n/a"
    abs_x = abs(x)
    if abs_x >= 1_000_000_000_000:
        return f"{x / 1_000_000_000_000:.2f}T"
    if abs_x >= 1_000_000_000:
        return f"{x / 1_000_000_000:.2f}B"
    if abs_x >= 1_000_000:
        return f"{x / 1_000_000:.2f}M"
    return f"{x:,.0f}"


def _as_bool(v: Any) -> bool:
    if v is None:
        return False
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().lower() in {"1", "true", "yes", "y", "ok"}
    try:
        return float(v) != 0
    except Exception:
        return False


def _norm_text(v: Any) -> str:
    if v is None:
        return ""
    try:
        if pd.isna(v):
            return ""
    except Exception:
        pass
    return str(v)


def _merge_policy(policy_path: Optional[Path]) -> Dict[str, Any]:
    policy = json.loads(json.dumps(DEFAULT_POLICY))
    if policy_path and policy_path.exists():
        user = _read_json(policy_path)
        policy = _deep_update(policy, user)
    return policy


def _deep_update(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(a)
    for k, v in b.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_update(out[k], v)
        else:
            out[k] = v
    return out


def _find_signal_dir(root: Path, signal_dir: Optional[str | Path], target_date: Optional[str]) -> Path:
    if signal_dir:
        p = Path(signal_dir)
        if not p.is_absolute():
            p = root / p
        return p
    daily = root / "signals" / "daily"
    if target_date:
        # Accept YYYY-MM-DD and convert to signal_20_may_2026 naming.
        try:
            ts = pd.to_datetime(target_date)
            name = f"signal_{ts.day}_{ts.strftime('%b').lower()}_{ts.year}"
            candidates = [daily / name, daily / f"signal_{target_date}"]
            for c in candidates:
                if c.exists():
                    return c
        except Exception:
            pass
    if not daily.exists():
        raise FileNotFoundError(f"No signal directory found: {daily}")
    dirs = [p for p in daily.iterdir() if p.is_dir()]
    if not dirs:
        raise FileNotFoundError(f"No signal run directories inside: {daily}")
    return sorted(dirs, key=lambda p: p.stat().st_mtime)[-1]


def _score_columns(row: pd.Series) -> List[Tuple[str, float]]:
    vals: List[Tuple[str, float]] = []
    for c, v in row.items():
        if str(c).startswith("score_"):
            x = _safe_float(v)
            if x is not None:
                vals.append((str(c), x))
    vals.sort(key=lambda t: t[1], reverse=True)
    return vals


def _infer_strategy_name(row: pd.Series, source_name: str = "") -> str:
    for c in ["strategy", "strategy_name", "strategy_tag", "source_strategy", "signal_strategy"]:
        if c in row and _norm_text(row.get(c)):
            return _norm_text(row.get(c))
    for c in ["score_col", "primary_score_col"]:
        s = _norm_text(row.get(c)).lower()
        if s:
            if "ara" in s:
                return "ara_candidate"
            if "mm" in s or "market_maker" in s:
                return "market_maker"
            if "momentum" in s:
                return "momentum"
            if "scalp" in s:
                return "scalp"
            if "swing" in s:
                return "swing"
            if "position" in s:
                return "position"
            if "sm" in s or "brok" in s:
                return "smart_money"
    s = source_name.lower()
    if "ara" in s:
        return "ara_candidate"
    if "market_maker" in s or "mm" in s:
        return "market_maker"
    if "momentum" in s:
        return "momentum"
    if "scalp" in s:
        return "scalp"
    if "swing" in s:
        return "swing"
    if "position" in s:
        return "position"
    return "general"


def _strategy_profile(policy: Dict[str, Any], strategy: str) -> Dict[str, Any]:
    profiles = policy.get("strategy_profiles", {})
    s = strategy.lower()
    for key, prof in profiles.items():
        if key in s:
            return prof
    return {"style": "multi-factor tactical setup", "default_entry_mode": "Wait for confirmation, avoid chasing", "holding_bias": "1-3 days", "risk_level": "medium"}


def _confidence_bucket(score: Optional[float], risk_flags: str) -> str:
    flags = risk_flags.upper()
    if score is None:
        return "Unknown"
    if "DOMINANT" in flags or "ANOMALY" in flags or "BELOW_EXECUTION" in flags:
        if score >= 0.65:
            return "Medium, risk-adjusted"
        return "Low-to-medium"
    if score >= 0.70:
        return "High"
    if score >= 0.60:
        return "Medium-high"
    if score >= 0.50:
        return "Medium"
    return "Watchlist only"


def _risk_grade(row: pd.Series, policy: Dict[str, Any]) -> str:
    flags = _norm_text(row.get("risk_flags")).upper()
    vol = _safe_float(row.get("volatility_20d"))
    buyer_share = _safe_float(row.get("rank1_buyer_daily_share"))
    anomaly = _safe_int(row.get("broker_value_anomaly_flag")) or 0
    high_vol = policy["risk"].get("high_volatility_20d", 0.08)
    dom = policy["risk"].get("dominant_rank1_buyer_share", 0.30)

    points = 0
    if "DOMINANT" in flags or (buyer_share is not None and buyer_share >= dom):
        points += 1
    if "ANOMALY" in flags or anomaly > 0:
        points += 1
    if vol is not None and vol >= high_vol:
        points += 1
    if "BELOW_EXECUTION" in flags:
        points += 1
    if points >= 3:
        return "High"
    if points == 2:
        return "Medium-high"
    if points == 1:
        return "Medium"
    return "Controlled"


def _best_score(row: pd.Series) -> Tuple[str, Optional[float]]:
    # Prefer explicit score column for row if available.
    score_col = _norm_text(row.get("score_col")) or _norm_text(row.get("primary_score_col"))
    if score_col and score_col in row:
        return score_col, _safe_float(row.get(score_col))
    if "score" in row:
        return "score", _safe_float(row.get("score"))
    scores = _score_columns(row)
    if scores:
        return scores[0]
    return "score", None


def _market_context_from_scores(all_scores: pd.DataFrame, diagnostics: Dict[str, Any]) -> str:
    if all_scores.empty:
        return "Market context could not be reconstructed because all_scores.csv is empty."
    latest_date = None
    if "date" in all_scores.columns:
        try:
            latest_date = str(pd.to_datetime(all_scores["date"]).max().date())
        except Exception:
            latest_date = str(all_scores["date"].iloc[-1])

    parts = []
    parts.append(f"Signal universe is built from the latest available market panel dated **{latest_date or 'n/a'}**.")

    for c, label in [
        ("macro_risk_score", "macro risk score"),
        ("market_ret_5d", "5-day market return proxy"),
        ("market_volatility_20d", "20-day market volatility proxy"),
        ("fx_return", "FX pressure"),
        ("brent_return", "Brent move"),
        ("coal_proxy_return", "coal proxy move"),
    ]:
        if c in all_scores.columns:
            val = _safe_float(all_scores[c].dropna().iloc[-1]) if not all_scores[c].dropna().empty else None
            if val is not None:
                if "return" in c or "ret" in c:
                    parts.append(f"{label}: {_fmt_pct(val)}.")
                else:
                    parts.append(f"{label}: {_fmt_num(val)}.")

    if "market_regime" in all_scores.columns and not all_scores["market_regime"].dropna().empty:
        regime = _norm_text(all_scores["market_regime"].dropna().iloc[-1])
        parts.append(f"Regime label: **{regime}**.")

    if diagnostics:
        if "selected_signal_date" in diagnostics:
            parts.append(f"Selected signal date from diagnostics: **{diagnostics.get('selected_signal_date')}**.")
        if "risk_control" in diagnostics:
            parts.append("Risk controls were active during policy selection.")
    return " ".join(parts)


def _row_thesis(row: pd.Series, strategy: str, policy: Dict[str, Any]) -> Dict[str, str]:
    profile = _strategy_profile(policy, strategy)
    score_col, score = _best_score(row)
    risk_flags = _norm_text(row.get("risk_flags")) or "OK"
    ticker = _norm_text(row.get("ticker"))

    close = _safe_float(row.get("close"))
    ma20 = _safe_float(row.get("ma_20"))
    ret5 = _safe_float(row.get("ret_5d"))
    ret20 = _safe_float(row.get("ret_20d"))
    vol20 = _safe_float(row.get("volatility_20d"))
    volume_ratio = _safe_float(row.get("volume_ratio_20d"))
    traded_value = _safe_float(row.get("traded_value_proxy")) or _safe_float(row.get("value"))

    net_flow = _safe_float(row.get("net_flow_ratio"))
    buyer_dom = _safe_float(row.get("buyer_dominance_ratio"))
    buyer_share = _safe_float(row.get("rank1_buyer_daily_share"))
    streak = _safe_int(row.get("rank1_same_buyer_streak"))
    rank1_buyer = _norm_text(row.get("rank1_buyer"))
    rank1_seller = _norm_text(row.get("rank1_seller"))
    has_bdm = _as_bool(row.get("has_bdm_any"))

    price_parts = []
    if close is not None and ma20 is not None:
        if close >= ma20:
            price_parts.append(f"price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base")
        else:
            price_parts.append(f"price is still below the 20-day mean, so the setup needs stronger confirmation before execution")
    if ret5 is not None:
        price_parts.append(f"5-day return is {_fmt_pct(ret5)}")
    if ret20 is not None:
        price_parts.append(f"20-day return is {_fmt_pct(ret20)}")
    if vol20 is not None:
        price_parts.append(f"20-day volatility is {_fmt_pct(vol20)}")
    if volume_ratio is not None:
        if volume_ratio >= policy["risk"].get("high_volume_ratio", 1.5):
            price_parts.append(f"volume expansion is visible with volume ratio {_fmt_num(volume_ratio, 2)}")
        elif volume_ratio < policy["risk"].get("low_volume_ratio", 0.7):
            price_parts.append(f"volume participation is still thin with volume ratio {_fmt_num(volume_ratio, 2)}")
        else:
            price_parts.append(f"volume ratio is neutral at {_fmt_num(volume_ratio, 2)}")

    broker_parts = []
    if net_flow is not None:
        if net_flow > 0.05:
            broker_parts.append(f"broker flow is net-accumulative with net flow ratio {_fmt_num(net_flow, 3)}")
        elif net_flow < -0.05:
            broker_parts.append(f"broker flow is distribution-biased with net flow ratio {_fmt_num(net_flow, 3)}")
        else:
            broker_parts.append(f"broker flow is relatively balanced with net flow ratio {_fmt_num(net_flow, 3)}")
    if rank1_buyer:
        broker_parts.append(f"rank-1 buyer is {rank1_buyer}" + (f" with streak {streak}" if streak is not None else ""))
    if rank1_seller:
        broker_parts.append(f"rank-1 seller is {rank1_seller}")
    if buyer_dom is not None:
        broker_parts.append(f"buyer dominance is {_fmt_pct(buyer_dom)}")
    if buyer_share is not None:
        broker_parts.append(f"daily share of the dominant buyer is {_fmt_pct(buyer_share)}")
    if has_bdm:
        broker_parts.append("BDM confirmation is present, improving behavioural confidence")
    else:
        broker_parts.append("BDM confirmation is not present, so broker/price behaviour must carry the thesis")

    if not price_parts:
        price_parts.append("price structure evidence is limited in the current panel")
    if not broker_parts:
        broker_parts.append("broker-flow evidence is limited in the current panel")

    thesis = (
        f"{ticker} is selected by the **{strategy}** setup ({profile.get('style')}). "
        f"The primary model evidence is `{score_col}` at {_fmt_num(score)}. "
        f"The price/volume context indicates that " + "; ".join(price_parts) + ". "
        f"Behavioural context shows that " + "; ".join(broker_parts) + "."
    )

    entry = (
        f"Entry should not be treated as automatic at the open. {profile.get('default_entry_mode')} "
        "A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, "
        "and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window."
    )

    invalidation_items = []
    if ma20 is not None:
        invalidation_items.append("a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open")
    invalidation_items.append("loss of momentum after entry, especially if price rejects the breakout/retest zone")
    invalidation_items.append("broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative")
    if "DOMINANT" in risk_flags.upper():
        invalidation_items.append("excessive dependence on one broker continuing to dominate without broader participation")
    if vol20 is not None and close is not None:
        buffer_pct = max(0.025, min(0.08, vol20 * 1.25))
        approx_invalid = close * (1 - buffer_pct)
        invalidation_items.append(f"as a volatility-adjusted reference, thesis quality weakens materially around {approx_invalid:.0f} if structure also breaks")

    invalidation = "The setup is invalidated by " + "; ".join(invalidation_items) + ". Stop loss should be interpreted as thesis invalidation, not as an arbitrary number."

    exit_plan = (
        "Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. "
        "Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. "
        "Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest."
    )

    no_trade = (
        "No-trade is the correct decision if opening movement is purely gap-driven without confirmation, "
        "if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence."
    )

    return {
        "ticker": ticker,
        "strategy": strategy,
        "score_col": score_col,
        "score": "" if score is None else f"{score:.6f}",
        "confidence": _confidence_bucket(score, risk_flags),
        "risk_grade": _risk_grade(row, policy),
        "risk_flags": risk_flags,
        "trade_thesis": thesis,
        "entry_plan": entry,
        "invalidation_plan": invalidation,
        "exit_plan": exit_plan,
        "no_trade_condition": no_trade,
        "liquidity_context": f"Traded value proxy: {_fmt_money(traded_value)}; volume ratio: {_fmt_num(volume_ratio, 2)}.",
        "broker_context": "; ".join(broker_parts),
        "price_context": "; ".join(price_parts),
    }


@dataclass
class NarrativeBuildResult:
    signal_dir: Path
    markdown_path: Path
    cards_csv_path: Path
    cards_json_path: Path
    rows: int


def _candidate_sources(signal_dir: Path, policy: Dict[str, Any]) -> List[Tuple[str, pd.DataFrame]]:
    preferred = [
        "execution_shortlist.csv",
        "signals_main.csv",
        "all_strategy_candidates.csv",
        "all_strategy_watchlist.csv",
    ]
    seen_tickers: set[str] = set()
    out: List[Tuple[str, pd.DataFrame]] = []
    for fname in preferred:
        df = _read_csv(signal_dir / fname)
        if df.empty:
            continue
        if "ticker" not in df.columns:
            continue
        rows = []
        for _, row in df.iterrows():
            t = _norm_text(row.get("ticker"))
            if not t or t in seen_tickers:
                continue
            seen_tickers.add(t)
            rows.append(row)
        if rows:
            out.append((fname, pd.DataFrame(rows)))
    return out


def _load_strategy_frames(signal_dir: Path) -> List[Tuple[str, pd.DataFrame]]:
    skip = {
        "all_scores.csv",
        "all_strategy_candidates.csv",
        "all_strategy_watchlist.csv",
        "signals_main.csv",
        "execution_shortlist.csv",
        "narrative_signal_cards.csv",
    }
    frames = []
    for p in sorted(signal_dir.glob("*.csv")):
        if p.name in skip:
            continue
        df = _read_csv(p)
        if not df.empty and "ticker" in df.columns:
            frames.append((p.stem, df))
    return frames


def _build_cards(signal_dir: Path, policy: Dict[str, Any]) -> pd.DataFrame:
    max_rows = int(policy.get("max_report_signals", 30))
    cards: List[Dict[str, str]] = []
    seen: set[str] = set()

    # Prioritize execution and final candidates, then fill with per-strategy watchlists.
    for source, df in _candidate_sources(signal_dir, policy):
        for _, row in df.iterrows():
            if len(cards) >= max_rows:
                break
            ticker = _norm_text(row.get("ticker"))
            if not ticker or ticker in seen:
                continue
            seen.add(ticker)
            strategy = _infer_strategy_name(row, source)
            card = _row_thesis(row, strategy, policy)
            card["source_file"] = source
            cards.append(card)

    for source, df in _load_strategy_frames(signal_dir):
        for _, row in df.iterrows():
            if len(cards) >= max_rows:
                break
            ticker = _norm_text(row.get("ticker"))
            if not ticker or ticker in seen:
                continue
            seen.add(ticker)
            strategy = _infer_strategy_name(row, source)
            card = _row_thesis(row, strategy, policy)
            card["source_file"] = f"{source}.csv"
            cards.append(card)

    return pd.DataFrame(cards)


def _write_markdown(signal_dir: Path, cards: pd.DataFrame, policy: Dict[str, Any]) -> Path:
    diagnostics = _read_json(signal_dir / "diagnostics.json")
    all_scores = _read_csv(signal_dir / "all_scores.csv")
    report_path = signal_dir / "narrative_trading_report.md"

    lines: List[str] = []
    lines.append("# Narrative Trading Intelligence Report")
    lines.append("")
    lines.append("## Market Context")
    lines.append("")
    lines.append(_market_context_from_scores(all_scores, diagnostics))
    lines.append("")
    lines.append("## Operating Principle")
    lines.append("")
    lines.append(
        "This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. "
        "Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. "
        "If those conditions fail, no-trade or early exit is the correct risk decision."
    )
    lines.append("")

    if cards.empty:
        lines.append("## Signal Assessment")
        lines.append("")
        lines.append("No valid signal or watchlist candidate was available for this run.")
    else:
        lines.append("## Signal Thesis and Execution Plan")
        lines.append("")
        for i, row in cards.iterrows():
            lines.append(f"### {i + 1}. {row['ticker']} — {row['strategy']}")
            lines.append("")
            lines.append(f"**Confidence:** {row['confidence']}  ")
            lines.append(f"**Risk Grade:** {row['risk_grade']}  ")
            lines.append(f"**Primary Score:** `{row['score_col']}` = {row['score'] or 'n/a'}  ")
            lines.append(f"**Risk Flags:** {row['risk_flags']}  ")
            lines.append("")
            lines.append("**Trade thesis.** " + row["trade_thesis"])
            lines.append("")
            lines.append("**Execution plan.** " + row["entry_plan"])
            lines.append("")
            lines.append("**Invalidation / stop logic.** " + row["invalidation_plan"])
            lines.append("")
            lines.append("**Exit / take-profit logic.** " + row["exit_plan"])
            lines.append("")
            lines.append("**No-trade condition.** " + row["no_trade_condition"])
            lines.append("")
            lines.append("---")
            lines.append("")

    lines.append("## Portfolio-Level Notes")
    lines.append("")
    lines.append(
        "Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, "
        "avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. "
        "If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only."
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path


def build_narrative_trading_report(
    root: str | Path,
    signal_dir: Optional[str | Path] = None,
    target_date: Optional[str] = None,
    policy_path: Optional[str | Path] = None,
) -> Dict[str, Any]:
    root = Path(root)
    signal_dir_path = _find_signal_dir(root, signal_dir, target_date)
    policy = _merge_policy(Path(policy_path) if policy_path else root / "configs" / "narrative_policy.json")

    cards = _build_cards(signal_dir_path, policy)
    cards_csv = signal_dir_path / "narrative_signal_cards.csv"
    cards_json = signal_dir_path / "narrative_signal_cards.json"
    if not cards.empty:
        cards.to_csv(cards_csv, index=False)
        cards.to_json(cards_json, orient="records", indent=2, force_ascii=False)
    else:
        pd.DataFrame().to_csv(cards_csv, index=False)
        cards_json.write_text("[]", encoding="utf-8")
    md = _write_markdown(signal_dir_path, cards, policy)
    return {
        "signal_dir": str(signal_dir_path),
        "markdown_report": str(md),
        "cards_csv": str(cards_csv),
        "cards_json": str(cards_json),
        "rows": int(len(cards)),
    }
