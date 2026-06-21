import argparse, json
from pathlib import Path
import polars as pl
from alpha_research.features.sanity import harden_broker_ratios, sanitize_numeric
from alpha_research.core.io import safe_write_parquet

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--scope',choices=['history','live'],required=True)
    a=ap.parse_args(); root=Path(a.root)
    p=root/"data/features/history/base_features.parquet" if a.scope=='history' else root/"data/features/live/latest/base_features.parquet"
    df=pl.read_parquet(p); df=harden_broker_ratios(sanitize_numeric(df)); safe_write_parquet(df,p)
    print(json.dumps({"path":str(p),"rows":df.height,"cols":df.width},indent=2))
if __name__=='__main__': main()
