import argparse, json
from alpha_research.evaluation.backtest import run_signal_backtest

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--panel', required=True)
    ap.add_argument('--output-dir', required=True)
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
    print(json.dumps(run_signal_backtest(a.panel, a.output_dir, a.score_col, a.top_k, a.hold_days, a.min_score, a.price_min, a.price_max, a.min_traded_value, a.require_broksum, a.exclude_broker_value_anomaly), indent=2, default=str))
if __name__ == '__main__':
    main()
