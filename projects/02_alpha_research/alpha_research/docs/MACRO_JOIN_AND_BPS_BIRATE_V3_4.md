# Macro Join + BPS BI Rate Hardening v3.4

This patch fixes two architecture-level issues:

1. `safe_left_join()` now supports many-to-one joins such as macro date-level data joined to ticker-date panels.
   The right side is still required to be unique on the join key, and output row count must remain unchanged.
2. Macro builder now supports BI Rate from BPS WebAPI JSON cache at `data/raw/bps_bi_rate/bi_rate_YYYY.json`.

## Recommended BI Rate workflow

Place BPS JSON files under:

```text
data/raw/bps_bi_rate/bi_rate_2015.json
...
data/raw/bps_bi_rate/bi_rate_2026.json
```

Then run:

```bash
python3 workflows/build_macro.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13 \
  --mode scrape \
  --force
```

If local files are missing and you have a BPS key:

```bash
python3 workflows/build_macro.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13 \
  --mode scrape \
  --force \
  --download-bi-rate \
  --bps-api-key "$BPS_API_KEY"
```

## Macro join contract

Macro is a date-level table and must be unique on `date`. The feature panel is ticker-date and is naturally not unique on `date`. Therefore macro joins are many-to-one.
