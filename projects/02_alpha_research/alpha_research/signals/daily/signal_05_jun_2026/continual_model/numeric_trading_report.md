# Numeric Trading Desk Report — 2026-06-04

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 3 |
| CONDITIONAL | 7 |
| NO_TRADE | 32 |

## TRIN — ara_candidate_continual — ACTIONABLE

**Score:** 0.839 vs policy min 0.50 · **Close:** 332 · **ATR14:** 66.3 · **Volume ratio 20D:** 2.77 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 308–346, entry trigger **346**, stop **322**, risk 24 points (6.94%).

**Targets:** TP1 **380** (1.42R), TP2 **466** (5.00R), TP3 **486** (5.83R). Recommended base-case RR: **5.00R**.

**Why entry:** Hybrid entry uses close 332 and ATR14 66.3: buy zone 308–346. Entry is valid only if price can trade/hold around 346 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.42R), TP2 466 (5.00R), TP3 486 (5.83R). Targets are ATR/structure capped for hold_days=1. ATR14=66.3, resistance_5/10/20/60=486/600/740/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRIN — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.609 vs policy min 0.30 · **Close:** 332 · **ATR14:** 66.3 · **Volume ratio 20D:** 2.77 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 308–346, entry trigger **346**, stop **322**, risk 24 points (6.94%).

**Targets:** TP1 **486** (5.83R), TP2 **498** (6.33R), TP3 **510** (6.83R). Recommended base-case RR: **6.33R**.

**Why entry:** Hybrid entry uses close 332 and ATR14 66.3: buy zone 308–346. Entry is valid only if price can trade/hold around 346 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 486 (5.83R), TP2 498 (6.33R), TP3 510 (6.83R). Targets are ATR/structure capped for hold_days=5. ATR14=66.3, resistance_5/10/20/60=486/600/740/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRIN — position_continual — ACTIONABLE

**Score:** 0.312 vs policy min 0.30 · **Close:** 332 · **ATR14:** 66.3 · **Volume ratio 20D:** 2.77 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 308–346, entry trigger **346**, stop **322**, risk 24 points (6.94%).

**Targets:** TP1 **486** (5.83R), TP2 **498** (6.33R), TP3 **510** (6.83R). Recommended base-case RR: **6.33R**.

**Why entry:** Hybrid entry uses close 332 and ATR14 66.3: buy zone 308–346. Entry is valid only if price can trade/hold around 346 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 486 (5.83R), TP2 498 (6.33R), TP3 510 (6.83R). Targets are ATR/structure capped for hold_days=10. ATR14=66.3, resistance_5/10/20/60=486/600/740/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PADA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.665 vs policy min 0.30 · **Close:** 102 · **ATR14:** 19.1 · **Volume ratio 20D:** 1.01 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 95–106, entry trigger **106**, stop **101**, risk 5 points (4.72%).

**Targets:** TP1 **116** (2.00R), TP2 **148** (8.40R), TP3 **151** (9.00R). Recommended base-case RR: **8.40R**.

**Why entry:** Hybrid entry uses close 102 and ATR14 19.1: buy zone 95–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is placed below support structure (102 / 102). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 116 (2.00R), TP2 148 (8.40R), TP3 151 (9.00R). Targets are ATR/structure capped for hold_days=3. ATR14=19.1, resistance_5/10/20/60=148/166/197/218. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## PADA — swing_continual_defensive — CONDITIONAL

**Score:** 0.665 vs policy min 0.30 · **Close:** 102 · **ATR14:** 19.1 · **Volume ratio 20D:** 1.01 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 95–106, entry trigger **106**, stop **101**, risk 5 points (4.72%).

**Targets:** TP1 **116** (2.00R), TP2 **119** (2.60R), TP3 **148** (8.40R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 102 and ATR14 19.1: buy zone 95–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is placed below support structure (102 / 102). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 116 (2.00R), TP2 119 (2.60R), TP3 148 (8.40R). Targets are ATR/structure capped for hold_days=1. ATR14=19.1, resistance_5/10/20/60=148/166/197/218. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## IRSX — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.658 vs policy min 0.30 · **Close:** 284 · **ATR14:** 49.4 · **Volume ratio 20D:** 1.28 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 266–294, entry trigger **294**, stop **282**, risk 12 points (4.08%).

**Targets:** TP1 **380** (7.17R), TP2 **386** (7.67R), TP3 **392** (8.17R). Recommended base-case RR: **7.67R**.

**Why entry:** Hybrid entry uses close 284 and ATR14 49.4: buy zone 266–294. Entry is valid only if price can trade/hold around 294 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (7.17R), TP2 386 (7.67R), TP3 392 (8.17R). Targets are ATR/structure capped for hold_days=3. ATR14=49.4, resistance_5/10/20/60=386/470/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## IRSX — swing_continual_defensive — CONDITIONAL

**Score:** 0.658 vs policy min 0.30 · **Close:** 284 · **ATR14:** 49.4 · **Volume ratio 20D:** 1.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 266–294, entry trigger **294**, stop **282**, risk 12 points (4.08%).

**Targets:** TP1 **320** (2.17R), TP2 **384** (7.50R), TP3 **386** (7.67R). Recommended base-case RR: **7.50R**.

**Why entry:** Hybrid entry uses close 284 and ATR14 49.4: buy zone 266–294. Entry is valid only if price can trade/hold around 294 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 320 (2.17R), TP2 384 (7.50R), TP3 386 (7.67R). Targets are ATR/structure capped for hold_days=1. ATR14=49.4, resistance_5/10/20/60=386/470/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## PADA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.628 vs policy min 0.30 · **Close:** 102 · **ATR14:** 19.1 · **Volume ratio 20D:** 1.01 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 95–106, entry trigger **106**, stop **101**, risk 5 points (4.72%).

**Targets:** TP1 **148** (8.40R), TP2 **151** (9.00R), TP3 **154** (9.60R). Recommended base-case RR: **9.00R**.

**Why entry:** Hybrid entry uses close 102 and ATR14 19.1: buy zone 95–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is placed below support structure (102 / 102). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 148 (8.40R), TP2 151 (9.00R), TP3 154 (9.60R). Targets are ATR/structure capped for hold_days=5. ATR14=19.1, resistance_5/10/20/60=148/166/197/218. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## IRSX — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.596 vs policy min 0.30 · **Close:** 284 · **ATR14:** 49.4 · **Volume ratio 20D:** 1.28 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 266–294, entry trigger **294**, stop **282**, risk 12 points (4.08%).

**Targets:** TP1 **386** (7.67R), TP2 **392** (8.17R), TP3 **398** (8.67R). Recommended base-case RR: **8.17R**.

**Why entry:** Hybrid entry uses close 284 and ATR14 49.4: buy zone 266–294. Entry is valid only if price can trade/hold around 294 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 282 is placed below support structure (284 / 284). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 386 (7.67R), TP2 392 (8.17R), TP3 398 (8.67R). Targets are ATR/structure capped for hold_days=5. ATR14=49.4, resistance_5/10/20/60=386/470/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## PADA — position_continual — CONDITIONAL

**Score:** 0.311 vs policy min 0.30 · **Close:** 102 · **ATR14:** 19.1 · **Volume ratio 20D:** 1.01 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 95–106, entry trigger **106**, stop **101**, risk 5 points (4.72%).

**Targets:** TP1 **148** (8.40R), TP2 **151** (9.00R), TP3 **154** (9.60R). Recommended base-case RR: **9.00R**.

**Why entry:** Hybrid entry uses close 102 and ATR14 19.1: buy zone 95–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is placed below support structure (102 / 102). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 148 (8.40R), TP2 151 (9.00R), TP3 154 (9.60R). Targets are ATR/structure capped for hold_days=10. ATR14=19.1, resistance_5/10/20/60=148/166/197/218. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## OASA — scalping_continual_defensive — NO_TRADE

**Score:** 0.749 vs policy min 0.05 · **Close:** 270 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.95 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 254–280, entry trigger **280**, stop **256**, risk 24 points (8.57%).

**Targets:** TP1 **304** (1.00R), TP2 **322** (1.75R), TP3 **390** (4.58R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 270 and ATR14 43.7: buy zone 254–280. Entry is valid only if price can trade/hold around 280 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 256 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 304 (1.00R), TP2 322 (1.75R), TP3 390 (4.58R). Targets are ATR/structure capped for hold_days=1. ATR14=43.7, resistance_5/10/20/60=392/432/466/472. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.57% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — scalping_continual_defensive — NO_TRADE

**Score:** 0.745 vs policy min 0.05 · **Close:** 605 · **ATR14:** 237.1 · **Volume ratio 20D:** 6.25 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 520–655, entry trigger **655**, stop **600**, risk 55 points (8.40%).

**Targets:** TP1 **775** (2.18R), TP2 **805** (2.73R), TP3 **1,225** (10.36R). Recommended base-case RR: **2.73R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 237.1: buy zone 520–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 is placed below support structure (605 / 605). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 775 (2.18R), TP2 805 (2.73R), TP3 1,225 (10.36R). Targets are ATR/structure capped for hold_days=1. ATR14=237.1, resistance_5/10/20/60=1,225/1,725/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.26% > max 8.00%; entry-to-stop risk 8.40% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — scalping_continual_defensive — NO_TRADE

**Score:** 0.713 vs policy min 0.05 · **Close:** 179 · **ATR14:** 26.1 · **Volume ratio 20D:** 1.18 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 169–185, entry trigger **185**, stop **170**, risk 15 points (8.11%).

**Targets:** TP1 **200** (1.00R), TP2 **212** (1.80R), TP3 **244** (3.93R). Recommended base-case RR: **1.80R**.

**Why entry:** Hybrid entry uses close 179 and ATR14 26.1: buy zone 169–185. Entry is valid only if price can trade/hold around 185 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 170 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 200 (1.00R), TP2 212 (1.80R), TP3 244 (3.93R). Targets are ATR/structure capped for hold_days=1. ATR14=26.1, resistance_5/10/20/60=244/276/334/408. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — scalping_continual_defensive — NO_TRADE

**Score:** 0.712 vs policy min 0.05 · **Close:** 144 · **ATR14:** 23.4 · **Volume ratio 20D:** 1.71 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 135–149, entry trigger **149**, stop **137**, risk 12 points (8.05%).

**Targets:** TP1 **161** (1.00R), TP2 **190** (3.42R), TP3 **196** (3.92R). Recommended base-case RR: **3.42R**.

**Why entry:** Hybrid entry uses close 144 and ATR14 23.4: buy zone 135–149. Entry is valid only if price can trade/hold around 149 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 137 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 161 (1.00R), TP2 190 (3.42R), TP3 196 (3.92R). Targets are ATR/structure capped for hold_days=1. ATR14=23.4, resistance_5/10/20/60=190/232/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — scalping_continual_defensive — NO_TRADE

**Score:** 0.705 vs policy min 0.05 · **Close:** 101 · **ATR14:** 20.8 · **Volume ratio 20D:** 0.70 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **117** (1.22R), TP2 **143** (4.11R), TP3 **148** (4.67R). Recommended base-case RR: **4.11R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.8: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 117 (1.22R), TP2 143 (4.11R), TP3 148 (4.67R). Targets are ATR/structure capped for hold_days=1. ATR14=20.8, resistance_5/10/20/60=143/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.662 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.8 · **Volume ratio 20D:** 0.70 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **143** (4.11R), TP2 **148** (4.67R), TP3 **153** (5.22R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.8: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 143 (4.11R), TP2 148 (4.67R), TP3 153 (5.22R). Targets are ATR/structure capped for hold_days=3. ATR14=20.8, resistance_5/10/20/60=143/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — swing_continual_defensive — NO_TRADE

**Score:** 0.662 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.8 · **Volume ratio 20D:** 0.70 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **117** (1.22R), TP2 **143** (4.11R), TP3 **148** (4.67R). Recommended base-case RR: **4.11R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.8: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 117 (1.22R), TP2 143 (4.11R), TP3 148 (4.67R). Targets are ATR/structure capped for hold_days=1. ATR14=20.8, resistance_5/10/20/60=143/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.628 vs policy min 0.30 · **Close:** 270 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.95 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 254–280, entry trigger **280**, stop **256**, risk 24 points (8.57%).

**Targets:** TP1 **304** (1.00R), TP2 **392** (4.67R), TP3 **404** (5.17R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 270 and ATR14 43.7: buy zone 254–280. Entry is valid only if price can trade/hold around 280 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 256 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 304 (1.00R), TP2 392 (4.67R), TP3 404 (5.17R). Targets are ATR/structure capped for hold_days=3. ATR14=43.7, resistance_5/10/20/60=392/432/466/472. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.57% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — swing_continual_defensive — NO_TRADE

**Score:** 0.628 vs policy min 0.30 · **Close:** 270 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.95 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 254–280, entry trigger **280**, stop **256**, risk 24 points (8.57%).

**Targets:** TP1 **304** (1.00R), TP2 **322** (1.75R), TP3 **390** (4.58R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 270 and ATR14 43.7: buy zone 254–280. Entry is valid only if price can trade/hold around 280 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 256 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 304 (1.00R), TP2 322 (1.75R), TP3 390 (4.58R). Targets are ATR/structure capped for hold_days=1. ATR14=43.7, resistance_5/10/20/60=392/432/466/472. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.57% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## COCO — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.624 vs policy min 0.30 · **Close:** 187 · **ATR14:** 36.9 · **Volume ratio 20D:** 0.69 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 174–195, entry trigger **195**, stop **179**, risk 16 points (8.21%).

**Targets:** TP1 **260** (4.06R), TP2 **266** (4.44R), TP3 **274** (4.94R). Recommended base-case RR: **4.44R**.

**Why entry:** Hybrid entry uses close 187 and ATR14 36.9: buy zone 174–195. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 179 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 260 (4.06R), TP2 266 (4.44R), TP3 274 (4.94R). Targets are ATR/structure capped for hold_days=3. ATR14=36.9, resistance_5/10/20/60=266/308/402/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## COCO — swing_continual_defensive — NO_TRADE

**Score:** 0.624 vs policy min 0.30 · **Close:** 187 · **ATR14:** 36.9 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 174–195, entry trigger **195**, stop **179**, risk 16 points (8.21%).

**Targets:** TP1 **214** (1.19R), TP2 **262** (4.19R), TP3 **266** (4.44R). Recommended base-case RR: **4.19R**.

**Why entry:** Hybrid entry uses close 187 and ATR14 36.9: buy zone 174–195. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 179 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 214 (1.19R), TP2 262 (4.19R), TP3 266 (4.44R). Targets are ATR/structure capped for hold_days=1. ATR14=36.9, resistance_5/10/20/60=266/308/402/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.21% exceeds max strategy risk 8.00%; TP1 reward/risk 1.19R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.618 vs policy min 0.30 · **Close:** 286 · **ATR14:** 46.1 · **Volume ratio 20D:** 1.50 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 268–296, entry trigger **296**, stop **272**, risk 24 points (8.11%).

**Targets:** TP1 **368** (3.00R), TP2 **380** (3.50R), TP3 **392** (4.00R). Recommended base-case RR: **3.50R**.

**Why entry:** Hybrid entry uses close 286 and ATR14 46.1: buy zone 268–296. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 368 (3.00R), TP2 380 (3.50R), TP3 392 (4.00R). Targets are ATR/structure capped for hold_days=5. ATR14=46.1, resistance_5/10/20/60=368/450/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ASPR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.618 vs policy min 0.30 · **Close:** 157 · **ATR14:** 62.9 · **Volume ratio 20D:** 0.28 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 134–170, entry trigger **170**, stop **156**, risk 14 points (8.24%).

**Targets:** TP1 **224** (3.86R), TP2 **232** (4.43R), TP3 **240** (5.00R). Recommended base-case RR: **4.43R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 62.9: buy zone 134–170. Entry is valid only if price can trade/hold around 170 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 156 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (3.86R), TP2 232 (4.43R), TP3 240 (5.00R). Targets are ATR/structure capped for hold_days=3. ATR14=62.9, resistance_5/10/20/60=224/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.28% > max 8.00%; entry-to-stop risk 8.24% exceeds max strategy risk 8.00%; volume ratio 0.28 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## ASPR — swing_continual_defensive — NO_TRADE

**Score:** 0.618 vs policy min 0.30 · **Close:** 157 · **ATR14:** 62.9 · **Volume ratio 20D:** 0.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 134–170, entry trigger **170**, stop **156**, risk 14 points (8.24%).

**Targets:** TP1 **224** (3.86R), TP2 **232** (4.43R), TP3 **240** (5.00R). Recommended base-case RR: **4.43R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 62.9: buy zone 134–170. Entry is valid only if price can trade/hold around 170 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 156 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (3.86R), TP2 232 (4.43R), TP3 240 (5.00R). Targets are ATR/structure capped for hold_days=1. ATR14=62.9, resistance_5/10/20/60=224/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.28% > max 8.00%; entry-to-stop risk 8.24% exceeds max strategy risk 8.00%; volume ratio 0.28 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.617 vs policy min 0.30 · **Close:** 144 · **ATR14:** 23.4 · **Volume ratio 20D:** 1.71 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 135–149, entry trigger **149**, stop **137**, risk 12 points (8.05%).

**Targets:** TP1 **190** (3.42R), TP2 **196** (3.92R), TP3 **202** (4.42R). Recommended base-case RR: **3.92R**.

**Why entry:** Hybrid entry uses close 144 and ATR14 23.4: buy zone 135–149. Entry is valid only if price can trade/hold around 149 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 137 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (3.42R), TP2 196 (3.92R), TP3 202 (4.42R). Targets are ATR/structure capped for hold_days=5. ATR14=23.4, resistance_5/10/20/60=190/232/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.616 vs policy min 0.30 · **Close:** 605 · **ATR14:** 237.1 · **Volume ratio 20D:** 6.25 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 520–655, entry trigger **655**, stop **600**, risk 55 points (8.40%).

**Targets:** TP1 **775** (2.18R), TP2 **1,225** (10.36R), TP3 **1,255** (10.91R). Recommended base-case RR: **10.36R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 237.1: buy zone 520–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 is placed below support structure (605 / 605). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 775 (2.18R), TP2 1,225 (10.36R), TP3 1,255 (10.91R). Targets are ATR/structure capped for hold_days=3. ATR14=237.1, resistance_5/10/20/60=1,225/1,725/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.26% > max 8.00%; entry-to-stop risk 8.40% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — swing_continual_defensive — NO_TRADE

**Score:** 0.616 vs policy min 0.30 · **Close:** 605 · **ATR14:** 237.1 · **Volume ratio 20D:** 6.25 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 520–655, entry trigger **655**, stop **600**, risk 55 points (8.40%).

**Targets:** TP1 **775** (2.18R), TP2 **805** (2.73R), TP3 **1,225** (10.36R). Recommended base-case RR: **2.73R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 237.1: buy zone 520–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 is placed below support structure (605 / 605). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 775 (2.18R), TP2 805 (2.73R), TP3 1,225 (10.36R). Targets are ATR/structure capped for hold_days=1. ATR14=237.1, resistance_5/10/20/60=1,225/1,725/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.26% > max 8.00%; entry-to-stop risk 8.40% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.608 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.8 · **Volume ratio 20D:** 0.70 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **143** (4.11R), TP2 **148** (4.67R), TP3 **153** (5.22R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.8: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 143 (4.11R), TP2 148 (4.67R), TP3 153 (5.22R). Targets are ATR/structure capped for hold_days=5. ATR14=20.8, resistance_5/10/20/60=143/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.593 vs policy min 0.30 · **Close:** 270 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.95 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 254–280, entry trigger **280**, stop **256**, risk 24 points (8.57%).

**Targets:** TP1 **378** (4.08R), TP2 **392** (4.67R), TP3 **404** (5.17R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 270 and ATR14 43.7: buy zone 254–280. Entry is valid only if price can trade/hold around 280 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 256 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 378 (4.08R), TP2 392 (4.67R), TP3 404 (5.17R). Targets are ATR/structure capped for hold_days=5. ATR14=43.7, resistance_5/10/20/60=392/432/466/472. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.57% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HUMI — momentum_20d_continual_research — NO_TRADE

**Score:** 0.492 vs policy min 0.30 · **Close:** 108 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.10 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 101–112, entry trigger **112**, stop **103**, risk 9 points (8.04%).

**Targets:** TP1 **160** (5.33R), TP2 **165** (5.89R), TP3 **170** (6.44R). Recommended base-case RR: **5.89R**.

**Why entry:** Hybrid entry uses close 108 and ATR14 18.1: buy zone 101–112. Entry is valid only if price can trade/hold around 112 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is placed below support structure (104 / 104). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 160 (5.33R), TP2 165 (5.89R), TP3 170 (6.44R). Targets are ATR/structure capped for hold_days=10. ATR14=18.1, resistance_5/10/20/60=160/194/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.04% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_20d_continual_research — NO_TRADE

**Score:** 0.491 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.8 · **Volume ratio 20D:** 0.70 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **143** (4.11R), TP2 **148** (4.67R), TP3 **153** (5.22R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.8: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 143 (4.11R), TP2 148 (4.67R), TP3 153 (5.22R). Targets are ATR/structure capped for hold_days=10. ATR14=20.8, resistance_5/10/20/60=143/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.49% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — momentum_20d_continual_research — NO_TRADE

**Score:** 0.460 vs policy min 0.30 · **Close:** 113 · **ATR14:** 20.1 · **Volume ratio 20D:** 1.25 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 105–118, entry trigger **118**, stop **108**, risk 10 points (8.47%).

**Targets:** TP1 **173** (5.50R), TP2 **178** (6.00R), TP3 **183** (6.50R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 113 and ATR14 20.1: buy zone 105–118. Entry is valid only if price can trade/hold around 118 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 173 (5.50R), TP2 178 (6.00R), TP3 183 (6.50R). Targets are ATR/structure capped for hold_days=10. ATR14=20.1, resistance_5/10/20/60=173/208/238/334. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.47% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — momentum_20d_continual_research — NO_TRADE

**Score:** 0.442 vs policy min 0.30 · **Close:** 605 · **ATR14:** 237.1 · **Volume ratio 20D:** 6.25 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 520–655, entry trigger **655**, stop **600**, risk 55 points (8.40%).

**Targets:** TP1 **1,225** (10.36R), TP2 **1,255** (10.91R), TP3 **1,285** (11.45R). Recommended base-case RR: **10.91R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 237.1: buy zone 520–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 is placed below support structure (605 / 605). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,225 (10.36R), TP2 1,255 (10.91R), TP3 1,285 (11.45R). Targets are ATR/structure capped for hold_days=10. ATR14=237.1, resistance_5/10/20/60=1,225/1,725/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry trigger is too far from latest close: 8.26% > max 8.00%; entry-to-stop risk 8.40% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ESIP — momentum_20d_continual_research — NO_TRADE

**Score:** 0.426 vs policy min 0.30 · **Close:** 104 · **ATR14:** 22.1 · **Volume ratio 20D:** 0.06 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 96–109, entry trigger **109**, stop **100**, risk 9 points (8.26%).

**Targets:** TP1 **139** (3.33R), TP2 **144** (3.89R), TP3 **149** (4.44R). Recommended base-case RR: **3.89R**.

**Why entry:** Hybrid entry uses close 104 and ATR14 22.1: buy zone 96–109. Entry is valid only if price can trade/hold around 109 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 100 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 139 (3.33R), TP2 144 (3.89R), TP3 149 (4.44R). Targets are ATR/structure capped for hold_days=10. ATR14=22.1, resistance_5/10/20/60=139/175/238/238. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; volume ratio 0.06 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — NO_TRADE

**Score:** 0.331 vs policy min 0.30 · **Close:** 286 · **ATR14:** 46.1 · **Volume ratio 20D:** 1.50 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 268–296, entry trigger **296**, stop **272**, risk 24 points (8.11%).

**Targets:** TP1 **368** (3.00R), TP2 **380** (3.50R), TP3 **392** (4.00R). Recommended base-case RR: **3.50R**.

**Why entry:** Hybrid entry uses close 286 and ATR14 46.1: buy zone 268–296. Entry is valid only if price can trade/hold around 296 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 272 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 368 (3.00R), TP2 380 (3.50R), TP3 392 (4.00R). Targets are ATR/structure capped for hold_days=10. ATR14=46.1, resistance_5/10/20/60=368/450/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — position_continual — NO_TRADE

**Score:** 0.328 vs policy min 0.30 · **Close:** 605 · **ATR14:** 237.1 · **Volume ratio 20D:** 6.25 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 520–655, entry trigger **655**, stop **600**, risk 55 points (8.40%).

**Targets:** TP1 **1,225** (10.36R), TP2 **1,255** (10.91R), TP3 **1,285** (11.45R). Recommended base-case RR: **10.91R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 237.1: buy zone 520–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 is placed below support structure (605 / 605). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,225 (10.36R), TP2 1,255 (10.91R), TP3 1,285 (11.45R). Targets are ATR/structure capped for hold_days=10. ATR14=237.1, resistance_5/10/20/60=1,225/1,725/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.26% > max 8.00%; entry-to-stop risk 8.40% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HUMI — position_continual — NO_TRADE

**Score:** 0.326 vs policy min 0.30 · **Close:** 108 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.10 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 101–112, entry trigger **112**, stop **103**, risk 9 points (8.04%).

**Targets:** TP1 **160** (5.33R), TP2 **165** (5.89R), TP3 **170** (6.44R). Recommended base-case RR: **5.89R**.

**Why entry:** Hybrid entry uses close 108 and ATR14 18.1: buy zone 101–112. Entry is valid only if price can trade/hold around 112 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is placed below support structure (104 / 104). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 160 (5.33R), TP2 165 (5.89R), TP3 170 (6.44R). Targets are ATR/structure capped for hold_days=10. ATR14=18.1, resistance_5/10/20/60=160/194/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.04% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — position_continual — NO_TRADE

**Score:** 0.326 vs policy min 0.30 · **Close:** 179 · **ATR14:** 26.1 · **Volume ratio 20D:** 1.18 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 169–185, entry trigger **185**, stop **170**, risk 15 points (8.11%).

**Targets:** TP1 **244** (3.93R), TP2 **252** (4.47R), TP3 **260** (5.00R). Recommended base-case RR: **4.47R**.

**Why entry:** Hybrid entry uses close 179 and ATR14 26.1: buy zone 169–185. Entry is valid only if price can trade/hold around 185 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 170 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 244 (3.93R), TP2 252 (4.47R), TP3 260 (5.00R). Targets are ATR/structure capped for hold_days=10. ATR14=26.1, resistance_5/10/20/60=244/276/334/408. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — position_continual — NO_TRADE

**Score:** 0.323 vs policy min 0.30 · **Close:** 144 · **ATR14:** 23.4 · **Volume ratio 20D:** 1.71 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 135–149, entry trigger **149**, stop **137**, risk 12 points (8.05%).

**Targets:** TP1 **190** (3.42R), TP2 **196** (3.92R), TP3 **202** (4.42R). Recommended base-case RR: **3.92R**.

**Why entry:** Hybrid entry uses close 144 and ATR14 23.4: buy zone 135–149. Entry is valid only if price can trade/hold around 149 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 137 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (3.42R), TP2 196 (3.92R), TP3 202 (4.42R). Targets are ATR/structure capped for hold_days=10. ATR14=23.4, resistance_5/10/20/60=190/232/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — position_continual — NO_TRADE

**Score:** 0.322 vs policy min 0.30 · **Close:** 270 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.95 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 254–280, entry trigger **280**, stop **256**, risk 24 points (8.57%).

**Targets:** TP1 **392** (4.67R), TP2 **404** (5.17R), TP3 **416** (5.67R). Recommended base-case RR: **5.17R**.

**Why entry:** Hybrid entry uses close 270 and ATR14 43.7: buy zone 254–280. Entry is valid only if price can trade/hold around 280 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 256 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 392 (4.67R), TP2 404 (5.17R), TP3 416 (5.67R). Targets are ATR/structure capped for hold_days=10. ATR14=43.7, resistance_5/10/20/60=392/432/466/472. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.57% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — position_continual — NO_TRADE

**Score:** 0.321 vs policy min 0.30 · **Close:** 113 · **ATR14:** 20.1 · **Volume ratio 20D:** 1.25 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 105–118, entry trigger **118**, stop **108**, risk 10 points (8.47%).

**Targets:** TP1 **173** (5.50R), TP2 **178** (6.00R), TP3 **183** (6.50R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 113 and ATR14 20.1: buy zone 105–118. Entry is valid only if price can trade/hold around 118 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 173 (5.50R), TP2 178 (6.00R), TP3 183 (6.50R). Targets are ATR/structure capped for hold_days=10. ATR14=20.1, resistance_5/10/20/60=173/208/238/334. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.47% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — NO_TRADE

**Score:** 0.317 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.8 · **Volume ratio 20D:** 0.70 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **143** (4.11R), TP2 **148** (4.67R), TP3 **153** (5.22R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.8: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 143 (4.11R), TP2 148 (4.67R), TP3 153 (5.22R). Targets are ATR/structure capped for hold_days=10. ATR14=20.8, resistance_5/10/20/60=143/174/224/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---
