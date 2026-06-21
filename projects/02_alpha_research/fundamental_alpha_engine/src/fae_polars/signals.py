from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table, write_table

MODE_THRESHOLDS = {
    "research_all": 0.0,
    "tradable": 1_000_000_000.0,
    "liquid": 5_000_000_000.0,
    "strict_liquid": 10_000_000_000.0,
}


def _apply_universe_gates(
    df: pl.DataFrame,
    mode: str = "research_all",
    min_avg_value_20d: float | None = None,
    min_price: float | None = None,
    max_volatility_20d: float | None = None,
    exclude_special_monitoring: bool = False,
) -> pl.DataFrame:
    min_val = MODE_THRESHOLDS.get(mode, 0.0) if min_avg_value_20d is None else float(min_avg_value_20d)
    if min_val > 0 and "avg_value_20d" in df.columns:
        df = df.filter(pl.col("avg_value_20d").fill_null(0) >= min_val)
    if min_price is not None and "close" in df.columns:
        df = df.filter(pl.col("close").fill_null(0) >= float(min_price))
    if max_volatility_20d is not None and "volatility_20d" in df.columns:
        df = df.filter(pl.col("volatility_20d").fill_null(0) <= float(max_volatility_20d))
    if exclude_special_monitoring and "board" in df.columns:
        df = df.filter(~pl.col("board").str.to_lowercase().str.contains("pemantauan", literal=False).fill_null(False))
    return df


def generate_signals(
    scored_panel_path: str | Path,
    output_path: str | Path,
    as_of_date: str | None = None,
    top_n: int = 50,
    min_score: float = 55.0,
    include_avoid: bool = False,
    model_scored_path: str | Path | None = None,
    mode: str = "research_all",
    min_avg_value_20d: float | None = None,
    score_mode: str = "hybrid",
    min_price: float | None = None,
    max_volatility_20d: float | None = None,
) -> pl.DataFrame:
    df = read_table(model_scored_path) if model_scored_path else read_table(scored_panel_path)
    if df.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    if as_of_date:
        target = pl.lit(as_of_date).str.strptime(pl.Date, format="%Y-%m-%d", strict=False)
        df = df.filter(pl.col("as_of_date") <= target)
    if df.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    latest = df.select(pl.col("as_of_date").max()).item()
    cur = df.filter(pl.col("as_of_date") == latest)
    if not include_avoid and "signal_red_flag_avoid" in cur.columns:
        cur = cur.filter(pl.col("signal_red_flag_avoid") != 1)
    cur = _apply_universe_gates(cur, mode=mode, min_avg_value_20d=min_avg_value_20d, min_price=min_price, max_volatility_20d=max_volatility_20d)
    if cur.is_empty():
        out = cur; write_table(out, output_path, csv_copy=True); return out

    if score_mode == "scorecard" or "final_alpha_score_v2" not in cur.columns:
        cur = cur.with_columns(pl.col("fundamental_score").alias("final_alpha_score"))
    elif score_mode == "model":
        cur = cur.with_columns(pl.col("ml_alpha_score").fill_null(pl.col("final_alpha_score_v2")).alias("final_alpha_score"))
    elif score_mode == "hybrid":
        cur = cur.with_columns(pl.col("final_alpha_score_v2").alias("final_alpha_score"))
    else:
        raise ValueError("score_mode must be one of: scorecard, model, hybrid")

    if "final_alpha_score" in cur.columns:
        cur = cur.filter(pl.col("final_alpha_score") >= float(min_score))
    cur = cur.sort("final_alpha_score", descending=True).head(int(top_n))
    output_cols = [
        "as_of_date", "ticker", "company_name", "sector", "subsector", "industry", "subindustry", "final_alpha_score", "final_alpha_score_v2",
        "fundamental_score", "ml_alpha_score", "return_rank_score", "prob_outperform_score", "downside_risk_score", "pred_excess_return",
        "prob_outperform", "prob_bad_drawdown", "quality_score", "growth_score", "valuation_score", "insider_score", "balance_sheet_score",
        "dividend_score", "liquidity_score", "risk_penalty", "signal_family", "conviction", "reason_codes", "action", "close",
        "avg_value_20d", "trading_value", "return_1d", "return_20d", "return_60d", "volatility_20d", "pe_ttm", "pbv", "ps_ttm", "ev_ebitda",
        "roe_ttm", "debt_to_equity", "dividend_yield", "payout_ratio", "insider_buy_count_30d", "insider_sell_count_30d",
        "insider_net_trade_value_30d", "insider_net_shares_changed_pct_30d",
    ]
    out = cur.select([c for c in output_cols if c in cur.columns])
    write_table(out, output_path, csv_copy=True)
    return out
