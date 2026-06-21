from __future__ import annotations
from pathlib import Path
from datetime import date, timedelta
import calendar
import polars as pl
from alpha_research.core.io import write_json, safe_write_parquet
from alpha_research.core.dates import parse_date_any
from alpha_research.features.contract import get_feature_cols

def _periods(freq, first_year, last_year):
    if freq=="year":
        for y in range(first_year,last_year+1): yield f"{y}", date(y,1,1), date(y,12,31)
    elif freq=="quarter":
        for y in range(first_year,last_year+1):
            for q,(m1,m2) in enumerate([(1,3),(4,6),(7,9),(10,12)],1):
                yield f"{y}Q{q}", date(y,m1,1), date(y,m2,calendar.monthrange(y,m2)[1])
    elif freq=="month":
        for y in range(first_year,last_year+1):
            for m in range(1,13): yield f"{y}-{m:02d}", date(y,m,1), date(y,m,calendar.monthrange(y,m)[1])
    else: raise ValueError(freq)

def build_folds(root, freq="year", fold_set="yearly", first_val_year=2018, last_val_year=2025, train_start="2016-01-01", purge_days=30, embargo_days=5, mode="expanding"):
    root=Path(root); df=pl.read_parquet(root/"data/datasets/training/full_labeled.parquet")
    df=df.with_columns(pl.col("date").cast(pl.Date, strict=False)).sort(["date","ticker"])
    train_start=parse_date_any(train_start)
    outdir=root/"data/datasets/folds"/fold_set; outdir.mkdir(parents=True,exist_ok=True)
    folds=[]; idx=0
    for name,vs,ve in _periods(freq,first_val_year,last_val_year):
        val=df.filter((pl.col("date")>=pl.lit(vs))&(pl.col("date")<=pl.lit(ve)))
        if val.is_empty(): continue
        train_end=vs-timedelta(days=purge_days+embargo_days)
        train=df.filter((pl.col("date")>=pl.lit(train_start))&(pl.col("date")<=pl.lit(train_end)))
        if train.is_empty(): continue
        idx+=1
        safe_write_parquet(train,outdir/f"fold_{idx:02d}_train.parquet")
        safe_write_parquet(val,outdir/f"fold_{idx:02d}_val.parquet")
        folds.append({"fold":idx,"period":name,"train_start":train["date"].min(),"train_end":train["date"].max(),"val_start":val["date"].min(),"val_end":val["date"].max(),"train_rows":train.height,"val_rows":val.height})
    meta={"fold_set":fold_set,"freq":freq,"mode":mode,"n_folds":len(folds),"purge_days":purge_days,"embargo_days":embargo_days,"feature_count":len(get_feature_cols(df)),"feature_cols":get_feature_cols(df),"folds":folds}
    write_json(root/"data/datasets/folds"/f"fold_meta_{fold_set}.json", meta)
    return meta
