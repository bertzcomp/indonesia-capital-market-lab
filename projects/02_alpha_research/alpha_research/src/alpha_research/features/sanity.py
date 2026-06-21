from __future__ import annotations
import polars as pl

def safe_ratio(num, den, clip_low=None, clip_high=None):
    expr = pl.when(den.abs() > 1e-9).then(num / den).otherwise(None)
    if clip_low is not None or clip_high is not None:
        lo = -float("inf") if clip_low is None else clip_low
        hi = float("inf") if clip_high is None else clip_high
        expr = expr.clip(lo, hi)
    return expr

def sanitize_numeric(df: pl.DataFrame) -> pl.DataFrame:
    exprs=[]
    for c,d in zip(df.columns, df.dtypes):
        if d in (pl.Float32, pl.Float64):
            exprs.append(pl.when(pl.col(c).is_nan() | pl.col(c).is_infinite()).then(None).otherwise(pl.col(c)).alias(c))
    return df.with_columns(exprs) if exprs else df

def harden_broker_ratios(df: pl.DataFrame) -> pl.DataFrame:
    if {"buy_val_total_sane","sell_val_total_sane"}.issubset(df.columns):
        denom = pl.col("buy_val_total_sane").abs() + pl.col("sell_val_total_sane").abs()
        df = df.with_columns([
            safe_ratio(pl.col("buy_val_total_sane") - pl.col("sell_val_total_sane"), denom, -1.0, 1.0).alias("net_flow_ratio"),
            pl.when((pl.col("buy_val_total_sane") - pl.col("sell_val_total_sane")) > 0).then(1).otherwise(0).cast(pl.Int8).alias("net_buy_flag")
        ])
    if {"rank1_buy_val_sane","buy_val_total_sane"}.issubset(df.columns):
        df = df.with_columns(safe_ratio(pl.col("rank1_buy_val_sane"), pl.col("buy_val_total_sane").abs(), 0.0, 1.0).alias("buyer_dominance_ratio"))
    if {"rank1_sell_val_sane","sell_val_total_sane"}.issubset(df.columns):
        df = df.with_columns(safe_ratio(pl.col("rank1_sell_val_sane"), pl.col("sell_val_total_sane").abs(), 0.0, 1.0).alias("seller_dominance_ratio"))
    return sanitize_numeric(df)
