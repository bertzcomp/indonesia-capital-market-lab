import argparse, json
from alpha_research.evaluation.backtest import randomized_backtest_search

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--panel', required=True)
    ap.add_argument('--output-dir', required=True)
    ap.add_argument('--n-iter', type=int, default=100)
    ap.add_argument('--seed', type=int, default=42)
    a = ap.parse_args()
    print(json.dumps(randomized_backtest_search(a.panel, a.output_dir, a.n_iter, a.seed), indent=2, default=str))
if __name__ == '__main__':
    main()
