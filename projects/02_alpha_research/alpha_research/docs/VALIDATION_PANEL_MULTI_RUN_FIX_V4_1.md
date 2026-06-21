# Validation Signal Panel Multi-Run Fix v4.1

This patch fixes a recurring validation panel bug:

```text
polars.exceptions.DuplicateError: column with name 'score_sm_right' already exists
```

## Root cause

Several folds and/or algorithms can produce the same logical score name, e.g. all `sm_tracker` algos for `label_brok_cont` map to `score_sm`.

The previous builder joined every fold prediction independently. Polars then had to create `score_sm_right`; when a later join needed the same suffix again, the builder crashed.

## New behavior

The builder now:

1. Collects prediction files from one or more run IDs.
2. Vertically concatenates folds for each unique `(run_id, family, algo, target)` component.
3. Creates deterministic component score columns.
4. Joins unique component columns wide by `date,ticker`.
5. Creates canonical aliases such as `score_sm` from the best component based on average `selection_score` in model metadata.

## Commands

Single family run:

```bash
python3 workflows/build_validation_signal_panel.py \
  --root . \
  --run-id 20260518_120742
```

Multi-run panel:

```bash
python3 workflows/build_validation_signal_panel.py \
  --root . \
  --run-ids 20260518_120742,20260518_230704,20260519_124624 \
  --output signals/validation/validation_signal_panel.parquet
```

## Output

The output metadata includes:

- `score_cols`
- `primary_aliases`
- `components`
- `run_ids`

If a run contains multiple algos for `score_sm`, the panel may contain:

```text
score_sm__sm_tracker__hgb__brok_cont
score_sm__sm_tracker__rank_hgb__brok_cont
score_sm__sm_tracker__regime_hgb__brok_cont
score_sm
```

The plain `score_sm` alias is chosen from the best validation component.

# Forward Test

## Forward test Swing (defensive):
```bash
python3 workflows/run_forward_test.py \
  --panel signals/validation/validation_signal_panel.parquet \
  --output-dir data/evaluation/forward_tests/swing_hgb_defensive \
  --forward-start 2025-01-01 \
  --score-col "score_swing__multi_strategy_time__hgb__swing" \
  --top-k 15 \
  --hold-days 1 \
  --min-score 0.50 \
  --min-traded-value 500000000 \
  --require-broksum \
  --exclude-broker-value-anomaly
```

## Forward test Momentum 10d:
```bash
python3 workflows/run_forward_test.py \
  --panel signals/validation/validation_signal_panel.parquet \
  --output-dir data/evaluation/forward_tests/momentum_10d_hgb \
  --forward-start 2025-01-01 \
  --score-col "score_momentum_10d__momentum_ranker__hgb__momentum_10d" \
  --top-k 15 \
  --hold-days 2 \
  --min-score 0.60 \
  --min-traded-value 500000000 \
  --require-broksum
```

## Forward test Scalp rank_hgb:
```bash
python3 workflows/run_forward_test.py \
  --panel signals/validation/validation_signal_panel.parquet \
  --output-dir data/evaluation/forward_tests/scalp_rank_hgb \
  --forward-start 2025-01-01 \
  --score-col "score_scalp__multi_strategy_time__rank_hgb__scalp" \
  --top-k 1 \
  --hold-days 1 \
  --min-score 0.60 \
  --min-traded-value 500000000 \
  --require-broksum
```

## ARA forward test, high risk
```bash
python3 workflows/run_forward_test.py \
  --panel signals/validation/validation_signal_panel.parquet \
  --output-dir data/evaluation/forward_tests/ara_watchlist_only \
  --forward-start 2025-01-01 \
  --score-col "score_ara" \
  --top-k 1 \
  --hold-days 1 \
  --min-score 0.50 \
  --min-traded-value 1000000000 \
  --require-broksum
```