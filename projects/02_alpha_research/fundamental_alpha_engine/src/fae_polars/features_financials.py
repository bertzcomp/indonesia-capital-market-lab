from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table, write_table


def _coalesce_existing(df: pl.DataFrame, candidates: list[str], out: str) -> pl.Expr:
    exprs = [pl.col(c) for c in candidates if c in df.columns]
    return pl.coalesce(exprs).alias(out) if exprs else pl.lit(None, dtype=pl.Float64).alias(out)


def _safe_div(num: str, den: str, out: str) -> pl.Expr:
    return pl.when(pl.col(den).is_not_null() & (pl.col(den).abs() > 1e-12)).then(pl.col(num) / pl.col(den)).otherwise(None).alias(out)


def build_financial_features(input_path: str | Path, output_path: str | Path) -> pl.DataFrame:
    df = read_table(input_path)
    if df.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    base = df.filter(pl.col("value_idr").is_not_null()).select([
        "ticker", "available_date", "period_end_date", "statement_type_name", "metric_key", "value_idr"
    ])
    if base.is_empty():
        out = pl.DataFrame(); write_table(out, output_path, csv_copy=True); return out
    wide = base.pivot(
        index=["ticker", "available_date", "period_end_date", "statement_type_name"],
        columns="metric_key",
        values="value_idr",
        aggregate_function="last",
    ).sort(["ticker", "period_end_date", "available_date"])

    wide = wide.with_columns([
        _coalesce_existing(wide, ["total_revenue", "revenue_ttm", "revenue"], "revenue"),
        _coalesce_existing(wide, ["gross_profit"], "gross_profit"),
        _coalesce_existing(wide, ["income_from_operations", "operating_income", "income_from_operation"], "operating_income"),
        _coalesce_existing(wide, ["net_income_for_the_period", "net_income_attributable_to", "net_income", "owners_of_the_company"], "net_income"),
        _coalesce_existing(wide, ["cash_from_operating", "cash_from_operations"], "cfo"),
        _coalesce_existing(wide, ["cash_from_investing"], "cfi"),
        _coalesce_existing(wide, ["assets", "total_assets"], "assets"),
        _coalesce_existing(wide, ["liabilities", "total_liabilities"], "liabilities"),
        _coalesce_existing(wide, ["equity", "total_equity", "common_equity"], "equity"),
        _coalesce_existing(wide, ["current_assets"], "current_assets"),
        _coalesce_existing(wide, ["current_liabilities"], "current_liabilities"),
        _coalesce_existing(wide, ["cash_and_cash_equivalent", "cash_and_cash_equivalents", "cash"], "cash"),
        _coalesce_existing(wide, ["share_outstanding", "shares_outstanding"], "share_outstanding"),
    ]).with_columns([
        _safe_div("gross_profit", "revenue", "gross_margin"),
        _safe_div("operating_income", "revenue", "operating_margin"),
        _safe_div("net_income", "revenue", "net_margin"),
        _safe_div("net_income", "equity", "roe_financial"),
        _safe_div("net_income", "assets", "roa_financial"),
        _safe_div("liabilities", "equity", "debt_to_equity_financial"),
        _safe_div("current_assets", "current_liabilities", "current_ratio_financial"),
        _safe_div("cash", "assets", "cash_to_assets"),
        _safe_div("cfo", "net_income", "cfo_to_net_income"),
        (pl.col("cfo") + pl.col("cfi")).alias("rough_fcf"),
    ]).with_columns([
        (pl.col("revenue") / pl.col("revenue").shift(4).over(["ticker", "statement_type_name"]) - 1).alias("revenue_growth_4p"),
        (pl.col("revenue") / pl.col("revenue").shift(1).over(["ticker", "statement_type_name"]) - 1).alias("revenue_growth_1p"),
        (pl.col("net_income") / pl.col("net_income").shift(4).over(["ticker", "statement_type_name"]) - 1).alias("net_income_growth_4p"),
        (pl.col("net_income") / pl.col("net_income").shift(1).over(["ticker", "statement_type_name"]) - 1).alias("net_income_growth_1p"),
        (pl.col("share_outstanding") / pl.col("share_outstanding").shift(4).over(["ticker", "statement_type_name"]) - 1).alias("share_dilution_4p"),
    ]).with_columns([
        pl.when(pl.col("statement_type_name") == "Quarterly").then(pl.col("revenue_growth_4p")).otherwise(pl.col("revenue_growth_1p")).alias("revenue_yoy_growth"),
        pl.when(pl.col("statement_type_name") == "Quarterly").then(pl.col("net_income_growth_4p")).otherwise(pl.col("net_income_growth_1p")).alias("net_income_yoy_growth"),
        pl.when(pl.col("statement_type_name") == "Quarterly").then(pl.col("share_dilution_4p")).otherwise(None).alias("share_dilution_yoy"),
        pl.col("available_date").alias("as_of_date"),
    ])
    keep = [
        "ticker", "as_of_date", "period_end_date", "statement_type_name", "revenue", "gross_profit", "operating_income", "net_income",
        "cfo", "cfi", "rough_fcf", "assets", "liabilities", "equity", "current_assets", "current_liabilities", "cash",
        "share_outstanding", "gross_margin", "operating_margin", "net_margin", "roe_financial", "roa_financial",
        "debt_to_equity_financial", "current_ratio_financial", "cash_to_assets", "cfo_to_net_income", "revenue_yoy_growth",
        "net_income_yoy_growth", "share_dilution_yoy",
    ]
    out = wide.select([c for c in keep if c in wide.columns]).sort(["ticker", "as_of_date"])
    write_table(out, output_path, csv_copy=True)
    return out
