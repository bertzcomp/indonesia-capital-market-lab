# Numeric Trading Desk Report — 2026-06-09

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| CONDITIONAL | 18 |
| WATCHLIST_ONLY | 1 |
| NO_TRADE | 23 |

## MPMX — ara_candidate_continual — CONDITIONAL

**Score:** 0.892 vs policy min 0.50 · **Close:** 915 · **ATR14:** 41.4 · **Volume ratio 20D:** 2.15 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 900–925, entry trigger **925**, stop **905**, risk 20 points (2.16%).

**Targets:** TP1 **950** (1.25R), TP2 **960** (1.75R), TP3 **975** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 915 and ATR14 41.4: buy zone 900–925. Entry is valid only if price can trade/hold around 925 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 905 is placed below support structure (910 / 910). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 950 (1.25R), TP2 960 (1.75R), TP3 975 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=41.4, resistance_5/10/20/60=1,135/1,150/1,150/1,150. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GPSO — scalping_continual_defensive — CONDITIONAL

**Score:** 0.739 vs policy min 0.05 · **Close:** 320 · **ATR14:** 29.6 · **Volume ratio 20D:** 0.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 308–326, entry trigger **326**, stop **302**, risk 24 points (7.36%).

**Targets:** TP1 **350** (1.00R), TP2 **368** (1.75R), TP3 **384** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 320 and ATR14 29.6: buy zone 308–326. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 302 is placed below support structure (304 / 304). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 350 (1.00R), TP2 368 (1.75R), TP3 384 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=29.6, resistance_5/10/20/60=520/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UVCR — scalping_continual_defensive — CONDITIONAL

**Score:** 0.703 vs policy min 0.05 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 126–137, entry trigger **137**, stop **128**, risk 9 points (6.57%).

**Targets:** TP1 **146** (1.00R), TP2 **153** (1.78R), TP3 **159** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 133 and ATR14 17.9: buy zone 126–137. Entry is valid only if price can trade/hold around 137 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 128 is placed below support structure (129 / 129). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 146 (1.00R), TP2 153 (1.78R), TP3 159 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DPUM — scalping_continual_defensive — CONDITIONAL

**Score:** 0.701 vs policy min 0.05 · **Close:** 128 · **ATR14:** 18.7 · **Volume ratio 20D:** 0.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 121–132, entry trigger **132**, stop **127**, risk 5 points (3.79%).

**Targets:** TP1 **142** (2.00R), TP2 **145** (2.60R), TP3 **148** (3.20R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 18.7: buy zone 121–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 127 is placed below support structure (128 / 116). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 142 (2.00R), TP2 145 (2.60R), TP3 148 (3.20R). Targets are ATR/structure capped for hold_days=1. ATR14=18.7, resistance_5/10/20/60=200/216/236/236. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MPMX — scalping_continual_defensive — CONDITIONAL

**Score:** 0.524 vs policy min 0.05 · **Close:** 915 · **ATR14:** 41.4 · **Volume ratio 20D:** 2.15 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 900–925, entry trigger **925**, stop **905**, risk 20 points (2.16%).

**Targets:** TP1 **950** (1.25R), TP2 **960** (1.75R), TP3 **975** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 915 and ATR14 41.4: buy zone 900–925. Entry is valid only if price can trade/hold around 925 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 905 is placed below support structure (910 / 910). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 950 (1.25R), TP2 960 (1.75R), TP3 975 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=41.4, resistance_5/10/20/60=1,135/1,150/1,150/1,150. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DPUM — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.494 vs policy min 0.30 · **Close:** 128 · **ATR14:** 18.7 · **Volume ratio 20D:** 0.54 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 121–132, entry trigger **132**, stop **127**, risk 5 points (3.79%).

**Targets:** TP1 **142** (2.00R), TP2 **145** (2.60R), TP3 **200** (13.60R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 18.7: buy zone 121–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 127 is placed below support structure (128 / 116). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 142 (2.00R), TP2 145 (2.60R), TP3 200 (13.60R). Targets are ATR/structure capped for hold_days=3. ATR14=18.7, resistance_5/10/20/60=200/216/236/236. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DPUM — swing_continual_defensive — CONDITIONAL

**Score:** 0.494 vs policy min 0.30 · **Close:** 128 · **ATR14:** 18.7 · **Volume ratio 20D:** 0.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 121–132, entry trigger **132**, stop **127**, risk 5 points (3.79%).

**Targets:** TP1 **142** (2.00R), TP2 **145** (2.60R), TP3 **148** (3.20R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 18.7: buy zone 121–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 127 is placed below support structure (128 / 116). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 142 (2.00R), TP2 145 (2.60R), TP3 148 (3.20R). Targets are ATR/structure capped for hold_days=1. ATR14=18.7, resistance_5/10/20/60=200/216/236/236. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UVCR — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.490 vs policy min 0.30 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 126–137, entry trigger **137**, stop **128**, risk 9 points (6.57%).

**Targets:** TP1 **146** (1.00R), TP2 **153** (1.78R), TP3 **159** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 133 and ATR14 17.9: buy zone 126–137. Entry is valid only if price can trade/hold around 137 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 128 is placed below support structure (129 / 129). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 146 (1.00R), TP2 153 (1.78R), TP3 159 (2.44R). Targets are ATR/structure capped for hold_days=3. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UVCR — swing_continual_defensive — CONDITIONAL

**Score:** 0.490 vs policy min 0.30 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 126–137, entry trigger **137**, stop **128**, risk 9 points (6.57%).

**Targets:** TP1 **146** (1.00R), TP2 **153** (1.78R), TP3 **159** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 133 and ATR14 17.9: buy zone 126–137. Entry is valid only if price can trade/hold around 137 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 128 is placed below support structure (129 / 129). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 146 (1.00R), TP2 153 (1.78R), TP3 159 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GPSO — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.452 vs policy min 0.30 · **Close:** 320 · **ATR14:** 29.6 · **Volume ratio 20D:** 0.54 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 308–326, entry trigger **326**, stop **302**, risk 24 points (7.36%).

**Targets:** TP1 **350** (1.00R), TP2 **368** (1.75R), TP3 **384** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 320 and ATR14 29.6: buy zone 308–326. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 302 is placed below support structure (304 / 304). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 350 (1.00R), TP2 368 (1.75R), TP3 384 (2.42R). Targets are ATR/structure capped for hold_days=5. ATR14=29.6, resistance_5/10/20/60=520/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GPSO — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.443 vs policy min 0.30 · **Close:** 320 · **ATR14:** 29.6 · **Volume ratio 20D:** 0.54 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 308–326, entry trigger **326**, stop **302**, risk 24 points (7.36%).

**Targets:** TP1 **350** (1.00R), TP2 **368** (1.75R), TP3 **384** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 320 and ATR14 29.6: buy zone 308–326. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 302 is placed below support structure (304 / 304). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 350 (1.00R), TP2 368 (1.75R), TP3 384 (2.42R). Targets are ATR/structure capped for hold_days=3. ATR14=29.6, resistance_5/10/20/60=520/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GPSO — swing_continual_defensive — CONDITIONAL

**Score:** 0.443 vs policy min 0.30 · **Close:** 320 · **ATR14:** 29.6 · **Volume ratio 20D:** 0.54 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 308–326, entry trigger **326**, stop **302**, risk 24 points (7.36%).

**Targets:** TP1 **350** (1.00R), TP2 **368** (1.75R), TP3 **384** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 320 and ATR14 29.6: buy zone 308–326. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 302 is placed below support structure (304 / 304). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 350 (1.00R), TP2 368 (1.75R), TP3 384 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=29.6, resistance_5/10/20/60=520/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.54 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UVCR — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.426 vs policy min 0.30 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 126–137, entry trigger **137**, stop **128**, risk 9 points (6.57%).

**Targets:** TP1 **146** (1.00R), TP2 **153** (1.78R), TP3 **238** (11.22R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 133 and ATR14 17.9: buy zone 126–137. Entry is valid only if price can trade/hold around 137 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 128 is placed below support structure (129 / 129). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 146 (1.00R), TP2 153 (1.78R), TP3 238 (11.22R). Targets are ATR/structure capped for hold_days=5. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.415 vs policy min 0.30 · **Close:** 240 · **ATR14:** 43.0 · **Volume ratio 20D:** 0.88 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 224–250, entry trigger **250**, stop **230**, risk 20 points (8.00%).

**Targets:** TP1 **272** (1.10R), TP2 **354** (5.20R), TP3 **364** (5.70R). Recommended base-case RR: **5.20R**.

**Why entry:** Hybrid entry uses close 240 and ATR14 43.0: buy zone 224–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 230 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 272 (1.10R), TP2 354 (5.20R), TP3 364 (5.70R). Targets are ATR/structure capped for hold_days=3. ATR14=43.0, resistance_5/10/20/60=354/408/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.10R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## OASA — swing_continual_defensive — CONDITIONAL

**Score:** 0.415 vs policy min 0.30 · **Close:** 240 · **ATR14:** 43.0 · **Volume ratio 20D:** 0.88 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–250, entry trigger **250**, stop **230**, risk 20 points (8.00%).

**Targets:** TP1 **272** (1.10R), TP2 **284** (1.70R), TP3 **354** (5.20R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 240 and ATR14 43.0: buy zone 224–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 230 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 272 (1.10R), TP2 284 (1.70R), TP3 354 (5.20R). Targets are ATR/structure capped for hold_days=1. ATR14=43.0, resistance_5/10/20/60=354/408/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.10R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.390 vs policy min 0.30 · **Close:** 240 · **ATR14:** 43.0 · **Volume ratio 20D:** 0.88 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 224–250, entry trigger **250**, stop **230**, risk 20 points (8.00%).

**Targets:** TP1 **348** (4.90R), TP2 **354** (5.20R), TP3 **364** (5.70R). Recommended base-case RR: **5.20R**.

**Why entry:** Hybrid entry uses close 240 and ATR14 43.0: buy zone 224–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 230 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 348 (4.90R), TP2 354 (5.20R), TP3 364 (5.70R). Targets are ATR/structure capped for hold_days=5. ATR14=43.0, resistance_5/10/20/60=354/408/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## UVCR — position_continual — CONDITIONAL

**Score:** 0.318 vs policy min 0.30 · **Close:** 133 · **ATR14:** 17.9 · **Volume ratio 20D:** 2.51 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 126–137, entry trigger **137**, stop **128**, risk 9 points (6.57%).

**Targets:** TP1 **146** (1.00R), TP2 **240** (11.44R), TP3 **242** (11.67R). Recommended base-case RR: **11.44R**.

**Why entry:** Hybrid entry uses close 133 and ATR14 17.9: buy zone 126–137. Entry is valid only if price can trade/hold around 137 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 128 is placed below support structure (129 / 129). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 146 (1.00R), TP2 240 (11.44R), TP3 242 (11.67R). Targets are ATR/structure capped for hold_days=10. ATR14=17.9, resistance_5/10/20/60=242/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — position_continual — CONDITIONAL

**Score:** 0.306 vs policy min 0.30 · **Close:** 240 · **ATR14:** 43.0 · **Volume ratio 20D:** 0.88 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 224–250, entry trigger **250**, stop **230**, risk 20 points (8.00%).

**Targets:** TP1 **354** (5.20R), TP2 **364** (5.70R), TP3 **374** (6.20R). Recommended base-case RR: **5.70R**.

**Why entry:** Hybrid entry uses close 240 and ATR14 43.0: buy zone 224–250. Entry is valid only if price can trade/hold around 250 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 230 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 354 (5.20R), TP2 364 (5.70R), TP3 374 (6.20R). Targets are ATR/structure capped for hold_days=10. ATR14=43.0, resistance_5/10/20/60=354/408/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DPUM — position_continual — WATCHLIST_ONLY

**Score:** 0.288 vs policy min 0.30 · **Close:** 128 · **ATR14:** 18.7 · **Volume ratio 20D:** 0.54 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 121–132, entry trigger **132**, stop **127**, risk 5 points (3.79%).

**Targets:** TP1 **192** (12.00R), TP2 **200** (13.60R), TP3 **204** (14.40R). Recommended base-case RR: **13.60R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 18.7: buy zone 121–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 127 is placed below support structure (128 / 116). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 192 (12.00R), TP2 200 (13.60R), TP3 204 (14.40R). Targets are ATR/structure capped for hold_days=10. ATR14=18.7, resistance_5/10/20/60=200/216/236/236. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.288 below policy min_score 0.30; volume ratio 0.54 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## FUTR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.481 vs policy min 0.30 · **Close:** 124 · **ATR14:** 25.6 · **Volume ratio 20D:** 1.67 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 115–130, entry trigger **130**, stop **119**, risk 11 points (8.46%).

**Targets:** TP1 **171** (3.73R), TP2 **177** (4.27R), TP3 **183** (4.82R). Recommended base-case RR: **4.27R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 25.6: buy zone 115–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 119 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 171 (3.73R), TP2 177 (4.27R), TP3 183 (4.82R). Targets are ATR/structure capped for hold_days=3. ATR14=25.6, resistance_5/10/20/60=171/191/246/314. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FUTR — swing_continual_defensive — NO_TRADE

**Score:** 0.481 vs policy min 0.30 · **Close:** 124 · **ATR14:** 25.6 · **Volume ratio 20D:** 1.67 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 115–130, entry trigger **130**, stop **119**, risk 11 points (8.46%).

**Targets:** TP1 **143** (1.18R), TP2 **171** (3.73R), TP3 **177** (4.27R). Recommended base-case RR: **3.73R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 25.6: buy zone 115–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 119 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 143 (1.18R), TP2 171 (3.73R), TP3 177 (4.27R). Targets are ATR/structure capped for hold_days=1. ATR14=25.6, resistance_5/10/20/60=171/191/246/314. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%; TP1 reward/risk 1.18R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## APIC — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.454 vs policy min 0.30 · **Close:** 560 · **ATR14:** 210.0 · **Volume ratio 20D:** 0.32 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 486–605, entry trigger **605**, stop **555**, risk 50 points (8.26%).

**Targets:** TP1 **710** (2.10R), TP2 **735** (2.60R), TP3 **760** (3.10R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 560 and ATR14 210.0: buy zone 486–605. Entry is valid only if price can trade/hold around 605 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 710 (2.10R), TP2 735 (2.60R), TP3 760 (3.10R). Targets are ATR/structure capped for hold_days=3. ATR14=210.0, resistance_5/10/20/60=710/1,635/2,090/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.04% > max 8.00%; entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; volume ratio 0.32 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — swing_continual_defensive — NO_TRADE

**Score:** 0.454 vs policy min 0.30 · **Close:** 560 · **ATR14:** 210.0 · **Volume ratio 20D:** 0.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 486–605, entry trigger **605**, stop **555**, risk 50 points (8.26%).

**Targets:** TP1 **710** (2.10R), TP2 **735** (2.60R), TP3 **760** (3.10R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 560 and ATR14 210.0: buy zone 486–605. Entry is valid only if price can trade/hold around 605 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 710 (2.10R), TP2 735 (2.60R), TP3 760 (3.10R). Targets are ATR/structure capped for hold_days=1. ATR14=210.0, resistance_5/10/20/60=710/1,635/2,090/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.04% > max 8.00%; entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; volume ratio 0.32 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ASPR — scalping_continual_defensive — NO_TRADE

**Score:** 0.437 vs policy min 0.05 · **Close:** 175 · **ATR14:** 57.7 · **Volume ratio 20D:** 1.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 154–187, entry trigger **187**, stop **172**, risk 15 points (8.02%).

**Targets:** TP1 **218** (2.07R), TP2 **226** (2.60R), TP3 **234** (3.13R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 175 and ATR14 57.7: buy zone 154–187. Entry is valid only if price can trade/hold around 187 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 172 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 218 (2.07R), TP2 226 (2.60R), TP3 234 (3.13R). Targets are ATR/structure capped for hold_days=1. ATR14=57.7, resistance_5/10/20/60=218/378/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.02% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KJEN — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.436 vs policy min 0.30 · **Close:** 107 · **ATR14:** 26.4 · **Volume ratio 20D:** 0.81 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 97–113, entry trigger **113**, stop **103**, risk 10 points (8.85%).

**Targets:** TP1 **159** (4.60R), TP2 **165** (5.20R), TP3 **170** (5.70R). Recommended base-case RR: **5.20R**.

**Why entry:** Hybrid entry uses close 107 and ATR14 26.4: buy zone 97–113. Entry is valid only if price can trade/hold around 113 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 159 (4.60R), TP2 165 (5.20R), TP3 170 (5.70R). Targets are ATR/structure capped for hold_days=3. ATR14=26.4, resistance_5/10/20/60=165/252/252/252. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.85% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KJEN — swing_continual_defensive — NO_TRADE

**Score:** 0.436 vs policy min 0.30 · **Close:** 107 · **ATR14:** 26.4 · **Volume ratio 20D:** 0.81 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 97–113, entry trigger **113**, stop **103**, risk 10 points (8.85%).

**Targets:** TP1 **127** (1.40R), TP2 **161** (4.80R), TP3 **165** (5.20R). Recommended base-case RR: **4.80R**.

**Why entry:** Hybrid entry uses close 107 and ATR14 26.4: buy zone 97–113. Entry is valid only if price can trade/hold around 113 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 127 (1.40R), TP2 161 (4.80R), TP3 165 (5.20R). Targets are ATR/structure capped for hold_days=1. ATR14=26.4, resistance_5/10/20/60=165/252/252/252. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.85% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FUTR — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.411 vs policy min 0.30 · **Close:** 124 · **ATR14:** 25.6 · **Volume ratio 20D:** 1.67 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 115–130, entry trigger **130**, stop **119**, risk 11 points (8.46%).

**Targets:** TP1 **171** (3.73R), TP2 **177** (4.27R), TP3 **183** (4.82R). Recommended base-case RR: **4.27R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 25.6: buy zone 115–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 119 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 171 (3.73R), TP2 177 (4.27R), TP3 183 (4.82R). Targets are ATR/structure capped for hold_days=5. ATR14=25.6, resistance_5/10/20/60=171/191/246/314. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## PADA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.385 vs policy min 0.30 · **Close:** 105 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.10 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 98–109, entry trigger **109**, stop **100**, risk 9 points (8.26%).

**Targets:** TP1 **142** (3.67R), TP2 **147** (4.22R), TP3 **152** (4.78R). Recommended base-case RR: **4.22R**.

**Why entry:** Hybrid entry uses close 105 and ATR14 17.4: buy zone 98–109. Entry is valid only if price can trade/hold around 109 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 100 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 142 (3.67R), TP2 147 (4.22R), TP3 152 (4.78R). Targets are ATR/structure capped for hold_days=5. ATR14=17.4, resistance_5/10/20/60=142/148/197/218. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GULA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.381 vs policy min 0.30 · **Close:** 560 · **ATR14:** 41.5 · **Volume ratio 20D:** 1.41 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 545–570, entry trigger **570**, stop **520**, risk 50 points (8.77%).

**Targets:** TP1 **620** (1.00R), TP2 **655** (1.70R), TP3 **690** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 560 and ATR14 41.5: buy zone 545–570. Entry is valid only if price can trade/hold around 570 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 520 uses 1.20×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 620 (1.00R), TP2 655 (1.70R), TP3 690 (2.40R). Targets are ATR/structure capped for hold_days=5. ATR14=41.5, resistance_5/10/20/60=570/570/570/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.77% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SOCI — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.380 vs policy min 0.30 · **Close:** 296 · **ATR14:** 40.1 · **Volume ratio 20D:** 0.86 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 280–306, entry trigger **306**, stop **280**, risk 26 points (8.50%).

**Targets:** TP1 **396** (3.46R), TP2 **410** (4.00R), TP3 **424** (4.54R). Recommended base-case RR: **4.00R**.

**Why entry:** Hybrid entry uses close 296 and ATR14 40.1: buy zone 280–306. Entry is valid only if price can trade/hold around 306 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 280 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 396 (3.46R), TP2 410 (4.00R), TP3 424 (4.54R). Targets are ATR/structure capped for hold_days=5. ATR14=40.1, resistance_5/10/20/60=396/416/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.50% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FUTR — momentum_20d_continual_research — NO_TRADE

**Score:** 0.321 vs policy min 0.30 · **Close:** 124 · **ATR14:** 25.6 · **Volume ratio 20D:** 1.67 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 115–130, entry trigger **130**, stop **119**, risk 11 points (8.46%).

**Targets:** TP1 **171** (3.73R), TP2 **177** (4.27R), TP3 **183** (4.82R). Recommended base-case RR: **4.27R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 25.6: buy zone 115–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 119 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 171 (3.73R), TP2 177 (4.27R), TP3 183 (4.82R). Targets are ATR/structure capped for hold_days=10. ATR14=25.6, resistance_5/10/20/60=171/191/246/314. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.46% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## FUTR — position_continual — NO_TRADE

**Score:** 0.312 vs policy min 0.30 · **Close:** 124 · **ATR14:** 25.6 · **Volume ratio 20D:** 1.67 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 115–130, entry trigger **130**, stop **119**, risk 11 points (8.46%).

**Targets:** TP1 **171** (3.73R), TP2 **177** (4.27R), TP3 **183** (4.82R). Recommended base-case RR: **4.27R**.

**Why entry:** Hybrid entry uses close 124 and ATR14 25.6: buy zone 115–130. Entry is valid only if price can trade/hold around 130 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 119 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 171 (3.73R), TP2 177 (4.27R), TP3 183 (4.82R). Targets are ATR/structure capped for hold_days=10. ATR14=25.6, resistance_5/10/20/60=171/191/246/314. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_20d_continual_research — NO_TRADE

**Score:** 0.300 vs policy min 0.30 · **Close:** 306 · **ATR14:** 46.0 · **Volume ratio 20D:** 1.22 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 288–316, entry trigger **316**, stop **290**, risk 26 points (8.23%).

**Targets:** TP1 **388** (2.77R), TP2 **402** (3.31R), TP3 **416** (3.85R). Recommended base-case RR: **3.31R**.

**Why entry:** Hybrid entry uses close 306 and ATR14 46.0: buy zone 288–316. Entry is valid only if price can trade/hold around 316 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 290 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 388 (2.77R), TP2 402 (3.31R), TP3 416 (3.85R). Targets are ATR/structure capped for hold_days=10. ATR14=46.0, resistance_5/10/20/60=388/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.23% exceeds max strategy risk 8.00%; score 0.300 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BIPI — position_continual — NO_TRADE

**Score:** 0.296 vs policy min 0.30 · **Close:** 146 · **ATR14:** 21.9 · **Volume ratio 20D:** 1.19 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 138–151, entry trigger **151**, stop **138**, risk 13 points (8.61%).

**Targets:** TP1 **181** (2.31R), TP2 **188** (2.85R), TP3 **195** (3.38R). Recommended base-case RR: **2.85R**.

**Why entry:** Hybrid entry uses close 146 and ATR14 21.9: buy zone 138–151. Entry is valid only if price can trade/hold around 151 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 138 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 181 (2.31R), TP2 188 (2.85R), TP3 195 (3.38R). Targets are ATR/structure capped for hold_days=10. ATR14=21.9, resistance_5/10/20/60=181/190/262/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.61% exceeds max strategy risk 8.00%; score 0.296 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BULL — position_continual — NO_TRADE

**Score:** 0.295 vs policy min 0.30 · **Close:** 306 · **ATR14:** 46.0 · **Volume ratio 20D:** 1.22 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 288–316, entry trigger **316**, stop **290**, risk 26 points (8.23%).

**Targets:** TP1 **388** (2.77R), TP2 **402** (3.31R), TP3 **416** (3.85R). Recommended base-case RR: **3.31R**.

**Why entry:** Hybrid entry uses close 306 and ATR14 46.0: buy zone 288–316. Entry is valid only if price can trade/hold around 316 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 290 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 388 (2.77R), TP2 402 (3.31R), TP3 416 (3.85R). Targets are ATR/structure capped for hold_days=10. ATR14=46.0, resistance_5/10/20/60=388/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.23% exceeds max strategy risk 8.00%; score 0.295 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## INET — position_continual — NO_TRADE

**Score:** 0.290 vs policy min 0.30 · **Close:** 183 · **ATR14:** 27.1 · **Volume ratio 20D:** 1.66 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 173–189, entry trigger **189**, stop **173**, risk 16 points (8.47%).

**Targets:** TP1 **230** (2.56R), TP2 **238** (3.06R), TP3 **246** (3.56R). Recommended base-case RR: **3.06R**.

**Why entry:** Hybrid entry uses close 183 and ATR14 27.1: buy zone 173–189. Entry is valid only if price can trade/hold around 189 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 173 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 230 (2.56R), TP2 238 (3.06R), TP3 246 (3.56R). Targets are ATR/structure capped for hold_days=10. ATR14=27.1, resistance_5/10/20/60=230/244/334/360. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.47% exceeds max strategy risk 8.00%; score 0.290 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NIKL — position_continual — NO_TRADE

**Score:** 0.289 vs policy min 0.30 · **Close:** 189 · **ATR14:** 30.6 · **Volume ratio 20D:** 2.26 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 178–196, entry trigger **196**, stop **180**, risk 16 points (8.16%).

**Targets:** TP1 **246** (3.12R), TP2 **254** (3.62R), TP3 **262** (4.12R). Recommended base-case RR: **3.62R**.

**Why entry:** Hybrid entry uses close 189 and ATR14 30.6: buy zone 178–196. Entry is valid only if price can trade/hold around 196 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 180 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 246 (3.12R), TP2 254 (3.62R), TP3 262 (4.12R). Targets are ATR/structure capped for hold_days=10. ATR14=30.6, resistance_5/10/20/60=246/280/510/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.16% exceeds max strategy risk 8.00%; score 0.289 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BRMS — position_continual — NO_TRADE

**Score:** 0.289 vs policy min 0.30 · **Close:** 520 · **ATR14:** 73.9 · **Volume ratio 20D:** 1.07 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 494–535, entry trigger **535**, stop **492**, risk 43 points (8.04%).

**Targets:** TP1 **590** (1.28R), TP2 **610** (1.74R), TP3 **640** (2.44R). Recommended base-case RR: **1.74R**.

**Why entry:** Hybrid entry uses close 520 and ATR14 73.9: buy zone 494–535. Entry is valid only if price can trade/hold around 535 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 492 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 590 (1.28R), TP2 610 (1.74R), TP3 640 (2.44R). Targets are ATR/structure capped for hold_days=10. ATR14=73.9, resistance_5/10/20/60=590/640/845/1,045. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.04% exceeds max strategy risk 8.00%; score 0.289 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — NO_TRADE

**Score:** 0.285 vs policy min 0.30 · **Close:** 280 · **ATR14:** 46.0 · **Volume ratio 20D:** 1.50 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 262–290, entry trigger **290**, stop **266**, risk 24 points (8.28%).

**Targets:** TP1 **340** (2.08R), TP2 **352** (2.58R), TP3 **364** (3.08R). Recommended base-case RR: **2.58R**.

**Why entry:** Hybrid entry uses close 280 and ATR14 46.0: buy zone 262–290. Entry is valid only if price can trade/hold around 290 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 266 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 340 (2.08R), TP2 352 (2.58R), TP3 364 (3.08R). Targets are ATR/structure capped for hold_days=10. ATR14=46.0, resistance_5/10/20/60=340/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.28% exceeds max strategy risk 8.00%; score 0.285 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.282 vs policy min 0.30 · **Close:** 695 · **ATR14:** 110.0 · **Volume ratio 20D:** 1.32 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 655–720, entry trigger **720**, stop **660**, risk 60 points (8.33%).

**Targets:** TP1 **875** (2.58R), TP2 **905** (3.08R), TP3 **935** (3.58R). Recommended base-case RR: **3.08R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 110.0: buy zone 655–720. Entry is valid only if price can trade/hold around 720 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 660 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 875 (2.58R), TP2 905 (3.08R), TP3 935 (3.58R). Targets are ATR/structure capped for hold_days=10. ATR14=110.0, resistance_5/10/20/60=875/950/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; score 0.282 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## SOFA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.280 vs policy min 0.30 · **Close:** 258 · **ATR14:** 43.0 · **Volume ratio 20D:** 2.28 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 242–268, entry trigger **268**, stop **246**, risk 22 points (8.21%).

**Targets:** TP1 **362** (4.27R), TP2 **374** (4.82R), TP3 **386** (5.36R). Recommended base-case RR: **4.82R**.

**Why entry:** Hybrid entry uses close 258 and ATR14 43.0: buy zone 242–268. Entry is valid only if price can trade/hold around 268 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 246 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 362 (4.27R), TP2 374 (4.82R), TP3 386 (5.36R). Targets are ATR/structure capped for hold_days=10. ATR14=43.0, resistance_5/10/20/60=362/446/446/580. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; score 0.280 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## DPUM — momentum_20d_continual_research — NO_TRADE

**Score:** 0.276 vs policy min 0.30 · **Close:** 128 · **ATR14:** 18.7 · **Volume ratio 20D:** 0.54 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 121–132, entry trigger **132**, stop **127**, risk 5 points (3.79%).

**Targets:** TP1 **192** (12.00R), TP2 **200** (13.60R), TP3 **204** (14.40R). Recommended base-case RR: **13.60R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 18.7: buy zone 121–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 127 is placed below support structure (128 / 116). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 192 (12.00R), TP2 200 (13.60R), TP3 204 (14.40R). Targets are ATR/structure capped for hold_days=10. ATR14=18.7, resistance_5/10/20/60=200/216/236/236. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; score 0.276 below policy min_score 0.30; volume ratio 0.54 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
