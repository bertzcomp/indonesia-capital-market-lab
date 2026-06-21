# End-to-End Workflow

## 0. Validate layout

```bash
python3 workflows/validate_project_layout.py --root . --create
```

## 1. Build canonical raw tables

```bash
python3 workflows/build_canonical_raw.py --root . --start-date 2015-01-01 --end-date 2026-05-13
```

Canonical outputs live in `data/raw_canonical/`:

- `ohlcv.parquet`
- `broker_summary.parquet`
- `insider_activity.parquet`
- `corporate_action.parquet`
- `neo_bdm.parquet`
- `macro.parquet`
- `orderbook_snapshot.parquet`
- `orderbook_levels.parquet`
- `tradebook_price.parquet`
- `tradebook_time.parquet`

## 2. Build feature stores

Historical:

```bash
python3 workflows/build_feature_store.py --root . --scope history --start-date 2016-01-01 --end-date 2025-12-31
```

Live:

```bash
python3 workflows/build_feature_store.py --root . --scope live --start-date 2026-03-09 --end-date 2026-05-13
```

Historical and live must have the same feature schema.

## 3. Build labels and training dataset

```bash
python3 workflows/build_training_dataset.py --root . --feature-scope history --start-date 2016-01-01 --end-date 2025-12-31
```

## 4. Build folds

```bash
python3 workflows/build_folds.py --root . --freq year --fold-set yearly --first-val-year 2018 --last-val-year 2025
```

## 5. Train models

```bash
python3 workflows/train_models.py --root . --fold-set yearly --families sm_tracker,ara_predictor,multi_strategy_time,market_maker_accumulation --algos hgb,rank_hgb,regime_hgb
```

## 6. Build registry

```bash
python3 workflows/build_model_registry.py --root . --run-id latest --output configs/model_registry.json
```

## 7. Daily signal

After EOD data lands in `data/pure_raw/`, run:

```bash
python3 workflows/build_canonical_raw.py --root . --start-date 2015-01-01 --end-date 2026-05-18
python3 workflows/build_feature_store.py --root . --scope live --start-date 2026-03-18 --end-date 2026-05-18
python3 workflows/run_daily_signal.py --root . --from-date 2026-03-18 --end-date 2026-05-18 --target-date 2026-05-19 --registry configs/model_registry.json --require-broksum
```

## 8. Continual retraining

```bash
python3 workflows/run_continual_retrain.py --root . --as-of-date 2026-05-18 --start-date 2018-01-01 --freq month --families sm_tracker,ara_predictor,multi_strategy_time,market_maker_accumulation --algos hgb,rank_hgb,regime_hgb
```

Continual runs are challengers and are not auto-promoted.
