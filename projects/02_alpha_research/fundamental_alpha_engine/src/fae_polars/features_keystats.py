from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table, write_table


def _coalesce_existing(df: pl.DataFrame, candidates: list[str], out: str) -> pl.Expr:
    exprs = [pl.col(c) for c in candidates if c in df.columns]
    return pl.coalesce(exprs).alias(out) if exprs else pl.lit(None, dtype=pl.Float64).alias(out)


def build_keystats_features(
    ratios_path: str | Path,
    quarterly_path: str | Path,
    dividends_path: str | Path,
    output_path: str | Path,
) -> pl.DataFrame:
    ratios = read_table(ratios_path)
    features: list[pl.DataFrame] = []
    if not ratios.is_empty():
        rwide = ratios.select(["ticker", "snapshot_date", "metric_key", "value_num"]).pivot(
            index=["ticker", "snapshot_date"], columns="metric_key", values="value_num", aggregate_function="last"
        ).rename({"snapshot_date": "as_of_date"})
        rwide = rwide.with_columns([
            _coalesce_existing(rwide, ["current_pe_ratio_ttm", "current_pe_ratio_annualised"], "pe_ttm"),
            _coalesce_existing(rwide, ["current_price_to_book_value"], "pbv"),
            _coalesce_existing(rwide, ["current_price_to_sales_ttm"], "ps_ttm"),
            _coalesce_existing(rwide, ["ev_to_ebitda_ttm"], "ev_ebitda"),
            _coalesce_existing(rwide, ["earnings_yield_ttm"], "earnings_yield"),
            _coalesce_existing(rwide, ["return_on_equity_ttm"], "roe_ttm"),
            _coalesce_existing(rwide, ["return_on_assets_ttm"], "roa_ttm"),
            _coalesce_existing(rwide, ["return_on_invested_capital_ttm"], "roic_ttm"),
            _coalesce_existing(rwide, ["debt_to_equity_ratio_quarter", "total_liabilities_equity_quarter"], "debt_to_equity"),
            _coalesce_existing(rwide, ["current_ratio_quarter"], "current_ratio"),
            _coalesce_existing(rwide, ["quick_ratio_quarter"], "quick_ratio"),
            _coalesce_existing(rwide, ["interest_coverage_ttm"], "interest_coverage"),
            _coalesce_existing(rwide, ["altman_z_score_modified"], "altman_z_score"),
            _coalesce_existing(rwide, ["piotroski_f_score"], "piotroski_f_score"),
            _coalesce_existing(rwide, ["relative_strength_rating"], "relative_strength_rating"),
            _coalesce_existing(rwide, ["dividend_yield"], "dividend_yield"),
            _coalesce_existing(rwide, ["payout_ratio"], "payout_ratio"),
            _coalesce_existing(rwide, ["revenue_quarter_yoy_growth"], "revenue_quarter_yoy_growth"),
            _coalesce_existing(rwide, ["net_income_quarter_yoy_growth"], "net_income_quarter_yoy_growth"),
            _coalesce_existing(rwide, ["revenue_ttm"], "revenue_ttm_keystat"),
            _coalesce_existing(rwide, ["net_income_ttm"], "net_income_ttm_keystat"),
            _coalesce_existing(rwide, ["free_cash_flow_ttm"], "free_cash_flow_ttm"),
            _coalesce_existing(rwide, ["rank_market_cap"], "rank_market_cap"),
            _coalesce_existing(rwide, ["1_month_price_returns"], "price_return_1m_keystat"),
            _coalesce_existing(rwide, ["3_month_price_returns"], "price_return_3m_keystat"),
        ])
        keep = [
            "ticker", "as_of_date", "pe_ttm", "pbv", "ps_ttm", "ev_ebitda", "earnings_yield", "roe_ttm", "roa_ttm", "roic_ttm",
            "debt_to_equity", "current_ratio", "quick_ratio", "interest_coverage", "altman_z_score", "piotroski_f_score",
            "relative_strength_rating", "dividend_yield", "payout_ratio", "revenue_quarter_yoy_growth", "net_income_quarter_yoy_growth",
            "revenue_ttm_keystat", "net_income_ttm_keystat", "free_cash_flow_ttm", "rank_market_cap", "price_return_1m_keystat", "price_return_3m_keystat",
        ]
        features.append(rwide.select([c for c in keep if c in rwide.columns]))

    q = read_table(quarterly_path)
    if not q.is_empty():
        qwide = q.select(["ticker", "snapshot_date", "fitem_key", "ttm_value_num", "annualised_value_num", "dividend_num", "payout_ratio_num", "dividend_yield_num"]).pivot(
            index=["ticker", "snapshot_date"], columns="fitem_key", values="ttm_value_num", aggregate_function="last"
        ).rename({"snapshot_date": "as_of_date"})
        # Keep these as supplementary columns if present.
        qwide = qwide.rename({c: f"q_{c}" for c in qwide.columns if c not in ["ticker", "as_of_date"]})
        features.append(qwide)

    if not features:
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out

    out = features[0]
    for f in features[1:]:
        out = out.join(f, on=["ticker", "as_of_date"], how="outer", coalesce=True)

    div = read_table(dividends_path)
    if not div.is_empty():
        dfeat = div.group_by("ticker").agg([
            pl.col("dividend").drop_nulls().sum().alias("dividend_sum_history"),
            pl.col("dividend").drop_nulls().mean().alias("dividend_avg_history"),
            pl.col("period").n_unique().alias("dividend_years_count"),
            pl.col("ex_date").max().alias("latest_dividend_ex_date"),
        ])
        out = out.join(dfeat, on="ticker", how="left")

    out = out.sort(["ticker", "as_of_date"])
    write_table(out, output_path, csv_copy=True)
    return out
