# Numeric Trading Desk Report — 2026-06-05

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 11 |
| CONDITIONAL | 10 |
| NO_TRADE | 21 |

## IRSX — scalping_continual_defensive — ACTIONABLE

**Score:** 0.729 vs policy min 0.05 · **Close:** 242 · **ATR14:** 50.1 · **Volume ratio 20D:** 0.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–254, entry trigger **254**, stop **240**, risk 14 points (5.51%).

**Targets:** TP1 **280** (1.86R), TP2 **288** (2.43R), TP3 **380** (9.00R). Recommended base-case RR: **2.43R**.

**Why entry:** Hybrid entry uses close 242 and ATR14 50.1: buy zone 224–254. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 240 is placed below support structure (242 / 242). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 280 (1.86R), TP2 288 (2.43R), TP3 380 (9.00R). Targets are ATR/structure capped for hold_days=1. ATR14=50.1, resistance_5/10/20/60=386/460/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HUMI — scalping_continual_defensive — ACTIONABLE

**Score:** 0.709 vs policy min 0.05 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 93–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **114** (1.25R), TP2 **118** (1.75R), TP3 **151** (5.88R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 18.4: buy zone 93–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is placed below support structure (97 / 97). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 114 (1.25R), TP2 118 (1.75R), TP3 151 (5.88R). Targets are ATR/structure capped for hold_days=1. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HUMI — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.632 vs policy min 0.30 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 93–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **114** (1.25R), TP2 **151** (5.88R), TP3 **155** (6.38R). Recommended base-case RR: **5.88R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 18.4: buy zone 93–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is placed below support structure (97 / 97). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 114 (1.25R), TP2 151 (5.88R), TP3 155 (6.38R). Targets are ATR/structure capped for hold_days=3. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HUMI — swing_continual_defensive — ACTIONABLE

**Score:** 0.632 vs policy min 0.30 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 93–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **114** (1.25R), TP2 **118** (1.75R), TP3 **151** (5.88R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 18.4: buy zone 93–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is placed below support structure (97 / 97). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 114 (1.25R), TP2 118 (1.75R), TP3 151 (5.88R). Targets are ATR/structure capped for hold_days=1. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## IRSX — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.591 vs policy min 0.30 · **Close:** 242 · **ATR14:** 50.1 · **Volume ratio 20D:** 0.91 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 224–254, entry trigger **254**, stop **240**, risk 14 points (5.51%).

**Targets:** TP1 **280** (1.86R), TP2 **386** (9.43R), TP3 **394** (10.00R). Recommended base-case RR: **9.43R**.

**Why entry:** Hybrid entry uses close 242 and ATR14 50.1: buy zone 224–254. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 240 is placed below support structure (242 / 242). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 280 (1.86R), TP2 386 (9.43R), TP3 394 (10.00R). Targets are ATR/structure capped for hold_days=3. ATR14=50.1, resistance_5/10/20/60=386/460/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## IRSX — swing_continual_defensive — ACTIONABLE

**Score:** 0.591 vs policy min 0.30 · **Close:** 242 · **ATR14:** 50.1 · **Volume ratio 20D:** 0.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–254, entry trigger **254**, stop **240**, risk 14 points (5.51%).

**Targets:** TP1 **280** (1.86R), TP2 **288** (2.43R), TP3 **380** (9.00R). Recommended base-case RR: **2.43R**.

**Why entry:** Hybrid entry uses close 242 and ATR14 50.1: buy zone 224–254. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 240 is placed below support structure (242 / 242). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 280 (1.86R), TP2 288 (2.43R), TP3 380 (9.00R). Targets are ATR/structure capped for hold_days=1. ATR14=50.1, resistance_5/10/20/60=386/460/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HUMI — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.522 vs policy min 0.30 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 93–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **146** (5.25R), TP2 **151** (5.88R), TP3 **155** (6.38R). Recommended base-case RR: **5.88R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 18.4: buy zone 93–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is placed below support structure (97 / 97). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 146 (5.25R), TP2 151 (5.88R), TP3 155 (6.38R). Targets are ATR/structure capped for hold_days=5. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## IRSX — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.494 vs policy min 0.30 · **Close:** 242 · **ATR14:** 50.1 · **Volume ratio 20D:** 0.91 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 224–254, entry trigger **254**, stop **240**, risk 14 points (5.51%).

**Targets:** TP1 **280** (1.86R), TP2 **386** (9.43R), TP3 **394** (10.00R). Recommended base-case RR: **9.43R**.

**Why entry:** Hybrid entry uses close 242 and ATR14 50.1: buy zone 224–254. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 240 is placed below support structure (242 / 242). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 280 (1.86R), TP2 386 (9.43R), TP3 394 (10.00R). Targets are ATR/structure capped for hold_days=5. ATR14=50.1, resistance_5/10/20/60=386/460/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — position_continual — ACTIONABLE

**Score:** 0.321 vs policy min 0.30 · **Close:** 168 · **ATR14:** 26.1 · **Volume ratio 20D:** 0.91 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 158–174, entry trigger **174**, stop **161**, risk 13 points (7.47%).

**Targets:** TP1 **244** (5.38R), TP2 **252** (6.00R), TP3 **260** (6.62R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 168 and ATR14 26.1: buy zone 158–174. Entry is valid only if price can trade/hold around 174 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 161 is placed below support structure (162 / 162). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 244 (5.38R), TP2 252 (6.00R), TP3 260 (6.62R). Targets are ATR/structure capped for hold_days=10. ATR14=26.1, resistance_5/10/20/60=244/262/334/408. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## IRSX — position_continual — ACTIONABLE

**Score:** 0.320 vs policy min 0.30 · **Close:** 242 · **ATR14:** 50.1 · **Volume ratio 20D:** 0.91 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 224–254, entry trigger **254**, stop **240**, risk 14 points (5.51%).

**Targets:** TP1 **386** (9.43R), TP2 **394** (10.00R), TP3 **402** (10.57R). Recommended base-case RR: **10.00R**.

**Why entry:** Hybrid entry uses close 242 and ATR14 50.1: buy zone 224–254. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 240 is placed below support structure (242 / 242). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 386 (9.43R), TP2 394 (10.00R), TP3 402 (10.57R). Targets are ATR/structure capped for hold_days=10. ATR14=50.1, resistance_5/10/20/60=386/460/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HUMI — position_continual — ACTIONABLE

**Score:** 0.314 vs policy min 0.30 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 93–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **151** (5.88R), TP2 **155** (6.38R), TP3 **159** (6.88R). Recommended base-case RR: **6.38R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 18.4: buy zone 93–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is placed below support structure (97 / 97). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 151 (5.88R), TP2 155 (6.38R), TP3 159 (6.88R). Targets are ATR/structure capped for hold_days=10. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — scalping_continual_defensive — CONDITIONAL

**Score:** 0.714 vs policy min 0.05 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 280–308, entry trigger **308**, stop **288**, risk 20 points (6.49%).

**Targets:** TP1 **332** (1.20R), TP2 **392** (4.20R), TP3 **410** (5.10R). Recommended base-case RR: **4.20R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 46.3: buy zone 280–308. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 332 (1.20R), TP2 392 (4.20R), TP3 410 (5.10R). Targets are ATR/structure capped for hold_days=1. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.20R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## INET — scalping_continual_defensive — CONDITIONAL

**Score:** 0.713 vs policy min 0.05 · **Close:** 168 · **ATR14:** 26.1 · **Volume ratio 20D:** 0.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 158–174, entry trigger **174**, stop **161**, risk 13 points (7.47%).

**Targets:** TP1 **188** (1.08R), TP2 **197** (1.77R), TP3 **240** (5.08R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 168 and ATR14 26.1: buy zone 158–174. Entry is valid only if price can trade/hold around 174 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 161 is placed below support structure (162 / 162). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 188 (1.08R), TP2 197 (1.77R), TP3 240 (5.08R). Targets are ATR/structure capped for hold_days=1. ATR14=26.1, resistance_5/10/20/60=244/262/334/408. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.08R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.597 vs policy min 0.30 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 280–308, entry trigger **308**, stop **288**, risk 20 points (6.49%).

**Targets:** TP1 **332** (1.20R), TP2 **410** (5.10R), TP3 **420** (5.60R). Recommended base-case RR: **5.10R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 46.3: buy zone 280–308. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 332 (1.20R), TP2 410 (5.10R), TP3 420 (5.60R). Targets are ATR/structure capped for hold_days=3. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.20R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BULL — swing_continual_defensive — CONDITIONAL

**Score:** 0.597 vs policy min 0.30 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 280–308, entry trigger **308**, stop **288**, risk 20 points (6.49%).

**Targets:** TP1 **332** (1.20R), TP2 **392** (4.20R), TP3 **410** (5.10R). Recommended base-case RR: **4.20R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 46.3: buy zone 280–308. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 332 (1.20R), TP2 392 (4.20R), TP3 410 (5.10R). Targets are ATR/structure capped for hold_days=1. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.20R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## TPMA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.590 vs policy min 0.30 · **Close:** 360 · **ATR14:** 25.2 · **Volume ratio 20D:** 0.61 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 350–366, entry trigger **366**, stop **358**, risk 8 points (2.19%).

**Targets:** TP1 **380** (1.75R), TP2 **384** (2.25R), TP3 **386** (2.50R). Recommended base-case RR: **2.25R**.

**Why entry:** Hybrid entry uses close 360 and ATR14 25.2: buy zone 350–366. Entry is valid only if price can trade/hold around 366 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 358 is placed below support structure (360 / 360). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.75R), TP2 384 (2.25R), TP3 386 (2.50R). Targets are ATR/structure capped for hold_days=3. ATR14=25.2, resistance_5/10/20/60=500/515/565/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## TPMA — swing_continual_defensive — CONDITIONAL

**Score:** 0.590 vs policy min 0.30 · **Close:** 360 · **ATR14:** 25.2 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 350–366, entry trigger **366**, stop **358**, risk 8 points (2.19%).

**Targets:** TP1 **380** (1.75R), TP2 **384** (2.25R), TP3 **386** (2.50R). Recommended base-case RR: **2.25R**.

**Why entry:** Hybrid entry uses close 360 and ATR14 25.2: buy zone 350–366. Entry is valid only if price can trade/hold around 366 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 358 is placed below support structure (360 / 360). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.75R), TP2 384 (2.25R), TP3 386 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=25.2, resistance_5/10/20/60=500/515/565/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.558 vs policy min 0.30 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 280–308, entry trigger **308**, stop **288**, risk 20 points (6.49%).

**Targets:** TP1 **410** (5.10R), TP2 **420** (5.60R), TP3 **430** (6.10R). Recommended base-case RR: **5.60R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 46.3: buy zone 280–308. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 410 (5.10R), TP2 420 (5.60R), TP3 430 (6.10R). Targets are ATR/structure capped for hold_days=5. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## TPMA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.500 vs policy min 0.30 · **Close:** 360 · **ATR14:** 25.2 · **Volume ratio 20D:** 0.61 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 350–366, entry trigger **366**, stop **358**, risk 8 points (2.19%).

**Targets:** TP1 **380** (1.75R), TP2 **384** (2.25R), TP3 **500** (16.75R). Recommended base-case RR: **2.25R**.

**Why entry:** Hybrid entry uses close 360 and ATR14 25.2: buy zone 350–366. Entry is valid only if price can trade/hold around 366 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 358 is placed below support structure (360 / 360). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 380 (1.75R), TP2 384 (2.25R), TP3 500 (16.75R). Targets are ATR/structure capped for hold_days=5. ATR14=25.2, resistance_5/10/20/60=500/515/565/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — position_continual — CONDITIONAL

**Score:** 0.321 vs policy min 0.30 · **Close:** 640 · **ATR14:** 106.8 · **Volume ratio 20D:** 0.73 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 600–665, entry trigger **665**, stop **635**, risk 30 points (4.51%).

**Targets:** TP1 **950** (9.50R), TP2 **965** (10.00R), TP3 **980** (10.50R). Recommended base-case RR: **10.00R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 106.8: buy zone 600–665. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is placed below support structure (640 / 640). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 950 (9.50R), TP2 965 (10.00R), TP3 980 (10.50R). Targets are ATR/structure capped for hold_days=10. ATR14=106.8, resistance_5/10/20/60=950/950/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BULL — position_continual — CONDITIONAL

**Score:** 0.317 vs policy min 0.30 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 280–308, entry trigger **308**, stop **288**, risk 20 points (6.49%).

**Targets:** TP1 **410** (5.10R), TP2 **420** (5.60R), TP3 **430** (6.10R). Recommended base-case RR: **5.60R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 46.3: buy zone 280–308. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 410 (5.10R), TP2 420 (5.60R), TP3 430 (6.10R). Targets are ATR/structure capped for hold_days=10. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — ara_candidate_continual — NO_TRADE

**Score:** 0.899 vs policy min 0.50 · **Close:** 610 · **ATR14:** 122.4 · **Volume ratio 20D:** 1.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 565–635, entry trigger **635**, stop **580**, risk 55 points (8.66%).

**Targets:** TP1 **760** (2.27R), TP2 **765** (2.36R), TP3 **770** (2.45R). Recommended base-case RR: **2.36R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 122.4: buy zone 565–635. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 580 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 760 (2.27R), TP2 765 (2.36R), TP3 770 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=122.4, resistance_5/10/20/60=765/820/1,760/84,875. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.66% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BIPI — scalping_continual_defensive — NO_TRADE

**Score:** 0.721 vs policy min 0.05 · **Close:** 137 · **ATR14:** 22.9 · **Volume ratio 20D:** 0.47 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 128–142, entry trigger **142**, stop **130**, risk 12 points (8.45%).

**Targets:** TP1 **154** (1.00R), TP2 **184** (3.50R), TP3 **190** (4.00R). Recommended base-case RR: **3.50R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 22.9: buy zone 128–142. Entry is valid only if price can trade/hold around 142 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 130 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.00R), TP2 184 (3.50R), TP3 190 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=22.9, resistance_5/10/20/60=190/212/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.45% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.47 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.626 vs policy min 0.30 · **Close:** 262 · **ATR14:** 45.2 · **Volume ratio 20D:** 0.92 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 246–272, entry trigger **272**, stop **250**, risk 22 points (8.09%).

**Targets:** TP1 **352** (3.64R), TP2 **364** (4.18R), TP3 **376** (4.73R). Recommended base-case RR: **4.18R**.

**Why entry:** Hybrid entry uses close 262 and ATR14 45.2: buy zone 246–272. Entry is valid only if price can trade/hold around 272 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 250 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 352 (3.64R), TP2 364 (4.18R), TP3 376 (4.73R). Targets are ATR/structure capped for hold_days=3. ATR14=45.2, resistance_5/10/20/60=352/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — swing_continual_defensive — NO_TRADE

**Score:** 0.626 vs policy min 0.30 · **Close:** 262 · **ATR14:** 45.2 · **Volume ratio 20D:** 0.92 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 246–272, entry trigger **272**, stop **250**, risk 22 points (8.09%).

**Targets:** TP1 **296** (1.09R), TP2 **352** (3.64R), TP3 **364** (4.18R). Recommended base-case RR: **3.64R**.

**Why entry:** Hybrid entry uses close 262 and ATR14 45.2: buy zone 246–272. Entry is valid only if price can trade/hold around 272 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 250 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 296 (1.09R), TP2 352 (3.64R), TP3 364 (4.18R). Targets are ATR/structure capped for hold_days=1. ATR14=45.2, resistance_5/10/20/60=352/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ASPR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.604 vs policy min 0.30 · **Close:** 134 · **ATR14:** 59.8 · **Volume ratio 20D:** 0.42 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 113–146, entry trigger **146**, stop **134**, risk 12 points (8.22%).

**Targets:** TP1 **224** (6.50R), TP2 **230** (7.00R), TP3 **236** (7.50R). Recommended base-case RR: **7.00R**.

**Why entry:** Hybrid entry uses close 134 and ATR14 59.8: buy zone 113–146. Entry is valid only if price can trade/hold around 146 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 134 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (6.50R), TP2 230 (7.00R), TP3 236 (7.50R). Targets are ATR/structure capped for hold_days=3. ATR14=59.8, resistance_5/10/20/60=224/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.96% > max 8.00%; entry-to-stop risk 8.22% exceeds max strategy risk 8.00%; volume ratio 0.42 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## ASPR — swing_continual_defensive — NO_TRADE

**Score:** 0.604 vs policy min 0.30 · **Close:** 134 · **ATR14:** 59.8 · **Volume ratio 20D:** 0.42 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 113–146, entry trigger **146**, stop **134**, risk 12 points (8.22%).

**Targets:** TP1 **176** (2.50R), TP2 **224** (6.50R), TP3 **230** (7.00R). Recommended base-case RR: **6.50R**.

**Why entry:** Hybrid entry uses close 134 and ATR14 59.8: buy zone 113–146. Entry is valid only if price can trade/hold around 146 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 134 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 176 (2.50R), TP2 224 (6.50R), TP3 230 (7.00R). Targets are ATR/structure capped for hold_days=1. ATR14=59.8, resistance_5/10/20/60=224/540/620/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.96% > max 8.00%; entry-to-stop risk 8.22% exceeds max strategy risk 8.00%; volume ratio 0.42 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.588 vs policy min 0.30 · **Close:** 256 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.32 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 240–266, entry trigger **266**, stop **244**, risk 22 points (8.27%).

**Targets:** TP1 **288** (1.00R), TP2 **372** (4.82R), TP3 **384** (5.36R). Recommended base-case RR: **4.82R**.

**Why entry:** Hybrid entry uses close 256 and ATR14 43.7: buy zone 240–266. Entry is valid only if price can trade/hold around 266 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 244 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 288 (1.00R), TP2 372 (4.82R), TP3 384 (5.36R). Targets are ATR/structure capped for hold_days=3. ATR14=43.7, resistance_5/10/20/60=372/432/466/468. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.32 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — swing_continual_defensive — NO_TRADE

**Score:** 0.588 vs policy min 0.30 · **Close:** 256 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 240–266, entry trigger **266**, stop **244**, risk 22 points (8.27%).

**Targets:** TP1 **288** (1.00R), TP2 **304** (1.73R), TP3 **372** (4.82R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 256 and ATR14 43.7: buy zone 240–266. Entry is valid only if price can trade/hold around 266 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 244 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 288 (1.00R), TP2 304 (1.73R), TP3 372 (4.82R). Targets are ATR/structure capped for hold_days=1. ATR14=43.7, resistance_5/10/20/60=372/432/466/468. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.32 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.570 vs policy min 0.30 · **Close:** 262 · **ATR14:** 45.2 · **Volume ratio 20D:** 0.92 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 246–272, entry trigger **272**, stop **250**, risk 22 points (8.09%).

**Targets:** TP1 **352** (3.64R), TP2 **364** (4.18R), TP3 **376** (4.73R). Recommended base-case RR: **4.18R**.

**Why entry:** Hybrid entry uses close 262 and ATR14 45.2: buy zone 246–272. Entry is valid only if price can trade/hold around 272 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 250 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 352 (3.64R), TP2 364 (4.18R), TP3 376 (4.73R). Targets are ATR/structure capped for hold_days=5. ATR14=45.2, resistance_5/10/20/60=352/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CTTH — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.517 vs policy min 0.30 · **Close:** 112 · **ATR14:** 95.4 · **Volume ratio 20D:** 0.97 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 78–132, entry trigger **132**, stop **121**, risk 11 points (8.33%).

**Targets:** TP1 **180** (4.36R), TP2 **186** (4.91R), TP3 **192** (5.45R). Recommended base-case RR: **4.91R**.

**Why entry:** Hybrid entry uses close 112 and ATR14 95.4: buy zone 78–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 121 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 180 (4.36R), TP2 186 (4.91R), TP3 192 (5.45R). Targets are ATR/structure capped for hold_days=5. ATR14=95.4, resistance_5/10/20/60=176/182/216/216. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 17.86% > max 8.00%; entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.510 vs policy min 0.30 · **Close:** 137 · **ATR14:** 22.9 · **Volume ratio 20D:** 0.47 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 128–142, entry trigger **142**, stop **130**, risk 12 points (8.45%).

**Targets:** TP1 **190** (4.00R), TP2 **196** (4.50R), TP3 **202** (5.00R). Recommended base-case RR: **4.50R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 22.9: buy zone 128–142. Entry is valid only if price can trade/hold around 142 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 130 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (4.00R), TP2 196 (4.50R), TP3 202 (5.00R). Targets are ATR/structure capped for hold_days=5. ATR14=22.9, resistance_5/10/20/60=190/212/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.45% exceeds max strategy risk 8.00%; volume ratio 0.47 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_20d_continual_research — NO_TRADE

**Score:** 0.383 vs policy min 0.30 · **Close:** 298 · **ATR14:** 46.3 · **Volume ratio 20D:** 0.89 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 280–308, entry trigger **308**, stop **288**, risk 20 points (6.49%).

**Targets:** TP1 **410** (5.10R), TP2 **420** (5.60R), TP3 **430** (6.10R). Recommended base-case RR: **5.60R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 46.3: buy zone 280–308. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 288 is placed below support structure (290 / 290). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 410 (5.10R), TP2 420 (5.60R), TP3 430 (6.10R). Targets are ATR/structure capped for hold_days=10. ATR14=46.3, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.358 vs policy min 0.30 · **Close:** 640 · **ATR14:** 106.8 · **Volume ratio 20D:** 0.73 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 600–665, entry trigger **665**, stop **635**, risk 30 points (4.51%).

**Targets:** TP1 **950** (9.50R), TP2 **965** (10.00R), TP3 **980** (10.50R). Recommended base-case RR: **10.00R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 106.8: buy zone 600–665. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 635 is placed below support structure (640 / 640). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 950 (9.50R), TP2 965 (10.00R), TP3 980 (10.50R). Targets are ATR/structure capped for hold_days=10. ATR14=106.8, resistance_5/10/20/60=950/950/1,230/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GTSI — momentum_20d_continual_research — NO_TRADE

**Score:** 0.341 vs policy min 0.30 · **Close:** 109 · **ATR14:** 20.3 · **Volume ratio 20D:** 0.87 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **104**, risk 10 points (8.77%).

**Targets:** TP1 **164** (5.00R), TP2 **169** (5.50R), TP3 **174** (6.00R). Recommended base-case RR: **5.50R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 20.3: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 104 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 164 (5.00R), TP2 169 (5.50R), TP3 174 (6.00R). Targets are ATR/structure capped for hold_days=10. ATR14=20.3, resistance_5/10/20/60=164/192/238/334. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.77% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PACK — momentum_20d_continual_research — NO_TRADE

**Score:** 0.328 vs policy min 0.30 · **Close:** 222 · **ATR14:** 41.9 · **Volume ratio 20D:** 0.92 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 206–232, entry trigger **232**, stop **220**, risk 12 points (5.17%).

**Targets:** TP1 **330** (8.17R), TP2 **336** (8.67R), TP3 **342** (9.17R). Recommended base-case RR: **8.67R**.

**Why entry:** Hybrid entry uses close 222 and ATR14 41.9: buy zone 206–232. Entry is valid only if price can trade/hold around 232 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 220 is placed below support structure (222 / 216). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 330 (8.17R), TP2 336 (8.67R), TP3 342 (9.17R). Targets are ATR/structure capped for hold_days=10. ATR14=41.9, resistance_5/10/20/60=330/406/406/406. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## HUMI — momentum_20d_continual_research — NO_TRADE

**Score:** 0.326 vs policy min 0.30 · **Close:** 100 · **ATR14:** 18.4 · **Volume ratio 20D:** 0.80 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 93–104, entry trigger **104**, stop **96**, risk 8 points (7.69%).

**Targets:** TP1 **151** (5.88R), TP2 **155** (6.38R), TP3 **159** (6.88R). Recommended base-case RR: **6.38R**.

**Why entry:** Hybrid entry uses close 100 and ATR14 18.4: buy zone 93–104. Entry is valid only if price can trade/hold around 104 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 96 is placed below support structure (97 / 97). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 151 (5.88R), TP2 155 (6.38R), TP3 159 (6.88R). Targets are ATR/structure capped for hold_days=10. ATR14=18.4, resistance_5/10/20/60=151/174/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRIN — position_continual — NO_TRADE

**Score:** 0.321 vs policy min 0.30 · **Close:** 312 · **ATR14:** 67.4 · **Volume ratio 20D:** 1.59 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 288–326, entry trigger **326**, stop **298**, risk 28 points (8.59%).

**Targets:** TP1 **486** (5.71R), TP2 **500** (6.21R), TP3 **515** (6.75R). Recommended base-case RR: **6.21R**.

**Why entry:** Hybrid entry uses close 312 and ATR14 67.4: buy zone 288–326. Entry is valid only if price can trade/hold around 326 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 298 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 486 (5.71R), TP2 500 (6.21R), TP3 515 (6.75R). Targets are ATR/structure capped for hold_days=10. ATR14=67.4, resistance_5/10/20/60=486/580/715/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.59% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — NO_TRADE

**Score:** 0.317 vs policy min 0.30 · **Close:** 262 · **ATR14:** 45.2 · **Volume ratio 20D:** 0.92 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 246–272, entry trigger **272**, stop **250**, risk 22 points (8.09%).

**Targets:** TP1 **352** (3.64R), TP2 **364** (4.18R), TP3 **376** (4.73R). Recommended base-case RR: **4.18R**.

**Why entry:** Hybrid entry uses close 262 and ATR14 45.2: buy zone 246–272. Entry is valid only if price can trade/hold around 272 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 250 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 352 (3.64R), TP2 364 (4.18R), TP3 376 (4.73R). Targets are ATR/structure capped for hold_days=10. ATR14=45.2, resistance_5/10/20/60=352/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — position_continual — NO_TRADE

**Score:** 0.316 vs policy min 0.30 · **Close:** 109 · **ATR14:** 20.3 · **Volume ratio 20D:** 0.87 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 101–114, entry trigger **114**, stop **104**, risk 10 points (8.77%).

**Targets:** TP1 **164** (5.00R), TP2 **169** (5.50R), TP3 **174** (6.00R). Recommended base-case RR: **5.50R**.

**Why entry:** Hybrid entry uses close 109 and ATR14 20.3: buy zone 101–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 104 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 164 (5.00R), TP2 169 (5.50R), TP3 174 (6.00R). Targets are ATR/structure capped for hold_days=10. ATR14=20.3, resistance_5/10/20/60=164/192/238/334. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.77% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — position_continual — NO_TRADE

**Score:** 0.309 vs policy min 0.30 · **Close:** 137 · **ATR14:** 22.9 · **Volume ratio 20D:** 0.47 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 128–142, entry trigger **142**, stop **130**, risk 12 points (8.45%).

**Targets:** TP1 **190** (4.00R), TP2 **196** (4.50R), TP3 **202** (5.00R). Recommended base-case RR: **4.50R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 22.9: buy zone 128–142. Entry is valid only if price can trade/hold around 142 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 130 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (4.00R), TP2 196 (4.50R), TP3 202 (5.00R). Targets are ATR/structure capped for hold_days=10. ATR14=22.9, resistance_5/10/20/60=190/212/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.45% exceeds max strategy risk 8.00%; volume ratio 0.47 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## APIC — position_continual — NO_TRADE

**Score:** 0.305 vs policy min 0.30 · **Close:** 515 · **ATR14:** 227.5 · **Volume ratio 20D:** 2.13 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 434–565, entry trigger **565**, stop **515**, risk 50 points (8.85%).

**Targets:** TP1 **1,200** (12.70R), TP2 **1,225** (13.20R), TP3 **1,250** (13.70R). Recommended base-case RR: **13.20R**.

**Why entry:** Hybrid entry uses close 515 and ATR14 227.5: buy zone 434–565. Entry is valid only if price can trade/hold around 565 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,200 (12.70R), TP2 1,225 (13.20R), TP3 1,250 (13.70R). Targets are ATR/structure capped for hold_days=10. ATR14=227.5, resistance_5/10/20/60=1,200/1,725/2,090/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 9.71% > max 8.00%; entry-to-stop risk 8.85% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---
