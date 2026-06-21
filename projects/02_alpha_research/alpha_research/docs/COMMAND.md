Recommended end-to-end execution

0. Validate/create layout
```py
python3 workflows/validate_project_layout.py \
  --root . \
  --create
```

Lalu letakkan data Anda:
```
data/pure_raw/
├── trading_summary/
├── broker_summary/
├── neo_bdm/
├── insider_activity/
├── tradebook/
├── corporate_action/
└── fundamental/
```

1. Prepare raw data
```py
python3 workflows/prepare_raw_data.py \
  --root . \
  --from-date 2016-01-01 \
  --end-date 2026-05-13
```

Output canonical raw akan masuk ke:
```
data/raw/
```

2. Build historical feature store
```py
python3 workflows/build_feature_store.py \
  --root . \
  --scope history \
  --start-date 2016-01-01 \
  --end-date 2025-12-31
```
Output:
```
data/features/history/base_features.parquet
data/features/history/feature_registry.json
data/features/history/manifest.json
```

3. Build training dataset
```py
python3 workflows/build_training_dataset.py \
  --root . \
  --feature-scope history \
  --start-date 2016-01-01 \
  --end-date 2025-12-31
```

Output:
```
data/datasets/training/full_labeled.parquet
data/datasets/training/dataset_meta.json
```

4. Build folds

- Yearly:
    ```py
    python3 workflows/build_folds.py \
    --root . \
    --freq year \
    --fold-set yearly \
    --first-val-year 2018 \
    --last-val-year 2025 \
    --purge-days 30 \
    --embargo-days 5
    ```

- Quarterly robustness:
    ```py
    python3 workflows/build_folds.py \
    --root . \
    --freq quarter \
    --fold-set quarterly \
    --first-val-year 2021 \
    --last-val-year 2025 \
    --purge-days 30 \
    --embargo-days 5
    ```

5. Train model families

- Baseline without external boosting dependency:
    ```py
    python3 workflows/train_models.py \
    --root . \
    --fold-set yearly \
    --families multi_strategy_time,sm_tracker,ara_predictor,market_maker_accumulation \
    --algos hgb,regime_hgb,rank_hgb
    ```

- With LightGBM/XGBoost if installed:
    ```py
    python3 workflows/train_models.py \
    --root . \
    --fold-set yearly \
    --families multi_strategy_time,sm_tracker,ara_predictor,market_maker_accumulation \
    --algos lgb,xgb,hgb,regime_hgb,rank_hgb
    ```
Output:
```
models/runs/<run_id>/
data/validation/predictions/<run_id>/
```

6. Build model registry
```py
python3 workflows/build_model_registry.py \
  --root . \
  --run-id latest \
  --output configs/model_registry.yaml
```

Output:
```
configs/model_registry.yaml
Registry ini yang dipakai inference. Tidak ada model-path guessing lagi.
```

## Daily live signal

7. Run full daily signal pipeline
Setelah data harian terbaru diletakkan di data/pure_raw/:
```py
python3 workflows/run_daily_signal.py \
  --root . \
  --from-date 2026-01-01 \
  --end-date 2026-05-13 \
  --target-date 2026-05-18 \
  --holiday-dates 2026-05-14,2026-05-15 \
  --registry configs/model_registry.yaml \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 500000000 \
  --require-broksum
```
Output:
```
signals/daily/signal_18_may_2026/
├── signals_main.csv
├── execution_shortlist.csv
├── sm_tracker_signal.csv
├── ara_predict_signal.csv
├── market_maker_signal.csv
├── multi_strategy_time_signal.csv
├── all_scores.csv
├── diagnostics.json
└── report.md
```

## Continual retraining

8. Run continual retraining challenger
```py
python3 workflows/run_continual_retrain.py \
  --root . \
  --as-of-date 2026-05-13 \
  --start-date 2018-01-01 \
  --freq month \
  --families sm_tracker,ara_predictor,multi_strategy_time,market_maker_accumulation \
  --algos hgb,regime_hgb,rank_hgb
```

Output:
```
data/datasets/continual/continual_labeled_asof_2026-05-13/
models/runs/<new_run_id>/
```
Catatan: continual model ini masih challenger. Anda tetap harus build registry candidate, backtest, Monte Carlo, dan promote manual.

### One-command research pipeline

Kalau ingin menjalankan historical pipeline sekaligus:
```py
python3 workflows/run_research_pipeline.py \
  --root . \
  --start-date 2016-01-01 \
  --end-date 2025-12-31 \
  --fold-set yearly \
  --families multi_strategy_time,sm_tracker,ara_predictor,market_maker_accumulation \
  --algos hgb,regime_hgb,rank_hgb
```

Ini menjalankan:
```
build history feature store
build training dataset
build folds
train models
build model registry
```



Recommended execution setelah patch
1. Build canonical raw tables

Gunakan full range supaya semua source historis terbaca.
```
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13
```
Output utama:
```
data/raw_canonical/canonical_manifest.json
```
Cek ringkas:
```
cat data/raw_canonical/canonical_manifest.json
```

2. Build historical feature store
```
python3 workflows/build_feature_store.py \
  --root . \
  --scope history \
  --start-date 2016-01-01 \
  --end-date 2025-12-31
```
Expected: kolom historical harus jauh lebih banyak dari sebelumnya dan mendekati schema live.


3. Build live feature store
```
python3 workflows/build_feature_store.py \
  --root . \
  --scope live \
  --start-date 2026-03-09 \
  --end-date 2026-05-13
```


4. Verify schema parity

Jalankan ini:
```py
import polars as pl

hist = pl.read_parquet("data/features/history/base_features.parquet")
live = pl.read_parquet("data/features/live/latest/base_features.parquet")

hist_cols = set(hist.columns)
live_cols = set(live.columns)

print("history shape:", hist.shape)
print("live shape:", live.shape)

print("cols only in history:", sorted(hist_cols - live_cols)[:50], len(hist_cols - live_cols))
print("cols only in live:", sorted(live_cols - hist_cols)[:50], len(live_cols - hist_cols))

print(
    hist.select([
        pl.col("date").min().alias("hist_min"),
        pl.col("date").max().alias("hist_max"),
        pl.struct(["date", "ticker"]).is_duplicated().sum().alias("hist_dup"),
    ])
)

print(
    live.select([
        pl.col("date").min().alias("live_min"),
        pl.col("date").max().alias("live_max"),
        pl.struct(["date", "ticker"]).is_duplicated().sum().alias("live_dup"),
    ])
)
```

Expected:
```
hist_dup = 0
live_dup = 0
cols only in history/live = kecil atau 0
```

Catatan penting

Patch ini memperbaiki fundamental layer, tapi belum berarti kita langsung lanjut training. Setelah Anda build ulang canonical raw + feature store, kita perlu audit:
```
1. canonical_manifest.json
2. shape historical feature store
3. shape live feature store
4. schema parity
5. broker feature coverage
6. BDM coverage
7. macro_missing_flag coverage
```
Baru setelah itu kita lanjut ke labels/training.

Jadi next step sekarang adalah jalankan:
```
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13
```

lalu kirimkan canonical_manifest.json dan hasil shape/schema parity.