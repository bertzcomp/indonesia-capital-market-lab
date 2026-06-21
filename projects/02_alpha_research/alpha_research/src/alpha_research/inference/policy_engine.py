from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import polars as pl


# --- BEGIN v1.4.2 dtype-safe dataframe concat helpers ---
def _dtype_name(dtype) -> str:
    return str(dtype)


def _is_float_dtype(dtype) -> bool:
    return _dtype_name(dtype) in {"Float32", "Float64"}


def _is_int_dtype(dtype) -> bool:
    return _dtype_name(dtype) in {
        "Int8", "Int16", "Int32", "Int64",
        "UInt8", "UInt16", "UInt32", "UInt64",
    }


def _is_numeric_dtype(dtype) -> bool:
    return _is_float_dtype(dtype) or _is_int_dtype(dtype)


def _is_string_like_dtype(dtype) -> bool:
    n = _dtype_name(dtype)
    return n in {"String", "Utf8", "Categorical"} or n.startswith("Categorical")


def _is_bool_dtype(dtype) -> bool:
    return _dtype_name(dtype) in {"Boolean", "Bool"}


def _is_datetime_like_dtype(dtype) -> bool:
    n = _dtype_name(dtype)
    return n == "Date" or n.startswith("Datetime")


def _choose_concat_dtype(dtypes):
    """Choose a stable supertype for a column across strategy frames.

    Rules are intentionally conservative:
    - all numeric -> Float64 if any float else Int64
    - any string/categorical mixed with anything -> Utf8
    - all date/datetime-like -> Date/Datetime
    - all bool -> Boolean
    - otherwise -> Utf8
    """
    dtypes = [d for d in dtypes if d is not None]
    if not dtypes:
        return pl.Utf8

    if all(_is_numeric_dtype(d) for d in dtypes):
        return pl.Float64 if any(_is_float_dtype(d) for d in dtypes) else pl.Int64

    if any(_is_string_like_dtype(d) for d in dtypes):
        return pl.Utf8

    if all(_is_datetime_like_dtype(d) for d in dtypes):
        names = [_dtype_name(d) for d in dtypes]
        if all(n == "Date" for n in names):
            return pl.Date
        for d in dtypes:
            if _dtype_name(d).startswith("Datetime"):
                return d
        return pl.Date

    if all(_is_bool_dtype(d) for d in dtypes):
        return pl.Boolean

    return pl.Utf8


def _normalize_concat_frames(frames):
    """Normalize column order and dtype before concatenating strategy frames.

    This fixes Polars errors such as:
        SchemaError: type Float32 is incompatible with expected type Float64

    We select every frame into the same ordered schema and cast compatible
    columns to a common dtype. Missing columns are inserted as nulls.
    """
    frames = [f for f in frames if f is not None and not f.is_empty()]
    if not frames:
        return []

    columns = []
    seen = set()
    for df in frames:
        for c in df.columns:
            if c not in seen:
                seen.add(c)
                columns.append(c)

    target = {}
    for c in columns:
        dtypes = [df.schema.get(c) for df in frames if c in df.columns]
        target[c] = _choose_concat_dtype(dtypes)

    normalized = []
    for df in frames:
        exprs = []
        for c in columns:
            dtype = target[c]
            if c in df.columns:
                exprs.append(pl.col(c).cast(dtype, strict=False).alias(c))
            else:
                exprs.append(pl.lit(None).cast(dtype).alias(c))
        normalized.append(df.select(exprs))
    return normalized


def _concat_diagonal_safe(frames):
    """Dtype-safe concat for per-strategy frames.

    After _normalize_concat_frames(), every frame has identical columns and
    identical dtypes, so vertical concat is safer than recursive diagonal concat.
    """
    frames = _normalize_concat_frames(frames)
    if not frames:
        return pl.DataFrame()
    if len(frames) == 1:
        return frames[0]
    return pl.concat(frames, how="vertical")
# --- END v1.4.2 dtype-safe dataframe concat helpers ---


POLICY_GROUP_KEYS = [
    "core_execution",
    "aggressive_challenger",
    "watchlist_only",
]


@dataclass
class StrategySpec:
    name: str
    group: str
    score_col: str
    top_k: int = 10
    hold_days: int = 1
    min_score: Optional[float] = None
    min_traded_value: Optional[float] = None
    require_broksum: bool = False
    exclude_broker_value_anomaly: bool = False
    execution_enabled: bool = True
    watchlist_enabled: bool = True
    allow_watchlist_below_threshold: bool = True
    watchlist_top_k: Optional[int] = None
    watchlist_min_score: Optional[float] = None
    raw: Dict[str, Any] | None = None


def load_json(path: str | Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _as_strategy_list(obj: Any, group: str) -> List[Tuple[str, Dict[str, Any]]]:
    out: List[Tuple[str, Dict[str, Any]]] = []
    if obj is None:
        return out
    if isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, dict):
                name = str(item.get("name") or item.get("strategy") or item.get("id") or f"{group}_{i+1}")
                out.append((name, item))
    elif isinstance(obj, dict):
        for name, item in obj.items():
            if isinstance(item, dict):
                spec = dict(item)
                spec.setdefault("name", name)
                out.append((str(name), spec))
    return out


def _as_bool(x: Any, default: bool = False) -> bool:
    if x is None:
        return default
    if isinstance(x, bool):
        return x
    if isinstance(x, (int, float)):
        return bool(x)
    if isinstance(x, str):
        return x.strip().lower() in {"1", "true", "yes", "y", "on"}
    return bool(x)


def _as_optional_float(obj: Dict[str, Any], key: str) -> Optional[float]:
    if obj.get(key) is None:
        return None
    return float(obj[key])


def collect_strategy_specs(policy: Dict[str, Any]) -> List[StrategySpec]:
    """Collect strategies from all supported policy layouts.

    Supported shapes:
    1) {"core_execution": [{...}], "aggressive_challenger": [...], "watchlist_only": [...]}
    2) {"strategy_groups": {"core_execution": [...], ...}}
    3) {"champion_strategies": {"main": {...}, ...}}
    4) {"strategies": [{...}]}
    5) direct dict entries whose values contain `score_col`.
    """
    pairs: List[Tuple[str, str, Dict[str, Any]]] = []

    for group in POLICY_GROUP_KEYS:
        for name, spec in _as_strategy_list(policy.get(group), group):
            pairs.append((group, name, spec))

    groups = policy.get("strategy_groups")
    if isinstance(groups, dict):
        for group, obj in groups.items():
            for name, spec in _as_strategy_list(obj, str(group)):
                pairs.append((str(group), name, spec))

    for container_key, default_group in [
        ("champion_strategies", "core_execution"),
        ("strategies", "core_execution"),
        ("policies", "core_execution"),
    ]:
        container = policy.get(container_key)
        for name, spec in _as_strategy_list(container, default_group):
            group = str(spec.get("group") or spec.get("strategy_group") or default_group)
            pairs.append((group, name, spec))

    ignored = set(POLICY_GROUP_KEYS + [
        "strategy_groups", "champion_strategies", "strategies", "policies",
        "risk_controls", "portfolio_controls", "metadata"
    ])
    for name, spec in policy.items():
        if name in ignored:
            continue
        if isinstance(spec, dict) and "score_col" in spec:
            group = str(spec.get("group") or spec.get("strategy_group") or "core_execution")
            pairs.append((group, str(name), spec))

    seen: set[Tuple[str, str, str]] = set()
    strategies: List[StrategySpec] = []
    for group, name, spec in pairs:
        score_col = spec.get("score_col") or spec.get("score")
        if not score_col:
            continue
        key = (group, name, str(score_col))
        if key in seen:
            continue
        seen.add(key)
        execution_enabled = _as_bool(spec.get("execution_enabled"), group != "watchlist_only")
        watchlist_enabled = _as_bool(spec.get("watchlist_enabled"), True)
        top_k = int(spec.get("top_k", spec.get("top_n", 10)))
        watchlist_top_k = int(spec.get("watchlist_top_k", top_k)) if spec.get("watchlist_top_k", top_k) is not None else top_k
        strategies.append(
            StrategySpec(
                name=str(spec.get("name") or name),
                group=str(group),
                score_col=str(score_col),
                top_k=top_k,
                hold_days=int(spec.get("hold_days", 1)),
                min_score=_as_optional_float(spec, "min_score"),
                min_traded_value=_as_optional_float(spec, "min_traded_value"),
                require_broksum=_as_bool(spec.get("require_broksum"), False),
                exclude_broker_value_anomaly=_as_bool(spec.get("exclude_broker_value_anomaly"), False),
                execution_enabled=execution_enabled,
                watchlist_enabled=watchlist_enabled,
                allow_watchlist_below_threshold=_as_bool(spec.get("allow_watchlist_below_threshold"), True),
                watchlist_top_k=watchlist_top_k,
                watchlist_min_score=_as_optional_float(spec, "watchlist_min_score"),
                raw=dict(spec),
            )
        )
    return strategies


def collect_policy_score_cols(policy: Dict[str, Any]) -> List[str]:
    cols: List[str] = []
    for s in collect_strategy_specs(policy):
        if s.score_col not in cols:
            cols.append(s.score_col)
    return cols


def collect_registry_score_cols(registry: Dict[str, Any]) -> List[str]:
    comps = registry.get("components", registry)
    cols: List[str] = []
    if not isinstance(comps, dict):
        return cols
    for key, spec in comps.items():
        if not isinstance(spec, dict):
            continue
        candidates = [key, spec.get("score_col"), spec.get("alias"), spec.get("output_col")]
        for c in candidates:
            if c and c not in cols:
                cols.append(str(c))
    return cols


def get_risk_controls(policy: Dict[str, Any]) -> Dict[str, Any]:
    rc = policy.get("risk_controls") or policy.get("portfolio_controls") or {}
    if not isinstance(rc, dict):
        rc = {}
    return {
        "max_total_final_signals": int(rc.get("max_total_final_signals", rc.get("top_k_final", 30))),
        "max_per_strategy": int(rc.get("max_per_strategy", 999999)),
        "max_per_rank1_buyer": int(rc.get("max_per_rank1_buyer", 999999)),
        "max_lower_liquidity_signals": int(rc.get("max_lower_liquidity_signals", 999999)),
        "prefer_risk_flags_ok": _as_bool(rc.get("prefer_risk_flags_ok"), True),
        "deduplicate_tickers_across_strategies": _as_bool(rc.get("deduplicate_tickers_across_strategies"), True),
    }


def _value_col(df: pl.DataFrame) -> Optional[str]:
    for c in ["value", "traded_value_proxy", "regular_value", "all_market_value"]:
        if c in df.columns:
            return c
    return None


def _filter_common(
    df: pl.DataFrame,
    spec: StrategySpec,
    global_price_min: Optional[float] = None,
    global_price_max: Optional[float] = None,
    enforce_min_score: bool = True,
    top_k: Optional[int] = None,
) -> pl.DataFrame:
    if spec.score_col not in df.columns:
        return pl.DataFrame()
    out = df.filter(pl.col(spec.score_col).is_not_null())
    if "close" in out.columns:
        if global_price_min is not None:
            out = out.filter(pl.col("close") >= float(global_price_min))
        if global_price_max is not None:
            out = out.filter(pl.col("close") <= float(global_price_max))

    score_threshold = spec.min_score if enforce_min_score else spec.watchlist_min_score
    if score_threshold is not None:
        out = out.filter(pl.col(spec.score_col) >= float(score_threshold))

    vcol = _value_col(out)
    if vcol and spec.min_traded_value is not None:
        out = out.filter(pl.col(vcol).fill_null(0) >= float(spec.min_traded_value))
    if spec.require_broksum and "has_broksum" in out.columns:
        out = out.filter(pl.col("has_broksum").fill_null(0) == 1)
    if enforce_min_score and spec.exclude_broker_value_anomaly and "broker_value_anomaly_flag" in out.columns:
        out = out.filter(pl.col("broker_value_anomaly_flag").fill_null(0) == 0)

    if out.is_empty():
        return out

    passes_expr = pl.lit(True)
    if spec.min_score is not None:
        passes_expr = pl.col(spec.score_col) >= float(spec.min_score)

    out = out.with_columns([
        pl.lit(spec.name).alias("strategy_name"),
        pl.lit(spec.group).alias("strategy_group"),
        pl.lit(spec.score_col).alias("score_col"),
        pl.col(spec.score_col).alias("strategy_score"),
        pl.lit(spec.hold_days).alias("suggested_hold_days"),
        pl.lit(1 if spec.execution_enabled else 0).alias("execution_enabled"),
        passes_expr.cast(pl.Int8).alias("passes_execution_threshold"),
        pl.lit(0 if enforce_min_score else 1).cast(pl.Int8).alias("watchlist_mode"),
    ])
    k = int(top_k or spec.top_k)
    return out.sort("strategy_score", descending=True, nulls_last=True).head(k)


def _filter_strategy_execution(df: pl.DataFrame, spec: StrategySpec, price_min: Optional[float], price_max: Optional[float]) -> pl.DataFrame:
    return _filter_common(df, spec, price_min, price_max, enforce_min_score=True, top_k=spec.top_k)


def _filter_strategy_watchlist(df: pl.DataFrame, spec: StrategySpec, price_min: Optional[float], price_max: Optional[float]) -> pl.DataFrame:
    if not spec.watchlist_enabled:
        return pl.DataFrame()
    enforce_min_score = not spec.allow_watchlist_below_threshold
    return _filter_common(df, spec, price_min, price_max, enforce_min_score=enforce_min_score, top_k=spec.watchlist_top_k or spec.top_k)


def _add_risk_flags(df: pl.DataFrame, min_traded_value: Optional[float] = None) -> pl.DataFrame:
    if df.is_empty():
        return df.with_columns(pl.lit("OK").alias("risk_flags")) if "risk_flags" not in df.columns else df
    vcol = _value_col(df)
    flags = []
    if vcol and min_traded_value is not None:
        flags.append(pl.when(pl.col(vcol).fill_null(0) < float(min_traded_value)).then(pl.lit("LOWER_LIQUIDITY")).otherwise(pl.lit("")))
    if "broker_value_anomaly_flag" in df.columns:
        flags.append(pl.when(pl.col("broker_value_anomaly_flag").fill_null(0) == 1).then(pl.lit("BROKER_VALUE_ANOMALY")).otherwise(pl.lit("")))
    if "rank1_buyer_daily_share" in df.columns:
        flags.append(pl.when(pl.col("rank1_buyer_daily_share").fill_null(0) >= 0.30).then(pl.lit("DOMINANT_RANK1_BUYER")).otherwise(pl.lit("")))
    if "passes_execution_threshold" in df.columns:
        flags.append(pl.when(pl.col("passes_execution_threshold").fill_null(0) == 0).then(pl.lit("BELOW_EXECUTION_THRESHOLD")).otherwise(pl.lit("")))
    if not flags:
        return df.with_columns(pl.lit("OK").alias("risk_flags"))
    df = df.with_columns(pl.concat_str(flags, separator="|").alias("risk_flags"))
    df = df.with_columns(
        pl.when((pl.col("risk_flags") == "") | (pl.col("risk_flags").str.replace_all("\\|", "") == ""))
        .then(pl.lit("OK"))
        .otherwise(pl.col("risk_flags").str.strip_chars("|"))
        .alias("risk_flags")
    )
    return df


def apply_portfolio_controls(candidates: pl.DataFrame, policy: Dict[str, Any]) -> pl.DataFrame:
    if candidates.is_empty():
        return candidates
    rc = get_risk_controls(policy)
    strategies = collect_strategy_specs(policy)
    priority = {s.name: i for i, s in enumerate(strategies)}

    pdf = candidates.sort("strategy_score", descending=True).to_pandas()
    pdf["_strategy_priority"] = pdf["strategy_name"].map(priority).fillna(9999).astype(int)
    if rc["prefer_risk_flags_ok"] and "risk_flags" in pdf.columns:
        pdf["_risk_ok"] = (pdf["risk_flags"].fillna("OK") == "OK").astype(int)
    else:
        pdf["_risk_ok"] = 0
    pdf = pdf.sort_values(["_risk_ok", "_strategy_priority", "strategy_score"], ascending=[False, True, False])

    selected = []
    seen_tickers = set()
    per_strategy: Dict[str, int] = {}
    per_broker: Dict[str, int] = {}
    lower_liq = 0
    for _, row in pdf.iterrows():
        ticker = row.get("ticker")
        strategy = row.get("strategy_name")
        broker = row.get("rank1_buyer", None)
        risk_flags = str(row.get("risk_flags", "OK"))
        if rc["deduplicate_tickers_across_strategies"] and ticker in seen_tickers:
            continue
        if per_strategy.get(strategy, 0) >= rc["max_per_strategy"]:
            continue
        if broker is not None and not (isinstance(broker, float) and math.isnan(broker)):
            if per_broker.get(str(broker), 0) >= rc["max_per_rank1_buyer"]:
                continue
        if "LOWER_LIQUIDITY" in risk_flags and lower_liq >= rc["max_lower_liquidity_signals"]:
            continue
        selected.append(row)
        seen_tickers.add(ticker)
        per_strategy[strategy] = per_strategy.get(strategy, 0) + 1
        if broker is not None and not (isinstance(broker, float) and math.isnan(broker)):
            per_broker[str(broker)] = per_broker.get(str(broker), 0) + 1
        if "LOWER_LIQUIDITY" in risk_flags:
            lower_liq += 1
        if len(selected) >= rc["max_total_final_signals"]:
            break

    if not selected:
        return pl.DataFrame()
    out = pl.from_pandas(__import__("pandas").DataFrame(selected))
    drop_cols = [c for c in ["_strategy_priority", "_risk_ok"] if c in out.columns]
    if drop_cols:
        out = out.drop(drop_cols)
    return out


def build_policy_signals(
    base_scores: pl.DataFrame,
    policy: Dict[str, Any],
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    default_min_traded_value: Optional[float] = None,
) -> Dict[str, Any]:
    strategies = collect_strategy_specs(policy)
    per_strategy_watchlist: Dict[str, pl.DataFrame] = {}
    per_strategy_execution: Dict[str, pl.DataFrame] = {}
    execution_frames: List[pl.DataFrame] = []
    watchlist_frames: List[pl.DataFrame] = []

    for spec in strategies:
        if spec.min_traded_value is None and default_min_traded_value is not None:
            spec = StrategySpec(**{**spec.__dict__, "min_traded_value": default_min_traded_value})

        watch = _filter_strategy_watchlist(base_scores, spec, price_min, price_max)
        watch = _add_risk_flags(watch, spec.min_traded_value)
        per_strategy_watchlist[spec.name] = watch
        if not watch.is_empty():
            watchlist_frames.append(watch)

        exe = _filter_strategy_execution(base_scores, spec, price_min, price_max)
        exe = _add_risk_flags(exe, spec.min_traded_value)
        per_strategy_execution[spec.name] = exe
        if not exe.is_empty():
            execution_frames.append(exe)

    all_watchlist = _concat_diagonal_safe(watchlist_frames) if watchlist_frames else pl.DataFrame()
    all_candidates = _concat_diagonal_safe(execution_frames) if execution_frames else pl.DataFrame()
    execution_candidates = all_candidates.filter(pl.col("execution_enabled") == 1) if not all_candidates.is_empty() and "execution_enabled" in all_candidates.columns else pl.DataFrame()
    main = apply_portfolio_controls(execution_candidates, policy) if not execution_candidates.is_empty() else pl.DataFrame()
    shortlist = main.filter(pl.col("risk_flags") == "OK") if not main.is_empty() and "risk_flags" in main.columns else main
    return {
        "per_strategy": per_strategy_watchlist,
        "per_strategy_execution": per_strategy_execution,
        "all_strategy_watchlist": all_watchlist,
        "all_strategy_candidates": all_candidates,
        "signals_main": main,
        "execution_shortlist": shortlist,
    }
