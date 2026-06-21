from __future__ import annotations
import polars as pl

ID_COLS = ["date", "ticker"]
LABEL_PREFIXES = ("label_", "target_", "fwd_")

BDM_GROUPS = ["market_maker", "foreign", "non_retail"]
BDM_WINDOWS = ["day", "week"]
BDM_BASE_FIELDS = ["price", "chg", "tx"]
BDM_HIST_FIELDS = ["hist1", "hist2", "hist3", "hist4", "hist5"]
BDM_FEATURE_COLUMNS = [
    f"bdm_{g}_{w}_{f}"
    for g in BDM_GROUPS
    for w in BDM_WINDOWS
    for f in (BDM_BASE_FIELDS + BDM_HIST_FIELDS)
]

MACRO_WINDOWS = [5, 10, 20, 60]
MACRO_BASE_COLUMNS = [
    "idr_usd", "usd_idr", "wti", "brent", "coal_proxy", "ihsg", "bi_rate",
    "coal_gap_flag", "oil_avg", "wti_return", "brent_return", "fx_return",
    "coal_proxy_return", "bi_rate_change", "market_ret_1d", "market_ret_5d",
    "market_ret_20d", "market_volatility_20d", "macro_risk_score",
    "macro_risk_zscore", "macro_missing_flag", "usd_idr_zscore",
    "idr_weak_flag", "idr_strong_flag", "brent_zscore", "coal_proxy_zscore",
    "ihsg_zscore", "oil_crash_flag", "oil_rally_flag", "wti_brent_spread",
    "coal_rally_flag", "coal_slump_flag", "bi_rate_cut_flag", "bi_rate_hike_flag",
    "oil_idr_divergence", "coal_oil_spread_ret",
]
MACRO_ROLLING_COLUMNS = []
for w in MACRO_WINDOWS:
    MACRO_ROLLING_COLUMNS.extend([
        f"idr_usd_ret_{w}d", f"idr_usd_vol_{w}d",
        f"brent_ret_{w}d", f"wti_ret_{w}d", f"oil_avg_ret_{w}d", f"brent_vol_{w}d",
        f"coal_ret_{w}d", f"coal_vol_{w}d", f"ihsg_ret_{w}d",
    ])
MACRO_FEATURE_COLUMNS = MACRO_BASE_COLUMNS + MACRO_ROLLING_COLUMNS

FEATURE_COLUMNS = [
    # price/base
    "open","high","low","close","volume","value","frequency","foreign_buy","foreign_sell",
    "ret_1d","ret_5d","ret_10d","ret_20d","ma_5","ma_20","volume_ma20","volatility_20d","close_vs_ma20","volume_ratio_20d","traded_value_proxy",
    # broker flow
    "has_broksum","buy_val_total","sell_val_total","net_val_total","buy_lot_total","sell_lot_total","buy_freq_total","sell_freq_total",
    "buy_val_total_sane","sell_val_total_sane","net_val_total_sane","rank1_buy_val_sane","rank1_sell_val_sane",
    "net_flow_ratio","net_buy_flag","buyer_dominance_ratio","seller_dominance_ratio","broker_value_anomaly_flag",
    "rank1_same_buyer_flag","rank1_same_buyer_streak","rank1_buyer_daily_count","rank1_buyer_daily_share","rank1_buyer_overcrowded_flag",
    # insider
    "insider_event_count","insider_buy_count","insider_sell_count","insider_net_shares","insider_net_pct_sum","insider_foreign_event_count","insider_local_event_count","has_insider_activity",
    # corporate action
    "has_corporate_action","ca_event_count",
    # macro, first-class contract
    *MACRO_FEATURE_COLUMNS,
    # BDM sparse flags
    "has_bdm_any","has_bdm_market_maker","has_bdm_non_retail","has_bdm_foreign",
    # BDM sparse numeric full contract, including history vectors
    *BDM_FEATURE_COLUMNS,
    # cross-sectional ranks
    "cs_rank_ret_5d","cs_rank_ret_10d","cs_rank_ret_20d","cs_rank_volume_ratio_20d","cs_rank_net_flow_ratio","cs_rank_rank1_same_buyer_streak","cs_rank_buyer_dominance_ratio"
]

CATEGORICAL_COLUMNS = ["rank1_buyer", "rank1_seller", "rank1_buyer_type", "rank1_seller_type", "market_regime"]

FLAG_COLUMNS = {
    c for c in FEATURE_COLUMNS
    if c.startswith("has_") or c.endswith("_flag") or c in {
        "net_buy_flag", "rank1_same_buyer_flag", "rank1_buyer_overcrowded_flag", "macro_missing_flag"
    }
}


def ensure_feature_contract(df: pl.DataFrame) -> pl.DataFrame:
    """Force a stable model feature schema for history, live, and continual scopes.

    Sparse sources such as BDM must still appear in historical feature stores even when
    no rows exist in the requested historical date range. This prevents history/live
    schema drift and silent train-vs-inference mismatch.
    """
    # Add categorical columns as string nulls
    for c in CATEGORICAL_COLUMNS:
        if c not in df.columns:
            df = df.with_columns(pl.lit(None).cast(pl.Utf8).alias(c))
    # Add numeric/flag columns
    for c in FEATURE_COLUMNS:
        if c not in df.columns:
            if c in FLAG_COLUMNS:
                df = df.with_columns(pl.lit(0).cast(pl.Int8).alias(c))
            else:
                df = df.with_columns(pl.lit(None).cast(pl.Float64).alias(c))
    # final order: id, categorical, feature numeric, remaining non-label cols
    ordered=[]
    for c in ID_COLS + CATEGORICAL_COLUMNS + FEATURE_COLUMNS:
        if c in df.columns and c not in ordered:
            ordered.append(c)
    rest=[c for c in df.columns if c not in ordered and not c.startswith(LABEL_PREFIXES)]
    return df.select(ordered + rest)


def get_feature_cols(df: pl.DataFrame):
    banned=set(ID_COLS + CATEGORICAL_COLUMNS)
    out=[]
    for c,d in zip(df.columns, df.dtypes):
        if c in banned or c.startswith(LABEL_PREFIXES): continue
        if d.is_numeric(): out.append(c)
    return out
