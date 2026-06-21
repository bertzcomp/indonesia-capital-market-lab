import argparse, json
from alpha_research.continual.pipeline import run_continual

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--as-of-date',required=True); ap.add_argument('--start-date',default='2018-01-01'); ap.add_argument('--freq',default='month'); ap.add_argument('--families',default='sm_tracker,ara_predictor,multi_strategy_time'); ap.add_argument('--algos',default='hgb,rank_hgb,regime_hgb')
    a=ap.parse_args(); print(json.dumps(run_continual(a.root,a.as_of_date,a.start_date,a.freq,a.families.split(','),a.algos.split(',')),indent=2,default=str))
if __name__=='__main__': main()
