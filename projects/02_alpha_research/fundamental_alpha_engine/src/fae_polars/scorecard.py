from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table, write_table


def _ensure_cols(df: pl.DataFrame, cols: list[str]) -> pl.DataFrame:
    missing = [pl.lit(None, dtype=pl.Float64).alias(c) for c in cols if c not in df.columns]
    return df.with_columns(missing) if missing else df


def _rank_score(col: str, higher: bool = True) -> pl.Expr:
    rank = pl.col(col).rank(method="average").over("as_of_date")
    n = pl.len().over("as_of_date")
    pct = pl.when(n > 1).then((rank - 1) / (n - 1) * 100.0).otherwise(50.0)
    score = pct if higher else (100.0 - pct)
    return pl.when(pl.col(col).is_null()).then(50.0).otherwise(score)


def _avg_scores(cols: list[str], out: str) -> pl.Expr:
    exprs = [pl.col(c).fill_null(50.0) for c in cols]
    total = exprs[0]
    for e in exprs[1:]:
        total = total + e
    return (total / len(exprs)).alias(out)


def score_panel(panel_path: str | Path, output_path: str | Path, min_liquidity: float = 0.0) -> pl.DataFrame:
    df = read_table(panel_path)
    if df.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    needed = [
        "roe_ttm", "roa_ttm", "roic_ttm", "roe_financial", "roa_financial", "gross_margin", "operating_margin", "net_margin", "cfo_to_net_income",
        "revenue_yoy_growth", "net_income_yoy_growth", "revenue_quarter_yoy_growth", "net_income_quarter_yoy_growth",
        "pe_ttm", "pbv", "ps_ttm", "ev_ebitda", "earnings_yield", "debt_to_equity", "debt_to_equity_financial", "current_ratio", "current_ratio_financial",
        "quick_ratio", "interest_coverage", "altman_z_score", "piotroski_f_score", "dividend_yield", "payout_ratio", "avg_value_20d",
        "insider_net_trade_value_30d", "insider_net_trade_value_90d", "insider_net_shares_changed_pct_30d", "insider_buy_count_30d", "insider_sell_count_30d",
    ]
    df = _ensure_cols(df, needed)
    # Unify duplicate financial/key-stat variants.
    df = df.with_columns([
        pl.coalesce([pl.col("roe_ttm"), pl.col("roe_financial")]).alias("roe_u"),
        pl.coalesce([pl.col("roa_ttm"), pl.col("roa_financial")]).alias("roa_u"),
        pl.coalesce([pl.col("debt_to_equity"), pl.col("debt_to_equity_financial")]).alias("debt_to_equity_u"),
        pl.coalesce([pl.col("current_ratio"), pl.col("current_ratio_financial")]).alias("current_ratio_u"),
    ]).with_columns([
        _rank_score("roe_u", True).alias("s_roe"),
        _rank_score("roa_u", True).alias("s_roa"),
        _rank_score("roic_ttm", True).alias("s_roic"),
        _rank_score("gross_margin", True).alias("s_gross_margin"),
        _rank_score("operating_margin", True).alias("s_operating_margin"),
        _rank_score("net_margin", True).alias("s_net_margin"),
        _rank_score("cfo_to_net_income", True).alias("s_cfo_quality"),
        _rank_score("revenue_yoy_growth", True).alias("s_revenue_growth"),
        _rank_score("net_income_yoy_growth", True).alias("s_net_income_growth"),
        _rank_score("revenue_quarter_yoy_growth", True).alias("s_revenue_q_growth"),
        _rank_score("net_income_quarter_yoy_growth", True).alias("s_net_income_q_growth"),
        _rank_score("pe_ttm", False).alias("s_pe"),
        _rank_score("pbv", False).alias("s_pbv"),
        _rank_score("ps_ttm", False).alias("s_ps"),
        _rank_score("ev_ebitda", False).alias("s_ev_ebitda"),
        _rank_score("earnings_yield", True).alias("s_earnings_yield"),
        _rank_score("debt_to_equity_u", False).alias("s_debt"),
        _rank_score("current_ratio_u", True).alias("s_current_ratio"),
        _rank_score("quick_ratio", True).alias("s_quick_ratio"),
        _rank_score("interest_coverage", True).alias("s_interest_coverage"),
        _rank_score("altman_z_score", True).alias("s_altman"),
        _rank_score("piotroski_f_score", True).alias("s_piotroski"),
        _rank_score("dividend_yield", True).alias("s_div_yield"),
        _rank_score("avg_value_20d", True).alias("s_liquidity"),
        _rank_score("insider_net_trade_value_30d", True).alias("s_insider_value_30"),
        _rank_score("insider_net_trade_value_90d", True).alias("s_insider_value_90"),
        _rank_score("insider_net_shares_changed_pct_30d", True).alias("s_insider_pct"),
        _rank_score("insider_buy_count_30d", True).alias("s_insider_buy_count"),
        _rank_score("insider_sell_count_30d", False).alias("s_insider_sell_count"),
    ]).with_columns([
        _avg_scores(["s_roe", "s_roa", "s_roic", "s_gross_margin", "s_operating_margin", "s_net_margin", "s_cfo_quality", "s_piotroski"], "quality_score"),
        _avg_scores(["s_revenue_growth", "s_net_income_growth", "s_revenue_q_growth", "s_net_income_q_growth"], "growth_score"),
        _avg_scores(["s_pe", "s_pbv", "s_ps", "s_ev_ebitda", "s_earnings_yield"], "valuation_score"),
        _avg_scores(["s_debt", "s_current_ratio", "s_quick_ratio", "s_interest_coverage", "s_altman"], "balance_sheet_score"),
        _avg_scores(["s_insider_value_30", "s_insider_value_90", "s_insider_pct", "s_insider_buy_count", "s_insider_sell_count"], "insider_score"),
        _avg_scores(["s_div_yield"], "dividend_score"),
        _avg_scores(["s_liquidity"], "liquidity_score"),
    ])
    df = df.with_columns([
        (
            (pl.when(pl.col("debt_to_equity_u") > 3).then(12).otherwise(0))
            + (pl.when(pl.col("current_ratio_u") < 0.8).then(8).otherwise(0))
            + (pl.when(pl.col("payout_ratio") > 1.2).then(5).otherwise(0))
            + (pl.when(pl.col("insider_sell_count_30d") > pl.col("insider_buy_count_30d")).then(8).otherwise(0))
            + (pl.when((pl.col("avg_value_20d") < min_liquidity) & pl.col("avg_value_20d").is_not_null()).then(10).otherwise(0))
        ).alias("risk_penalty")
    ]).with_columns([
        (
            0.20 * pl.col("quality_score")
            + 0.20 * pl.col("growth_score")
            + 0.20 * pl.col("valuation_score")
            + 0.15 * pl.col("insider_score")
            + 0.15 * pl.col("balance_sheet_score")
            + 0.05 * pl.col("dividend_score")
            + 0.05 * pl.col("liquidity_score")
            - pl.col("risk_penalty")
        ).clip(0, 100).alias("fundamental_score")
    ])
    df = df.with_columns([
        (pl.col("quality_score") >= 70).cast(pl.Int8).alias("signal_quality_growth"),
        ((pl.col("valuation_score") >= 70) & (pl.col("quality_score") >= 50)).cast(pl.Int8).alias("signal_value_rerating"),
        (pl.col("insider_score") >= 70).cast(pl.Int8).alias("signal_insider_accumulation"),
        ((pl.col("growth_score") >= 70) & (pl.col("quality_score") < 60)).cast(pl.Int8).alias("signal_turnaround_early"),
        (pl.col("balance_sheet_score") >= 70).cast(pl.Int8).alias("signal_balance_sheet_strength"),
        (pl.col("dividend_score") >= 70).cast(pl.Int8).alias("signal_dividend_quality"),
        (pl.col("risk_penalty") >= 20).cast(pl.Int8).alias("signal_red_flag_avoid"),
    ]).with_columns([
        pl.when(pl.col("signal_red_flag_avoid") == 1).then(pl.lit("RED_FLAG_AVOID"))
        .when(pl.col("signal_insider_accumulation") == 1).then(pl.lit("INSIDER_ACCUMULATION"))
        .when(pl.col("signal_value_rerating") == 1).then(pl.lit("VALUE_RERATING"))
        .when(pl.col("signal_quality_growth") == 1).then(pl.lit("QUALITY_GROWTH"))
        .when(pl.col("signal_turnaround_early") == 1).then(pl.lit("TURNAROUND_EARLY"))
        .when(pl.col("signal_balance_sheet_strength") == 1).then(pl.lit("BALANCE_SHEET_STRENGTH"))
        .when(pl.col("signal_dividend_quality") == 1).then(pl.lit("DIVIDEND_QUALITY"))
        .otherwise(pl.lit("NEUTRAL")).alias("signal_family"),
        pl.when(pl.col("fundamental_score") >= 75).then(pl.lit("HIGH"))
        .when(pl.col("fundamental_score") >= 50).then(pl.lit("MEDIUM"))
        .otherwise(pl.lit("LOW")).alias("conviction"),
    ]).with_columns([
        pl.concat_str([
            pl.when(pl.col("quality_score") >= 70).then(pl.lit("quality strong; ")).otherwise(pl.lit("")),
            pl.when(pl.col("growth_score") >= 70).then(pl.lit("growth improving; ")).otherwise(pl.lit("")),
            pl.when(pl.col("valuation_score") >= 70).then(pl.lit("valuation attractive; ")).otherwise(pl.lit("")),
            pl.when(pl.col("insider_score") >= 70).then(pl.lit("insider accumulation; ")).otherwise(pl.lit("")),
            pl.when(pl.col("risk_penalty") >= 20).then(pl.lit("risk flags detected; ")).otherwise(pl.lit("")),
        ]).alias("reason_codes"),
        pl.when(pl.col("signal_red_flag_avoid") == 1).then(pl.lit("avoid"))
        .when(pl.col("fundamental_score") >= 55).then(pl.lit("add_to_watchlist_wait_technical_confirmation"))
        .otherwise(pl.lit("monitor_only")).alias("action"),
    ]).sort(["as_of_date", "fundamental_score"], descending=[False, True])
    write_table(df, output_path, csv_copy=True)
    return df
