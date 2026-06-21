# Macro + Broker Sanity Patch v2.2

This patch adds:

1. Safe broker-ratio repair:
   - recomputes `net_flow_ratio` from sane buy/sell values with denominator `abs(buy)+abs(sell)`;
   - clips ratio to `[-1, 1]`;
   - recomputes dominance ratios when possible;
   - removes NaN/Inf from numeric columns.

2. Macro builder:
   - local macro load if available;
   - optional scraping via Frankfurter + yfinance;
   - safe fallback from market-derived OHLCV proxy with `macro_missing_flag=1`;
   - writes:
     - `data/raw_canonical/macro.parquet`
     - `data/features/macro/macro_features.parquet`.

3. Workflow integration:
   - `workflows/build_canonical_raw.py` now builds macro unless `--skip-macro`.
   - `workflows/build_feature_store.py` updates macro first and runs feature-store sanity after build.

## Commands

Build macro explicitly:

```bash
python3 workflows/build_macro.py --root . --start-date 2015-01-01 --end-date 2026-05-13
```

Enable online macro scraping:

```bash
python3 workflows/build_macro.py --root . --start-date 2015-01-01 --end-date 2026-05-13 --scrape --force
```

Sanitize feature store manually:

```bash
python3 workflows/sanitize_feature_store.py --root . --scope history
python3 workflows/sanitize_feature_store.py --root . --scope live
```

Daily signal workflow after EOD:

1. Put new daily files in `data/pure_raw`.
2. Build canonical raw:
   `python3 workflows/build_canonical_raw.py --root . --start-date 2015-01-01 --end-date <EOD_DATE>`
3. Build live feature:
   `python3 workflows/build_feature_store.py --root . --scope live --start-date <LOOKBACK_START> --end-date <EOD_DATE>`
4. Run daily signal for next trading day.

Continual learning:

1. Update canonical raw.
2. Build/refresh history or continual feature dataset.
3. Run continual retraining with maturity cutoff.
4. Evaluate challenger; do not auto-promote.
