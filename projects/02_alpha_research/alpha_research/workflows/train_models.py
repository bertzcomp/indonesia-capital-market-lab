import argparse, json
from alpha_research.training.trainer import train_models

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--fold-set', default='quarterly')
    ap.add_argument('--families', default='sm_tracker,ara_predictor,multi_strategy_time,market_maker_accumulation,momentum_ranker')
    ap.add_argument('--algos', default='hgb,rank_hgb,regime_hgb')
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--tune-trials', type=int, default=0, help='Random hyperparameter trials per fold/target/algo. 0 = default params only.')
    a = ap.parse_args()
    print(json.dumps(train_models(a.root, a.fold_set, [x for x in a.families.split(',') if x], [x for x in a.algos.split(',') if x], a.seed, a.tune_trials), indent=2, default=str))
if __name__ == '__main__':
    main()
