# Signal Policy Watchlist Mode v1.3

This patch separates strategy output into two layers:

1. **Execution candidates**: rows that pass `min_score` and all execution filters.
2. **Watchlist candidates**: top-k rows per strategy that pass universe/liquidity/broksum filters, but may be below execution score threshold.

New output files:

- `all_strategy_watchlist.csv/parquet`: all per-strategy watchlist rows.
- Per-strategy CSV files now contain watchlist rows by default.
- `all_strategy_candidates.csv/parquet`: execution-threshold candidates only.
- `signals_main.csv/parquet`: portfolio-controlled execution candidates.
- `execution_shortlist.csv/parquet`: risk-clean final candidates.

New optional policy fields per strategy:

```json
{
  "watchlist_enabled": true,
  "allow_watchlist_below_threshold": true,
  "watchlist_top_k": 10,
  "watchlist_min_score": null
}
```

If omitted, watchlist output is enabled by default and uses `top_k` as `watchlist_top_k`.
