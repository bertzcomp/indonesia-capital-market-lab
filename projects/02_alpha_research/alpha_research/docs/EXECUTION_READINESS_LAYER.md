# Execution Readiness Layer

This layer is a post-signal decision layer. It does not replace the model, the signal policy, or live orderbook confirmation.

Daily production now becomes:

```text
canonical raw -> live feature store -> run_daily_signal_profile.py -> numeric report -> execution readiness score -> live WNS/execution
```

## Build ERS for continual model

```bash
python3 workflows/build_execution_readiness_score.py \
  --root . \
  --signal-dir signals/daily/signal_26_may_2026/continual_model \
  --policy configs/execution_readiness_policy.json
```

The workflow expects these files inside `--signal-dir`:

```text
all_strategy_watchlist.csv
numeric_trade_plan.json
all_scores.csv   # optional but recommended
```

If your `all_scores.csv` is still outside the profile directory, pass it explicitly:

```bash
python3 workflows/build_execution_readiness_score.py \
  --root . \
  --signal-dir signals/daily/signal_26_may_2026/continual_model \
  --all-scores signals/daily/signal_26_may_2026/continual_model/all_scores.csv \
  --policy configs/execution_readiness_policy.json
```

Outputs:

```text
execution_readiness.csv
execution_readiness.json
execution_priority_shortlist.csv
execution_readiness_report.md
```

## Tier meaning

- `A_READY_WNS`: priority wait-and-see. Not auto-buy.
- `B_WATCH_CONFIRM`: good but needs better confirmation.
- `C_CONDITIONAL`: only trade if live setup is exceptional.
- `D_LOW_PRIORITY`: avoid/low priority.

## Why after numeric report?

The raw watchlist knows model scores and strategies. The numeric report knows trigger, stop, target, risk, RR, and no-trade reasons. ERS needs both.
