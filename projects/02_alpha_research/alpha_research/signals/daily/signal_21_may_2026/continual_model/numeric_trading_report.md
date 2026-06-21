# Numeric Trading Desk Report — 2026-05-20

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 10 |
| CONDITIONAL | 3 |
| WATCHLIST_ONLY | 4 |
| NO_TRADE | 25 |

## CUAN — scalping_continual_defensive — ACTIONABLE

**Score:** 0.727 vs policy min 0.05 · **Close:** 590 · **ATR14:** 121.4 · **Volume ratio 20D:** 1.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 545–615, entry trigger **615**, stop **570**, risk 45 points (7.32%).

**Targets:** TP1 **680** (1.44R), TP2 **695** (1.78R), TP3 **725** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 590 and ATR14 121.4: buy zone 545–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is placed below support structure (575 / 575). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.44R), TP2 695 (1.78R), TP3 725 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=121.4, resistance_5/10/20/60=1,305/1,340/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — scalping_continual_defensive — ACTIONABLE

**Score:** 0.704 vs policy min 0.05 · **Close:** 925 · **ATR14:** 85.4 · **Volume ratio 20D:** 1.21 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 895–945, entry trigger **945**, stop **910**, risk 35 points (3.70%).

**Targets:** TP1 **990** (1.29R), TP2 **1,005** (1.71R), TP3 **1,030** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 925 and ATR14 85.4: buy zone 895–945. Entry is valid only if price can trade/hold around 945 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 910 is placed below support structure (915 / 915). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 990 (1.29R), TP2 1,005 (1.71R), TP3 1,030 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=85.4, resistance_5/10/20/60=1,420/1,460/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.554 vs policy min 0.30 · **Close:** 590 · **ATR14:** 121.4 · **Volume ratio 20D:** 1.45 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 545–615, entry trigger **615**, stop **570**, risk 45 points (7.32%).

**Targets:** TP1 **680** (1.44R), TP2 **695** (1.78R), TP3 **1,295** (15.11R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 590 and ATR14 121.4: buy zone 545–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is placed below support structure (575 / 575). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.44R), TP2 695 (1.78R), TP3 1,295 (15.11R). Targets are ATR/structure capped for hold_days=5. ATR14=121.4, resistance_5/10/20/60=1,305/1,340/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.468 vs policy min 0.30 · **Close:** 590 · **ATR14:** 121.4 · **Volume ratio 20D:** 1.45 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 545–615, entry trigger **615**, stop **570**, risk 45 points (7.32%).

**Targets:** TP1 **680** (1.44R), TP2 **695** (1.78R), TP3 **725** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 590 and ATR14 121.4: buy zone 545–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is placed below support structure (575 / 575). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.44R), TP2 695 (1.78R), TP3 725 (2.44R). Targets are ATR/structure capped for hold_days=3. ATR14=121.4, resistance_5/10/20/60=1,305/1,340/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — swing_continual_defensive — ACTIONABLE

**Score:** 0.468 vs policy min 0.30 · **Close:** 590 · **ATR14:** 121.4 · **Volume ratio 20D:** 1.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 545–615, entry trigger **615**, stop **570**, risk 45 points (7.32%).

**Targets:** TP1 **680** (1.44R), TP2 **695** (1.78R), TP3 **725** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 590 and ATR14 121.4: buy zone 545–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is placed below support structure (575 / 575). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.44R), TP2 695 (1.78R), TP3 725 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=121.4, resistance_5/10/20/60=1,305/1,340/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.436 vs policy min 0.30 · **Close:** 925 · **ATR14:** 85.4 · **Volume ratio 20D:** 1.21 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 895–945, entry trigger **945**, stop **910**, risk 35 points (3.70%).

**Targets:** TP1 **990** (1.29R), TP2 **1,005** (1.71R), TP3 **1,030** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 925 and ATR14 85.4: buy zone 895–945. Entry is valid only if price can trade/hold around 945 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 910 is placed below support structure (915 / 915). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 990 (1.29R), TP2 1,005 (1.71R), TP3 1,030 (2.43R). Targets are ATR/structure capped for hold_days=3. ATR14=85.4, resistance_5/10/20/60=1,420/1,460/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — swing_continual_defensive — ACTIONABLE

**Score:** 0.436 vs policy min 0.30 · **Close:** 925 · **ATR14:** 85.4 · **Volume ratio 20D:** 1.21 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 895–945, entry trigger **945**, stop **910**, risk 35 points (3.70%).

**Targets:** TP1 **990** (1.29R), TP2 **1,005** (1.71R), TP3 **1,030** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 925 and ATR14 85.4: buy zone 895–945. Entry is valid only if price can trade/hold around 945 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 910 is placed below support structure (915 / 915). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 990 (1.29R), TP2 1,005 (1.71R), TP3 1,030 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=85.4, resistance_5/10/20/60=1,420/1,460/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.433 vs policy min 0.30 · **Close:** 250 · **ATR14:** 22.3 · **Volume ratio 20D:** 1.31 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 242–256, entry trigger **256**, stop **248**, risk 8 points (3.12%).

**Targets:** TP1 **268** (1.50R), TP2 **270** (1.75R), TP3 **276** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 250 and ATR14 22.3: buy zone 242–256. Entry is valid only if price can trade/hold around 256 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 248 is placed below support structure (250 / 250). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 268 (1.50R), TP2 270 (1.75R), TP3 276 (2.50R). Targets are ATR/structure capped for hold_days=3. ATR14=22.3, resistance_5/10/20/60=372/394/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — swing_continual_defensive — ACTIONABLE

**Score:** 0.433 vs policy min 0.30 · **Close:** 250 · **ATR14:** 22.3 · **Volume ratio 20D:** 1.31 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 242–256, entry trigger **256**, stop **248**, risk 8 points (3.12%).

**Targets:** TP1 **268** (1.50R), TP2 **270** (1.75R), TP3 **276** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 250 and ATR14 22.3: buy zone 242–256. Entry is valid only if price can trade/hold around 256 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 248 is placed below support structure (250 / 250). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 268 (1.50R), TP2 270 (1.75R), TP3 276 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=22.3, resistance_5/10/20/60=372/394/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — ACTIONABLE

**Score:** 0.314 vs policy min 0.30 · **Close:** 590 · **ATR14:** 121.4 · **Volume ratio 20D:** 1.45 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 545–615, entry trigger **615**, stop **570**, risk 45 points (7.32%).

**Targets:** TP1 **680** (1.44R), TP2 **1,305** (15.33R), TP3 **1,330** (15.89R). Recommended base-case RR: **15.33R**.

**Why entry:** Hybrid entry uses close 590 and ATR14 121.4: buy zone 545–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is placed below support structure (575 / 575). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.44R), TP2 1,305 (15.33R), TP3 1,330 (15.89R). Targets are ATR/structure capped for hold_days=10. ATR14=121.4, resistance_5/10/20/60=1,305/1,340/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NICL — scalping_continual_defensive — CONDITIONAL

**Score:** 0.721 vs policy min 0.05 · **Close:** 580 · **ATR14:** 60.4 · **Volume ratio 20D:** 0.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 555–595, entry trigger **595**, stop **555**, risk 40 points (6.72%).

**Targets:** TP1 **635** (1.00R), TP2 **665** (1.75R), TP3 **695** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 580 and ATR14 60.4: buy zone 555–595. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is placed below support structure (560 / 560). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.00R), TP2 665 (1.75R), TP3 695 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=60.4, resistance_5/10/20/60=875/925/1,100/1,285. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.59 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PSAB — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.544 vs policy min 0.30 · **Close:** 390 · **ATR14:** 37.6 · **Volume ratio 20D:** 1.17 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 376–398, entry trigger **398**, stop **376**, risk 22 points (5.53%).

**Targets:** TP1 **420** (1.00R), TP2 **436** (1.73R), TP3 **580** (8.27R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 390 and ATR14 37.6: buy zone 376–398. Entry is valid only if price can trade/hold around 398 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 376 is placed below support structure (378 / 378). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 420 (1.00R), TP2 436 (1.73R), TP3 580 (8.27R). Targets are ATR/structure capped for hold_days=5. ATR14=37.6, resistance_5/10/20/60=580/580/590/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NICL — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.539 vs policy min 0.30 · **Close:** 580 · **ATR14:** 60.4 · **Volume ratio 20D:** 0.59 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 555–595, entry trigger **595**, stop **555**, risk 40 points (6.72%).

**Targets:** TP1 **635** (1.00R), TP2 **840** (6.12R), TP3 **875** (7.00R). Recommended base-case RR: **6.12R**.

**Why entry:** Hybrid entry uses close 580 and ATR14 60.4: buy zone 555–595. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is placed below support structure (560 / 560). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.00R), TP2 840 (6.12R), TP3 875 (7.00R). Targets are ATR/structure capped for hold_days=5. ATR14=60.4, resistance_5/10/20/60=875/925/1,100/1,285. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.59 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — position_continual — WATCHLIST_ONLY

**Score:** 0.299 vs policy min 0.30 · **Close:** 925 · **ATR14:** 85.4 · **Volume ratio 20D:** 1.21 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 895–945, entry trigger **945**, stop **910**, risk 35 points (3.70%).

**Targets:** TP1 **990** (1.29R), TP2 **1,420** (13.57R), TP3 **1,440** (14.14R). Recommended base-case RR: **13.57R**.

**Why entry:** Hybrid entry uses close 925 and ATR14 85.4: buy zone 895–945. Entry is valid only if price can trade/hold around 945 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 910 is placed below support structure (915 / 915). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 990 (1.29R), TP2 1,420 (13.57R), TP3 1,440 (14.14R). Targets are ATR/structure capped for hold_days=10. ATR14=85.4, resistance_5/10/20/60=1,420/1,460/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.299 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## PSAB — position_continual — WATCHLIST_ONLY

**Score:** 0.296 vs policy min 0.30 · **Close:** 390 · **ATR14:** 37.6 · **Volume ratio 20D:** 1.17 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 376–398, entry trigger **398**, stop **376**, risk 22 points (5.53%).

**Targets:** TP1 **420** (1.00R), TP2 **580** (8.27R), TP3 **595** (8.95R). Recommended base-case RR: **8.27R**.

**Why entry:** Hybrid entry uses close 390 and ATR14 37.6: buy zone 376–398. Entry is valid only if price can trade/hold around 398 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 376 is placed below support structure (378 / 378). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 420 (1.00R), TP2 580 (8.27R), TP3 595 (8.95R). Targets are ATR/structure capped for hold_days=10. ATR14=37.6, resistance_5/10/20/60=580/580/590/590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.296 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## CDIA — position_continual — WATCHLIST_ONLY

**Score:** 0.295 vs policy min 0.30 · **Close:** 790 · **ATR14:** 101.4 · **Volume ratio 20D:** 0.74 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 750–815, entry trigger **815**, stop **770**, risk 45 points (5.52%).

**Targets:** TP1 **870** (1.22R), TP2 **1,230** (9.22R), TP3 **1,255** (9.78R). Recommended base-case RR: **9.22R**.

**Why entry:** Hybrid entry uses close 790 and ATR14 101.4: buy zone 750–815. Entry is valid only if price can trade/hold around 815 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 770 is placed below support structure (775 / 775). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.22R), TP2 1,230 (9.22R), TP3 1,255 (9.78R). Targets are ATR/structure capped for hold_days=10. ATR14=101.4, resistance_5/10/20/60=1,230/1,230/1,340/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.295 below policy min_score 0.30; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NICL — position_continual — WATCHLIST_ONLY

**Score:** 0.294 vs policy min 0.30 · **Close:** 580 · **ATR14:** 60.4 · **Volume ratio 20D:** 0.59 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 555–595, entry trigger **595**, stop **555**, risk 40 points (6.72%).

**Targets:** TP1 **635** (1.00R), TP2 **875** (7.00R), TP3 **895** (7.50R). Recommended base-case RR: **7.00R**.

**Why entry:** Hybrid entry uses close 580 and ATR14 60.4: buy zone 555–595. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is placed below support structure (560 / 560). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.00R), TP2 875 (7.00R), TP3 895 (7.50R). Targets are ATR/structure capped for hold_days=10. ATR14=60.4, resistance_5/10/20/60=875/925/1,100/1,285. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.294 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.59 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## ASPR — ara_candidate_continual — NO_TRADE

**Score:** 0.855 vs policy min 0.50 · **Close:** 396 · **ATR14:** 57.1 · **Volume ratio 20D:** 3.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 376–408, entry trigger **408**, stop **374**, risk 34 points (8.33%).

**Targets:** TP1 **442** (1.00R), TP2 **466** (1.71R), TP3 **540** (3.88R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 396 and ATR14 57.1: buy zone 376–408. Entry is valid only if price can trade/hold around 408 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 374 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 442 (1.00R), TP2 466 (1.71R), TP3 540 (3.88R). Targets are ATR/structure capped for hold_days=1. ATR14=57.1, resistance_5/10/20/60=540/540/540/540. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## NSSS — scalping_continual_defensive — NO_TRADE

**Score:** 0.708 vs policy min 0.05 · **Close:** 565 · **ATR14:** 81.4 · **Volume ratio 20D:** 0.41 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 535–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **635** (1.00R), TP2 **670** (1.70R), TP3 **705** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 565 and ATR14 81.4: buy zone 535–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (1.00R), TP2 670 (1.70R), TP3 705 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=81.4, resistance_5/10/20/60=850/905/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.41 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## WBSA — scalping_continual_defensive — NO_TRADE

**Score:** 0.703 vs policy min 0.05 · **Close:** 785 · **ATR14:** 695.0 · **Volume ratio 20D:** 4.78 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 540–925, entry trigger **925**, stop **850**, risk 75 points (8.11%).

**Targets:** TP1 **1,605** (9.07R), TP2 **1,645** (9.60R), TP3 **1,685** (10.13R). Recommended base-case RR: **9.60R**.

**Why entry:** Hybrid entry uses close 785 and ATR14 695.0: buy zone 540–925. Entry is valid only if price can trade/hold around 925 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 850 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,605 (9.07R), TP2 1,645 (9.60R), TP3 1,685 (10.13R). Targets are ATR/structure capped for hold_days=1. ATR14=695.0, resistance_5/10/20/60=1,605/1,605/1,605/1,605. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 17.83% > max 8.00%; entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.548 vs policy min 0.30 · **Close:** 378 · **ATR14:** 35.5 · **Volume ratio 20D:** 2.19 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 364–386, entry trigger **386**, stop **354**, risk 32 points (8.29%).

**Targets:** TP1 **418** (1.00R), TP2 **530** (4.50R), TP3 **535** (4.66R). Recommended base-case RR: **4.50R**.

**Why entry:** Hybrid entry uses close 378 and ATR14 35.5: buy zone 364–386. Entry is valid only if price can trade/hold around 386 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 418 (1.00R), TP2 530 (4.50R), TP3 535 (4.66R). Targets are ATR/structure capped for hold_days=5. ATR14=35.5, resistance_5/10/20/60=535/535/595/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.29% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.545 vs policy min 0.30 · **Close:** 460 · **ATR14:** 51.4 · **Volume ratio 20D:** 2.73 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 442–472, entry trigger **472**, stop **434**, risk 38 points (8.05%).

**Targets:** TP1 **510** (1.00R), TP2 **665** (5.08R), TP3 **685** (5.61R). Recommended base-case RR: **5.08R**.

**Why entry:** Hybrid entry uses close 460 and ATR14 51.4: buy zone 442–472. Entry is valid only if price can trade/hold around 472 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 665 (5.08R), TP3 685 (5.61R). Targets are ATR/structure capped for hold_days=5. ATR14=51.4, resistance_5/10/20/60=665/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.540 vs policy min 0.30 · **Close:** 710 · **ATR14:** 220.4 · **Volume ratio 20D:** 4.45 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 630–755, entry trigger **755**, stop **690**, risk 65 points (8.61%).

**Targets:** TP1 **870** (1.77R), TP2 **1,525** (11.85R), TP3 **1,560** (12.38R). Recommended base-case RR: **11.85R**.

**Why entry:** Hybrid entry uses close 710 and ATR14 220.4: buy zone 630–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.77R), TP2 1,525 (11.85R), TP3 1,560 (12.38R). Targets are ATR/structure capped for hold_days=5. ATR14=220.4, resistance_5/10/20/60=1,525/1,895/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.61% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.540 vs policy min 0.30 · **Close:** 202 · **ATR14:** 24.7 · **Volume ratio 20D:** 1.42 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 193–208, entry trigger **208**, stop **191**, risk 17 points (8.17%).

**Targets:** TP1 **262** (3.18R), TP2 **272** (3.76R), TP3 **282** (4.35R). Recommended base-case RR: **3.76R**.

**Why entry:** Hybrid entry uses close 202 and ATR14 24.7: buy zone 193–208. Entry is valid only if price can trade/hold around 208 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 191 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 262 (3.18R), TP2 272 (3.76R), TP3 282 (4.35R). Targets are ATR/structure capped for hold_days=5. ATR14=24.7, resistance_5/10/20/60=262/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.17% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.519 vs policy min 0.30 · **Close:** 815 · **ATR14:** 108.6 · **Volume ratio 20D:** 1.12 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 775–840, entry trigger **840**, stop **770**, risk 70 points (8.33%).

**Targets:** TP1 **910** (1.00R), TP2 **1,175** (4.79R), TP3 **1,210** (5.29R). Recommended base-case RR: **4.79R**.

**Why entry:** Hybrid entry uses close 815 and ATR14 108.6: buy zone 775–840. Entry is valid only if price can trade/hold around 840 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 770 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 910 (1.00R), TP2 1,175 (4.79R), TP3 1,210 (5.29R). Targets are ATR/structure capped for hold_days=3. ATR14=108.6, resistance_5/10/20/60=1,175/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — swing_continual_defensive — NO_TRADE

**Score:** 0.519 vs policy min 0.30 · **Close:** 815 · **ATR14:** 108.6 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 775–840, entry trigger **840**, stop **770**, risk 70 points (8.33%).

**Targets:** TP1 **910** (1.00R), TP2 **960** (1.71R), TP3 **1,010** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 815 and ATR14 108.6: buy zone 775–840. Entry is valid only if price can trade/hold around 840 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 770 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 910 (1.00R), TP2 960 (1.71R), TP3 1,010 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=108.6, resistance_5/10/20/60=1,175/1,175/1,390/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.507 vs policy min 0.30 · **Close:** 460 · **ATR14:** 51.4 · **Volume ratio 20D:** 2.73 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 442–472, entry trigger **472**, stop **434**, risk 38 points (8.05%).

**Targets:** TP1 **510** (1.00R), TP2 **540** (1.79R), TP3 **665** (5.08R). Recommended base-case RR: **1.79R**.

**Why entry:** Hybrid entry uses close 460 and ATR14 51.4: buy zone 442–472. Entry is valid only if price can trade/hold around 472 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 540 (1.79R), TP3 665 (5.08R). Targets are ATR/structure capped for hold_days=3. ATR14=51.4, resistance_5/10/20/60=665/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — swing_continual_defensive — NO_TRADE

**Score:** 0.507 vs policy min 0.30 · **Close:** 460 · **ATR14:** 51.4 · **Volume ratio 20D:** 2.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 442–472, entry trigger **472**, stop **434**, risk 38 points (8.05%).

**Targets:** TP1 **510** (1.00R), TP2 **540** (1.79R), TP3 **565** (2.45R). Recommended base-case RR: **1.79R**.

**Why entry:** Hybrid entry uses close 460 and ATR14 51.4: buy zone 442–472. Entry is valid only if price can trade/hold around 472 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.00R), TP2 540 (1.79R), TP3 565 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=51.4, resistance_5/10/20/60=665/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.442 vs policy min 0.30 · **Close:** 790 · **ATR14:** 101.4 · **Volume ratio 20D:** 0.74 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 750–815, entry trigger **815**, stop **770**, risk 45 points (5.52%).

**Targets:** TP1 **870** (1.22R), TP2 **1,230** (9.22R), TP3 **1,255** (9.78R). Recommended base-case RR: **9.22R**.

**Why entry:** Hybrid entry uses close 790 and ATR14 101.4: buy zone 750–815. Entry is valid only if price can trade/hold around 815 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 770 is placed below support structure (775 / 775). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.22R), TP2 1,230 (9.22R), TP3 1,255 (9.78R). Targets are ATR/structure capped for hold_days=10. ATR14=101.4, resistance_5/10/20/60=1,230/1,230/1,340/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.441 vs policy min 0.30 · **Close:** 710 · **ATR14:** 220.4 · **Volume ratio 20D:** 4.45 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 630–755, entry trigger **755**, stop **690**, risk 65 points (8.61%).

**Targets:** TP1 **870** (1.77R), TP2 **905** (2.31R), TP3 **1,525** (11.85R). Recommended base-case RR: **2.31R**.

**Why entry:** Hybrid entry uses close 710 and ATR14 220.4: buy zone 630–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.77R), TP2 905 (2.31R), TP3 1,525 (11.85R). Targets are ATR/structure capped for hold_days=3. ATR14=220.4, resistance_5/10/20/60=1,525/1,895/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.61% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — NO_TRADE

**Score:** 0.441 vs policy min 0.30 · **Close:** 710 · **ATR14:** 220.4 · **Volume ratio 20D:** 4.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 630–755, entry trigger **755**, stop **690**, risk 65 points (8.61%).

**Targets:** TP1 **870** (1.77R), TP2 **905** (2.31R), TP3 **915** (2.46R). Recommended base-case RR: **2.31R**.

**Why entry:** Hybrid entry uses close 710 and ATR14 220.4: buy zone 630–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.77R), TP2 905 (2.31R), TP3 915 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=220.4, resistance_5/10/20/60=1,525/1,895/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.61% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KOKA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.435 vs policy min 0.30 · **Close:** 121 · **ATR14:** 12.9 · **Volume ratio 20D:** 0.96 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 116–124, entry trigger **124**, stop **114**, risk 10 points (8.06%).

**Targets:** TP1 **134** (1.00R), TP2 **141** (1.70R), TP3 **178** (5.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 12.9: buy zone 116–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 114 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 134 (1.00R), TP2 141 (1.70R), TP3 178 (5.40R). Targets are ATR/structure capped for hold_days=3. ATR14=12.9, resistance_5/10/20/60=178/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.06% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KOKA — swing_continual_defensive — NO_TRADE

**Score:** 0.435 vs policy min 0.30 · **Close:** 121 · **ATR14:** 12.9 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 116–124, entry trigger **124**, stop **114**, risk 10 points (8.06%).

**Targets:** TP1 **134** (1.00R), TP2 **141** (1.70R), TP3 **148** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 12.9: buy zone 116–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 114 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 134 (1.00R), TP2 141 (1.70R), TP3 148 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=12.9, resistance_5/10/20/60=178/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.06% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## NSSS — momentum_20d_continual_research — NO_TRADE

**Score:** 0.428 vs policy min 0.30 · **Close:** 565 · **ATR14:** 81.4 · **Volume ratio 20D:** 0.41 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 535–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **845** (5.20R), TP2 **850** (5.30R), TP3 **875** (5.80R). Recommended base-case RR: **5.30R**.

**Why entry:** Hybrid entry uses close 565 and ATR14 81.4: buy zone 535–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 845 (5.20R), TP2 850 (5.30R), TP3 875 (5.80R). Targets are ATR/structure capped for hold_days=10. ATR14=81.4, resistance_5/10/20/60=850/905/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; volume ratio 0.41 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.427 vs policy min 0.30 · **Close:** 590 · **ATR14:** 121.4 · **Volume ratio 20D:** 1.45 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 545–615, entry trigger **615**, stop **570**, risk 45 points (7.32%).

**Targets:** TP1 **680** (1.44R), TP2 **1,305** (15.33R), TP3 **1,330** (15.89R). Recommended base-case RR: **15.33R**.

**Why entry:** Hybrid entry uses close 590 and ATR14 121.4: buy zone 545–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is placed below support structure (575 / 575). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.44R), TP2 1,305 (15.33R), TP3 1,330 (15.89R). Targets are ATR/structure capped for hold_days=10. ATR14=121.4, resistance_5/10/20/60=1,305/1,340/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.424 vs policy min 0.30 · **Close:** 460 · **ATR14:** 51.4 · **Volume ratio 20D:** 2.73 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 442–472, entry trigger **472**, stop **434**, risk 38 points (8.05%).

**Targets:** TP1 **635** (4.29R), TP2 **665** (5.08R), TP3 **685** (5.61R). Recommended base-case RR: **5.08R**.

**Why entry:** Hybrid entry uses close 460 and ATR14 51.4: buy zone 442–472. Entry is valid only if price can trade/hold around 472 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (4.29R), TP2 665 (5.08R), TP3 685 (5.61R). Targets are ATR/structure capped for hold_days=10. ATR14=51.4, resistance_5/10/20/60=665/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.05% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — momentum_20d_continual_research — NO_TRADE

**Score:** 0.407 vs policy min 0.30 · **Close:** 250 · **ATR14:** 22.3 · **Volume ratio 20D:** 1.31 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 242–256, entry trigger **256**, stop **248**, risk 8 points (3.12%).

**Targets:** TP1 **268** (1.50R), TP2 **372** (14.50R), TP3 **376** (15.00R). Recommended base-case RR: **14.50R**.

**Why entry:** Hybrid entry uses close 250 and ATR14 22.3: buy zone 242–256. Entry is valid only if price can trade/hold around 256 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 248 is placed below support structure (250 / 250). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 268 (1.50R), TP2 372 (14.50R), TP3 376 (15.00R). Targets are ATR/structure capped for hold_days=10. ATR14=22.3, resistance_5/10/20/60=372/394/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SIMP — position_continual — NO_TRADE

**Score:** 0.321 vs policy min 0.30 · **Close:** 560 · **ATR14:** 53.6 · **Volume ratio 20D:** 0.82 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 540–575, entry trigger **575**, stop **525**, risk 50 points (8.70%).

**Targets:** TP1 **745** (3.40R), TP2 **755** (3.60R), TP3 **780** (4.10R). Recommended base-case RR: **3.60R**.

**Why entry:** Hybrid entry uses close 560 and ATR14 53.6: buy zone 540–575. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 525 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 745 (3.40R), TP2 755 (3.60R), TP3 780 (4.10R). Targets are ATR/structure capped for hold_days=10. ATR14=53.6, resistance_5/10/20/60=755/855/930/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.70% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NSSS — position_continual — NO_TRADE

**Score:** 0.317 vs policy min 0.30 · **Close:** 565 · **ATR14:** 81.4 · **Volume ratio 20D:** 0.41 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 535–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **845** (5.20R), TP2 **850** (5.30R), TP3 **875** (5.80R). Recommended base-case RR: **5.30R**.

**Why entry:** Hybrid entry uses close 565 and ATR14 81.4: buy zone 535–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 845 (5.20R), TP2 850 (5.30R), TP3 875 (5.80R). Targets are ATR/structure capped for hold_days=10. ATR14=81.4, resistance_5/10/20/60=850/905/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; volume ratio 0.41 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — NO_TRADE

**Score:** 0.315 vs policy min 0.30 · **Close:** 710 · **ATR14:** 220.4 · **Volume ratio 20D:** 4.45 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 630–755, entry trigger **755**, stop **690**, risk 65 points (8.61%).

**Targets:** TP1 **870** (1.77R), TP2 **1,525** (11.85R), TP3 **1,560** (12.38R). Recommended base-case RR: **11.85R**.

**Why entry:** Hybrid entry uses close 710 and ATR14 220.4: buy zone 630–755. Entry is valid only if price can trade/hold around 755 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 690 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.77R), TP2 1,525 (11.85R), TP3 1,560 (12.38R). Targets are ATR/structure capped for hold_days=10. ATR14=220.4, resistance_5/10/20/60=1,525/1,895/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.61% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — position_continual — NO_TRADE

**Score:** 0.311 vs policy min 0.30 · **Close:** 460 · **ATR14:** 51.4 · **Volume ratio 20D:** 2.73 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 442–472, entry trigger **472**, stop **434**, risk 38 points (8.05%).

**Targets:** TP1 **635** (4.29R), TP2 **665** (5.08R), TP3 **685** (5.61R). Recommended base-case RR: **5.08R**.

**Why entry:** Hybrid entry uses close 460 and ATR14 51.4: buy zone 442–472. Entry is valid only if price can trade/hold around 472 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 635 (4.29R), TP2 665 (5.08R), TP3 685 (5.61R). Targets are ATR/structure capped for hold_days=10. ATR14=51.4, resistance_5/10/20/60=665/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KOKA — position_continual — NO_TRADE

**Score:** 0.297 vs policy min 0.30 · **Close:** 121 · **ATR14:** 12.9 · **Volume ratio 20D:** 0.96 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 116–124, entry trigger **124**, stop **114**, risk 10 points (8.06%).

**Targets:** TP1 **134** (1.00R), TP2 **178** (5.40R), TP3 **183** (5.90R). Recommended base-case RR: **5.40R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 12.9: buy zone 116–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 114 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 134 (1.00R), TP2 178 (5.40R), TP3 183 (5.90R). Targets are ATR/structure capped for hold_days=10. ATR14=12.9, resistance_5/10/20/60=178/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.06% exceeds max strategy risk 8.00%; score 0.297 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
