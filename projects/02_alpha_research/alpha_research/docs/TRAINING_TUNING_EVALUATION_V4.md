# Training, Tuning, and Evaluation V4

This patch adds:

1. Quarterly folds as the default operational fold set.
2. `momentum_ranker` model family.
3. Randomized hyperparameter search during model training.
4. Validation prediction panel for downstream evaluation.
5. Three required evaluation scenarios:
   - Backtest
   - Forward test
   - Monte Carlo simulation

## Recommended execution

```bash
python3 workflows/build_folds.py \
  --root . \
  --freq quarter \
  --fold-set quarterly \
  --first-val-year 2021 \
  --last-val-year 2025 \
  --purge-days 30 \
  --embargo-days 5
```

Smoke training:

```bash
python3 workflows/train_tuned_models.py \
  --root . \
  --fold-set quarterly \
  --families sm_tracker,ara_predictor,momentum_ranker \
  --algos hgb,rank_hgb,regime_hgb \
  --tune-trials 8
```

Specific training for smart money:

```bash
python3 workflows/train_tuned_models.py \
  --root . \
  --fold-set quarterly \
  --families market_maker_accumulation\
  --algos xgb,hgb,regime_hgb \
  --tune-trials 4
```


Full challenger training:

```bash
python3 workflows/train_tuned_models.py \
  --root . \
  --fold-set quarterly \
  --families multi_strategy_time,sm_tracker,ara_predictor,market_maker_accumulation,momentum_ranker \
  --algos hgb,rank_hgb,regime_hgb \
  --tune-trials 12
```

Build validation panel:
1. Smart Money Tracker
    ```bash
    python3 workflows/build_validation_signal_panel.py \
      --root . \
      --run-id 20260518_120742 \
      --output signals/validation/sm_tracker_panel.parquet
    ```
2. ARA Predictor
    ```bash
    python3 workflows/build_validation_signal_panel.py \
      --root . \
      --run-id 20260518_230704 \
      --output signals/validation/ara_predictor.parquet
    ```
3. Market Maker Accumulation
    ```bash
    python3 workflows/build_validation_signal_panel.py \
      --root . \
      --run-id 20260519_124624 \
      --output signals/validation/market_maker_accum.parquet
    ```
4. Multi-run
    ```
    python3 workflows/build_validation_signal_panel.py \
      --root . \
      --run-ids 20260518_120742,20260518_230704,20260519_124624,20260519_124452,20260518_115525 \
      --output signals/validation/validation_signal_panel.parquet
    ```


## Backtest:
1. Specific back test score for Smart Money:
    ```
    python3 workflows/run_backtest.py \
      --panel signals/validation/validation_signal_panel.parquet \
      --output-dir data/evaluation/backtests/sm \
      --score-col score_sm \
      --top-k 5 \
      --hold-days 5 \
      --min-score 0.60 \
      --require-broksum
    ```

Randomized search back test score;
```bash
python3 workflows/run_randomized_backtest_search.py \
  --panel signals/validation/validation_signal_panel.parquet \
  --output-dir data/evaluation/backtests/validation_multirun \
  --n-iter 100 \
  --seed 42
```

Forward test:

```bash
python3 workflows/run_forward_test.py \
  --panel signals/validation/validation_signal_panel.parquet \
  --output-dir data/evaluation/forward_tests/20260518_120742 \
  --forward-start 2025-01-01 \
  --score-col score_sm \
  --top-k 5 \
  --hold-days 5 \
  --require-broksum
```

Monte Carlo:

```bash
python3 workflows/run_monte_carlo.py \
  --trades data/evaluation/backtests/ara/trades.parquet \
  --output-dir data/evaluation/monte_carlo/ara \
  --n-iter 5000
```

## Notes

- Do not promote a model based only on validation metrics.
- Backtest optimizes trading parameters.
- Forward test checks temporal generalization.
- Monte Carlo checks path robustness.
