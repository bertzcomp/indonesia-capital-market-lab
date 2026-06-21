import argparse, json
from alpha_research.inference.scoring import build_live_base_scores

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--feature-scope',default='live'); ap.add_argument('--registry',default='configs/model_registry.json'); ap.add_argument('--from-date',default=None); ap.add_argument('--end-date',default=None); ap.add_argument('--price-min',type=float,default=100); ap.add_argument('--price-max',type=float,default=1000); ap.add_argument('--min-traded-value',type=float,default=500000000); ap.add_argument('--require-broksum',action='store_true'); ap.add_argument('--model-selection',default='latest_fold')
    a=ap.parse_args(); print(json.dumps(build_live_base_scores(a.root,a.registry,a.from_date,a.end_date,a.price_min,a.price_max,a.min_traded_value,a.require_broksum,a.model_selection),indent=2,default=str))
if __name__=='__main__': main()
