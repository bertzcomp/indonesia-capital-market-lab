# Daily Signal Model Profiles

This patch adds a profile-based daily signal workflow so the legacy/champion model and the continual model can coexist.

## Profiles

- `champion`
  - Registry: `configs/model_registry.json`
  - Policy: `configs/signal_policy.json`

- `continual_q3_2024_q1_2026`
  - Registry: `configs/model_registry.continual_q3_2024_q1_2026.json`
  - Policy: `configs/signal_policy.continual_q3_2024_q1_2026.json`
  - Run ID: `continual_q3_2024_q1_2026_20260521_143823`

## Recommended daily flow

Canonical raw and live feature store are shared across profiles:

```bash
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-21 \
  --macro-mode scrape \
  --force-macro \
  --download-bi-rate \
  --bps-api-key "$BPS_API_KEY"

python3 workflows/build_feature_store.py \
  --root . \
  --scope live \
  --start-date 2026-03-09 \
  --end-date 2026-05-21
```

Then choose profile.

### Continual profile

```bash
python3 workflows/run_daily_signal_profile.py \
  --root . \
  --profile continual_q3_2024_q1_2026 \
  --from-date 2026-03-09 \
  --end-date 2026-05-21 \
  --target-date 2026-05-22 \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 500000000 \
  --require-broksum
```

### Champion/legacy profile

```bash
python3 workflows/run_daily_signal_profile.py \
  --root . \
  --profile champion \
  --from-date 2026-03-09 \
  --end-date 2026-05-21 \
  --target-date 2026-05-22 \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 500000000 \
  --require-broksum
```

## Manual commands without wrapper

Continual base scores:

```bash
python3 workflows/build_live_base_scores.py \
  --root . \
  --feature-scope live \
  --registry configs/model_registry.continual_q3_2024_q1_2026.json \
  --from-date 2026-03-09 \
  --end-date 2026-05-21 \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 500000000 \
  --require-broksum
```

Continual daily signal:

```bash
python3 workflows/run_daily_signal.py \
  --root . \
  --from-date 2026-03-09 \
  --end-date 2026-05-21 \
  --target-date 2026-05-22 \
  --registry configs/model_registry.continual_q3_2024_q1_2026.json \
  --signal-policy configs/signal_policy.continual_q3_2024_q1_2026.json \
  --price-min 100 \
  --price-max 1000 \
  --min-traded-value 500000000 \
  --require-broksum \
  --skip-base-scores
```

Reports then use the generated signal directory as usual.
