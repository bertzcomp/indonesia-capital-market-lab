# 1. Build canonical raw

Jika BI Rate telah tersedia di lokal, tidak perlu ```--download-bi-rate``` setiap hari.
```bash
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-20 \
  --macro-mode scrape \
  --force-macro
```

Kalau tetap ingin force macro:
```bash
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-20 \
  --macro-mode scrape \
  --force-macro
```
Kalau butuh download BI Rate juga:

```bash
export BPS_API_KEY="cdc65504d0b176f0b763f2d8dcd855dd"

python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-06-12 \
  --macro-mode scrape \
  --force-macro \
  --download-bi-rate \
  --bps-api-key "$BPS_API_KEY"
```


# 2. Build live feature store
Untuk EOD 2026-05-25:
```bash
python3 workflows/build_feature_store.py \
  --root . \
  --scope live \
  --start-date 2026-02-22 \
  --end-date 2026-06-12
```
2026-03-09 masih oke karena memberi lookback sekitar 2+ bulan. Bisa juga nanti dibuat otomatis end_date - 90 calendar days.


# Mode A — Pakai model continual baru
```bash
python3 workflows/run_daily_signal_profile.py \
  --root . \
  --profile continual_model \
  --from-date 2026-02-22 \
  --end-date 2026-06-12 \
  --target-date 2026-06-15 \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 2000000000 \
  --require-broksum
```
Wrapper ini otomatis menjalankan:
```bash
1. build_live_base_scores.py dengan registry continual
2. run_daily_signal.py dengan signal_policy continual
```


# Mode B — Pakai model lama / champion
```bash
python3 workflows/run_daily_signal_profile.py \
  --root . \
  --profile base_model \
  --from-date 2026-02-22 \
  --end-date 2026-06-12 \
  --target-date 2026-06-15 \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 2000000000 \
  --require-broksum
```


# 3. Trading intelligence report
### Continual model
```bash
python3 workflows/build_narrative_trade_report.py \
  --root . \
  --signal-dir signals/daily/signal_15_jun_2026/continual_model \
  --policy configs/narrative_policy.json
```

```bash
python3 workflows/build_numeric_trade_report.py \
  --root . \
  --signal-dir signals/daily/signal_15_jun_2026/continual_model \
  --policy configs/numeric_report_policy.json \
  --signal-policy configs/signal_policy.continual_q3_2024_q1_2026.json \
  --source-file all_strategy_watchlist.csv
```


### Base model
```bash
python3 workflows/build_narrative_trade_report.py \
  --root . \
  --signal-dir signals/daily/signal_15_jun_2026/base_model \
  --policy configs/narrative_policy.json
```

```bash
python3 workflows/build_numeric_trade_report.py \
  --root . \
  --signal-dir signals/daily/signal_15_jun_2026/base_model \
  --policy configs/numeric_report_policy.json \
  --signal-policy configs/signal_policy.json \
  --source-file all_strategy_watchlist.csv
```

# 4. Execution Readiness Score layer
```bash
python3 workflows/build_execution_readiness_score.py \
  --root . \
  --signal-dir signals/daily/signal_29_may_2026/continual_model \
  --policy configs/execution_readiness_policy.json
```

# 5. Dashboard
```bash
python3 workflows/run_local_dashboard.py \
  --root . \
  --port 8501
```