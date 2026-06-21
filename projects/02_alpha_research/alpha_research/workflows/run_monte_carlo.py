import argparse, json
from alpha_research.evaluation.backtest import monte_carlo_from_trades

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--trades', required=True)
    ap.add_argument('--output-dir', required=True)
    ap.add_argument('--n-iter', type=int, default=5000)
    ap.add_argument('--seed', type=int, default=42)
    a = ap.parse_args()
    print(json.dumps(monte_carlo_from_trades(a.trades, a.output_dir, a.n_iter, a.seed), indent=2, default=str))
if __name__ == '__main__':
    main()
