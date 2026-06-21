# Execution Readiness Score Report

This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.

## Tier counts

- A_READY_WNS: 1
- B_WATCH_CONFIRM: 9
- C_CONDITIONAL: 3
- D_LOW_PRIORITY: 0

## Top candidates

| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |
|---:|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | INET | 75.08 | A_READY_WNS | distressed_rebound | 5 | 224.0 | 216.0 | 9.5 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 2 | DEWA | 72.66 | B_WATCH_CONFIRM | distressed_rebound | 5 | 342.0 | 322.0 | 8.15 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 3 | BUVA | 72.25 | B_WATCH_CONFIRM | distressed_rebound | 6 | 720.0 | 690.0 | 13.666667 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 4 | BNBR | 72.16 | B_WATCH_CONFIRM | distressed_rebound | 5 | 130.0 | 125.0 | 11.8 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 5 | BRMS | 72.06 | B_WATCH_CONFIRM | distressed_rebound | 4 | 580.0 | 560.0 | 10.25 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 6 | BIPI | 69.82 | B_WATCH_CONFIRM | distressed_rebound | 4 | 178.0 | 171.0 | 8.571429 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 7 | CDIA | 69.0 | B_WATCH_CONFIRM | distressed_rebound | 3 | 730.0 | 690.0 | 8.125 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 8 | VKTR | 68.35 | B_WATCH_CONFIRM | distressed_rebound | 4 | 675.0 | 650.0 | 9.4 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 9 | MBMA | 64.82 | B_WATCH_CONFIRM | distressed_rebound | 1 | 452.0 | 422.0 | 5.933333 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 10 | IRSX | 62.63 | B_WATCH_CONFIRM | single_or_mixed_signal | 1 | 384.0 | 372.0 | 8.5 | numeric_no_trade_reason_present |
| 11 | PSAB | 57.93 | C_CONDITIONAL | single_or_mixed_signal | 1 | 380.0 | 362.0 | 1.777778 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 12 | DSSA | 48.45 | C_CONDITIONAL | distressed_rebound | 1 | 655.0 | 600.0 | 8.909091 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |
| 13 | CUAN | 47.95 | C_CONDITIONAL | distressed_rebound | 2 | 560.0 | 515.0 | 7.777778 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;still_far_below_ma20 |

## Execution notes

- A tier means priority WNS, not automatic buy.
- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.
- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.