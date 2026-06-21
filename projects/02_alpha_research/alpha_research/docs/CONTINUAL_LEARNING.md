as_of_date          = tanggal data terakhir tersedia
label_horizon_days  = horizon label terpanjang yang harus mature
maturity_cutoff     = as_of_date - label_horizon_days
lookback_days       = panjang window training ke belakang
train_start         = maturity_cutoff - lookback_days
train_end           = maturity_cutoff

```
lookback 365–730 hari = [multi_strategy_time, momentum_ranker, ara_predictor]
lookback 730–1095 hari = [sm_tracker, market_maker_accumulatiown]
```


# Update canonical raw sampai data terakhir
```bash
export BPS_API_KEY="YOUR_BPS_API_KEY"

python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-20 \
  --macro-mode scrape \
  --force-macro \
  --download-bi-rate \
  --bps-api-key "$BPS_API_KEY"
```

# Build continual feature store
```bash
python3 workflows/build_feature_store.py \
  --root . \
  --scope continual \
  --start-date 2024-07-01 \
  --end-date 2026-05-20 \
  --output-dir data/features/continual/q3_2024_to_2026_05_20
```

# Build continual labeled dataset
```bash
python3 workflows/build_training_dataset.py \
  --root . \
  --feature-path data/features/continual/q3_2024_to_2026_05_20/base_features.parquet \
  --output-dir data/datasets/continual/q3_2024_to_2026_04_30 \
  --start-date 2024-07-01 \
  --end-date 2026-04-30 \
  --as-of-date 2026-05-20 \
  --drop-unmatured-labels
```

# Build quarterly folds khusus continual
```bash
python3 workflows/build_folds.py \
  --root . \
  --dataset data/datasets/continual/q3_2024_to_2026_04_30/full_labeled.parquet \
  --fold-set continual_q3_2024_q1_2026 \
  --freq quarter \
  --first-val-year 2025 \
  --last-val-year 2026 \
  --purge-days 30 \
  --embargo-days 5 \
  --output-dir data/datasets/continual/q3_2024_to_2026_04_30/folds
```

# Family-specific training plan
## Short-horizon adaptive models
```bash
python3 workflows/train_tuned_models.py \
  --root . \
  --dataset data/datasets/continual/q3_2024_to_2026_04_30/full_labeled.parquet \
  --fold-dir data/datasets/continual/q3_2024_to_2026_04_30/folds \
  --run-prefix continual_q3_2024_q1_2026 \
  --fold-set continual_q3_2024_q1_2026 \
  --families multi_strategy_time,momentum_ranker,ara_predictor \
  --algos hgb,rank_hgb,regime_hgb,xgb \
  --tune-trials 16
```

Setelah training challenger

# Build validation panel
```bash
python3 workflows/build_validation_signal_panel.py \
  --root . \
  --run-ids <RUN_MULTI>,<RUN_MOMENTUM>,<RUN_ARA>,<RUN_SM>,<RUN_MM> \
  --output signals/validation/continual_q3_2024_q1_2026_panel.parquet
```

# Randomized backtest search
```bash
python3 workflows/run_randomized_backtest_search.py \
  --panel signals/validation/continual_q3_2024_q1_2026_panel.parquet \
  --output-dir data/evaluation/backtests/continual_q3_2024_q1_2026 \
  --n-iter 500 \
  --seed 42
```

# Forward test khusus 2026
```bash
python3 workflows/run_forward_test.py \
  --panel signals/validation/continual_q3_2024_q1_2026_panel.parquet \
  --output-dir data/evaluation/forward_tests/continual_q3_2024_q1_2026 \
  --forward-start 2026-01-20 \
  --score-col "score_swing" \
  --top-k 10 \
  --hold-days 1 \
  --min-score 0.50 \
  --min-traded-value 500000000 \
  --require-broksum
```

```bash
python3 workflows/train_tuned_models.py \
  --root . \
  --dataset data/datasets/continual/q3_2024_to_2026_04_30/full_labeled.parquet \
  --fold-dir data/datasets/continual/q3_2024_to_2026_04_30/folds \
  --run-prefix continual_q3_2024_q1_2026 \
  --fold-set continual_q3_2024_q1_2026 \
  --families market_maker_accumulation, sm_tracker \
  --algos hgb,rank_hgb,regime_hgb,xgb \
  --tune-trials 4
```