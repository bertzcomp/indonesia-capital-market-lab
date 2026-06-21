from __future__ import annotations
from pathlib import Path
import json, shutil
import polars as pl
import pandas as pd
from alpha_research.core.dates import ensure_start_end
from alpha_research.core.io import safe_write_parquet, write_json
from alpha_research.core.contracts import assert_unique, safe_left_join, normalize_date_ticker
from alpha_research.features.contract import ensure_feature_contract, get_feature_cols
from alpha_research.features.sanity import harden_broker_ratios, sanitize_numeric
from alpha_research.macro.builder import build_macro

VALUE_CAP=1e13
RATIO_THRESHOLD=20.0

def _read(root, name):
    p=Path(root)/"data/raw_canonical"/f"{name}.parquet"
    return pl.read_parquet(p) if p.exists() else pl.DataFrame()

def _filter(df,start,end):
    if df.is_empty() or "date" not in df.columns: return df
    s,e=ensure_start_end(start,end)
    return df.with_columns(pl.col("date").cast(pl.Date, strict=False)).filter((pl.col("date")>=pl.lit(s))&(pl.col("date")<=pl.lit(e)))

def add_price_features(df):
    if df.is_empty(): return df
    df=normalize_date_ticker(df).sort(["ticker","date"])
    # Stage 1 returns and moving averages
    df=df.with_columns([
        pl.col("close").pct_change().over("ticker").alias("ret_1d"),
        (pl.col("close")/pl.col("close").shift(5).over("ticker")-1).alias("ret_5d"),
        (pl.col("close")/pl.col("close").shift(10).over("ticker")-1).alias("ret_10d"),
        (pl.col("close")/pl.col("close").shift(20).over("ticker")-1).alias("ret_20d"),
        pl.col("close").rolling_mean(5).over("ticker").alias("ma_5"),
        pl.col("close").rolling_mean(20).over("ticker").alias("ma_20"),
        pl.col("volume").rolling_mean(20).over("ticker").alias("volume_ma20"),
        (pl.when(pl.col("value").is_not_null()).then(pl.col("value")).otherwise(pl.col("close")*pl.col("volume"))).alias("traded_value_proxy")
    ])
    # Stage 2 references aliases
    df=df.with_columns([
        pl.col("ret_1d").rolling_std(20).over("ticker").alias("volatility_20d"),
        (pl.col("close")/pl.col("ma_20")-1).alias("close_vs_ma20"),
        (pl.col("volume")/pl.col("volume_ma20")).alias("volume_ratio_20d")
    ])
    return sanitize_numeric(df)

def aggregate_broker(b):
    if b.is_empty(): return b
    b=normalize_date_ticker(b).sort(["date","ticker","rank"])
    total=b.group_by(["date","ticker"]).agg([
        pl.col("buy_val").sum().alias("buy_val_total"), pl.col("sell_val").sum().alias("sell_val_total"),
        pl.col("buy_lot").sum().alias("buy_lot_total"), pl.col("sell_lot").sum().alias("sell_lot_total"),
        pl.col("buy_freq").sum().alias("buy_freq_total"), pl.col("sell_freq").sum().alias("sell_freq_total"),
        pl.len().alias("broksum_rank_rows")
    ])
    r1=b.filter(pl.col("rank")==1).select([
        "date","ticker",
        pl.col("buy_broker").alias("rank1_buyer"), pl.col("buy_type").alias("rank1_buyer_type"), pl.col("buy_val").alias("rank1_buy_val"), pl.col("buy_lot").alias("rank1_buy_lot"), pl.col("buy_freq").alias("rank1_buy_freq"),
        pl.col("sell_broker").alias("rank1_seller"), pl.col("sell_type").alias("rank1_seller_type"), pl.col("sell_val").alias("rank1_sell_val"), pl.col("sell_lot").alias("rank1_sell_lot"), pl.col("sell_freq").alias("rank1_sell_freq")
    ]).unique(subset=["date","ticker"], keep="first")
    out=total.join(r1,on=["date","ticker"],how="left")
    out=out.with_columns([
        pl.lit(1).cast(pl.Int8).alias("has_broksum"),
        pl.when(pl.col("buy_val_total").abs()>VALUE_CAP).then(None).otherwise(pl.col("buy_val_total")).alias("buy_val_total_sane"),
        pl.when(pl.col("sell_val_total").abs()>VALUE_CAP).then(None).otherwise(pl.col("sell_val_total")).alias("sell_val_total_sane"),
        pl.when(pl.col("rank1_buy_val").abs()>VALUE_CAP).then(None).otherwise(pl.col("rank1_buy_val")).alias("rank1_buy_val_sane"),
        pl.when(pl.col("rank1_sell_val").abs()>VALUE_CAP).then(None).otherwise(pl.col("rank1_sell_val")).alias("rank1_sell_val_sane"),
        ((pl.col("buy_val_total").abs()>VALUE_CAP) | (pl.col("sell_val_total").abs()>VALUE_CAP)).cast(pl.Int8).alias("broker_value_anomaly_flag")
    ])
    out=out.with_columns((pl.col("buy_val_total_sane")-pl.col("sell_val_total_sane")).alias("net_val_total_sane"))
    out=harden_broker_ratios(out)
    # rank1 streak via pandas for simplicity and correctness
    pdf=out.sort(["ticker","date"]).to_pandas()
    if len(pdf):
        pdf["rank1_same_buyer_flag"]=(pdf.groupby("ticker")["rank1_buyer"].shift(1)==pdf["rank1_buyer"]).astype("int8")
        streak=[]
        for _,g in pdf.groupby("ticker", sort=False):
            cur=0; prev=None
            for bkr in g["rank1_buyer"]:
                if pd.notna(bkr) and bkr==prev: cur+=1
                else: cur=1 if pd.notna(bkr) else 0
                streak.append(cur); prev=bkr
        pdf["rank1_same_buyer_streak"]=streak
        out=pl.from_pandas(pdf).with_columns(pl.col("date").cast(pl.Date, strict=False))
    conc=out.group_by(["date","rank1_buyer"]).agg(pl.len().alias("rank1_buyer_daily_count"))
    totals=out.group_by("date").agg(pl.len().alias("daily_broksum_count"))
    conc=conc.join(totals,on="date",how="left").with_columns((pl.col("rank1_buyer_daily_count")/pl.col("daily_broksum_count")).alias("rank1_buyer_daily_share"))
    out=out.join(conc.select(["date","rank1_buyer","rank1_buyer_daily_count","rank1_buyer_daily_share"]),on=["date","rank1_buyer"],how="left")
    out=out.with_columns((pl.col("rank1_buyer_daily_share")>=0.30).cast(pl.Int8).alias("rank1_buyer_overcrowded_flag"))
    assert_unique(out,["date","ticker"],"broker_features")
    return sanitize_numeric(out)

def aggregate_insider(i):
    if i.is_empty(): return i
    i=normalize_date_ticker(i)
    i=i.with_columns([
        pl.when(pl.col("action_type").str.contains("BUY")).then(pl.col("shares_changed").abs()).when(pl.col("action_type").str.contains("SELL")).then(-pl.col("shares_changed").abs()).otherwise(0).alias("signed_shares"),
        pl.when(pl.col("action_type").str.contains("BUY")).then(pl.col("shares_changed_pct").abs()).when(pl.col("action_type").str.contains("SELL")).then(-pl.col("shares_changed_pct").abs()).otherwise(0).alias("signed_pct")
    ])
    out=i.group_by(["date","ticker"]).agg([
        pl.len().alias("insider_event_count"),
        pl.col("action_type").str.contains("BUY").sum().alias("insider_buy_count"),
        pl.col("action_type").str.contains("SELL").sum().alias("insider_sell_count"),
        pl.col("signed_shares").sum().alias("insider_net_shares"),
        pl.col("signed_pct").sum().alias("insider_net_pct_sum"),
        pl.col("nationality").str.contains("FOREIGN").sum().alias("insider_foreign_event_count"),
        pl.col("nationality").str.contains("LOCAL").sum().alias("insider_local_event_count"),
    ]).with_columns(pl.lit(1).cast(pl.Int8).alias("has_insider_activity"))
    return out

def aggregate_ca(ca):
    if ca.is_empty(): return ca
    ca=normalize_date_ticker(ca)
    return ca.group_by(["date","ticker"]).agg(pl.len().alias("ca_event_count")).with_columns(pl.lit(1).cast(pl.Int8).alias("has_corporate_action"))

def pivot_bdm(b):
    if b.is_empty(): return b
    b=normalize_date_ticker(b)
    frames=[]
    for group in ["market_maker","foreign","non_retail"]:
        for window in ["day","week"]:
            sub=b.filter((pl.col("group")==group)&(pl.col("window")==window))
            if sub.is_empty(): continue
            pref=f"bdm_{group}_{window}"
            cols=["price","chg","tx","hist1","hist2","hist3","hist4","hist5"]
            keep=["date","ticker"]+[c for c in cols if c in sub.columns]
            sub=sub.select(keep).rename({c:f"{pref}_{c}" for c in keep if c not in ["date","ticker"]})
            frames.append(sub.unique(subset=["date","ticker"],keep="last"))
    if not frames:
        return pl.DataFrame(schema={"date":pl.Date,"ticker":pl.Utf8})
    out=frames[0]
    for f in frames[1:]: out=out.join(f,on=["date","ticker"],how="outer_coalesce")
    mm=[c for c in out.columns if c.startswith("bdm_market_maker")]
    nr=[c for c in out.columns if c.startswith("bdm_non_retail")]
    fg=[c for c in out.columns if c.startswith("bdm_foreign")]
    out=out.with_columns([
        pl.any_horizontal([pl.col(c).is_not_null() for c in mm+nr+fg]).cast(pl.Int8).alias("has_bdm_any") if (mm+nr+fg) else pl.lit(0).cast(pl.Int8).alias("has_bdm_any"),
        pl.any_horizontal([pl.col(c).is_not_null() for c in mm]).cast(pl.Int8).alias("has_bdm_market_maker") if mm else pl.lit(0).cast(pl.Int8).alias("has_bdm_market_maker"),
        pl.any_horizontal([pl.col(c).is_not_null() for c in nr]).cast(pl.Int8).alias("has_bdm_non_retail") if nr else pl.lit(0).cast(pl.Int8).alias("has_bdm_non_retail"),
        pl.any_horizontal([pl.col(c).is_not_null() for c in fg]).cast(pl.Int8).alias("has_bdm_foreign") if fg else pl.lit(0).cast(pl.Int8).alias("has_bdm_foreign"),
    ])
    return out

def aggregate_macro(m):
    if m.is_empty(): return m
    # Macro is a date-level table and must be unique on date before joining
    # to ticker-date panels. Keep the latest row if any duplicated dates exist.
    return m.with_columns(pl.col("date").cast(pl.Date, strict=False)).unique(subset=["date"], keep="last")

def load_macro_for_feature_store(root: Path) -> pl.DataFrame:
    """Load engineered macro features first, fallback to raw macro.

    build_macro.py writes two artifacts:
      - data/raw_canonical/macro.parquet            (base macro series)
      - data/features/macro/macro_features.parquet  (engineered macro features)

    The feature store should join the engineered table, otherwise many computed
    macro features exist on disk but never reach the model feature panel.
    """
    candidates = [
        root / "data/features/macro/macro_features.parquet",
        root / "data/raw_canonical/macro.parquet",
    ]
    for p in candidates:
        if p.exists() and p.stat().st_size > 0:
            try:
                return pl.read_parquet(p)
            except Exception:
                continue
    return pl.DataFrame()

def add_cross_sectional(df):
    for c in ["ret_5d","ret_10d","ret_20d","volume_ratio_20d","net_flow_ratio","rank1_same_buyer_streak","buyer_dominance_ratio"]:
        if c in df.columns:
            df=df.with_columns(pl.col(c).rank("average").over("date").alias(f"cs_rank_{c}"))
    return df

def build_feature_store(root, start_date, end_date, scope="history", output_dir=None, build_macro_if_missing=True):
    root=Path(root)
    s,e=ensure_start_end(start_date,end_date)
    if build_macro_if_missing and not (root/"data/raw_canonical/macro.parquet").exists():
        build_macro(root, "2015-01-01", e.isoformat())
    o=_filter(pl.read_parquet(root/"data/raw_canonical/ohlcv.parquet"),s,e)
    if o.is_empty(): raise ValueError(f"No OHLCV rows for {s}->{e}")
    base=add_price_features(o)
    broker=aggregate_broker(_filter(pl.read_parquet(root/"data/raw_canonical/broker_summary.parquet"),s,e)) if (root/"data/raw_canonical/broker_summary.parquet").exists() else pl.DataFrame()
    if not broker.is_empty(): base=safe_left_join(base,broker,["date","ticker"],"broker")
    insider=aggregate_insider(_filter(pl.read_parquet(root/"data/raw_canonical/insider_activity.parquet"),s,e)) if (root/"data/raw_canonical/insider_activity.parquet").exists() else pl.DataFrame()
    if not insider.is_empty(): base=safe_left_join(base,insider,["date","ticker"],"insider")
    ca=aggregate_ca(_filter(pl.read_parquet(root/"data/raw_canonical/corporate_action.parquet"),s,e)) if (root/"data/raw_canonical/corporate_action.parquet").exists() else pl.DataFrame()
    if not ca.is_empty(): base=safe_left_join(base,ca,["date","ticker"],"corporate_action")
    bdm=pivot_bdm(_filter(pl.read_parquet(root/"data/raw_canonical/neo_bdm.parquet"),s,e)) if (root/"data/raw_canonical/neo_bdm.parquet").exists() else pl.DataFrame()
    if not bdm.is_empty(): base=safe_left_join(base,bdm,["date","ticker"],"bdm")
    macro=aggregate_macro(_filter(load_macro_for_feature_store(root),s,e))
    if not macro.is_empty(): base=safe_left_join(base,macro,["date"],"macro")
    # fill key flags
    for c in ["has_broksum","has_insider_activity","has_corporate_action","has_bdm_any","has_bdm_market_maker","has_bdm_non_retail","has_bdm_foreign","macro_missing_flag"]:
        if c in base.columns: base=base.with_columns(pl.col(c).fill_null(0).cast(pl.Int8).alias(c))
    base=add_cross_sectional(harden_broker_ratios(sanitize_numeric(base)))
    base=ensure_feature_contract(base).sort(["date","ticker"])
    assert_unique(base,["date","ticker"],f"feature_store_{scope}")
    outdir=Path(output_dir) if output_dir else root/"data/features"/scope
    if scope=="live":
        outdir=root/"data/features/live"/e.isoformat()
    outdir.mkdir(parents=True, exist_ok=True)
    safe_write_parquet(base,outdir/"base_features.parquet")
    if scope=="live":
        latest=root/"data/features/live/latest"
        if latest.exists(): shutil.rmtree(latest)
        latest.mkdir(parents=True, exist_ok=True)
        safe_write_parquet(base,latest/"base_features.parquet")
    feature_cols=get_feature_cols(base)
    manifest={"scope":scope,"start_date":s,"end_date":e,"rows":base.height,"cols":base.width,"path":str(outdir/"base_features.parquet"),"feature_count":len(feature_cols),"feature_cols":feature_cols}
    write_json(outdir/"manifest.json", manifest)
    if scope=="live": write_json(root/"data/features/live/latest/manifest.json", manifest)
    return manifest
