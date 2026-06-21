from __future__ import annotations
from pathlib import Path
import json, joblib
import numpy as np
import polars as pl
from alpha_research.core.io import read_json, safe_write_parquet, write_json

def _score_model(model, X):
    if hasattr(model,"predict_proba"):
        return model.predict_proba(X)[:,1]
    if hasattr(model,"decision_function"):
        z=model.decision_function(X); return 1/(1+np.exp(-z))
    return model.predict(X)

def _component_models(root, spec, selection="latest_fold"):
    root=Path(root); base=root/"models/runs"/spec["run_id"]/spec["family"]/spec["algo"]/spec["target"]
    folds=sorted(base.glob("fold_*/model.pkl"))
    if not folds: return []
    if selection=="latest_fold": folds=[folds[-1]]
    return folds

def build_live_base_scores(root, registry_path, from_date=None, end_date=None, price_min=100, price_max=1000, min_traded_value=500_000_000, require_broksum=False, model_selection="latest_fold"):
    root=Path(root); reg=read_json(root/registry_path if not Path(registry_path).is_absolute() else registry_path)
    feat=root/"data/features/live/latest/base_features.parquet"
    df=pl.read_parquet(feat).with_columns(pl.col("date").cast(pl.Date, strict=False))
    if end_date:
        import datetime as dt
        ed=dt.date.fromisoformat(str(end_date))
        df=df.filter(pl.col("date")<=pl.lit(ed))
    signal_date=df["date"].max()
    cur=df.filter(pl.col("date")==signal_date)
    cur=cur.filter((pl.col("close").is_not_null())&(pl.col("close")>=price_min)&(pl.col("close")<=price_max)&(pl.col("traded_value_proxy").fill_null(0)>=min_traded_value))
    if require_broksum and "has_broksum" in cur.columns:
        cur=cur.filter(pl.col("has_broksum").fill_null(0)==1)
    if cur.is_empty(): raise ValueError("No eligible rows for scoring")
    pdf=cur.to_pandas()
    scored=[]; skipped={}
    for score_col,spec in reg.get("components",{}).items():
        if spec.get("enabled",True) is False: continue
        models=_component_models(root,spec,model_selection)
        if not models:
            skipped[score_col]="no models"; continue
        preds=[]
        for mp in models:
            meta_path=mp.parent/"meta.json"; meta=json.loads(meta_path.read_text())
            fcols=meta["feature_cols"]
            X=pdf.reindex(columns=fcols).replace([np.inf,-np.inf],np.nan).fillna(0).to_numpy()
            m=joblib.load(mp); preds.append(_score_model(m,X))
        cur=cur.with_columns(pl.Series(score_col, np.mean(preds,axis=0)))
        scored.append(score_col)
    outdir=root/"signals/live"; outdir.mkdir(parents=True,exist_ok=True)
    date_str=str(signal_date)
    safe_write_parquet(cur,outdir/f"base_scores_{date_str}.parquet")
    cur.write_csv(outdir/f"base_scores_{date_str}.csv")
    meta={"signal_date":date_str,"rows":cur.height,"scored_components":scored,"skipped_components":skipped,"path":str(outdir/f'base_scores_{date_str}.parquet')}
    write_json(outdir/f"base_scores_{date_str}.json",meta)
    return meta
