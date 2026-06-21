#!/usr/bin/env python3
"""
Score news risk/alpha for all available ticker-day news feature rows, including rows
without future outcomes. This is the production-style scorer for the news gate.

Inputs:
  - CatBoost impact/risk models trained on ticker_day_modeling_eligible.parquet
  - ticker_day_modeling_full_with_flags.parquet OR ticker_day_live_features.parquet

Output:
  - news_scores_all_live.parquet
  - news_scores_all_live_tail_1000.csv
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

import pandas as pd
from catboost import CatBoostClassifier, Pool

DEFAULT_FEATURES = [
    "sector", "subsector", "industry", "subindustry", "listing_board",
    "dominant_event_type", "dominant_event_side", "dominant_impact_channel",
    "n_articles", "n_event_clusters", "n_event_types",
    "max_materiality_score", "max_uncertainty_score", "max_novelty_score",
    "sum_news_intensity_score", "max_news_intensity_score",
    "has_market_commentary", "has_earnings_fundamental", "has_business_development",
    "has_dividend", "has_dilution_corporate_action", "has_accumulation_flow",
    "has_distribution_flow", "has_macro_currency", "has_macro_rate",
    "has_geopolitical_risk", "has_index_rebalancing", "has_commodity_shock",
    "has_buyback", "has_stock_split", "has_debt_financing", "has_credit_rating",
    "daily_ret", "volume_ratio", "bwd_volatility_20d", "drawdown_20d",
    "bwd_ret_1d", "bwd_ret_3d", "bwd_ret_5d", "bwd_ret_7d", "bwd_ret_14d", "bwd_ret_30d",
    "bwd_volume_ratio_1d", "bwd_volume_ratio_3d", "bwd_volume_ratio_5d",
    "bwd_volume_ratio_7d", "bwd_volume_ratio_14d", "bwd_volume_ratio_30d",
]

CAT_FEATURES = [
    "sector", "subsector", "industry", "subindustry", "listing_board",
    "dominant_event_type", "dominant_event_side", "dominant_impact_channel",
]


def read_frame(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    return pd.read_parquet(path)


def prepare_features(df: pd.DataFrame, features: List[str], cat_features: List[str]) -> pd.DataFrame:
    x = df.copy()
    for c in features:
        if c in cat_features:
            x[c] = x[c].astype("string").fillna("UNKNOWN")
        else:
            x[c] = pd.to_numeric(x[c], errors="coerce").fillna(0)
    return x


def percentile_bucket(p: float) -> str:
    if p >= 0.95:
        return "EXTREME"
    if p >= 0.90:
        return "HIGH"
    if p >= 0.80:
        return "MEDIUM"
    return "LOW"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--input", default="data/news/event_intelligence/modeling/ticker_day_modeling_full_with_flags.parquet")
    ap.add_argument("--impact-model", default="data/news/event_intelligence/modeling/models/news_impact_catboost.cbm")
    ap.add_argument("--risk-model", default="data/news/event_intelligence/modeling/models/news_risk_catboost.cbm")
    ap.add_argument("--output", default="data/news/event_intelligence/modeling/models/news_scores_all_live.parquet")
    args = ap.parse_args()

    root = Path(args.root)
    inp = root / args.input
    impact_model_path = root / args.impact_model
    risk_model_path = root / args.risk_model
    out = root / args.output
    out.parent.mkdir(parents=True, exist_ok=True)

    df = read_frame(inp)
    if "news_date" in df.columns:
        df["news_date"] = pd.to_datetime(df["news_date"])
    elif "date" in df.columns:
        df["news_date"] = pd.to_datetime(df["date"])
    else:
        raise SystemExit("Input must contain news_date or date column.")

    if "ticker" not in df.columns:
        raise SystemExit("Input must contain ticker column.")

    features = [c for c in DEFAULT_FEATURES if c in df.columns]
    cat_features = [c for c in CAT_FEATURES if c in features]
    if not features:
        raise SystemExit("No model features found in input.")

    x = prepare_features(df, features, cat_features)
    pool = Pool(x[features], cat_features=cat_features)

    impact_model = CatBoostClassifier()
    impact_model.load_model(str(impact_model_path))
    risk_model = CatBoostClassifier()
    risk_model.load_model(str(risk_model_path))

    df["news_alpha_score"] = impact_model.predict_proba(pool)[:, 1]
    df["news_risk_score"] = risk_model.predict_proba(pool)[:, 1]
    df["news_risk_pct_rank"] = df["news_risk_score"].rank(pct=True)
    df["news_risk_bucket_pct"] = df["news_risk_pct_rank"].apply(percentile_bucket)

    keep = [
        "news_date", "ticker", "sector", "subsector", "industry", "listing_board",
        "dominant_event_type", "dominant_event_side", "dominant_impact_channel",
        "n_articles", "n_event_clusters", "n_event_types",
        "max_materiality_score", "max_uncertainty_score", "max_novelty_score",
        "news_alpha_score", "news_risk_score", "news_risk_pct_rank", "news_risk_bucket_pct",
        "sector_alpha_5d_w", "market_alpha_5d_w", "fwd_ret_5d_w", "mae_5d_w", "mfe_5d_w",
        "target_alpha_pos_5d", "target_downside_risk_5d",
        "is_modeling_eligible", "is_missing_outcome_5d",
    ]
    keep = [c for c in keep if c in df.columns]
    df[keep].to_parquet(out, index=False)
    df[keep].tail(1000).to_csv(out.with_name(out.stem + "_tail_1000.csv"), index=False)

    print("Saved:", out)
    print("Rows:", len(df))
    print("Date range:", df["news_date"].min(), "->", df["news_date"].max())
    print(df["news_risk_bucket_pct"].value_counts(dropna=False))
    print("Risk thresholds:")
    for q in [0.80, 0.90, 0.95, 0.99]:
        print(f"p{int(q*100)}:", df["news_risk_score"].quantile(q))


if __name__ == "__main__":
    main()
