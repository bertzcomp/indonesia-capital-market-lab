# Canonical Raw + Feature Contract v2

This patch replaces the under-specified feature builder with a contract-driven flow:

```text
raw / pure_raw sources
        ↓
data/raw_canonical/*.parquet
        ↓
feature store history/live with identical model feature schema
```

## Why this exists

The reconstruction pipeline was runnable but not faithful enough to the project data reality:

- OHLCV exists since 2015.
- Broker summary exists since 2016 and is a core historical signal source.
- Insider activity exists since 2017 and is also a core historical source.
- Macro must be treated as a first-class regime source.
- Neo BDM and tradebook/orderbook are sparse alternative data sources.

A feature store with only ~34 columns for history while live has ~107 columns is not valid for model training/inference parity.

## New commands

### 1. Build canonical raw tables

```bash
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13
```

Output:

```text
data/raw_canonical/ohlcv.parquet
data/raw_canonical/broker_summary.parquet
data/raw_canonical/insider_activity.parquet
data/raw_canonical/corporate_action.parquet
data/raw_canonical/neo_bdm.parquet
data/raw_canonical/macro.parquet
data/raw_canonical/orderbook_snapshot.parquet
data/raw_canonical/orderbook_levels.parquet
data/raw_canonical/tradebook_price.parquet
data/raw_canonical/tradebook_time.parquet
data/raw_canonical/canonical_manifest.json
```

### 2. Build historical feature store

```bash
python3 workflows/build_feature_store.py \
  --root . \
  --scope history \
  --start-date 2016-01-01 \
  --end-date 2025-12-31
```

Output:

```text
data/features/history/base_features.parquet
data/features/history/feature_registry.json
data/features/history/manifest.json
```

### 3. Build live feature store

```bash
python3 workflows/build_feature_store.py \
  --root . \
  --scope live \
  --start-date 2026-03-09 \
  --end-date 2026-05-13
```

Output:

```text
data/features/live/2026-05-13/base_features.parquet
data/features/live/latest/base_features.parquet
```

## Feature contract

Feature schema is defined in code at:

```text
src/alpha_research/features/contract.py
```

and documented at:

```text
configs/feature_contract.yaml
```

History and live feature stores should now expose the same model feature contract. Optional sources such as BDM remain nullable but their columns and coverage flags still exist.

## Macro note

If no valid macro file is found, the canonicalizer creates a macro table with `macro_missing_flag=1` and the feature builder creates market-proxy features from OHLCV. This is a safe fallback, not a replacement for a proper macro loader. A real macro ingestion module should later populate USD/IDR, Brent, Coal, IHSG, and regime fields.




# Untuk daily EOD
Kalau nanti Anda punya data EOD 18 May dan ingin signal 19 May:

```
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-18 \
  --macro-mode scrape
```
```
python3 workflows/build_feature_store.py \
  --root . \
  --scope live \
  --start-date 2026-03-18 \
  --end-date 2026-05-18
```
```
python3 workflows/run_daily_signal.py \
  --root . \
  --from-date 2026-03-18 \
  --end-date 2026-05-18 \
  --target-date 2026-05-19 \
  --registry configs/model_registry.json \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 500000000 \
  --require-broksum
```