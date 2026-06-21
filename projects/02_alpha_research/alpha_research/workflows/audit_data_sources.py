import argparse, json
from pathlib import Path
import polars as pl
from alpha_research.core.io import write_json

def stat(path):
    p=Path(path)
    if not p.exists(): return {"exists":False}
    try:
        df=pl.read_parquet(p)
        out={"exists":True,"rows":df.height,"cols":df.width,"path":str(p)}
        if "date" in df.columns:
            out["min_date"]=str(df["date"].min()); out["max_date"]=str(df["date"].max())
        if {"date","ticker"}.issubset(df.columns):
            out["duplicate_ticker_date_groups"]=df.group_by(["date","ticker"]).len().filter(pl.col("len")>1).height
        return out
    except Exception as e: return {"exists":True,"error":str(e),"path":str(p)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--output',default='reports/data_source_audit.json')
    a=ap.parse_args(); root=Path(a.root)
    tables=["ohlcv","broker_summary","insider_activity","corporate_action","macro","neo_bdm","orderbook_snapshot","orderbook_levels","tradebook_price","tradebook_time"]
    res={t:stat(root/"data/raw_canonical"/f"{t}.parquet") for t in tables}
    write_json(root/a.output,res)
    md=["# Data Source Audit",""]
    for k,v in res.items(): md.append(f"## {k}\n\n```json\n{json.dumps(v,indent=2,default=str)}\n```\n")
    (root/Path(a.output).with_suffix('.md')).write_text('\n'.join(md),encoding='utf-8')
    print(json.dumps(res,indent=2,default=str))
if __name__=='__main__': main()
