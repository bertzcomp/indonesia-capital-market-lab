from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import polars as pl


@dataclass
class AggregateResult:
    article_rows: int
    event_clusters: int
    ticker_days: int
    market_days: int
    output_dir: str


DEFAULT_EVENT_TYPES = [
    "market_commentary", "earnings_fundamental", "business_development", "dividend",
    "dilution_corporate_action", "accumulation_flow", "distribution_flow", "analyst_view",
    "commodity_shock", "macro_currency", "macro_rate", "geopolitical_risk", "index_rebalancing",
    "suspension_uma", "delisting_bankruptcy", "buyback", "stock_split", "debt_financing",
    "credit_rating", "ipo_listing", "general_news", "general_macro",
]


def _safe_cols(df: pl.DataFrame, cols: list[str]) -> list[str]:
    return [c for c in cols if c in df.columns]


def build_event_clusters(df: pl.DataFrame) -> pl.DataFrame:
    if df.is_empty():
        return df
    score = (
        pl.col("materiality_score").fill_null(0) * 0.35
        + pl.col("news_intensity_score").fill_null(0) * 0.35
        + pl.col("uncertainty_score").fill_null(0) * 0.20
        + pl.col("novelty_score").fill_null(0) * 0.10
    ).alias("event_priority_score")
    work = df.with_columns(score).sort(["ticker", "news_date", "event_type", "event_priority_score"], descending=[False, False, False, True])
    group_cols = ["news_date", "ticker", "event_type", "event_side", "impact_channel"]
    clusters = (
        work.group_by(group_cols)
        .agg([
            pl.col("event_row_id").first().alias("representative_event_row_id"),
            pl.col("article_id").n_unique().alias("n_articles"),
            pl.col("source").n_unique().alias("n_sources"),
            pl.col("title").first().alias("dominant_title"),
            pl.col("sector").first().alias("sector"),
            pl.col("subsector").first().alias("subsector"),
            pl.col("industry").first().alias("industry"),
            pl.col("news_category").first().alias("news_category"),
            pl.col("event_priority_score").max().alias("dominant_event_score"),
            pl.col("materiality_score").mean().alias("avg_materiality_score"),
            pl.col("materiality_score").max().alias("max_materiality_score"),
            pl.col("uncertainty_score").mean().alias("avg_uncertainty_score"),
            pl.col("uncertainty_score").max().alias("max_uncertainty_score"),
            pl.col("novelty_score").mean().alias("avg_novelty_score"),
            pl.col("novelty_score").max().alias("max_novelty_score"),
            pl.col("news_intensity_score").sum().alias("sum_news_intensity_score"),
            pl.col("news_intensity_score").max().alias("max_news_intensity_score"),
        ])
        .with_columns([
            (pl.col("news_date").cast(pl.Utf8) + "|" + pl.col("ticker") + "|" + pl.col("event_type") + "|" + pl.col("event_side") + "|" + pl.col("impact_channel")).hash().cast(pl.Utf8).alias("event_cluster_id")
        ])
        .select(["event_cluster_id"] + group_cols + [c for c in [
            "representative_event_row_id", "n_articles", "n_sources", "dominant_title", "sector", "subsector", "industry", "news_category",
            "dominant_event_score", "avg_materiality_score", "max_materiality_score", "avg_uncertainty_score", "max_uncertainty_score",
            "avg_novelty_score", "max_novelty_score", "sum_news_intensity_score", "max_news_intensity_score"
        ] if c in work.columns or c in ["n_articles", "n_sources", "dominant_title", "dominant_event_score", "avg_materiality_score", "max_materiality_score", "avg_uncertainty_score", "max_uncertainty_score", "avg_novelty_score", "max_novelty_score", "sum_news_intensity_score", "max_news_intensity_score", "representative_event_row_id"]])
    )
    return clusters


def build_ticker_day_features(df: pl.DataFrame, event_types: list[str] | None = None) -> pl.DataFrame:
    event_types = event_types or DEFAULT_EVENT_TYPES
    work = df.filter(pl.col("ticker") != "__MARKET__")
    if work.is_empty():
        return work
    work = work.with_columns([
        (
            pl.col("materiality_score").fill_null(0) * 0.35
            + pl.col("news_intensity_score").fill_null(0) * 0.35
            + pl.col("uncertainty_score").fill_null(0) * 0.20
            + pl.col("novelty_score").fill_null(0) * 0.10
        ).alias("event_priority_score")
    ])
    # Pick dominant event per ticker-day.
    dom = (
        work.sort(["ticker", "news_date", "event_priority_score"], descending=[False, False, True])
        .group_by(["ticker", "news_date"])
        .agg([
            pl.col("event_type").first().alias("dominant_event_type"),
            pl.col("event_side").first().alias("dominant_event_side"),
            pl.col("impact_channel").first().alias("dominant_impact_channel"),
            pl.col("title").first().alias("dominant_title"),
            pl.col("event_priority_score").first().alias("dominant_event_score"),
        ])
    )
    base_aggs = [
        pl.col("article_id").n_unique().alias("n_articles"),
        pl.col("event_type").n_unique().alias("n_event_types"),
        pl.len().alias("n_event_rows"),
        pl.col("sector").first().alias("sector"),
        pl.col("subsector").first().alias("subsector"),
        pl.col("industry").first().alias("industry"),
        pl.col("listing_board").first().alias("listing_board"),
        pl.col("materiality_score").max().alias("max_materiality_score"),
        pl.col("uncertainty_score").max().alias("max_uncertainty_score"),
        pl.col("novelty_score").max().alias("max_novelty_score"),
        pl.col("news_intensity_score").sum().alias("sum_news_intensity_score"),
        pl.col("news_intensity_score").max().alias("max_news_intensity_score"),
    ]
    # Carry ticker-date market features/outcomes with first non-null-ish value.
    carry_prefixes = ["bwd_ret_", "bwd_volume_ratio_", "fwd_ret_", "ihsg_fwd_ret_", "sector_fwd_ret_", "market_alpha_", "sector_alpha_", "volatility_shock_", "mae_", "mfe_"]
    carry_cols = [c for c in work.columns if c in {"entry_date", "open", "high", "low", "close", "volume", "value", "frequency", "foreign_buy", "foreign_sell", "daily_ret", "is_zero_volume", "avg_volume_20d", "volume_ratio", "bwd_volatility_20d", "drawdown_20d", "reaction_label_5d", "directional_label_5d", "volatility_label_5d", "risk_label_5d", "sentiment_trap_label_5d", "sell_the_news_label_5d", "delayed_reaction_label_5d", "acceleration_trigger_label_5d", "confirmed_positive_label_5d", "confirmed_negative_label_5d"} or any(c.startswith(p) for p in carry_prefixes)]
    aggs = base_aggs + [pl.col(c).drop_nulls().first().alias(c) for c in carry_cols if c not in {"ticker", "news_date"}]
    # event type counts and flags
    for et in event_types:
        name = et.replace("/", "_").replace(" ", "_")
        aggs.append((pl.col("event_type") == et).sum().alias(f"count_{name}"))
        aggs.append(((pl.col("event_type") == et).sum() > 0).cast(pl.Int8).alias(f"has_{name}"))
    out = work.group_by(["ticker", "news_date"]).agg(aggs).join(dom, on=["ticker", "news_date"], how="left")
    return out


def build_market_day_regime(df: pl.DataFrame, event_types: list[str] | None = None) -> pl.DataFrame:
    event_types = event_types or DEFAULT_EVENT_TYPES
    if df.is_empty():
        return df
    work = df.with_columns([
        (
            pl.col("materiality_score").fill_null(0) * 0.35
            + pl.col("news_intensity_score").fill_null(0) * 0.35
            + pl.col("uncertainty_score").fill_null(0) * 0.20
            + pl.col("novelty_score").fill_null(0) * 0.10
        ).alias("event_priority_score")
    ])
    dom = (
        work.sort(["news_date", "event_priority_score"], descending=[False, True])
        .group_by("news_date")
        .agg([
            pl.col("event_type").first().alias("dominant_market_event_type"),
            pl.col("event_side").first().alias("dominant_market_event_side"),
            pl.col("title").first().alias("dominant_market_title"),
            pl.col("event_priority_score").first().alias("dominant_market_event_score"),
        ])
    )
    aggs = [
        pl.col("article_id").n_unique().alias("total_articles"),
        pl.len().alias("total_event_rows"),
        pl.col("ticker").n_unique().alias("n_tickers_mentioned"),
        (pl.col("news_category") == "macro").sum().alias("macro_event_rows"),
        (pl.col("news_category") == "market").sum().alias("market_event_rows"),
        pl.col("materiality_score").max().alias("market_materiality_max"),
        pl.col("uncertainty_score").max().alias("market_uncertainty_max"),
        pl.col("news_intensity_score").sum().alias("market_news_intensity_sum"),
    ]
    for et in event_types:
        name = et.replace("/", "_").replace(" ", "_")
        aggs.append((pl.col("event_type") == et).sum().alias(f"market_count_{name}"))
        aggs.append(((pl.col("event_type") == et).sum() > 0).cast(pl.Int8).alias(f"market_has_{name}"))
    out = work.group_by("news_date").agg(aggs).join(dom, on="news_date", how="left")
    out = out.with_columns([
        (
            pl.col("market_uncertainty_max").fill_null(0) * 0.35
            + pl.col("market_materiality_max").fill_null(0) * 0.35
            + (pl.col("market_news_intensity_sum").fill_null(0) / (pl.col("total_event_rows").fill_null(1))).clip(0, 1) * 0.30
        ).alias("market_event_stress_score")
    ])
    return out


def build_news_event_aggregates(input_path: str | Path, output_dir: str | Path) -> AggregateResult:
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    df = pl.read_parquet(input_path)
    clusters = build_event_clusters(df.filter(pl.col("ticker") != "__MARKET__"))
    ticker_day = build_ticker_day_features(df)
    market_day = build_market_day_regime(df)
    clusters.write_parquet(output_dir / "news_event_cluster.parquet")
    ticker_day.write_parquet(output_dir / "ticker_day_news_features.parquet")
    market_day.write_parquet(output_dir / "market_day_news_regime.parquet")
    clusters.head(20).write_csv(output_dir / "sample_event_cluster_20.csv")
    ticker_day.head(20).write_csv(output_dir / "sample_ticker_day_20.csv")
    market_day.head(20).write_csv(output_dir / "sample_market_day_20.csv")
    meta = {
        "article_rows": df.height,
        "event_clusters": clusters.height,
        "ticker_days": ticker_day.height,
        "market_days": market_day.height,
        "output_dir": str(output_dir),
    }
    (output_dir / "aggregate_meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    return AggregateResult(**meta)
