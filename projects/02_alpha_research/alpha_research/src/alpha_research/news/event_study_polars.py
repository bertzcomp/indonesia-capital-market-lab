from __future__ import annotations

from pathlib import Path
import polars as pl


def build_basic_event_study(df: pl.DataFrame, output_dir: str | Path) -> pl.DataFrame:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    if df.is_empty():
        out = pl.DataFrame()
        out.write_csv(output_dir / "event_study_by_event_type.csv")
        return out
    out = event_study(df, ["event_type"], min_rows=10)
    out.write_csv(output_dir / "event_study_by_event_type.csv")
    return out


def event_study(df: pl.DataFrame, group_cols: list[str], min_rows: int = 30, robust: bool = True) -> pl.DataFrame:
    work = df
    # robust clipped metrics are created if absent.
    if robust and "sector_alpha_5d_w" not in work.columns and "sector_alpha_5d" in work.columns:
        work = work.with_columns([
            pl.col("sector_alpha_5d").clip(-0.30, 0.30).alias("sector_alpha_5d_w"),
            pl.col("market_alpha_5d").clip(-0.30, 0.30).alias("market_alpha_5d_w") if "market_alpha_5d" in work.columns else pl.lit(None).alias("market_alpha_5d_w"),
            pl.col("mae_5d").clip(-0.50, 0.10).alias("mae_5d_w") if "mae_5d" in work.columns else pl.lit(None).alias("mae_5d_w"),
            pl.col("mfe_5d").clip(-0.10, 0.50).alias("mfe_5d_w") if "mfe_5d" in work.columns else pl.lit(None).alias("mfe_5d_w"),
            pl.col("volatility_shock_5d").clip(0.0, 5.0).alias("volatility_shock_5d_w") if "volatility_shock_5d" in work.columns else pl.lit(None).alias("volatility_shock_5d_w"),
        ])
    cols = work.columns
    aggs = [
        pl.len().alias("n_rows"),
        pl.col("article_id").n_unique().alias("n_articles") if "article_id" in cols else pl.len().alias("n_articles"),
        pl.col("ticker").n_unique().alias("n_tickers") if "ticker" in cols else pl.len().alias("n_tickers"),
    ]
    if "sector_alpha_5d_w" in cols or "sector_alpha_5d" in cols:
        a = "sector_alpha_5d_w" if "sector_alpha_5d_w" in work.columns else "sector_alpha_5d"
        aggs += [
            pl.col(a).mean().alias("avg_sector_alpha_5d"),
            pl.col(a).median().alias("median_sector_alpha_5d"),
            (pl.col(a) > 0).mean().alias("hit_rate_sector_alpha_5d"),
            (pl.col(a) > 0.01).mean().alias("hit_rate_sector_alpha_gt_1pct_5d"),
        ]
    if "market_alpha_5d_w" in work.columns or "market_alpha_5d" in cols:
        m = "market_alpha_5d_w" if "market_alpha_5d_w" in work.columns else "market_alpha_5d"
        aggs += [pl.col(m).mean().alias("avg_market_alpha_5d"), (pl.col(m) > 0).mean().alias("hit_rate_market_alpha_5d")]
    if "volatility_shock_5d_w" in work.columns or "volatility_shock_5d" in cols:
        v = "volatility_shock_5d_w" if "volatility_shock_5d_w" in work.columns else "volatility_shock_5d"
        aggs += [pl.col(v).mean().alias("avg_volatility_shock_5d"), (pl.col(v) > 1.5).mean().alias("volatility_shock_rate_5d")]
    for c in ["mae_5d_w", "mfe_5d_w", "mae_5d", "mfe_5d"]:
        if c in work.columns:
            aggs.append(pl.col(c).mean().alias(f"avg_{c}"))
    for c in ["sentiment_trap_label_5d", "delayed_reaction_label_5d", "acceleration_trigger_label_5d", "sell_the_news_label_5d"]:
        if c in work.columns:
            aggs.append((pl.col(c) == 1).mean().alias(c.replace("label", "rate")))
    return work.group_by(group_cols).agg(aggs).filter(pl.col("n_rows") >= min_rows).sort("n_rows", descending=True)


def build_ticker_day_event_study(input_path: str | Path, output_dir: str | Path, min_rows: int = 30) -> None:
    df = pl.read_parquet(input_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    specs = [
        (["dominant_event_type"], "ticker_day_study_by_dominant_event.csv"),
        (["dominant_event_type", "dominant_event_side"], "ticker_day_study_by_dominant_event_side.csv"),
        (["dominant_event_type", "sector"], "ticker_day_study_by_dominant_event_sector.csv"),
    ]
    for cols, fname in specs:
        actual = [c for c in cols if c in df.columns]
        if actual:
            event_study(df, actual, min_rows=min_rows).write_csv(out / fname)
