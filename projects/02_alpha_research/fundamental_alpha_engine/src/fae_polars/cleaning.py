from __future__ import annotations

from pathlib import Path
from typing import Any
import re

import polars as pl

from .io import read_csv_many, read_table, write_json, write_table
from .parsing import (
    available_date_expr,
    normalize_ticker_expr,
    parse_date_expr,
    parse_number_expr,
    parse_percent_points_expr,
    parse_period_end_expr,
    slugify_expr,
)


def _empty_write(output_path: str | Path) -> pl.DataFrame:
    out = pl.DataFrame()
    write_table(out, output_path, csv_copy=True)
    return out


def _ensure_cols(df: pl.DataFrame, cols: list[str]) -> pl.DataFrame:
    missing = [pl.lit(None).alias(c) for c in cols if c not in df.columns]
    return df.with_columns(missing) if missing else df


def _normalize_col_name(name: str) -> str:
    name = str(name).replace("\ufeff", "").strip()
    name = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name).strip("_")
    return name


def _normalize_columns(df: pl.DataFrame) -> pl.DataFrame:
    mapping: dict[str, str] = {}
    seen: dict[str, int] = {}
    for c in df.columns:
        base = _normalize_col_name(c) or str(c)
        new = base
        if new in seen:
            seen[base] += 1
            new = f"{base}_{seen[base]}"
        else:
            seen[base] = 0
        mapping[c] = new
    return df.rename(mapping)


def _apply_aliases(df: pl.DataFrame, aliases: dict[str, list[str]]) -> pl.DataFrame:
    rename_map: dict[str, str] = {}
    cols = set(df.columns)
    for target, candidates in aliases.items():
        if target in cols:
            continue
        for cand in candidates:
            cand_norm = _normalize_col_name(cand)
            if cand_norm in cols and cand_norm not in rename_map:
                rename_map[cand_norm] = target
                cols.add(target)
                break
    return df.rename(rename_map) if rename_map else df


def clean_financials(input_path: str | Path, output_path: str | Path, config: dict[str, Any]) -> pl.DataFrame:
    df = read_csv_many(input_path)
    if df.is_empty():
        return _empty_write(output_path)
    df = _normalize_columns(df)
    df = _apply_aliases(df, {
        "ticker": ["kode_emiten", "kodeemiten", "code", "symbol", "stock_code", "emiten"],
        "metric_name": ["metric", "name", "item", "item_name", "field", "fitem_name"],
    })
    required = [
        "ticker", "report_type_id", "report_type_name", "statement_type_id", "statement_type_name",
        "period_label", "period_display", "metric_name", "metric_level", "value_idr", "value_usd", "value_pct",
    ]
    df = _ensure_cols(df, required)
    df = df.with_columns([
        normalize_ticker_expr("ticker").alias("ticker"),
        pl.col("report_type_id").cast(pl.Int64, strict=False),
        pl.col("statement_type_id").cast(pl.Int64, strict=False),
        pl.col("metric_level").cast(pl.Int64, strict=False),
        slugify_expr("metric_name").alias("metric_key"),
        parse_number_expr("value_idr").alias("value_idr"),
        parse_number_expr("value_usd").alias("value_usd"),
        parse_number_expr("value_pct").alias("value_pct"),
        parse_period_end_expr("period_label", "period_display").alias("period_end_date"),
    ]).filter(
        pl.col("ticker").is_not_null() & pl.col("metric_key").is_not_null() & (pl.col("metric_key") != "")
    )
    df = df.with_columns(
        available_date_expr("period_end_date", "statement_type_name", config.get("available_date_lag_days", {})).alias("available_date")
    )
    key_cols = ["ticker", "report_type_name", "statement_type_name", "period_label", "metric_key", "metric_level"]
    df = df.sort(["ticker", "available_date", "report_type_name", "statement_type_name", "metric_key"]).unique(
        subset=key_cols, keep="last", maintain_order=True
    )
    ordered = [
        "ticker", "report_type_id", "report_type_name", "statement_type_id", "statement_type_name",
        "period_label", "period_display", "period_end_date", "available_date", "metric_name", "metric_key",
        "metric_level", "value_idr", "value_usd", "value_pct", "_source_file",
    ]
    df = df.select([c for c in ordered if c in df.columns])
    write_table(df, output_path, csv_copy=True)
    return df


def clean_keystats_ratios(input_path: str | Path, output_path: str | Path, as_of_date: str | None = None) -> pl.DataFrame:
    df = read_csv_many(input_path)
    if df.is_empty():
        return _empty_write(output_path)
    df = _normalize_columns(df)
    df = _apply_aliases(df, {
        "ticker": ["kode_emiten", "kodeemiten", "code", "symbol", "stock_code", "emiten"],
        "category": ["category_name", "metric_category", "group", "section", "kategori"],
        "metric_name": ["metric", "name", "ratio_name", "item", "item_name", "field", "fitem_name"],
        "metric_id": ["id", "ratio_id", "field_id"],
        "value": ["nilai", "value_raw", "current_value", "ratio_value", "amount"],
    })
    df = _ensure_cols(df, ["ticker", "category", "metric_name", "metric_id", "value"])
    snapshot_expr = parse_date_expr("__snapshot") if False else pl.lit(as_of_date).str.strptime(pl.Date, format="%Y-%m-%d", strict=False) if as_of_date else pl.lit(None, dtype=pl.Date)
    if as_of_date is None:
        # Null snapshot is intentionally not used; workflows should pass --as-of-date.
        snapshot_expr = pl.lit(None, dtype=pl.Date)
    df = df.with_columns([
        normalize_ticker_expr("ticker").alias("ticker"),
        slugify_expr("metric_name").alias("metric_key"),
        slugify_expr("category").alias("category_key"),
        pl.col("value").cast(pl.Utf8, strict=False).alias("value_raw"),
        parse_number_expr("value").alias("value_num"),
        pl.col("metric_id").cast(pl.Int64, strict=False),
        snapshot_expr.alias("snapshot_date"),
    ]).filter(pl.col("ticker").is_not_null() & pl.col("metric_key").is_not_null() & (pl.col("metric_key") != ""))
    df = df.unique(subset=["ticker", "metric_key", "snapshot_date"], keep="last", maintain_order=True)
    ordered = ["ticker", "snapshot_date", "category", "category_key", "metric_name", "metric_key", "metric_id", "value_raw", "value_num", "_source_file"]
    df = df.select([c for c in ordered if c in df.columns])
    write_table(df, output_path, csv_copy=True)
    return df


def clean_keystats_quarterly(input_path: str | Path, output_path: str | Path, as_of_date: str | None = None) -> pl.DataFrame:
    df = read_csv_many(input_path)
    if df.is_empty():
        return _empty_write(output_path)
    df = _normalize_columns(df)
    df = _apply_aliases(df, {
        "ticker": ["kode_emiten", "kodeemiten", "code", "symbol", "stock_code", "emiten"],
        "fitem_name": ["metric_name", "metric", "name", "item", "item_name", "field", "financial_item"],
        "most_recent_quarter_date": ["quarter_date", "mrq_date", "latest_quarter_date", "date"],
        "most_recent_quarter_period": ["quarter_period", "mrq_period", "latest_quarter_period"],
        "quarter_value": ["q_value", "quarterly_value", "value", "current_value"],
        "annualised_value": ["annualized_value", "annual_value"],
        "ttm_value": ["ttm", "trailing_twelve_months"],
    })
    required = ["ticker", "fitem_name", "most_recent_quarter_date", "most_recent_quarter_period", "year", "period", "quarter_value", "annualised_value", "ttm_value", "dividend", "payout_ratio", "dividend_yield"]
    df = _ensure_cols(df, required)
    snapshot_expr = pl.lit(as_of_date).str.strptime(pl.Date, format="%Y-%m-%d", strict=False) if as_of_date else pl.lit(None, dtype=pl.Date)
    df = df.with_columns([
        normalize_ticker_expr("ticker").alias("ticker"),
        slugify_expr("fitem_name").alias("fitem_key"),
        parse_date_expr("most_recent_quarter_date", dayfirst=True).alias("most_recent_quarter_date"),
        pl.col("year").cast(pl.Int64, strict=False),
        parse_number_expr("quarter_value").alias("quarter_value_num"),
        parse_number_expr("annualised_value").alias("annualised_value_num"),
        parse_number_expr("ttm_value").alias("ttm_value_num"),
        parse_number_expr("dividend").alias("dividend_num"),
        parse_number_expr("payout_ratio").alias("payout_ratio_num"),
        parse_number_expr("dividend_yield").alias("dividend_yield_num"),
        snapshot_expr.alias("snapshot_date"),
    ]).filter(pl.col("ticker").is_not_null() & pl.col("fitem_key").is_not_null() & (pl.col("fitem_key") != ""))
    write_table(df, output_path, csv_copy=True)
    return df


def clean_keystats_dividends(input_path: str | Path, output_path: str | Path) -> pl.DataFrame:
    df = read_csv_many(input_path)
    if df.is_empty():
        return _empty_write(output_path)
    df = _normalize_columns(df)
    df = _apply_aliases(df, {
        "ticker": ["kode_emiten", "kodeemiten", "code", "symbol", "stock_code", "emiten"],
        "period": ["year", "tahun", "fiscal_year"],
        "dividend": ["dividend_value", "cash_dividend", "amount", "value", "nilai"],
        "ex_date": ["exdate", "cum_date", "ex_dividend_date"],
        "payment_date": ["pay_date", "paid_date", "payment", "paymentdate"],
    })
    df = _ensure_cols(df, ["ticker", "period", "dividend", "ex_date", "payment_date"])
    df = df.with_columns([
        normalize_ticker_expr("ticker").alias("ticker"),
        pl.col("period").cast(pl.Int64, strict=False),
        parse_number_expr("dividend").alias("dividend"),
        parse_date_expr("ex_date", dayfirst=True).alias("ex_date"),
        parse_date_expr("payment_date", dayfirst=True).alias("payment_date"),
    ]).filter(pl.col("ticker").is_not_null())
    df = df.unique(subset=["ticker", "period", "ex_date", "payment_date", "dividend"], keep="last", maintain_order=True)
    write_table(df, output_path, csv_copy=True)
    return df


def clean_insider_activity(input_path: str | Path, output_path: str | Path) -> pl.DataFrame:
    df = read_csv_many(input_path)
    if df.is_empty():
        return _empty_write(output_path)
    df = _normalize_columns(df)
    df = _apply_aliases(df, {
        "ticker": ["kode_emiten", "kodeemiten", "code", "symbol", "stock_code", "emiten"],
        "date": ["transaction_date", "tanggal", "event_date"],
        "insider_name": ["name", "nama", "holder_name", "shareholder_name"],
        "action_type": ["action", "transaction_type", "type"],
    })
    required = [
        "id", "date", "ticker", "insider_name", "action_type", "shares_changed", "shares_changed_pct",
        "prev_shares", "prev_pct", "curr_shares", "curr_pct", "price", "broker_code", "broker_group",
        "nationality", "source_type", "source_label",
    ]
    df = _ensure_cols(df, required)
    df = df.with_columns([
        normalize_ticker_expr("ticker").alias("ticker"),
        parse_date_expr("date", dayfirst=True).alias("date"),
        pl.col("id").cast(pl.Utf8, strict=False).alias("id"),
        pl.col("insider_name").cast(pl.Utf8, strict=False),
        pl.col("action_type").cast(pl.Utf8, strict=False).str.strip_chars().str.to_uppercase().alias("action_type"),
        pl.col("broker_code").cast(pl.Utf8, strict=False),
        pl.col("broker_group").cast(pl.Utf8, strict=False),
        pl.col("nationality").cast(pl.Utf8, strict=False).str.strip_chars().str.to_uppercase().alias("nationality"),
        pl.col("source_type").cast(pl.Utf8, strict=False),
        pl.col("source_label").cast(pl.Utf8, strict=False),
        pl.col("shares_changed").cast(pl.Utf8, strict=False).alias("shares_changed_raw"),
        pl.col("prev_shares").cast(pl.Utf8, strict=False).alias("prev_shares_raw"),
        pl.col("curr_shares").cast(pl.Utf8, strict=False).alias("curr_shares_raw"),
        pl.col("price").cast(pl.Utf8, strict=False).alias("price_raw"),
        pl.col("shares_changed_pct").cast(pl.Utf8, strict=False).alias("shares_changed_pct_raw"),
        pl.col("prev_pct").cast(pl.Utf8, strict=False).alias("prev_pct_raw"),
        pl.col("curr_pct").cast(pl.Utf8, strict=False).alias("curr_pct_raw"),
        parse_number_expr("shares_changed").alias("shares_changed"),
        parse_number_expr("prev_shares").alias("prev_shares"),
        parse_number_expr("curr_shares").alias("curr_shares"),
        parse_number_expr("price").alias("price"),
        parse_percent_points_expr("shares_changed_pct").alias("shares_changed_pct"),
        parse_percent_points_expr("prev_pct").alias("prev_pct"),
        parse_percent_points_expr("curr_pct").alias("curr_pct"),
    ]).filter(pl.col("ticker").is_not_null() & pl.col("date").is_not_null())
    direction = (
        pl.when(pl.col("action_type") == "BUY").then(1)
        .when(pl.col("action_type") == "SELL").then(-1)
        .otherwise(0)
    )
    df = df.with_columns([
        direction.alias("action_direction"),
        (pl.col("shares_changed").abs() * pl.col("price")).alias("trade_value"),
    ]).with_columns([
        pl.when(pl.col("price").fill_null(0) > 0).then(pl.col("trade_value")).otherwise(None).alias("trade_value"),
        (pl.col("trade_value").fill_null(0) * pl.col("action_direction")).alias("signed_trade_value"),
        (pl.col("shares_changed").fill_null(0).abs() * pl.col("action_direction")).alias("signed_shares_changed"),
        (pl.col("shares_changed_pct").fill_null(0).abs() * pl.col("action_direction")).alias("signed_shares_changed_pct"),
        (pl.col("date") + pl.duration(days=1)).cast(pl.Date).alias("available_date"),
    ]).sort(["ticker", "date", "id"])
    write_table(df, output_path, csv_copy=True)
    return df


def build_data_quality_report(clean_paths: dict[str, str | Path], output_path: str | Path) -> dict[str, Any]:
    report: dict[str, Any] = {}
    for name, path in clean_paths.items():
        p = Path(path)
        if not p.exists() and not (p.suffix.lower() == ".parquet" and p.with_suffix(".csv").exists()):
            report[name] = {"exists": False}
            continue
        df = read_table(p)
        date_cols = [c for c, dt in df.schema.items() if dt in (pl.Date, pl.Datetime)]
        missing = df.null_count().to_dicts()[0] if df.width else {}
        report[name] = {
            "exists": True,
            "rows": int(df.height),
            "columns": int(df.width),
            "tickers": int(df.select(pl.col("ticker").n_unique()).item()) if "ticker" in df.columns and df.height else None,
            "date_min": str(df.select(pl.min_horizontal([pl.col(c).cast(pl.Date) for c in date_cols])).to_series().min()) if date_cols and df.height else None,
            "date_max": str(df.select(pl.max_horizontal([pl.col(c).cast(pl.Date) for c in date_cols])).to_series().max()) if date_cols and df.height else None,
            "missing_top": dict(sorted(missing.items(), key=lambda kv: kv[1], reverse=True)[:10]),
        }
    write_json(report, output_path)
    return report
