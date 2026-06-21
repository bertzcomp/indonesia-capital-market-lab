#!/usr/bin/env bash
set -euo pipefail

# Run from project root after copying your CSV samples into the expected folders:
#   cp financials_sample.csv data/raw/financials/
#   cp keystats_ratios_sample.csv data/raw/keystats/ratios/
#   cp keystats_quarterly_sample.csv data/raw/keystats/quarterly/
#   cp keystats_dividends_sample.csv data/raw/keystats/dividends/
#   cp insider_activity_*.csv data/raw/insider_activity/

python workflows/run_pipeline.py \
  --root . \
  --as-of-date 2026-06-12 \
  --top-n 50 \
  --min-score 40 \
  --include-avoid
