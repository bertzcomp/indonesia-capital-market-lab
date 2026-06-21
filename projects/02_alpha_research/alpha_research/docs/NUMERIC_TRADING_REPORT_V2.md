# Numeric Trading Report v2

This layer replaces generic narrative commentary with a structure-aware numeric trading plan.

## Inputs

- `signals/daily/signal_*/all_strategy_watchlist.csv` or another strategy output file
- `signals/daily/signal_*/all_scores.csv`
- `data/raw_canonical/ohlcv.parquet`
- `configs/signal_policy.json`
- `configs/numeric_report_policy.json`

## Outputs

- `numeric_trade_plan.csv`
- `numeric_trade_plan.json`
- `numeric_trading_report.md`

## Numeric logic

For each ticker the report computes:

- ATR14 from canonical OHLCV
- 5d/10d/20d supports
- 5d/10d/20d/60d resistances
- 5d and 20d price momentum
- volume ratio vs 20d average
- broker-flow fields when present

The generated plan includes:

- exact entry trigger
- buy zone
- structural stop-loss / invalidation level
- risk points and risk percent
- target 1/2/3
- RR for each target
- why these levels were selected
- no-trade or conditional flags

## Philosophy

The report must not say “buy because score is high”. It should explain why the numerical levels are valid or invalid in terms of structure, volatility, liquidity, momentum, and market behaviour.
