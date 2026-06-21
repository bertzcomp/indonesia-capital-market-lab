# Numeric Trading Desk Report — 2026-05-25

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 3 |
| CONDITIONAL | 10 |
| NO_TRADE | 29 |

## SSMS — scalping_continual_defensive — ACTIONABLE

**Score:** 0.743 vs policy min 0.05 · **Close:** 775 · **ATR14:** 85.0 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 745–795, entry trigger **795**, stop **765**, risk 30 points (3.77%).

**Targets:** TP1 **840** (1.50R), TP2 **850** (1.83R), TP3 **870** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 775 and ATR14 85.0: buy zone 745–795. Entry is valid only if price can trade/hold around 795 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 is placed below support structure (770 / 770). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 840 (1.50R), TP2 850 (1.83R), TP3 870 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=85.0, resistance_5/10/20/60=1,105/1,445/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.537 vs policy min 0.30 · **Close:** 775 · **ATR14:** 85.0 · **Volume ratio 20D:** 1.88 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 745–795, entry trigger **795**, stop **765**, risk 30 points (3.77%).

**Targets:** TP1 **840** (1.50R), TP2 **1,065** (9.00R), TP3 **1,105** (10.33R). Recommended base-case RR: **9.00R**.

**Why entry:** Hybrid entry uses close 775 and ATR14 85.0: buy zone 745–795. Entry is valid only if price can trade/hold around 795 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 is placed below support structure (770 / 770). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 840 (1.50R), TP2 1,065 (9.00R), TP3 1,105 (10.33R). Targets are ATR/structure capped for hold_days=3. ATR14=85.0, resistance_5/10/20/60=1,105/1,445/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SSMS — swing_continual_defensive — ACTIONABLE

**Score:** 0.537 vs policy min 0.30 · **Close:** 775 · **ATR14:** 85.0 · **Volume ratio 20D:** 1.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 745–795, entry trigger **795**, stop **765**, risk 30 points (3.77%).

**Targets:** TP1 **840** (1.50R), TP2 **850** (1.83R), TP3 **870** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 775 and ATR14 85.0: buy zone 745–795. Entry is valid only if price can trade/hold around 795 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 765 is placed below support structure (770 / 770). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 840 (1.50R), TP2 850 (1.83R), TP3 870 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=85.0, resistance_5/10/20/60=1,105/1,445/1,470/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ASPR — ara_candidate_continual — CONDITIONAL

**Score:** 0.869 vs policy min 0.50 · **Close:** 246 · **ATR14:** 66.9 · **Volume ratio 20D:** 0.05 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 222–260, entry trigger **260**, stop **244**, risk 16 points (6.15%).

**Targets:** TP1 **294** (2.12R), TP2 **302** (2.62R), TP3 **310** (3.12R). Recommended base-case RR: **2.62R**.

**Why entry:** Hybrid entry uses close 246 and ATR14 66.9: buy zone 222–260. Entry is valid only if price can trade/hold around 260 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 244 is placed below support structure (246 / 180). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 294 (2.12R), TP2 302 (2.62R), TP3 310 (3.12R). Targets are ATR/structure capped for hold_days=1. ATR14=66.9, resistance_5/10/20/60=540/540/540/540. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.05 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MSIN — scalping_continual_defensive — CONDITIONAL

**Score:** 0.744 vs policy min 0.05 · **Close:** 494 · **ATR14:** 79.4 · **Volume ratio 20D:** 1.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 466–510, entry trigger **510**, stop **474**, risk 36 points (7.06%).

**Targets:** TP1 **550** (1.11R), TP2 **655** (4.03R), TP3 **680** (4.72R). Recommended base-case RR: **4.03R**.

**Why entry:** Hybrid entry uses close 494 and ATR14 79.4: buy zone 466–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 474 is placed below support structure (480 / 480). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 550 (1.11R), TP2 655 (4.03R), TP3 680 (4.72R). Targets are ATR/structure capped for hold_days=1. ATR14=79.4, resistance_5/10/20/60=680/835/985/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.542 vs policy min 0.30 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 120–127, entry trigger **127**, stop **118**, risk 9 points (7.09%).

**Targets:** TP1 **136** (1.00R), TP2 **143** (1.78R), TP3 **172** (5.00R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.2: buy zone 120–127. Entry is valid only if price can trade/hold around 127 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 136 (1.00R), TP2 143 (1.78R), TP3 172 (5.00R). Targets are ATR/structure capped for hold_days=3. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — swing_continual_defensive — CONDITIONAL

**Score:** 0.542 vs policy min 0.30 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 120–127, entry trigger **127**, stop **118**, risk 9 points (7.09%).

**Targets:** TP1 **136** (1.00R), TP2 **143** (1.78R), TP3 **149** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.2: buy zone 120–127. Entry is valid only if price can trade/hold around 127 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 136 (1.00R), TP2 143 (1.78R), TP3 149 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.517 vs policy min 0.30 · **Close:** 494 · **ATR14:** 79.4 · **Volume ratio 20D:** 1.26 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 466–510, entry trigger **510**, stop **474**, risk 36 points (7.06%).

**Targets:** TP1 **550** (1.11R), TP2 **680** (4.72R), TP3 **700** (5.28R). Recommended base-case RR: **4.72R**.

**Why entry:** Hybrid entry uses close 494 and ATR14 79.4: buy zone 466–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 474 is placed below support structure (480 / 480). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 550 (1.11R), TP2 680 (4.72R), TP3 700 (5.28R). Targets are ATR/structure capped for hold_days=3. ATR14=79.4, resistance_5/10/20/60=680/835/985/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — swing_continual_defensive — CONDITIONAL

**Score:** 0.517 vs policy min 0.30 · **Close:** 494 · **ATR14:** 79.4 · **Volume ratio 20D:** 1.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 466–510, entry trigger **510**, stop **474**, risk 36 points (7.06%).

**Targets:** TP1 **550** (1.11R), TP2 **655** (4.03R), TP3 **680** (4.72R). Recommended base-case RR: **4.03R**.

**Why entry:** Hybrid entry uses close 494 and ATR14 79.4: buy zone 466–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 474 is placed below support structure (480 / 480). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 550 (1.11R), TP2 655 (4.03R), TP3 680 (4.72R). Targets are ATR/structure capped for hold_days=1. ATR14=79.4, resistance_5/10/20/60=680/835/985/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUMI — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.491 vs policy min 0.30 · **Close:** 171 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.17 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 164–175, entry trigger **175**, stop **161**, risk 14 points (8.00%).

**Targets:** TP1 **212** (2.64R), TP2 **220** (3.21R), TP3 **228** (3.79R). Recommended base-case RR: **3.21R**.

**Why entry:** Hybrid entry uses close 171 and ATR14 17.4: buy zone 164–175. Entry is valid only if price can trade/hold around 175 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 161 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (2.64R), TP2 220 (3.21R), TP3 228 (3.79R). Targets are ATR/structure capped for hold_days=5. ATR14=17.4, resistance_5/10/20/60=212/250/256/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.486 vs policy min 0.30 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 120–127, entry trigger **127**, stop **118**, risk 9 points (7.09%).

**Targets:** TP1 **136** (1.00R), TP2 **169** (4.67R), TP3 **172** (5.00R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.2: buy zone 120–127. Entry is valid only if price can trade/hold around 127 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 136 (1.00R), TP2 169 (4.67R), TP3 172 (5.00R). Targets are ATR/structure capped for hold_days=5. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — position_continual — CONDITIONAL

**Score:** 0.347 vs policy min 0.30 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 120–127, entry trigger **127**, stop **118**, risk 9 points (7.09%).

**Targets:** TP1 **136** (1.00R), TP2 **172** (5.00R), TP3 **177** (5.56R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.2: buy zone 120–127. Entry is valid only if price can trade/hold around 127 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 136 (1.00R), TP2 172 (5.00R), TP3 177 (5.56R). Targets are ATR/structure capped for hold_days=10. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUMI — position_continual — CONDITIONAL

**Score:** 0.314 vs policy min 0.30 · **Close:** 171 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.17 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 164–175, entry trigger **175**, stop **161**, risk 14 points (8.00%).

**Targets:** TP1 **212** (2.64R), TP2 **220** (3.21R), TP3 **228** (3.79R). Recommended base-case RR: **3.21R**.

**Why entry:** Hybrid entry uses close 171 and ATR14 17.4: buy zone 164–175. Entry is valid only if price can trade/hold around 175 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 161 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (2.64R), TP2 220 (3.21R), TP3 228 (3.79R). Targets are ATR/structure capped for hold_days=10. ATR14=17.4, resistance_5/10/20/60=212/250/256/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — scalping_continual_defensive — NO_TRADE

**Score:** 0.771 vs policy min 0.05 · **Close:** 480 · **ATR14:** 167.1 · **Volume ratio 20D:** 3.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 420–515, entry trigger **515**, stop **472**, risk 43 points (8.35%).

**Targets:** TP1 **600** (1.98R), TP2 **625** (2.56R), TP3 **860** (8.02R). Recommended base-case RR: **2.56R**.

**Why entry:** Hybrid entry uses close 480 and ATR14 167.1: buy zone 420–515. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 472 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 600 (1.98R), TP2 625 (2.56R), TP3 860 (8.02R). Targets are ATR/structure capped for hold_days=1. ATR14=167.1, resistance_5/10/20/60=860/1,700/3,360/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.35% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — scalping_continual_defensive — NO_TRADE

**Score:** 0.755 vs policy min 0.05 · **Close:** 486 · **ATR14:** 114.9 · **Volume ratio 20D:** 1.24 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 444–510, entry trigger **510**, stop **468**, risk 42 points (8.24%).

**Targets:** TP1 **570** (1.43R), TP2 **585** (1.79R), TP3 **775** (6.31R). Recommended base-case RR: **1.79R**.

**Why entry:** Hybrid entry uses close 486 and ATR14 114.9: buy zone 444–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 468 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 570 (1.43R), TP2 585 (1.79R), TP3 775 (6.31R). Targets are ATR/structure capped for hold_days=1. ATR14=114.9, resistance_5/10/20/60=775/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.24% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — scalping_continual_defensive — NO_TRADE

**Score:** 0.754 vs policy min 0.05 · **Close:** 284 · **ATR14:** 59.9 · **Volume ratio 20D:** 17.90 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 262–296, entry trigger **296**, stop **272**, risk 24 points (8.11%).

**Targets:** TP1 **326** (1.25R), TP2 **338** (1.75R), TP3 **430** (5.58R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 284 and ATR14 59.9: buy zone 262–296. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 326 (1.25R), TP2 338 (1.75R), TP3 430 (5.58R). Targets are ATR/structure capped for hold_days=1. ATR14=59.9, resistance_5/10/20/60=430/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.616 vs policy min 0.30 · **Close:** 486 · **ATR14:** 114.9 · **Volume ratio 20D:** 1.24 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 444–510, entry trigger **510**, stop **468**, risk 42 points (8.24%).

**Targets:** TP1 **570** (1.43R), TP2 **775** (6.31R), TP3 **800** (6.90R). Recommended base-case RR: **6.31R**.

**Why entry:** Hybrid entry uses close 486 and ATR14 114.9: buy zone 444–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 468 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 570 (1.43R), TP2 775 (6.31R), TP3 800 (6.90R). Targets are ATR/structure capped for hold_days=3. ATR14=114.9, resistance_5/10/20/60=775/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.24% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — swing_continual_defensive — NO_TRADE

**Score:** 0.616 vs policy min 0.30 · **Close:** 486 · **ATR14:** 114.9 · **Volume ratio 20D:** 1.24 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 444–510, entry trigger **510**, stop **468**, risk 42 points (8.24%).

**Targets:** TP1 **570** (1.43R), TP2 **585** (1.79R), TP3 **775** (6.31R). Recommended base-case RR: **1.79R**.

**Why entry:** Hybrid entry uses close 486 and ATR14 114.9: buy zone 444–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 468 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 570 (1.43R), TP2 585 (1.79R), TP3 775 (6.31R). Targets are ATR/structure capped for hold_days=1. ATR14=114.9, resistance_5/10/20/60=775/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.24% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.590 vs policy min 0.30 · **Close:** 480 · **ATR14:** 167.1 · **Volume ratio 20D:** 3.38 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 420–515, entry trigger **515**, stop **472**, risk 43 points (8.35%).

**Targets:** TP1 **600** (1.98R), TP2 **860** (8.02R), TP3 **885** (8.60R). Recommended base-case RR: **8.02R**.

**Why entry:** Hybrid entry uses close 480 and ATR14 167.1: buy zone 420–515. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 472 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 600 (1.98R), TP2 860 (8.02R), TP3 885 (8.60R). Targets are ATR/structure capped for hold_days=3. ATR14=167.1, resistance_5/10/20/60=860/1,700/3,360/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.35% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — NO_TRADE

**Score:** 0.590 vs policy min 0.30 · **Close:** 480 · **ATR14:** 167.1 · **Volume ratio 20D:** 3.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 420–515, entry trigger **515**, stop **472**, risk 43 points (8.35%).

**Targets:** TP1 **600** (1.98R), TP2 **625** (2.56R), TP3 **860** (8.02R). Recommended base-case RR: **2.56R**.

**Why entry:** Hybrid entry uses close 480 and ATR14 167.1: buy zone 420–515. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 472 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 600 (1.98R), TP2 625 (2.56R), TP3 860 (8.02R). Targets are ATR/structure capped for hold_days=1. ATR14=167.1, resistance_5/10/20/60=860/1,700/3,360/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.35% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.584 vs policy min 0.30 · **Close:** 284 · **ATR14:** 59.9 · **Volume ratio 20D:** 17.90 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 262–296, entry trigger **296**, stop **272**, risk 24 points (8.11%).

**Targets:** TP1 **326** (1.25R), TP2 **430** (5.58R), TP3 **442** (6.08R). Recommended base-case RR: **5.58R**.

**Why entry:** Hybrid entry uses close 284 and ATR14 59.9: buy zone 262–296. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 326 (1.25R), TP2 430 (5.58R), TP3 442 (6.08R). Targets are ATR/structure capped for hold_days=3. ATR14=59.9, resistance_5/10/20/60=430/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — swing_continual_defensive — NO_TRADE

**Score:** 0.584 vs policy min 0.30 · **Close:** 284 · **ATR14:** 59.9 · **Volume ratio 20D:** 17.90 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 262–296, entry trigger **296**, stop **272**, risk 24 points (8.11%).

**Targets:** TP1 **326** (1.25R), TP2 **338** (1.75R), TP3 **430** (5.58R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 284 and ATR14 59.9: buy zone 262–296. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 326 (1.25R), TP2 338 (1.75R), TP3 430 (5.58R). Targets are ATR/structure capped for hold_days=1. ATR14=59.9, resistance_5/10/20/60=430/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.555 vs policy min 0.30 · **Close:** 695 · **ATR14:** 105.7 · **Volume ratio 20D:** 0.83 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **660**, risk 60 points (8.33%).

**Targets:** TP1 **780** (1.00R), TP2 **1,010** (4.83R), TP3 **1,040** (5.33R). Recommended base-case RR: **4.83R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 105.7: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 660 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 780 (1.00R), TP2 1,010 (4.83R), TP3 1,040 (5.33R). Targets are ATR/structure capped for hold_days=3. ATR14=105.7, resistance_5/10/20/60=1,010/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — swing_continual_defensive — NO_TRADE

**Score:** 0.555 vs policy min 0.30 · **Close:** 695 · **ATR14:** 105.7 · **Volume ratio 20D:** 0.83 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **660**, risk 60 points (8.33%).

**Targets:** TP1 **780** (1.00R), TP2 **825** (1.75R), TP3 **985** (4.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 105.7: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 660 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 780 (1.00R), TP2 825 (1.75R), TP3 985 (4.42R). Targets are ATR/structure capped for hold_days=1. ATR14=105.7, resistance_5/10/20/60=1,010/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.534 vs policy min 0.30 · **Close:** 480 · **ATR14:** 167.1 · **Volume ratio 20D:** 3.38 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 420–515, entry trigger **515**, stop **472**, risk 43 points (8.35%).

**Targets:** TP1 **860** (8.02R), TP2 **885** (8.60R), TP3 **910** (9.19R). Recommended base-case RR: **8.60R**.

**Why entry:** Hybrid entry uses close 480 and ATR14 167.1: buy zone 420–515. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 472 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 860 (8.02R), TP2 885 (8.60R), TP3 910 (9.19R). Targets are ATR/structure capped for hold_days=5. ATR14=167.1, resistance_5/10/20/60=860/1,700/3,360/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.35% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.532 vs policy min 0.30 · **Close:** 486 · **ATR14:** 114.9 · **Volume ratio 20D:** 1.24 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 444–510, entry trigger **510**, stop **468**, risk 42 points (8.24%).

**Targets:** TP1 **770** (6.19R), TP2 **775** (6.31R), TP3 **800** (6.90R). Recommended base-case RR: **6.31R**.

**Why entry:** Hybrid entry uses close 486 and ATR14 114.9: buy zone 444–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 468 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 770 (6.19R), TP2 775 (6.31R), TP3 800 (6.90R). Targets are ATR/structure capped for hold_days=5. ATR14=114.9, resistance_5/10/20/60=775/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.24% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.508 vs policy min 0.30 · **Close:** 350 · **ATR14:** 41.0 · **Volume ratio 20D:** 0.98 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 334–360, entry trigger **360**, stop **330**, risk 30 points (8.33%).

**Targets:** TP1 **450** (3.00R), TP2 **466** (3.53R), TP3 **482** (4.07R). Recommended base-case RR: **3.53R**.

**Why entry:** Hybrid entry uses close 350 and ATR14 41.0: buy zone 334–360. Entry is valid only if price can trade/hold around 360 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 330 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 450 (3.00R), TP2 466 (3.53R), TP3 482 (4.07R). Targets are ATR/structure capped for hold_days=5. ATR14=41.0, resistance_5/10/20/60=450/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.505 vs policy min 0.30 · **Close:** 735 · **ATR14:** 107.9 · **Volume ratio 20D:** 1.01 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 695–760, entry trigger **760**, stop **695**, risk 65 points (8.55%).

**Targets:** TP1 **940** (2.77R), TP2 **975** (3.31R), TP3 **1,010** (3.85R). Recommended base-case RR: **3.31R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 107.9: buy zone 695–760. Entry is valid only if price can trade/hold around 760 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 695 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 940 (2.77R), TP2 975 (3.31R), TP3 1,010 (3.85R). Targets are ATR/structure capped for hold_days=5. ATR14=107.9, resistance_5/10/20/60=940/1,230/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.484 vs policy min 0.30 · **Close:** 131 · **ATR14:** 20.4 · **Volume ratio 20D:** 0.61 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 123–136, entry trigger **136**, stop **125**, risk 11 points (8.09%).

**Targets:** TP1 **174** (3.45R), TP2 **180** (4.00R), TP3 **186** (4.55R). Recommended base-case RR: **4.00R**.

**Why entry:** Hybrid entry uses close 131 and ATR14 20.4: buy zone 123–136. Entry is valid only if price can trade/hold around 136 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 174 (3.45R), TP2 180 (4.00R), TP3 186 (4.55R). Targets are ATR/structure capped for hold_days=5. ATR14=20.4, resistance_5/10/20/60=174/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.403 vs policy min 0.30 · **Close:** 480 · **ATR14:** 167.1 · **Volume ratio 20D:** 3.38 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 420–515, entry trigger **515**, stop **472**, risk 43 points (8.35%).

**Targets:** TP1 **860** (8.02R), TP2 **885** (8.60R), TP3 **910** (9.19R). Recommended base-case RR: **8.60R**.

**Why entry:** Hybrid entry uses close 480 and ATR14 167.1: buy zone 420–515. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 472 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 860 (8.02R), TP2 885 (8.60R), TP3 910 (9.19R). Targets are ATR/structure capped for hold_days=10. ATR14=167.1, resistance_5/10/20/60=860/1,700/3,360/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.35% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.389 vs policy min 0.30 · **Close:** 486 · **ATR14:** 114.9 · **Volume ratio 20D:** 1.24 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 444–510, entry trigger **510**, stop **468**, risk 42 points (8.24%).

**Targets:** TP1 **775** (6.31R), TP2 **800** (6.90R), TP3 **825** (7.50R). Recommended base-case RR: **6.90R**.

**Why entry:** Hybrid entry uses close 486 and ATR14 114.9: buy zone 444–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 468 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 775 (6.31R), TP2 800 (6.90R), TP3 825 (7.50R). Targets are ATR/structure capped for hold_days=10. ATR14=114.9, resistance_5/10/20/60=775/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.24% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.386 vs policy min 0.30 · **Close:** 695 · **ATR14:** 105.7 · **Volume ratio 20D:** 0.83 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **660**, risk 60 points (8.33%).

**Targets:** TP1 **1,010** (4.83R), TP2 **1,040** (5.33R), TP3 **1,070** (5.83R). Recommended base-case RR: **5.33R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 105.7: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 660 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,010 (4.83R), TP2 1,040 (5.33R), TP3 1,070 (5.83R). Targets are ATR/structure capped for hold_days=10. ATR14=105.7, resistance_5/10/20/60=1,010/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.381 vs policy min 0.30 · **Close:** 124 · **ATR14:** 10.2 · **Volume ratio 20D:** 1.68 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 120–127, entry trigger **127**, stop **118**, risk 9 points (7.09%).

**Targets:** TP1 **136** (1.00R), TP2 **172** (5.00R), TP3 **177** (5.56R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 10.2: buy zone 120–127. Entry is valid only if price can trade/hold around 127 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 136 (1.00R), TP2 172 (5.00R), TP3 177 (5.56R). Targets are ATR/structure capped for hold_days=10. ATR14=10.2, resistance_5/10/20/60=172/183/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.358 vs policy min 0.30 · **Close:** 735 · **ATR14:** 107.9 · **Volume ratio 20D:** 1.01 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 695–760, entry trigger **760**, stop **695**, risk 65 points (8.55%).

**Targets:** TP1 **940** (2.77R), TP2 **975** (3.31R), TP3 **1,010** (3.85R). Recommended base-case RR: **3.31R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 107.9: buy zone 695–760. Entry is valid only if price can trade/hold around 760 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 695 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 940 (2.77R), TP2 975 (3.31R), TP3 1,010 (3.85R). Targets are ATR/structure capped for hold_days=10. ATR14=107.9, resistance_5/10/20/60=940/1,230/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — position_continual — NO_TRADE

**Score:** 0.328 vs policy min 0.30 · **Close:** 695 · **ATR14:** 105.7 · **Volume ratio 20D:** 0.83 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **660**, risk 60 points (8.33%).

**Targets:** TP1 **1,010** (4.83R), TP2 **1,040** (5.33R), TP3 **1,070** (5.83R). Recommended base-case RR: **5.33R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 105.7: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 660 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,010 (4.83R), TP2 1,040 (5.33R), TP3 1,070 (5.83R). Targets are ATR/structure capped for hold_days=10. ATR14=105.7, resistance_5/10/20/60=1,010/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — NO_TRADE

**Score:** 0.327 vs policy min 0.30 · **Close:** 480 · **ATR14:** 167.1 · **Volume ratio 20D:** 3.38 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 420–515, entry trigger **515**, stop **472**, risk 43 points (8.35%).

**Targets:** TP1 **860** (8.02R), TP2 **885** (8.60R), TP3 **910** (9.19R). Recommended base-case RR: **8.60R**.

**Why entry:** Hybrid entry uses close 480 and ATR14 167.1: buy zone 420–515. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 472 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 860 (8.02R), TP2 885 (8.60R), TP3 910 (9.19R). Targets are ATR/structure capped for hold_days=10. ATR14=167.1, resistance_5/10/20/60=860/1,700/3,360/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.35% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — NO_TRADE

**Score:** 0.326 vs policy min 0.30 · **Close:** 486 · **ATR14:** 114.9 · **Volume ratio 20D:** 1.24 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 444–510, entry trigger **510**, stop **468**, risk 42 points (8.24%).

**Targets:** TP1 **775** (6.31R), TP2 **800** (6.90R), TP3 **825** (7.50R). Recommended base-case RR: **6.90R**.

**Why entry:** Hybrid entry uses close 486 and ATR14 114.9: buy zone 444–510. Entry is valid only if price can trade/hold around 510 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 468 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 775 (6.31R), TP2 800 (6.90R), TP3 825 (7.50R). Targets are ATR/structure capped for hold_days=10. ATR14=114.9, resistance_5/10/20/60=775/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.24% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — position_continual — NO_TRADE

**Score:** 0.325 vs policy min 0.30 · **Close:** 284 · **ATR14:** 59.9 · **Volume ratio 20D:** 17.90 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 262–296, entry trigger **296**, stop **272**, risk 24 points (8.11%).

**Targets:** TP1 **430** (5.58R), TP2 **442** (6.08R), TP3 **454** (6.58R). Recommended base-case RR: **6.08R**.

**Why entry:** Hybrid entry uses close 284 and ATR14 59.9: buy zone 262–296. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 430 (5.58R), TP2 442 (6.08R), TP3 454 (6.58R). Targets are ATR/structure capped for hold_days=10. ATR14=59.9, resistance_5/10/20/60=430/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — NO_TRADE

**Score:** 0.324 vs policy min 0.30 · **Close:** 131 · **ATR14:** 20.4 · **Volume ratio 20D:** 0.61 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 123–136, entry trigger **136**, stop **125**, risk 11 points (8.09%).

**Targets:** TP1 **174** (3.45R), TP2 **180** (4.00R), TP3 **186** (4.55R). Recommended base-case RR: **4.00R**.

**Why entry:** Hybrid entry uses close 131 and ATR14 20.4: buy zone 123–136. Entry is valid only if price can trade/hold around 136 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 125 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 174 (3.45R), TP2 180 (4.00R), TP3 186 (4.55R). Targets are ATR/structure capped for hold_days=10. ATR14=20.4, resistance_5/10/20/60=174/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — NO_TRADE

**Score:** 0.322 vs policy min 0.30 · **Close:** 350 · **ATR14:** 41.0 · **Volume ratio 20D:** 0.98 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 334–360, entry trigger **360**, stop **330**, risk 30 points (8.33%).

**Targets:** TP1 **450** (3.00R), TP2 **466** (3.53R), TP3 **482** (4.07R). Recommended base-case RR: **3.53R**.

**Why entry:** Hybrid entry uses close 350 and ATR14 41.0: buy zone 334–360. Entry is valid only if price can trade/hold around 360 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 330 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 450 (3.00R), TP2 466 (3.53R), TP3 482 (4.07R). Targets are ATR/structure capped for hold_days=10. ATR14=41.0, resistance_5/10/20/60=450/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — position_continual — NO_TRADE

**Score:** 0.321 vs policy min 0.30 · **Close:** 735 · **ATR14:** 107.9 · **Volume ratio 20D:** 1.01 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 695–760, entry trigger **760**, stop **695**, risk 65 points (8.55%).

**Targets:** TP1 **940** (2.77R), TP2 **975** (3.31R), TP3 **1,010** (3.85R). Recommended base-case RR: **3.31R**.

**Why entry:** Hybrid entry uses close 735 and ATR14 107.9: buy zone 695–760. Entry is valid only if price can trade/hold around 760 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 695 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 940 (2.77R), TP2 975 (3.31R), TP3 1,010 (3.85R). Targets are ATR/structure capped for hold_days=10. ATR14=107.9, resistance_5/10/20/60=940/1,230/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## NSSS — position_continual — NO_TRADE

**Score:** 0.314 vs policy min 0.30 · **Close:** 490 · **ATR14:** 72.6 · **Volume ratio 20D:** 0.46 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 464–505, entry trigger **505**, stop **464**, risk 41 points (8.12%).

**Targets:** TP1 **700** (4.76R), TP2 **725** (5.37R), TP3 **750** (5.98R). Recommended base-case RR: **5.37R**.

**Why entry:** Hybrid entry uses close 490 and ATR14 72.6: buy zone 464–505. Entry is valid only if price can trade/hold around 505 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 464 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 700 (4.76R), TP2 725 (5.37R), TP3 750 (5.98R). Targets are ATR/structure capped for hold_days=10. ATR14=72.6, resistance_5/10/20/60=700/850/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.12% exceeds max strategy risk 8.00%; volume ratio 0.46 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---
