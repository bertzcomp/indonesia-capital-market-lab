import argparse, json
from alpha_research.evaluation.backtest import forward_test

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--panel', required=True)
    ap.add_argument('--output-dir', required=True)
    ap.add_argument('--forward-start', required=True)
    ap.add_argument('--score-col', default='score_sm')
    ap.add_argument('--top-k', type=int, default=5)
    ap.add_argument('--hold-days', type=int, default=5)
    ap.add_argument('--min-score', type=float, default=None)
    ap.add_argument('--price-min', type=float, default=100)
    ap.add_argument('--price-max', type=float, default=1000)
    ap.add_argument('--min-traded-value', type=float, default=500000000)
    ap.add_argument('--require-broksum', action='store_true')
    ap.add_argument('--exclude-broker-value-anomaly', action='store_true')
    a = ap.parse_args()
    print(json.dumps(forward_test(a.panel, a.output_dir, a.forward_start, score_col=a.score_col, top_k=a.top_k, hold_days=a.hold_days, min_score=a.min_score, price_min=a.price_min, price_max=a.price_max, min_traded_value=a.min_traded_value, require_broksum=a.require_broksum, exclude_broker_value_anomaly=a.exclude_broker_value_anomaly), indent=2, default=str))
if __name__ == '__main__':
    main()
