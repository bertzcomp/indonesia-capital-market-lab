# Execution Readiness Score Report

This report ranks model-produced watchlist tickers by pre-market execution readiness. It does not replace live orderbook/running-trade confirmation.

## Tier counts

- A_READY_WNS: 0
- B_WATCH_CONFIRM: 8
- C_CONDITIONAL: 7
- D_LOW_PRIORITY: 1

## Top candidates

| Rank | Ticker | ERS | Tier | Setup | nStrat | Trigger | Stop | RR | Warnings |
|---:|---|---:|---|---|---:|---:|---:|---:|---|
| 1 | CUAN | 72.93 | B_WATCH_CONFIRM | distressed_rebound | 6 | 875.0 | 820.0 | 7.818182 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 2 | BEEF | 65.12 | B_WATCH_CONFIRM | multi_strategy_confluence | 5 | 162.0 | 150.0 | 4.666667 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 3 | MSIN | 64.91 | B_WATCH_CONFIRM | multi_strategy_confluence | 5 | 665.0 | 610.0 | 4.818182 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 4 | TIRA | 63.63 | B_WATCH_CONFIRM | distressed_rebound | 4 | 655.0 | 620.0 | 6.857143 | numeric_no_trade_reason_present;still_far_below_ma20 |
| 5 | KOKA | 62.35 | B_WATCH_CONFIRM | single_or_mixed_signal | 1 | 151.0 | 143.0 | 4.75 | numeric_no_trade_reason_present |
| 6 | MSJA | 62.33 | B_WATCH_CONFIRM | single_or_mixed_signal | 2 | 428.0 | 398.0 | 4.733333 | numeric_no_trade_reason_present;risk_above_ideal |
| 7 | MBMA | 61.86 | B_WATCH_CONFIRM | single_or_mixed_signal | 1 | 595.0 | 580.0 | 7.0 | numeric_no_trade_reason_present;volume_ratio_weak |
| 8 | TRUE | 60.28 | B_WATCH_CONFIRM | multi_strategy_confluence | 4 | 140.0 | 135.0 | 7.2 | numeric_no_trade_reason_present;volume_ratio_weak |
| 9 | CYBR | 54.16 | C_CONDITIONAL | distressed_rebound | 5 | 675.0 | 620.0 | 11.909091 | numeric_no_trade_reason_present;risk_above_ideal;still_far_below_ma20 |
| 10 | BIPI | 53.41 | C_CONDITIONAL | single_or_mixed_signal | 1 | 226.0 | 206.0 | 2.3 | numeric_no_trade_reason_present;risk_above_ideal |
| 11 | GZCO | 53.05 | C_CONDITIONAL | single_or_mixed_signal | 2 | 189.0 | 184.0 | 8.6 | numeric_no_trade_reason_present;volume_ratio_weak |
| 12 | BELL | 52.51 | C_CONDITIONAL | single_or_mixed_signal | 1 | 132.0 | 124.0 | 4.125 | numeric_no_trade_reason_present;volume_ratio_weak |
| 13 | BNBR | 51.56 | C_CONDITIONAL | single_or_mixed_signal | 1 | 179.0 | 164.0 | 3.533333 | numeric_no_trade_reason_present;risk_above_ideal |
| 14 | ASPR | 51.32 | C_CONDITIONAL | high_volume_event | 1 | 380.0 | 348.0 | 2.875 | numeric_no_trade_reason_present;risk_above_ideal |
| 15 | HBAT | 47.11 | C_CONDITIONAL | single_or_mixed_signal | 1 | 406.0 | 372.0 | 4.676471 | numeric_no_trade_reason_present;risk_above_ideal |
| 16 | MDIA | 42.36 | D_LOW_PRIORITY | single_or_mixed_signal | 2 | 121.0 | 111.0 | 2.9 | numeric_no_trade_reason_present;risk_above_ideal;trigger_not_close;volume_ratio_weak |

## Execution notes

- A tier means priority WNS, not automatic buy.
- Trigger tick area is where orderbook/running trade should be watched for acceptance/retest.
- If warnings include `numeric_no_trade_reason_present`, keep it watchlist-only unless live market confirmation is exceptional.