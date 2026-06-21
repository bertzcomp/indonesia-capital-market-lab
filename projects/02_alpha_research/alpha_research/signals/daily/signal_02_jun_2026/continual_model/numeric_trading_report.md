# Numeric Trading Desk Report — 2026-05-29

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 15 |
| CONDITIONAL | 5 |
| WATCHLIST_ONLY | 3 |
| NO_TRADE | 19 |

## APIC — ara_candidate_continual — ACTIONABLE

**Score:** 0.852 vs policy min 0.50 · **Close:** 980 · **ATR14:** 305.7 · **Volume ratio 20D:** 6.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 870–1,045, entry trigger **1,045**, stop **975**, risk 70 points (6.70%).

**Targets:** TP1 **1,200** (2.21R), TP2 **1,235** (2.71R), TP3 **1,725** (9.71R). Recommended base-case RR: **2.71R**.

**Why entry:** Hybrid entry uses close 980 and ATR14 305.7: buy zone 870–1,045. Entry is valid only if price can trade/hold around 1,045 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 975 is placed below support structure (980 / 980). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,200 (2.21R), TP2 1,235 (2.71R), TP3 1,725 (9.71R). Targets are ATR/structure capped for hold_days=1. ATR14=305.7, resistance_5/10/20/60=1,725/2,090/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — scalping_continual_defensive — ACTIONABLE

**Score:** 0.726 vs policy min 0.05 · **Close:** 700 · **ATR14:** 86.8 · **Volume ratio 20D:** 7.23 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 665–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **765** (1.50R), TP2 **775** (1.83R), TP3 **940** (7.33R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 700 and ATR14 86.8: buy zone 665–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 765 (1.50R), TP2 775 (1.83R), TP3 940 (7.33R). Targets are ATR/structure capped for hold_days=1. ATR14=86.8, resistance_5/10/20/60=950/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — scalping_continual_defensive — ACTIONABLE

**Score:** 0.710 vs policy min 0.05 · **Close:** 238 · **ATR14:** 56.5 · **Volume ratio 20D:** 4.52 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 218–250, entry trigger **250**, stop **236**, risk 14 points (5.60%).

**Targets:** TP1 **280** (2.14R), TP2 **350** (7.14R), TP3 **358** (7.71R). Recommended base-case RR: **7.14R**.

**Why entry:** Hybrid entry uses close 238 and ATR14 56.5: buy zone 218–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 236 is placed below support structure (238 / 238). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 280 (2.14R), TP2 350 (7.14R), TP3 358 (7.71R). Targets are ATR/structure capped for hold_days=1. ATR14=56.5, resistance_5/10/20/60=350/630/640/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## EMTK — scalping_continual_defensive — ACTIONABLE

**Score:** 0.676 vs policy min 0.05 · **Close:** 615 · **ATR14:** 40.7 · **Volume ratio 20D:** 2.77 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 600–625, entry trigger **625**, stop **610**, risk 15 points (2.40%).

**Targets:** TP1 **650** (1.67R), TP2 **700** (5.00R), TP3 **715** (6.00R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 615 and ATR14 40.7: buy zone 600–625. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 610 is placed below support structure (615 / 615). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 650 (1.67R), TP2 700 (5.00R), TP3 715 (6.00R). Targets are ATR/structure capped for hold_days=1. ATR14=40.7, resistance_5/10/20/60=715/830/930/1,025. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — scalping_continual_defensive — ACTIONABLE

**Score:** 0.675 vs policy min 0.05 · **Close:** 980 · **ATR14:** 305.7 · **Volume ratio 20D:** 6.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 870–1,045, entry trigger **1,045**, stop **975**, risk 70 points (6.70%).

**Targets:** TP1 **1,200** (2.21R), TP2 **1,235** (2.71R), TP3 **1,725** (9.71R). Recommended base-case RR: **2.71R**.

**Why entry:** Hybrid entry uses close 980 and ATR14 305.7: buy zone 870–1,045. Entry is valid only if price can trade/hold around 1,045 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 975 is placed below support structure (980 / 980). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,200 (2.21R), TP2 1,235 (2.71R), TP3 1,725 (9.71R). Targets are ATR/structure capped for hold_days=1. ATR14=305.7, resistance_5/10/20/60=1,725/2,090/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.553 vs policy min 0.30 · **Close:** 410 · **ATR14:** 82.9 · **Volume ratio 20D:** 5.79 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 380–428, entry trigger **428**, stop **400**, risk 28 points (6.54%).

**Targets:** TP1 **470** (1.50R), TP2 **610** (6.50R), TP3 **625** (7.04R). Recommended base-case RR: **6.50R**.

**Why entry:** Hybrid entry uses close 410 and ATR14 82.9: buy zone 380–428. Entry is valid only if price can trade/hold around 428 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 400 is placed below support structure (402 / 402). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 470 (1.50R), TP2 610 (6.50R), TP3 625 (7.04R). Targets are ATR/structure capped for hold_days=3. ATR14=82.9, resistance_5/10/20/60=610/835/940/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — swing_continual_defensive — ACTIONABLE

**Score:** 0.553 vs policy min 0.30 · **Close:** 410 · **ATR14:** 82.9 · **Volume ratio 20D:** 5.79 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 380–428, entry trigger **428**, stop **400**, risk 28 points (6.54%).

**Targets:** TP1 **470** (1.50R), TP2 **476** (1.71R), TP3 **610** (6.50R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 410 and ATR14 82.9: buy zone 380–428. Entry is valid only if price can trade/hold around 428 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 400 is placed below support structure (402 / 402). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 470 (1.50R), TP2 476 (1.71R), TP3 610 (6.50R). Targets are ATR/structure capped for hold_days=1. ATR14=82.9, resistance_5/10/20/60=610/835/940/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.523 vs policy min 0.30 · **Close:** 238 · **ATR14:** 56.5 · **Volume ratio 20D:** 4.52 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 218–250, entry trigger **250**, stop **236**, risk 14 points (5.60%).

**Targets:** TP1 **348** (7.00R), TP2 **350** (7.14R), TP3 **358** (7.71R). Recommended base-case RR: **7.14R**.

**Why entry:** Hybrid entry uses close 238 and ATR14 56.5: buy zone 218–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 236 is placed below support structure (238 / 238). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 348 (7.00R), TP2 350 (7.14R), TP3 358 (7.71R). Targets are ATR/structure capped for hold_days=3. ATR14=56.5, resistance_5/10/20/60=350/630/640/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — swing_continual_defensive — ACTIONABLE

**Score:** 0.523 vs policy min 0.30 · **Close:** 238 · **ATR14:** 56.5 · **Volume ratio 20D:** 4.52 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 218–250, entry trigger **250**, stop **236**, risk 14 points (5.60%).

**Targets:** TP1 **280** (2.14R), TP2 **350** (7.14R), TP3 **358** (7.71R). Recommended base-case RR: **7.14R**.

**Why entry:** Hybrid entry uses close 238 and ATR14 56.5: buy zone 218–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 236 is placed below support structure (238 / 238). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 280 (2.14R), TP2 350 (7.14R), TP3 358 (7.71R). Targets are ATR/structure capped for hold_days=1. ATR14=56.5, resistance_5/10/20/60=350/630/640/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.510 vs policy min 0.30 · **Close:** 700 · **ATR14:** 86.8 · **Volume ratio 20D:** 7.23 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 665–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **765** (1.50R), TP2 **950** (7.67R), TP3 **965** (8.17R). Recommended base-case RR: **7.67R**.

**Why entry:** Hybrid entry uses close 700 and ATR14 86.8: buy zone 665–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 765 (1.50R), TP2 950 (7.67R), TP3 965 (8.17R). Targets are ATR/structure capped for hold_days=3. ATR14=86.8, resistance_5/10/20/60=950/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — swing_continual_defensive — ACTIONABLE

**Score:** 0.510 vs policy min 0.30 · **Close:** 700 · **ATR14:** 86.8 · **Volume ratio 20D:** 7.23 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 665–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **765** (1.50R), TP2 **775** (1.83R), TP3 **940** (7.33R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 700 and ATR14 86.8: buy zone 665–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 765 (1.50R), TP2 775 (1.83R), TP3 940 (7.33R). Targets are ATR/structure capped for hold_days=1. ATR14=86.8, resistance_5/10/20/60=950/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.472 vs policy min 0.30 · **Close:** 980 · **ATR14:** 305.7 · **Volume ratio 20D:** 6.07 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 870–1,045, entry trigger **1,045**, stop **975**, risk 70 points (6.70%).

**Targets:** TP1 **1,200** (2.21R), TP2 **1,725** (9.71R), TP3 **1,760** (10.21R). Recommended base-case RR: **9.71R**.

**Why entry:** Hybrid entry uses close 980 and ATR14 305.7: buy zone 870–1,045. Entry is valid only if price can trade/hold around 1,045 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 975 is placed below support structure (980 / 980). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,200 (2.21R), TP2 1,725 (9.71R), TP3 1,760 (10.21R). Targets are ATR/structure capped for hold_days=3. ATR14=305.7, resistance_5/10/20/60=1,725/2,090/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — swing_continual_defensive — ACTIONABLE

**Score:** 0.472 vs policy min 0.30 · **Close:** 980 · **ATR14:** 305.7 · **Volume ratio 20D:** 6.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 870–1,045, entry trigger **1,045**, stop **975**, risk 70 points (6.70%).

**Targets:** TP1 **1,200** (2.21R), TP2 **1,235** (2.71R), TP3 **1,725** (9.71R). Recommended base-case RR: **2.71R**.

**Why entry:** Hybrid entry uses close 980 and ATR14 305.7: buy zone 870–1,045. Entry is valid only if price can trade/hold around 1,045 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 975 is placed below support structure (980 / 980). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,200 (2.21R), TP2 1,235 (2.71R), TP3 1,725 (9.71R). Targets are ATR/structure capped for hold_days=1. ATR14=305.7, resistance_5/10/20/60=1,725/2,090/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.443 vs policy min 0.30 · **Close:** 410 · **ATR14:** 82.9 · **Volume ratio 20D:** 5.79 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 380–428, entry trigger **428**, stop **400**, risk 28 points (6.54%).

**Targets:** TP1 **610** (6.50R), TP2 **625** (7.04R), TP3 **640** (7.57R). Recommended base-case RR: **7.04R**.

**Why entry:** Hybrid entry uses close 410 and ATR14 82.9: buy zone 380–428. Entry is valid only if price can trade/hold around 428 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 400 is placed below support structure (402 / 402). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (6.50R), TP2 625 (7.04R), TP3 640 (7.57R). Targets are ATR/structure capped for hold_days=5. ATR14=82.9, resistance_5/10/20/60=610/835/940/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — position_continual — ACTIONABLE

**Score:** 0.303 vs policy min 0.30 · **Close:** 410 · **ATR14:** 82.9 · **Volume ratio 20D:** 5.79 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 380–428, entry trigger **428**, stop **400**, risk 28 points (6.54%).

**Targets:** TP1 **610** (6.50R), TP2 **625** (7.04R), TP3 **640** (7.57R). Recommended base-case RR: **7.04R**.

**Why entry:** Hybrid entry uses close 410 and ATR14 82.9: buy zone 380–428. Entry is valid only if price can trade/hold around 428 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 400 is placed below support structure (402 / 402). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 610 (6.50R), TP2 625 (7.04R), TP3 640 (7.57R). Targets are ATR/structure capped for hold_days=10. ATR14=82.9, resistance_5/10/20/60=610/835/940/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BSDE — scalping_continual_defensive — CONDITIONAL

**Score:** 0.686 vs policy min 0.05 · **Close:** 630 · **ATR14:** 33.6 · **Volume ratio 20D:** 6.00 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 615–640, entry trigger **640**, stop **620**, risk 20 points (3.12%).

**Targets:** TP1 **660** (1.00R), TP2 **705** (3.25R), TP3 **720** (4.00R). Recommended base-case RR: **3.25R**.

**Why entry:** Hybrid entry uses close 630 and ATR14 33.6: buy zone 615–640. Entry is valid only if price can trade/hold around 640 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 660 (1.00R), TP2 705 (3.25R), TP3 720 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=33.6, resistance_5/10/20/60=720/780/835/910. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.511 vs policy min 0.30 · **Close:** 334 · **ATR14:** 42.3 · **Volume ratio 20D:** 0.63 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 318–344, entry trigger **344**, stop **318**, risk 26 points (7.56%).

**Targets:** TP1 **398** (2.08R), TP2 **412** (2.62R), TP3 **426** (3.15R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 42.3: buy zone 318–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.08R), TP2 412 (2.62R), TP3 426 (3.15R). Targets are ATR/structure capped for hold_days=5. ATR14=42.3, resistance_5/10/20/60=398/535/570/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FORE — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.436 vs policy min 0.30 · **Close:** 705 · **ATR14:** 82.5 · **Volume ratio 20D:** 0.96 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 675–725, entry trigger **725**, stop **680**, risk 45 points (6.21%).

**Targets:** TP1 **770** (1.00R), TP2 **985** (5.78R), TP3 **1,005** (6.22R). Recommended base-case RR: **5.78R**.

**Why entry:** Hybrid entry uses close 705 and ATR14 82.5: buy zone 675–725. Entry is valid only if price can trade/hold around 725 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 680 is placed below support structure (685 / 685). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 770 (1.00R), TP2 985 (5.78R), TP3 1,005 (6.22R). Targets are ATR/structure capped for hold_days=3. ATR14=82.5, resistance_5/10/20/60=1,005/1,035/1,050/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FORE — swing_continual_defensive — CONDITIONAL

**Score:** 0.436 vs policy min 0.30 · **Close:** 705 · **ATR14:** 82.5 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 675–725, entry trigger **725**, stop **680**, risk 45 points (6.21%).

**Targets:** TP1 **770** (1.00R), TP2 **805** (1.78R), TP3 **835** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 705 and ATR14 82.5: buy zone 675–725. Entry is valid only if price can trade/hold around 725 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 680 is placed below support structure (685 / 685). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 770 (1.00R), TP2 805 (1.78R), TP3 835 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=82.5, resistance_5/10/20/60=1,005/1,035/1,050/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — CONDITIONAL

**Score:** 0.315 vs policy min 0.30 · **Close:** 334 · **ATR14:** 42.3 · **Volume ratio 20D:** 0.63 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 318–344, entry trigger **344**, stop **318**, risk 26 points (7.56%).

**Targets:** TP1 **398** (2.08R), TP2 **412** (2.62R), TP3 **426** (3.15R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 42.3: buy zone 318–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.08R), TP2 412 (2.62R), TP3 426 (3.15R). Targets are ATR/structure capped for hold_days=10. ATR14=42.3, resistance_5/10/20/60=398/535/570/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KIJA — position_continual — WATCHLIST_ONLY

**Score:** 0.295 vs policy min 0.30 · **Close:** 124 · **ATR14:** 10.0 · **Volume ratio 20D:** 0.48 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 120–126, entry trigger **126**, stop **117**, risk 9 points (7.14%).

**Targets:** TP1 **158** (3.56R), TP2 **159** (3.67R), TP3 **164** (4.22R). Recommended base-case RR: **3.67R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.0: buy zone 120–126. Entry is valid only if price can trade/hold around 126 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 158 (3.56R), TP2 159 (3.67R), TP3 164 (4.22R). Targets are ATR/structure capped for hold_days=10. ATR14=10.0, resistance_5/10/20/60=159/182/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.295 below policy min_score 0.30; volume ratio 0.48 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## SSMS — position_continual — WATCHLIST_ONLY

**Score:** 0.294 vs policy min 0.30 · **Close:** 700 · **ATR14:** 86.8 · **Volume ratio 20D:** 7.23 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 665–720, entry trigger **720**, stop **690**, risk 30 points (4.17%).

**Targets:** TP1 **950** (7.67R), TP2 **965** (8.17R), TP3 **980** (8.67R). Recommended base-case RR: **8.17R**.

**Why entry:** Hybrid entry uses close 700 and ATR14 86.8: buy zone 665–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is placed below support structure (695 / 695). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 950 (7.67R), TP2 965 (8.17R), TP3 980 (8.67R). Targets are ATR/structure capped for hold_days=10. ATR14=86.8, resistance_5/10/20/60=950/1,420/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.294 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BANK — position_continual — WATCHLIST_ONLY

**Score:** 0.290 vs policy min 0.30 · **Close:** 238 · **ATR14:** 56.5 · **Volume ratio 20D:** 4.52 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 218–250, entry trigger **250**, stop **236**, risk 14 points (5.60%).

**Targets:** TP1 **350** (7.14R), TP2 **358** (7.71R), TP3 **366** (8.29R). Recommended base-case RR: **7.71R**.

**Why entry:** Hybrid entry uses close 238 and ATR14 56.5: buy zone 218–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 236 is placed below support structure (238 / 238). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 350 (7.14R), TP2 358 (7.71R), TP3 366 (8.29R). Targets are ATR/structure capped for hold_days=10. ATR14=56.5, resistance_5/10/20/60=350/630/640/640. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.290 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.541 vs policy min 0.30 · **Close:** 492 · **ATR14:** 151.1 · **Volume ratio 20D:** 8.32 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 438–525, entry trigger **525**, stop **482**, risk 43 points (8.19%).

**Targets:** TP1 **705** (4.19R), TP2 **730** (4.77R), TP3 **755** (5.35R). Recommended base-case RR: **4.77R**.

**Why entry:** Hybrid entry uses close 492 and ATR14 151.1: buy zone 438–525. Entry is valid only if price can trade/hold around 525 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 482 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 705 (4.19R), TP2 730 (4.77R), TP3 755 (5.35R). Targets are ATR/structure capped for hold_days=3. ATR14=151.1, resistance_5/10/20/60=705/1,525/3,120/95,200. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.19% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — NO_TRADE

**Score:** 0.541 vs policy min 0.30 · **Close:** 492 · **ATR14:** 151.1 · **Volume ratio 20D:** 8.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 438–525, entry trigger **525**, stop **482**, risk 43 points (8.19%).

**Targets:** TP1 **680** (3.60R), TP2 **705** (4.19R), TP3 **730** (4.77R). Recommended base-case RR: **4.19R**.

**Why entry:** Hybrid entry uses close 492 and ATR14 151.1: buy zone 438–525. Entry is valid only if price can trade/hold around 525 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 482 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (3.60R), TP2 705 (4.19R), TP3 730 (4.77R). Targets are ATR/structure capped for hold_days=1. ATR14=151.1, resistance_5/10/20/60=705/1,525/3,120/95,200. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.19% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.495 vs policy min 0.30 · **Close:** 176 · **ATR14:** 23.8 · **Volume ratio 20D:** 0.40 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 167–181, entry trigger **181**, stop **166**, risk 15 points (8.29%).

**Targets:** TP1 **208** (1.80R), TP2 **216** (2.33R), TP3 **218** (2.47R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 176 and ATR14 23.8: buy zone 167–181. Entry is valid only if price can trade/hold around 181 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 166 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 208 (1.80R), TP2 216 (2.33R), TP3 218 (2.47R). Targets are ATR/structure capped for hold_days=5. ATR14=23.8, resistance_5/10/20/60=208/262/302/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%; volume ratio 0.40 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.489 vs policy min 0.30 · **Close:** 492 · **ATR14:** 151.1 · **Volume ratio 20D:** 8.32 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 438–525, entry trigger **525**, stop **482**, risk 43 points (8.19%).

**Targets:** TP1 **705** (4.19R), TP2 **730** (4.77R), TP3 **755** (5.35R). Recommended base-case RR: **4.77R**.

**Why entry:** Hybrid entry uses close 492 and ATR14 151.1: buy zone 438–525. Entry is valid only if price can trade/hold around 525 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 482 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 705 (4.19R), TP2 730 (4.77R), TP3 755 (5.35R). Targets are ATR/structure capped for hold_days=5. ATR14=151.1, resistance_5/10/20/60=705/1,525/3,120/95,200. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.19% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.488 vs policy min 0.30 · **Close:** 760 · **ATR14:** 113.6 · **Volume ratio 20D:** 1.36 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 720–785, entry trigger **785**, stop **720**, risk 65 points (8.28%).

**Targets:** TP1 **850** (1.00R), TP2 **900** (1.77R), TP3 **945** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 760 and ATR14 113.6: buy zone 720–785. Entry is valid only if price can trade/hold around 785 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 850 (1.00R), TP2 900 (1.77R), TP3 945 (2.46R). Targets are ATR/structure capped for hold_days=5. ATR14=113.6, resistance_5/10/20/60=850/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.28% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.463 vs policy min 0.30 · **Close:** 129 · **ATR14:** 20.6 · **Volume ratio 20D:** 0.57 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 121–134, entry trigger **134**, stop **123**, risk 11 points (8.21%).

**Targets:** TP1 **154** (1.82R), TP2 **160** (2.36R), TP3 **161** (2.45R). Recommended base-case RR: **2.36R**.

**Why entry:** Hybrid entry uses close 129 and ATR14 20.6: buy zone 121–134. Entry is valid only if price can trade/hold around 134 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 123 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.82R), TP2 160 (2.36R), TP3 161 (2.45R). Targets are ATR/structure capped for hold_days=5. ATR14=20.6, resistance_5/10/20/60=154/218/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; volume ratio 0.57 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.452 vs policy min 0.30 · **Close:** 129 · **ATR14:** 20.6 · **Volume ratio 20D:** 0.57 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 121–134, entry trigger **134**, stop **123**, risk 11 points (8.21%).

**Targets:** TP1 **154** (1.82R), TP2 **160** (2.36R), TP3 **161** (2.45R). Recommended base-case RR: **2.36R**.

**Why entry:** Hybrid entry uses close 129 and ATR14 20.6: buy zone 121–134. Entry is valid only if price can trade/hold around 134 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 123 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.82R), TP2 160 (2.36R), TP3 161 (2.45R). Targets are ATR/structure capped for hold_days=3. ATR14=20.6, resistance_5/10/20/60=154/218/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; volume ratio 0.57 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — swing_continual_defensive — NO_TRADE

**Score:** 0.452 vs policy min 0.30 · **Close:** 129 · **ATR14:** 20.6 · **Volume ratio 20D:** 0.57 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 121–134, entry trigger **134**, stop **123**, risk 11 points (8.21%).

**Targets:** TP1 **154** (1.82R), TP2 **160** (2.36R), TP3 **161** (2.45R). Recommended base-case RR: **2.36R**.

**Why entry:** Hybrid entry uses close 129 and ATR14 20.6: buy zone 121–134. Entry is valid only if price can trade/hold around 134 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 123 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.82R), TP2 160 (2.36R), TP3 161 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=20.6, resistance_5/10/20/60=154/218/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; volume ratio 0.57 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.443 vs policy min 0.30 · **Close:** 478 · **ATR14:** 53.5 · **Volume ratio 20D:** 0.64 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 458–490, entry trigger **490**, stop **450**, risk 40 points (8.16%).

**Targets:** TP1 **530** (1.00R), TP2 **560** (1.75R), TP3 **590** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 478 and ATR14 53.5: buy zone 458–490. Entry is valid only if price can trade/hold around 490 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 450 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 530 (1.00R), TP2 560 (1.75R), TP3 590 (2.50R). Targets are ATR/structure capped for hold_days=5. ATR14=53.5, resistance_5/10/20/60=510/665/740/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.16% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.398 vs policy min 0.30 · **Close:** 760 · **ATR14:** 113.6 · **Volume ratio 20D:** 1.36 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 720–785, entry trigger **785**, stop **720**, risk 65 points (8.28%).

**Targets:** TP1 **850** (1.00R), TP2 **900** (1.77R), TP3 **945** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 760 and ATR14 113.6: buy zone 720–785. Entry is valid only if price can trade/hold around 785 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 850 (1.00R), TP2 900 (1.77R), TP3 945 (2.46R). Targets are ATR/structure capped for hold_days=10. ATR14=113.6, resistance_5/10/20/60=850/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.28% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.330 vs policy min 0.30 · **Close:** 334 · **ATR14:** 42.3 · **Volume ratio 20D:** 0.63 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 318–344, entry trigger **344**, stop **318**, risk 26 points (7.56%).

**Targets:** TP1 **398** (2.08R), TP2 **412** (2.62R), TP3 **426** (3.15R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 334 and ATR14 42.3: buy zone 318–344. Entry is valid only if price can trade/hold around 344 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 318 is placed below support structure (320 / 320). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.08R), TP2 412 (2.62R), TP3 426 (3.15R). Targets are ATR/structure capped for hold_days=10. ATR14=42.3, resistance_5/10/20/60=398/535/570/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — NO_TRADE

**Score:** 0.317 vs policy min 0.30 · **Close:** 129 · **ATR14:** 20.6 · **Volume ratio 20D:** 0.57 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 121–134, entry trigger **134**, stop **123**, risk 11 points (8.21%).

**Targets:** TP1 **154** (1.82R), TP2 **160** (2.36R), TP3 **161** (2.45R). Recommended base-case RR: **2.36R**.

**Why entry:** Hybrid entry uses close 129 and ATR14 20.6: buy zone 121–134. Entry is valid only if price can trade/hold around 134 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 123 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.82R), TP2 160 (2.36R), TP3 161 (2.45R). Targets are ATR/structure capped for hold_days=10. ATR14=20.6, resistance_5/10/20/60=154/218/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; volume ratio 0.57 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## APIC — momentum_20d_continual_research — NO_TRADE

**Score:** 0.314 vs policy min 0.30 · **Close:** 980 · **ATR14:** 305.7 · **Volume ratio 20D:** 6.07 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 870–1,045, entry trigger **1,045**, stop **975**, risk 70 points (6.70%).

**Targets:** TP1 **1,725** (9.71R), TP2 **1,760** (10.21R), TP3 **1,795** (10.71R). Recommended base-case RR: **10.21R**.

**Why entry:** Hybrid entry uses close 980 and ATR14 305.7: buy zone 870–1,045. Entry is valid only if price can trade/hold around 1,045 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 975 is placed below support structure (980 / 980). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,725 (9.71R), TP2 1,760 (10.21R), TP3 1,795 (10.71R). Targets are ATR/structure capped for hold_days=10. ATR14=305.7, resistance_5/10/20/60=1,725/2,090/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.309 vs policy min 0.30 · **Close:** 124 · **ATR14:** 10.0 · **Volume ratio 20D:** 0.48 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 120–126, entry trigger **126**, stop **117**, risk 9 points (7.14%).

**Targets:** TP1 **158** (3.56R), TP2 **159** (3.67R), TP3 **164** (4.22R). Recommended base-case RR: **3.67R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.0: buy zone 120–126. Entry is valid only if price can trade/hold around 126 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 158 (3.56R), TP2 159 (3.67R), TP3 164 (4.22R). Targets are ATR/structure capped for hold_days=10. ATR14=10.0, resistance_5/10/20/60=159/182/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; volume ratio 0.48 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRUE — momentum_20d_continual_research — NO_TRADE

**Score:** 0.308 vs policy min 0.30 · **Close:** 100 · **ATR14:** 15.1 · **Volume ratio 20D:** 0.77 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 94–104, entry trigger **104**, stop **95**, risk 9 points (8.65%).

**Targets:** TP1 **120** (1.78R), TP2 **125** (2.33R), TP3 **126** (2.44R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 15.1: buy zone 94–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 95 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 120 (1.78R), TP2 125 (2.33R), TP3 126 (2.44R). Targets are ATR/structure capped for hold_days=10. ATR14=15.1, resistance_5/10/20/60=120/173/190/290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.65% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BIPI — position_continual — NO_TRADE

**Score:** 0.304 vs policy min 0.30 · **Close:** 176 · **ATR14:** 23.8 · **Volume ratio 20D:** 0.40 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 167–181, entry trigger **181**, stop **166**, risk 15 points (8.29%).

**Targets:** TP1 **208** (1.80R), TP2 **216** (2.33R), TP3 **218** (2.47R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 176 and ATR14 23.8: buy zone 167–181. Entry is valid only if price can trade/hold around 181 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 166 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 208 (1.80R), TP2 216 (2.33R), TP3 218 (2.47R). Targets are ATR/structure capped for hold_days=10. ATR14=23.8, resistance_5/10/20/60=208/262/302/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%; volume ratio 0.40 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — NO_TRADE

**Score:** 0.302 vs policy min 0.30 · **Close:** 492 · **ATR14:** 151.1 · **Volume ratio 20D:** 8.32 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 438–525, entry trigger **525**, stop **482**, risk 43 points (8.19%).

**Targets:** TP1 **705** (4.19R), TP2 **730** (4.77R), TP3 **755** (5.35R). Recommended base-case RR: **4.77R**.

**Why entry:** Hybrid entry uses close 492 and ATR14 151.1: buy zone 438–525. Entry is valid only if price can trade/hold around 525 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 482 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 705 (4.19R), TP2 730 (4.77R), TP3 755 (5.35R). Targets are ATR/structure capped for hold_days=10. ATR14=151.1, resistance_5/10/20/60=705/1,525/3,120/95,200. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.19% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRUE — position_continual — NO_TRADE

**Score:** 0.287 vs policy min 0.30 · **Close:** 100 · **ATR14:** 15.1 · **Volume ratio 20D:** 0.77 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 94–104, entry trigger **104**, stop **95**, risk 9 points (8.65%).

**Targets:** TP1 **120** (1.78R), TP2 **125** (2.33R), TP3 **126** (2.44R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 15.1: buy zone 94–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 95 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 120 (1.78R), TP2 125 (2.33R), TP3 126 (2.44R). Targets are ATR/structure capped for hold_days=10. ATR14=15.1, resistance_5/10/20/60=120/173/190/290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.65% exceeds max strategy risk 8.00%; score 0.287 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BUVA — position_continual — NO_TRADE

**Score:** 0.285 vs policy min 0.30 · **Close:** 760 · **ATR14:** 113.6 · **Volume ratio 20D:** 1.36 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 720–785, entry trigger **785**, stop **720**, risk 65 points (8.28%).

**Targets:** TP1 **850** (1.00R), TP2 **900** (1.77R), TP3 **945** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 760 and ATR14 113.6: buy zone 720–785. Entry is valid only if price can trade/hold around 785 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 850 (1.00R), TP2 900 (1.77R), TP3 945 (2.46R). Targets are ATR/structure capped for hold_days=10. ATR14=113.6, resistance_5/10/20/60=850/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.28% exceeds max strategy risk 8.00%; score 0.285 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
