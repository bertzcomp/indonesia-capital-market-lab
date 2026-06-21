#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
import polars as pl


def col_or_lit(df: pl.DataFrame, name: str, value=None):
    return pl.col(name) if name in df.columns else pl.lit(value).alias(name)


def main() -> None:
    ap = argparse.ArgumentParser(description="Build leak-safe live feature and label views from ticker-day news features.")
    ap.add_argument("--root", default=".")
    ap.add_argument("--input", default="data/news/event_intelligence/aggregates/ticker_day_news_features.parquet")
    ap.add_argument("--output-dir", default="data/news/event_intelligence/modeling")
    ap.add_argument("--sample-rows", type=int, default=1000)
    ap.add_argument("--strict-tradability", action="store_true", help="Require valid OHLC and positive volume/avg_volume for modeling eligibility. Default is softer and suitable for first-pass research.")
    ap.add_argument("--require-stable-vol-denominator", action="store_true", help="Require bwd_volatility_20d > threshold for eligibility. Useful for volatility models, but too strict for alpha baseline.")
    ap.add_argument("--min-avg-volume", type=float, default=0.0, help="Optional minimum avg_volume_20d. Default 0 disables this additional filter.")
    args = ap.parse_args()

    root = Path(args.root)
    out = root / args.output_dir
    out.mkdir(parents=True, exist_ok=True)
    df = pl.read_parquet(root / args.input)

    leakage_prefixes = (
        "fwd_ret_", "ihsg_fwd_ret_", "sector_fwd_ret_", "market_alpha_",
        "sector_alpha_", "volatility_shock_", "mae_", "mfe_"
    )
    label_cols = [
        c for c in df.columns
        if c.startswith(leakage_prefixes) or c.endswith("_label_5d") or c == "reaction_label_5d"
    ]
    id_cols = [
        c for c in [
            "ticker", "news_date", "entry_date", "sector", "dominant_event_type",
            "dominant_event_side", "dominant_impact_channel"
        ]
        if c in df.columns
    ]
    live_cols = [c for c in df.columns if c not in set(label_cols)]
    labels = df.select([c for c in id_cols + label_cols if c in df.columns])
    live = df.select(live_cols)

    # ------------------------------------------------------------------
    # Quality flags
    # ------------------------------------------------------------------
    # Important fix vs rebuild_v1:
    #   * ticker-day aggregate may not always carry avg_volume_20d from older builds.
    #   * Do not mark all rows illiquid just because avg_volume_20d is missing.
    #   * Default eligibility is intentionally soft for first-pass alpha research.
    #     Use --strict-tradability for execution-grade datasets.

    close_bad = (
        (pl.col("close").is_null()) | (pl.col("close") <= 0)
        if "close" in df.columns else pl.lit(True)
    )
    ohl_bad_strict = (
        (pl.col("open").is_null()) | (pl.col("open") <= 0) |
        (pl.col("high").is_null()) | (pl.col("high") <= 0) |
        (pl.col("low").is_null()) | (pl.col("low") <= 0) |
        (pl.col("close").is_null()) | (pl.col("close") <= 0)
        if all(c in df.columns for c in ["open", "high", "low", "close"]) else close_bad
    )
    volume_bad = (
        (pl.col("volume").is_null()) | (pl.col("volume") <= 0)
        if "volume" in df.columns else pl.lit(False)
    )
    avg_volume_bad = (
        (pl.col("avg_volume_20d").is_not_null()) & (pl.col("avg_volume_20d") <= args.min_avg_volume)
        if "avg_volume_20d" in df.columns and args.min_avg_volume > 0 else pl.lit(False)
    )
    missing_outcome = (
        (pl.col("sector_alpha_5d").is_null()) | (pl.col("market_alpha_5d").is_null()) | (pl.col("fwd_ret_5d").is_null())
        if all(c in df.columns for c in ["sector_alpha_5d", "market_alpha_5d", "fwd_ret_5d"]) else pl.lit(True)
    )
    unstable_vol = (
        (pl.col("bwd_volatility_20d").is_null()) | (pl.col("bwd_volatility_20d") <= 1e-6)
        if "bwd_volatility_20d" in df.columns else pl.lit(False)
    )
    extreme_return = (
        (pl.col("bwd_ret_5d").abs() > 1.0) |
        (pl.col("fwd_ret_5d").abs() > 1.0) |
        (pl.col("sector_alpha_5d").abs() > 1.0)
        if all(c in df.columns for c in ["bwd_ret_5d", "fwd_ret_5d", "sector_alpha_5d"]) else pl.lit(False)
    )

    model = df.with_columns([
        close_bad.alias("is_bad_close_row"),
        ohl_bad_strict.alias("is_bad_ohlcv_row"),
        volume_bad.alias("is_zero_or_missing_volume_row"),
        avg_volume_bad.alias("is_below_min_avg_volume_row"),
        (volume_bad | avg_volume_bad).alias("is_illiquid_row"),
        missing_outcome.alias("is_missing_outcome_5d"),
        unstable_vol.alias("is_unstable_vol_denominator"),
        extreme_return.alias("is_extreme_return_row"),
    ])

    if "sector_alpha_5d" in model.columns:
        model = model.with_columns([
            pl.col("sector_alpha_5d").clip(-0.30, 0.30).alias("sector_alpha_5d_w"),
            pl.col("market_alpha_5d").clip(-0.30, 0.30).alias("market_alpha_5d_w") if "market_alpha_5d" in model.columns else pl.lit(None).alias("market_alpha_5d_w"),
            pl.col("fwd_ret_5d").clip(-0.30, 0.30).alias("fwd_ret_5d_w") if "fwd_ret_5d" in model.columns else pl.lit(None).alias("fwd_ret_5d_w"),
            pl.col("mae_5d").clip(-0.50, 0.10).alias("mae_5d_w") if "mae_5d" in model.columns else pl.lit(None).alias("mae_5d_w"),
            pl.col("mfe_5d").clip(-0.10, 0.50).alias("mfe_5d_w") if "mfe_5d" in model.columns else pl.lit(None).alias("mfe_5d_w"),
            pl.col("volatility_shock_5d").clip(0, 5).alias("volatility_shock_5d_w") if "volatility_shock_5d" in model.columns else pl.lit(None).alias("volatility_shock_5d_w"),
        ]).with_columns([
            (pl.col("sector_alpha_5d_w") > 0.01).cast(pl.Int8).alias("target_alpha_pos_5d"),
            (pl.col("sector_alpha_5d_w") < -0.01).cast(pl.Int8).alias("target_alpha_neg_5d"),
            (pl.col("mae_5d_w") < -0.03).cast(pl.Int8).alias("target_downside_risk_5d"),
            (pl.col("volatility_shock_5d_w") > 1.5).cast(pl.Int8).alias("target_volatility_shock_5d"),
        ])

    # Eligibility profiles:
    # default/research: valid close + outcome + no extreme returns.
    # strict: also require full OHLC and positive volume.
    eligible_expr = (~pl.col("is_bad_close_row")) & (~pl.col("is_missing_outcome_5d")) & (~pl.col("is_extreme_return_row"))
    if args.strict_tradability:
        eligible_expr = eligible_expr & (~pl.col("is_bad_ohlcv_row")) & (~pl.col("is_illiquid_row"))
    if args.require_stable_vol_denominator:
        eligible_expr = eligible_expr & (~pl.col("is_unstable_vol_denominator"))

    model = model.with_columns([eligible_expr.alias("is_modeling_eligible")])
    eligible = model.filter(pl.col("is_modeling_eligible"))

    live.write_parquet(out / "ticker_day_live_features.parquet")
    labels.write_parquet(out / "ticker_day_training_labels.parquet")
    model.write_parquet(out / "ticker_day_modeling_full_with_flags.parquet")
    eligible.write_parquet(out / "ticker_day_modeling_eligible.parquet")
    live.head(args.sample_rows).write_csv(out / "sample_live_features.csv")
    labels.head(args.sample_rows).write_csv(out / "sample_training_labels.csv")
    eligible.head(args.sample_rows).write_csv(out / "sample_modeling_eligible.csv")

    metrics = [
        "ticker_day_rows", "eligible_rows", "dropped_rows", "bad_close_rows", "bad_ohlcv_rows",
        "zero_or_missing_volume_rows", "below_min_avg_volume_rows", "illiquid_rows",
        "missing_outcome_rows", "unstable_vol_denominator_rows", "extreme_return_rows",
    ]
    values = [
        df.height,
        eligible.height,
        df.height - eligible.height,
        model.filter(pl.col("is_bad_close_row")).height,
        model.filter(pl.col("is_bad_ohlcv_row")).height,
        model.filter(pl.col("is_zero_or_missing_volume_row")).height,
        model.filter(pl.col("is_below_min_avg_volume_row")).height,
        model.filter(pl.col("is_illiquid_row")).height,
        model.filter(pl.col("is_missing_outcome_5d")).height,
        model.filter(pl.col("is_unstable_vol_denominator")).height,
        model.filter(pl.col("is_extreme_return_row")).height,
    ]
    summary = pl.DataFrame({"metric": metrics, "value": values})
    summary.write_csv(out / "modeling_quality_summary.csv")
    print(summary)
    print("Saved modeling views to", out)


if __name__ == "__main__":
    main()
