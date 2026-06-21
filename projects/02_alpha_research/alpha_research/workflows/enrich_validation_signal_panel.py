#!/usr/bin/env python3
"""
Enrich an existing validation signal panel with execution/backtest context from a
feature store (recommended) or labeled dataset.

Why this exists:
- build_validation_signal_panel may create score columns correctly but enrich
  close/traded_value_proxy/has_broksum/fwd_ret_* from the wrong baseline dataset.
- For continual/challenger validation, 2026 rows can end up with score values but
  null close/liquidity/forward-return fields, causing forward test n_trades=0.

Recommended context-data:
  data/features/continual/<window>/base_features.parquet
because it contains post-validation dates needed to compute fwd_ret_*.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import polars as pl


def _norm_keys(df: pl.DataFrame) -> pl.DataFrame:
    if df.is_empty():
        return df
    exprs = []
    if "date" in df.columns:
        dtype = df.schema["date"]
        if dtype == pl.Date:
            exprs.append(pl.col("date"))
        elif dtype in (pl.Datetime, pl.Datetime("ms"), pl.Datetime("us"), pl.Datetime("ns")):
            exprs.append(pl.col("date").dt.date().alias("date"))
        else:
            exprs.append(pl.col("date").cast(pl.Utf8).str.strptime(pl.Date, strict=False).alias("date"))
    if "ticker" in df.columns:
        exprs.append(pl.col("ticker").cast(pl.Utf8).str.strip_chars().str.to_uppercase().alias("ticker"))
    return df.with_columns(exprs) if exprs else df


def _safe_numeric(df: pl.DataFrame) -> pl.DataFrame:
    exprs = []
    for c, t in zip(df.columns, df.dtypes):
        if c in ("date", "ticker", "rank1_buyer"):
            continue
        if t in (pl.Float32, pl.Float64):
            exprs.append(
                pl.when(pl.col(c).is_nan() | pl.col(c).is_infinite())
                .then(None)
                .otherwise(pl.col(c).cast(pl.Float64))
                .alias(c)
            )
        elif t in (pl.Int8, pl.Int16, pl.Int32, pl.Int64, pl.UInt8, pl.UInt16, pl.UInt32, pl.UInt64):
            exprs.append(pl.col(c).cast(pl.Int64).alias(c))
    return df.with_columns(exprs) if exprs else df


def _compute_forward_returns(ctx: pl.DataFrame, horizons: Iterable[int]) -> pl.DataFrame:
    if "close" not in ctx.columns:
        return ctx
    ctx = ctx.sort(["ticker", "date"])
    exprs = []
    close = pl.col("close").cast(pl.Float64)
    for h in horizons:
        name = f"fwd_ret_{h}d"
        exprs.append(((close.shift(-h).over("ticker") / close) - 1.0).alias(name))
    return ctx.with_columns(exprs)


def _build_context(path: Path, horizons: list[int]) -> pl.DataFrame:
    ctx = pl.read_parquet(path) if path.suffix.lower() == ".parquet" else pl.read_csv(path, try_parse_dates=True)
    ctx = _norm_keys(ctx)

    # Build traded_value_proxy if missing and close/volume exist.
    if "traded_value_proxy" not in ctx.columns and {"close", "volume"}.issubset(ctx.columns):
        ctx = ctx.with_columns((pl.col("close").cast(pl.Float64) * pl.col("volume").cast(pl.Float64)).alias("traded_value_proxy"))

    ctx = _compute_forward_returns(ctx, horizons)

    desired = [
        "date", "ticker", "open", "high", "low", "close", "volume", "value", "frequency",
        "traded_value_proxy", "has_broksum", "broker_value_anomaly_flag", "rank1_buyer",
        "rank1_buyer_daily_share", "net_flow_ratio", "buyer_dominance_ratio", "seller_dominance_ratio",
        "volume_ratio_20d", "ret_5d", "ret_20d", "macro_risk_score", "usd_idr", "brent", "bi_rate",
    ] + [f"fwd_ret_{h}d" for h in horizons]
    desired = [c for c in desired if c in ctx.columns]
    ctx = ctx.select(desired).unique(["date", "ticker"], keep="last")
    return _safe_numeric(ctx)


def enrich_panel(panel_path: Path, context_path: Path, output_path: Path, horizons: list[int], diagnostic_start: str | None = None) -> dict:
    panel = pl.read_parquet(panel_path) if panel_path.suffix.lower() == ".parquet" else pl.read_csv(panel_path, try_parse_dates=True)
    panel = _safe_numeric(_norm_keys(panel))
    ctx = _build_context(context_path, horizons)

    ctx_cols = [c for c in ctx.columns if c not in ("date", "ticker")]
    ctx_renamed = ctx.rename({c: f"{c}__ctx" for c in ctx_cols})
    joined = panel.join(ctx_renamed, on=["date", "ticker"], how="left")

    # Prefer context columns; fall back to existing panel columns if context missing.
    exprs = []
    for c in ctx_cols:
        cc = f"{c}__ctx"
        if c in joined.columns:
            exprs.append(pl.coalesce([pl.col(cc), pl.col(c)]).alias(c))
        else:
            exprs.append(pl.col(cc).alias(c))
    joined = joined.with_columns(exprs)
    drop_cols = [f"{c}__ctx" for c in ctx_cols if f"{c}__ctx" in joined.columns]
    if drop_cols:
        joined = joined.drop(drop_cols)

    joined = _safe_numeric(joined).sort(["date", "ticker"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joined.write_parquet(output_path)
    csv_path = output_path.with_suffix(".csv")
    joined.write_csv(csv_path)

    diag_df = joined
    if diagnostic_start:
        start = pl.Series([diagnostic_start]).str.strptime(pl.Date, strict=False)[0]
        diag_df = joined.filter(pl.col("date") >= start)

    score_cols = [c for c in joined.columns if c.startswith("score_")]
    check_cols = [c for c in ["close", "traded_value_proxy", "has_broksum", "fwd_ret_1d", "fwd_ret_2d", "fwd_ret_5d", "fwd_ret_10d", "fwd_ret_20d", "fwd_ret_30d"] if c in joined.columns]
    stats = {}
    if not diag_df.is_empty():
        for c in check_cols:
            stats[c] = int(diag_df.select(pl.col(c).is_not_null().sum()).item())

    meta = {
        "panel_path": str(panel_path),
        "context_path": str(context_path),
        "output_path": str(output_path),
        "csv_path": str(csv_path),
        "rows": joined.height,
        "cols": joined.width,
        "min_date": str(joined.select(pl.col("date").min()).item()) if joined.height else None,
        "max_date": str(joined.select(pl.col("date").max()).item()) if joined.height else None,
        "duplicate_ticker_date": int(joined.select(pl.struct(["date", "ticker"]).is_duplicated().sum()).item()) if joined.height else 0,
        "score_cols": score_cols,
        "context_non_null_stats_from_diagnostic_start": stats,
        "diagnostic_start": diagnostic_start,
    }
    meta_path = output_path.with_suffix(".json")
    meta_path.write_text(json.dumps(meta, indent=2, default=str))
    return meta


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--panel", required=True, help="Existing validation signal panel parquet/csv.")
    ap.add_argument("--context-data", required=True, help="Feature store/labeled dataset with OHLCV/liquidity context. Prefer continual feature store covering future dates.")
    ap.add_argument("--output", required=True, help="Output enriched panel parquet path.")
    ap.add_argument("--horizons", default="1,2,3,5,10,20,30")
    ap.add_argument("--diagnostic-start", default=None, help="Optional date to report non-null stats from, e.g. 2026-01-20.")
    args = ap.parse_args()
    horizons = [int(x.strip()) for x in args.horizons.split(",") if x.strip()]
    meta = enrich_panel(Path(args.panel), Path(args.context_data), Path(args.output), horizons, args.diagnostic_start)
    print(json.dumps(meta, indent=2, default=str))


if __name__ == "__main__":
    main()
