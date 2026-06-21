from __future__ import annotations
from pathlib import Path
import polars as pl
from alpha_research.core.dates import ensure_start_end
from alpha_research.core.io import safe_write_parquet, write_json
from alpha_research.features.contract import get_feature_cols


def _rank_pct(expr: str) -> pl.Expr:
    # Cross-sectional percentile rank per date. Higher forward return -> closer to 1.0.
    return (pl.col(expr).rank(method="average").over("date") / pl.len().over("date")).alias(f"target_{expr}_rank")


def build_training_dataset(root, feature_scope="history", start_date=None, end_date=None):
    root = Path(root)
    feat = root / "data/features" / feature_scope / "base_features.parquet"
    if not feat.exists() and feature_scope == "live":
        feat = root / "data/features/live/latest/base_features.parquet"
    if not feat.exists():
        raise FileNotFoundError(feat)

    df = pl.read_parquet(feat).with_columns(pl.col("date").cast(pl.Date, strict=False)).sort(["ticker", "date"])
    if start_date and end_date:
        s, e = ensure_start_end(start_date, end_date)
        df = df.filter((pl.col("date") >= pl.lit(s)) & (pl.col("date") <= pl.lit(e)))

    # Forward returns. These remain null near the end of each ticker history; trainers drop null target rows per target.
    horizons = [1, 2, 3, 5, 10, 20, 30, 60]
    for h in horizons:
        df = df.with_columns((pl.col("close").shift(-h).over("ticker") / pl.col("close") - 1).alias(f"fwd_ret_{h}d"))

    # Cross-sectional future-return ranks for ranking/momentum targets.
    df = df.with_columns([
        _rank_pct("fwd_ret_3d"),
        _rank_pct("fwd_ret_5d"),
        _rank_pct("fwd_ret_10d"),
        _rank_pct("fwd_ret_20d"),
        _rank_pct("fwd_ret_30d"),
        _rank_pct("fwd_ret_60d"),
    ])

    # Core targets. Keep thresholds explicit here; future version can read configs/label_policy.json.
    df = df.with_columns([
        (pl.col("fwd_ret_3d") >= 0.025).cast(pl.Int8).alias("label_scalp"),
        (pl.col("fwd_ret_10d") >= 0.05).cast(pl.Int8).alias("label_swing"),
        (pl.col("fwd_ret_20d") >= 0.08).cast(pl.Int8).alias("label_position"),
        (pl.col("fwd_ret_1d") >= 0.095).cast(pl.Int8).alias("label_ara_tomorrow"),
        ((pl.col("fwd_ret_1d") >= 0.075) & (pl.col("fwd_ret_1d") < 0.095)).cast(pl.Int8).alias("label_near_ara_tomorrow"),
        ((pl.col("rank1_same_buyer_flag").shift(-1).over("ticker") == 1) & (pl.col("has_broksum").shift(-1).over("ticker") == 1)).cast(pl.Int8).alias("label_brok_cont"),
        (((pl.col("rank1_same_buyer_streak") >= 3) | (pl.col("buyer_dominance_ratio") >= 0.4)) & (pl.col("fwd_ret_20d") >= 0.10)).cast(pl.Int8).alias("label_silent_accum_breakout"),
        (pl.col("fwd_ret_30d") >= 0.20).cast(pl.Int8).alias("label_big_runner_30d"),
        (pl.col("fwd_ret_60d") >= 0.50).cast(pl.Int8).alias("label_multibagger_60d"),
    ])

    # Momentum ranker targets: top cross-sectional forward-return candidates.
    # These are not “buy threshold” labels; they train ranking-style binary classifiers.
    df = df.with_columns([
        ((pl.col("target_fwd_ret_5d_rank") >= 0.80) & (pl.col("fwd_ret_5d") > 0)).cast(pl.Int8).alias("label_momentum_5d"),
        ((pl.col("target_fwd_ret_10d_rank") >= 0.80) & (pl.col("fwd_ret_10d") > 0)).cast(pl.Int8).alias("label_momentum_10d"),
        ((pl.col("target_fwd_ret_20d_rank") >= 0.80) & (pl.col("fwd_ret_20d") > 0)).cast(pl.Int8).alias("label_momentum_20d"),
    ])

    outdir = root / "data/datasets/training"
    outdir.mkdir(parents=True, exist_ok=True)
    safe_write_parquet(df, outdir / "full_labeled.parquet")

    targets = [c for c in df.columns if c.startswith("label_")]
    target_summary = []
    for c in targets:
        vc = df.group_by(c).len().sort(c).to_dicts()
        target_summary.append({"target": c, "distribution": vc})

    meta = {
        "rows": df.height,
        "cols": df.width,
        "feature_count": len(get_feature_cols(df)),
        "feature_cols": get_feature_cols(df),
        "targets": targets,
        "target_summary": target_summary,
    }
    write_json(outdir / "dataset_meta.json", meta)
    return meta
