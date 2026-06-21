from __future__ import annotations

from pathlib import Path

import polars as pl

from .io import read_table, write_table
from .parsing import normalize_ticker_expr, parse_date_expr, parse_number_expr


def load_ohlcv(path: str | Path | None) -> pl.DataFrame:
    if not path:
        return pl.DataFrame()
    df = read_table(path)
    if df.is_empty():
        return df
    # Normalize common column variants.
    lower = {c: c.strip().lower() for c in df.columns}
    df = df.rename({c: lower[c] for c in df.columns})
    if "code" in df.columns and "ticker" not in df.columns:
        df = df.rename({"code": "ticker"})
    if "symbol" in df.columns and "ticker" not in df.columns:
        df = df.rename({"symbol": "ticker"})
    if "datetime" in df.columns and "date" not in df.columns:
        df = df.rename({"datetime": "date"})
    for c in ["ticker", "date", "open", "high", "low", "close", "volume"]:
        if c not in df.columns:
            df = df.with_columns(pl.lit(None).alias(c))
    numeric_exprs = []
    for c in ["open", "high", "low", "close", "volume"]:
        if df.schema.get(c) == pl.Utf8:
            numeric_exprs.append(parse_number_expr(c).alias(c))
        else:
            numeric_exprs.append(pl.col(c).cast(pl.Float64, strict=False).alias(c))
    df = df.with_columns([
        normalize_ticker_expr("ticker").alias("ticker"),
        parse_date_expr("date", dayfirst=False).alias("date") if df.schema.get("date") == pl.Utf8 else pl.col("date").cast(pl.Date, strict=False).alias("date"),
        *numeric_exprs,
    ]).filter(pl.col("ticker").is_not_null() & pl.col("date").is_not_null() & pl.col("close").is_not_null())
    return df.select(["ticker", "date", "open", "high", "low", "close", "volume"]).sort(["ticker", "date"])


def build_market_features(ohlcv_path: str | Path | None, output_path: str | Path | None = None) -> pl.DataFrame:
    df = load_ohlcv(ohlcv_path)
    if df.is_empty():
        out = pl.DataFrame()
        if output_path:
            write_table(out, output_path, csv_copy=True)
        return out
    df = df.sort(["ticker", "date"]).with_columns([
        (pl.col("close") * pl.col("volume")).alias("trading_value"),
        (pl.col("close") / pl.col("close").shift(1).over("ticker") - 1).alias("return_1d"),
        (pl.col("close") / pl.col("close").shift(20).over("ticker") - 1).alias("return_20d"),
        (pl.col("close") / pl.col("close").shift(60).over("ticker") - 1).alias("return_60d"),
    ]).with_columns([
        pl.col("trading_value").rolling_mean(window_size=20, min_periods=5).over("ticker").alias("avg_value_20d"),
        pl.col("return_1d").rolling_std(window_size=20, min_periods=5).over("ticker").alias("volatility_20d"),
    ]).rename({"date": "as_of_date"})
    if output_path:
        write_table(df, output_path, csv_copy=True)
    return df
