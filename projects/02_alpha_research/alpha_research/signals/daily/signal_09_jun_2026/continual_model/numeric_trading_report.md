# Numeric Trading Desk Report — 2026-06-08

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 13 |
| CONDITIONAL | 6 |
| NO_TRADE | 23 |

## ELPI — ara_candidate_continual — ACTIONABLE

**Score:** 0.870 vs policy min 0.50 · **Close:** 960 · **ATR14:** 213.6 · **Volume ratio 20D:** 0.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 885–1,005, entry trigger **1,005**, stop **955**, risk 50 points (4.98%).

**Targets:** TP1 **1,115** (2.20R), TP2 **1,140** (2.70R), TP3 **1,165** (3.20R). Recommended base-case RR: **2.70R**.

**Why entry:** Hybrid entry uses close 960 and ATR14 213.6: buy zone 885–1,005. Entry is valid only if price can trade/hold around 1,005 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 955 is placed below support structure (960 / 960). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,115 (2.20R), TP2 1,140 (2.70R), TP3 1,165 (3.20R). Targets are ATR/structure capped for hold_days=1. ATR14=213.6, resistance_5/10/20/60=1,735/1,790/2,030/2,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UVCR — scalping_continual_defensive — ACTIONABLE

**Score:** 0.705 vs policy min 0.05 · **Close:** 144 · **ATR14:** 17.1 · **Volume ratio 20D:** 1.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 138–148, entry trigger **148**, stop **143**, risk 5 points (3.38%).

**Targets:** TP1 **157** (1.80R), TP2 **160** (2.40R), TP3 **163** (3.00R). Recommended base-case RR: **2.40R**.

**Why entry:** Hybrid entry uses close 144 and ATR14 17.1: buy zone 138–148. Entry is valid only if price can trade/hold around 148 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 143 is placed below support structure (144 / 144). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 157 (1.80R), TP2 160 (2.40R), TP3 163 (3.00R). Targets are ATR/structure capped for hold_days=1. ATR14=17.1, resistance_5/10/20/60=250/250/250/250. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.563 vs policy min 0.30 · **Close:** 220 · **ATR14:** 43.4 · **Volume ratio 20D:** 0.66 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 204–230, entry trigger **230**, stop **216**, risk 14 points (6.09%).

**Targets:** TP1 **252** (1.57R), TP2 **366** (9.71R), TP3 **372** (10.14R). Recommended base-case RR: **9.71R**.

**Why entry:** Hybrid entry uses close 220 and ATR14 43.4: buy zone 204–230. Entry is valid only if price can trade/hold around 230 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 252 (1.57R), TP2 366 (9.71R), TP3 372 (10.14R). Targets are ATR/structure capped for hold_days=3. ATR14=43.4, resistance_5/10/20/60=372/432/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — swing_continual_defensive — ACTIONABLE

**Score:** 0.563 vs policy min 0.30 · **Close:** 220 · **ATR14:** 43.4 · **Volume ratio 20D:** 0.66 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 204–230, entry trigger **230**, stop **216**, risk 14 points (6.09%).

**Targets:** TP1 **252** (1.57R), TP2 **254** (1.71R), TP3 **264** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 220 and ATR14 43.4: buy zone 204–230. Entry is valid only if price can trade/hold around 230 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 252 (1.57R), TP2 254 (1.71R), TP3 264 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=43.4, resistance_5/10/20/60=372/432/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.562 vs policy min 0.30 · **Close:** 220 · **ATR14:** 43.4 · **Volume ratio 20D:** 0.66 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 204–230, entry trigger **230**, stop **216**, risk 14 points (6.09%).

**Targets:** TP1 **252** (1.57R), TP2 **372** (10.14R), TP3 **380** (10.71R). Recommended base-case RR: **10.14R**.

**Why entry:** Hybrid entry uses close 220 and ATR14 43.4: buy zone 204–230. Entry is valid only if price can trade/hold around 230 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 252 (1.57R), TP2 372 (10.14R), TP3 380 (10.71R). Targets are ATR/structure capped for hold_days=5. ATR14=43.4, resistance_5/10/20/60=372/432/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PSKT — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.553 vs policy min 0.30 · **Close:** 146 · **ATR14:** 26.3 · **Volume ratio 20D:** 0.67 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 136–152, entry trigger **152**, stop **144**, risk 8 points (5.26%).

**Targets:** TP1 **166** (1.75R), TP2 **230** (9.75R), TP3 **234** (10.25R). Recommended base-case RR: **9.75R**.

**Why entry:** Hybrid entry uses close 146 and ATR14 26.3: buy zone 136–152. Entry is valid only if price can trade/hold around 152 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 144 is placed below support structure (145 / 145). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 166 (1.75R), TP2 230 (9.75R), TP3 234 (10.25R). Targets are ATR/structure capped for hold_days=3. ATR14=26.3, resistance_5/10/20/60=230/234/270/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PSKT — swing_continual_defensive — ACTIONABLE

**Score:** 0.553 vs policy min 0.30 · **Close:** 146 · **ATR14:** 26.3 · **Volume ratio 20D:** 0.67 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 136–152, entry trigger **152**, stop **144**, risk 8 points (5.26%).

**Targets:** TP1 **166** (1.75R), TP2 **170** (2.25R), TP3 **172** (2.50R). Recommended base-case RR: **2.25R**.

**Why entry:** Hybrid entry uses close 146 and ATR14 26.3: buy zone 136–152. Entry is valid only if price can trade/hold around 152 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 144 is placed below support structure (145 / 145). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 166 (1.75R), TP2 170 (2.25R), TP3 172 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=26.3, resistance_5/10/20/60=230/234/270/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ELPI — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.551 vs policy min 0.30 · **Close:** 960 · **ATR14:** 213.6 · **Volume ratio 20D:** 0.73 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 885–1,005, entry trigger **1,005**, stop **955**, risk 50 points (4.98%).

**Targets:** TP1 **1,115** (2.20R), TP2 **1,675** (13.40R), TP3 **1,735** (14.60R). Recommended base-case RR: **13.40R**.

**Why entry:** Hybrid entry uses close 960 and ATR14 213.6: buy zone 885–1,005. Entry is valid only if price can trade/hold around 1,005 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 955 is placed below support structure (960 / 960). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,115 (2.20R), TP2 1,675 (13.40R), TP3 1,735 (14.60R). Targets are ATR/structure capped for hold_days=3. ATR14=213.6, resistance_5/10/20/60=1,735/1,790/2,030/2,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## ELPI — swing_continual_defensive — ACTIONABLE

**Score:** 0.551 vs policy min 0.30 · **Close:** 960 · **ATR14:** 213.6 · **Volume ratio 20D:** 0.73 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 885–1,005, entry trigger **1,005**, stop **955**, risk 50 points (4.98%).

**Targets:** TP1 **1,115** (2.20R), TP2 **1,140** (2.70R), TP3 **1,165** (3.20R). Recommended base-case RR: **2.70R**.

**Why entry:** Hybrid entry uses close 960 and ATR14 213.6: buy zone 885–1,005. Entry is valid only if price can trade/hold around 1,005 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 955 is placed below support structure (960 / 960). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,115 (2.20R), TP2 1,140 (2.70R), TP3 1,165 (3.20R). Targets are ATR/structure capped for hold_days=1. ATR14=213.6, resistance_5/10/20/60=1,735/1,790/2,030/2,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## VKTR — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.548 vs policy min 0.30 · **Close:** 535 · **ATR14:** 96.4 · **Volume ratio 20D:** 1.22 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 500–555, entry trigger **555**, stop **520**, risk 35 points (6.31%).

**Targets:** TP1 **605** (1.43R), TP2 **830** (7.86R), TP3 **850** (8.43R). Recommended base-case RR: **7.86R**.

**Why entry:** Hybrid entry uses close 535 and ATR14 96.4: buy zone 500–555. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 520 is placed below support structure (525 / 525). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 605 (1.43R), TP2 830 (7.86R), TP3 850 (8.43R). Targets are ATR/structure capped for hold_days=5. ATR14=96.4, resistance_5/10/20/60=830/830/995/1,090. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BBYB — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.547 vs policy min 0.30 · **Close:** 192 · **ATR14:** 19.5 · **Volume ratio 20D:** 1.96 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 185–196, entry trigger **196**, stop **188**, risk 8 points (4.08%).

**Targets:** TP1 **206** (1.25R), TP2 **268** (9.00R), TP3 **272** (9.50R). Recommended base-case RR: **9.00R**.

**Why entry:** Hybrid entry uses close 192 and ATR14 19.5: buy zone 185–196. Entry is valid only if price can trade/hold around 196 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 188 is placed below support structure (189 / 189). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 206 (1.25R), TP2 268 (9.00R), TP3 272 (9.50R). Targets are ATR/structure capped for hold_days=5. ATR14=19.5, resistance_5/10/20/60=268/282/324/376. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## OASA — position_continual — ACTIONABLE

**Score:** 0.338 vs policy min 0.30 · **Close:** 220 · **ATR14:** 43.4 · **Volume ratio 20D:** 0.66 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 204–230, entry trigger **230**, stop **216**, risk 14 points (6.09%).

**Targets:** TP1 **368** (9.86R), TP2 **372** (10.14R), TP3 **380** (10.71R). Recommended base-case RR: **10.14R**.

**Why entry:** Hybrid entry uses close 220 and ATR14 43.4: buy zone 204–230. Entry is valid only if price can trade/hold around 230 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is placed below support structure (218 / 218). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 368 (9.86R), TP2 372 (10.14R), TP3 380 (10.71R). Targets are ATR/structure capped for hold_days=10. ATR14=43.4, resistance_5/10/20/60=372/432/466/466. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PSKT — position_continual — ACTIONABLE

**Score:** 0.326 vs policy min 0.30 · **Close:** 146 · **ATR14:** 26.3 · **Volume ratio 20D:** 0.67 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 136–152, entry trigger **152**, stop **144**, risk 8 points (5.26%).

**Targets:** TP1 **230** (9.75R), TP2 **234** (10.25R), TP3 **238** (10.75R). Recommended base-case RR: **10.25R**.

**Why entry:** Hybrid entry uses close 146 and ATR14 26.3: buy zone 136–152. Entry is valid only if price can trade/hold around 152 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 144 is placed below support structure (145 / 145). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 230 (9.75R), TP2 234 (10.25R), TP3 238 (10.75R). Targets are ATR/structure capped for hold_days=10. ATR14=26.3, resistance_5/10/20/60=230/234/270/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.693 vs policy min 0.05 · **Close:** 550 · **ATR14:** 124.3 · **Volume ratio 20D:** 0.93 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 505–575, entry trigger **575**, stop **530**, risk 45 points (7.83%).

**Targets:** TP1 **640** (1.44R), TP2 **655** (1.78R), TP3 **890** (7.00R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 550 and ATR14 124.3: buy zone 505–575. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 530 is placed below support structure (535 / 535). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 640 (1.44R), TP2 655 (1.78R), TP3 890 (7.00R). Targets are ATR/structure capped for hold_days=1. ATR14=124.3, resistance_5/10/20/60=895/895/1,175/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.573 vs policy min 0.30 · **Close:** 550 · **ATR14:** 124.3 · **Volume ratio 20D:** 0.93 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 505–575, entry trigger **575**, stop **530**, risk 45 points (7.83%).

**Targets:** TP1 **640** (1.44R), TP2 **895** (7.11R), TP3 **920** (7.67R). Recommended base-case RR: **7.11R**.

**Why entry:** Hybrid entry uses close 550 and ATR14 124.3: buy zone 505–575. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 530 is placed below support structure (535 / 535). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 640 (1.44R), TP2 895 (7.11R), TP3 920 (7.67R). Targets are ATR/structure capped for hold_days=3. ATR14=124.3, resistance_5/10/20/60=895/895/1,175/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — swing_continual_defensive — CONDITIONAL

**Score:** 0.573 vs policy min 0.30 · **Close:** 550 · **ATR14:** 124.3 · **Volume ratio 20D:** 0.93 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 505–575, entry trigger **575**, stop **530**, risk 45 points (7.83%).

**Targets:** TP1 **640** (1.44R), TP2 **655** (1.78R), TP3 **890** (7.00R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 550 and ATR14 124.3: buy zone 505–575. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 530 is placed below support structure (535 / 535). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 640 (1.44R), TP2 655 (1.78R), TP3 890 (7.00R). Targets are ATR/structure capped for hold_days=1. ATR14=124.3, resistance_5/10/20/60=895/895/1,175/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.566 vs policy min 0.30 · **Close:** 550 · **ATR14:** 124.3 · **Volume ratio 20D:** 0.93 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 505–575, entry trigger **575**, stop **530**, risk 45 points (7.83%).

**Targets:** TP1 **855** (6.22R), TP2 **895** (7.11R), TP3 **920** (7.67R). Recommended base-case RR: **7.11R**.

**Why entry:** Hybrid entry uses close 550 and ATR14 124.3: buy zone 505–575. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 530 is placed below support structure (535 / 535). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 855 (6.22R), TP2 895 (7.11R), TP3 920 (7.67R). Targets are ATR/structure capped for hold_days=5. ATR14=124.3, resistance_5/10/20/60=895/895/1,175/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## COIN — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.524 vs policy min 0.30 · **Close:** 590 · **ATR14:** 94.3 · **Volume ratio 20D:** 0.53 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 555–610, entry trigger **610**, stop **585**, risk 25 points (4.10%).

**Targets:** TP1 **825** (8.60R), TP2 **850** (9.60R), TP3 **865** (10.20R). Recommended base-case RR: **9.60R**.

**Why entry:** Hybrid entry uses close 590 and ATR14 94.3: buy zone 555–610. Entry is valid only if price can trade/hold around 610 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 585 is placed below support structure (590 / 590). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 825 (8.60R), TP2 850 (9.60R), TP3 865 (10.20R). Targets are ATR/structure capped for hold_days=5. ATR14=94.3, resistance_5/10/20/60=850/905/1,370/1,655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.53 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — position_continual — CONDITIONAL

**Score:** 0.339 vs policy min 0.30 · **Close:** 550 · **ATR14:** 124.3 · **Volume ratio 20D:** 0.93 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 505–575, entry trigger **575**, stop **530**, risk 45 points (7.83%).

**Targets:** TP1 **895** (7.11R), TP2 **920** (7.67R), TP3 **945** (8.22R). Recommended base-case RR: **7.67R**.

**Why entry:** Hybrid entry uses close 550 and ATR14 124.3: buy zone 505–575. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 530 is placed below support structure (535 / 535). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 895 (7.11R), TP2 920 (7.67R), TP3 945 (8.22R). Targets are ATR/structure capped for hold_days=10. ATR14=124.3, resistance_5/10/20/60=895/895/1,175/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BULL — scalping_continual_defensive — NO_TRADE

**Score:** 0.701 vs policy min 0.05 · **Close:** 272 · **ATR14:** 46.6 · **Volume ratio 20D:** 0.72 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 254–282, entry trigger **282**, stop **258**, risk 24 points (8.51%).

**Targets:** TP1 **306** (1.00R), TP2 **324** (1.75R), TP3 **400** (4.92R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 272 and ATR14 46.6: buy zone 254–282. Entry is valid only if price can trade/hold around 282 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 258 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 306 (1.00R), TP2 324 (1.75R), TP3 400 (4.92R). Targets are ATR/structure capped for hold_days=1. ATR14=46.6, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.51% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## PACK — scalping_continual_defensive — NO_TRADE

**Score:** 0.696 vs policy min 0.05 · **Close:** 206 · **ATR14:** 40.6 · **Volume ratio 20D:** 0.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 191–216, entry trigger **216**, stop **198**, risk 18 points (8.33%).

**Targets:** TP1 **238** (1.22R), TP2 **248** (1.78R), TP3 **318** (5.67R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 206 and ATR14 40.6: buy zone 191–216. Entry is valid only if price can trade/hold around 216 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 198 is placed below support structure (200 / 200). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 238 (1.22R), TP2 248 (1.78R), TP3 318 (5.67R). Targets are ATR/structure capped for hold_days=1. ATR14=40.6, resistance_5/10/20/60=330/330/406/406. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — scalping_continual_defensive — NO_TRADE

**Score:** 0.694 vs policy min 0.05 · **Close:** 157 · **ATR14:** 26.4 · **Volume ratio 20D:** 1.17 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 147–163, entry trigger **163**, stop **149**, risk 14 points (8.59%).

**Targets:** TP1 **177** (1.00R), TP2 **187** (1.71R), TP3 **197** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 26.4: buy zone 147–163. Entry is valid only if price can trade/hold around 163 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 149 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 177 (1.00R), TP2 187 (1.71R), TP3 197 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=26.4, resistance_5/10/20/60=244/262/334/382. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.59% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## COCO — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.572 vs policy min 0.30 · **Close:** 158 · **ATR14:** 34.7 · **Volume ratio 20D:** 0.51 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 145–165, entry trigger **165**, stop **151**, risk 14 points (8.48%).

**Targets:** TP1 **183** (1.29R), TP2 **256** (6.50R), TP3 **264** (7.07R). Recommended base-case RR: **6.50R**.

**Why entry:** Hybrid entry uses close 158 and ATR14 34.7: buy zone 145–165. Entry is valid only if price can trade/hold around 165 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 151 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 183 (1.29R), TP2 256 (6.50R), TP3 264 (7.07R). Targets are ATR/structure capped for hold_days=3. ATR14=34.7, resistance_5/10/20/60=256/274/402/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.48% exceeds max strategy risk 8.00%; volume ratio 0.51 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## COCO — swing_continual_defensive — NO_TRADE

**Score:** 0.572 vs policy min 0.30 · **Close:** 158 · **ATR14:** 34.7 · **Volume ratio 20D:** 0.51 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 145–165, entry trigger **165**, stop **151**, risk 14 points (8.48%).

**Targets:** TP1 **183** (1.29R), TP2 **189** (1.71R), TP3 **252** (6.21R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 158 and ATR14 34.7: buy zone 145–165. Entry is valid only if price can trade/hold around 165 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 151 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 183 (1.29R), TP2 189 (1.71R), TP3 252 (6.21R). Targets are ATR/structure capped for hold_days=1. ATR14=34.7, resistance_5/10/20/60=256/274/402/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.48% exceeds max strategy risk 8.00%; volume ratio 0.51 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## FUTR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.562 vs policy min 0.30 · **Close:** 105 · **ATR14:** 25.0 · **Volume ratio 20D:** 2.03 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 96–110, entry trigger **110**, stop **101**, risk 9 points (8.18%).

**Targets:** TP1 **123** (1.44R), TP2 **184** (8.22R), TP3 **189** (8.78R). Recommended base-case RR: **8.22R**.

**Why entry:** Hybrid entry uses close 105 and ATR14 25.0: buy zone 96–110. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 123 (1.44R), TP2 184 (8.22R), TP3 189 (8.78R). Targets are ATR/structure capped for hold_days=3. ATR14=25.0, resistance_5/10/20/60=184/214/246/330. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## FUTR — swing_continual_defensive — NO_TRADE

**Score:** 0.562 vs policy min 0.30 · **Close:** 105 · **ATR14:** 25.0 · **Volume ratio 20D:** 2.03 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 96–110, entry trigger **110**, stop **101**, risk 9 points (8.18%).

**Targets:** TP1 **123** (1.44R), TP2 **126** (1.78R), TP3 **132** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 105 and ATR14 25.0: buy zone 96–110. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 123 (1.44R), TP2 126 (1.78R), TP3 132 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=25.0, resistance_5/10/20/60=184/214/246/330. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.553 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.5 · **Volume ratio 20D:** 0.95 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **117** (1.22R), TP2 **158** (5.78R), TP3 **163** (6.33R). Recommended base-case RR: **5.78R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.5: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 117 (1.22R), TP2 158 (5.78R), TP3 163 (6.33R). Targets are ATR/structure capped for hold_days=3. ATR14=20.5, resistance_5/10/20/60=158/189/238/332. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — swing_continual_defensive — NO_TRADE

**Score:** 0.553 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.5 · **Volume ratio 20D:** 0.95 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **117** (1.22R), TP2 **122** (1.78R), TP3 **158** (5.78R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.5: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 117 (1.22R), TP2 122 (1.78R), TP3 158 (5.78R). Targets are ATR/structure capped for hold_days=1. ATR14=20.5, resistance_5/10/20/60=158/189/238/332. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.550 vs policy min 0.30 · **Close:** 157 · **ATR14:** 26.4 · **Volume ratio 20D:** 1.17 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 147–163, entry trigger **163**, stop **149**, risk 14 points (8.59%).

**Targets:** TP1 **177** (1.00R), TP2 **244** (5.79R), TP3 **252** (6.36R). Recommended base-case RR: **5.79R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 26.4: buy zone 147–163. Entry is valid only if price can trade/hold around 163 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 149 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 177 (1.00R), TP2 244 (5.79R), TP3 252 (6.36R). Targets are ATR/structure capped for hold_days=5. ATR14=26.4, resistance_5/10/20/60=244/262/334/382. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.59% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.531 vs policy min 0.30 · **Close:** 250 · **ATR14:** 46.1 · **Volume ratio 20D:** 0.77 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 232–260, entry trigger **260**, stop **238**, risk 22 points (8.46%).

**Targets:** TP1 **352** (4.18R), TP2 **364** (4.73R), TP3 **376** (5.27R). Recommended base-case RR: **4.73R**.

**Why entry:** Hybrid entry uses close 250 and ATR14 46.1: buy zone 232–260. Entry is valid only if price can trade/hold around 260 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 238 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 352 (4.18R), TP2 364 (4.73R), TP3 376 (5.27R). Targets are ATR/structure capped for hold_days=5. ATR14=46.1, resistance_5/10/20/60=352/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — momentum_20d_continual_research — NO_TRADE

**Score:** 0.398 vs policy min 0.30 · **Close:** 272 · **ATR14:** 46.6 · **Volume ratio 20D:** 0.72 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 254–282, entry trigger **282**, stop **258**, risk 24 points (8.51%).

**Targets:** TP1 **410** (5.33R), TP2 **422** (5.83R), TP3 **434** (6.33R). Recommended base-case RR: **5.83R**.

**Why entry:** Hybrid entry uses close 272 and ATR14 46.6: buy zone 254–282. Entry is valid only if price can trade/hold around 282 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 258 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 410 (5.33R), TP2 422 (5.83R), TP3 434 (6.33R). Targets are ATR/structure capped for hold_days=10. ATR14=46.6, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.51% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## FUTR — momentum_20d_continual_research — NO_TRADE

**Score:** 0.397 vs policy min 0.30 · **Close:** 105 · **ATR14:** 25.0 · **Volume ratio 20D:** 2.03 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 96–110, entry trigger **110**, stop **101**, risk 9 points (8.18%).

**Targets:** TP1 **184** (8.22R), TP2 **189** (8.78R), TP3 **194** (9.33R). Recommended base-case RR: **8.78R**.

**Why entry:** Hybrid entry uses close 105 and ATR14 25.0: buy zone 96–110. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 184 (8.22R), TP2 189 (8.78R), TP3 194 (9.33R). Targets are ATR/structure capped for hold_days=10. ATR14=25.0, resistance_5/10/20/60=184/214/246/330. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — momentum_20d_continual_research — NO_TRADE

**Score:** 0.385 vs policy min 0.30 · **Close:** 157 · **ATR14:** 26.4 · **Volume ratio 20D:** 1.17 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 147–163, entry trigger **163**, stop **149**, risk 14 points (8.59%).

**Targets:** TP1 **244** (5.79R), TP2 **252** (6.36R), TP3 **260** (6.93R). Recommended base-case RR: **6.36R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 26.4: buy zone 147–163. Entry is valid only if price can trade/hold around 163 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 149 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 244 (5.79R), TP2 252 (6.36R), TP3 260 (6.93R). Targets are ATR/structure capped for hold_days=10. ATR14=26.4, resistance_5/10/20/60=244/262/334/382. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.59% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.383 vs policy min 0.30 · **Close:** 550 · **ATR14:** 124.3 · **Volume ratio 20D:** 0.93 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 505–575, entry trigger **575**, stop **530**, risk 45 points (7.83%).

**Targets:** TP1 **895** (7.11R), TP2 **920** (7.67R), TP3 **945** (8.22R). Recommended base-case RR: **7.67R**.

**Why entry:** Hybrid entry uses close 550 and ATR14 124.3: buy zone 505–575. Entry is valid only if price can trade/hold around 575 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 530 is placed below support structure (535 / 535). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 895 (7.11R), TP2 920 (7.67R), TP3 945 (8.22R). Targets are ATR/structure capped for hold_days=10. ATR14=124.3, resistance_5/10/20/60=895/895/1,175/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GTSI — momentum_20d_continual_research — NO_TRADE

**Score:** 0.373 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.5 · **Volume ratio 20D:** 0.95 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **158** (5.78R), TP2 **163** (6.33R), TP3 **168** (6.89R). Recommended base-case RR: **6.33R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.5: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 158 (5.78R), TP2 163 (6.33R), TP3 168 (6.89R). Targets are ATR/structure capped for hold_days=10. ATR14=20.5, resistance_5/10/20/60=158/189/238/332. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.49% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BULL — position_continual — NO_TRADE

**Score:** 0.352 vs policy min 0.30 · **Close:** 272 · **ATR14:** 46.6 · **Volume ratio 20D:** 0.72 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 254–282, entry trigger **282**, stop **258**, risk 24 points (8.51%).

**Targets:** TP1 **410** (5.33R), TP2 **422** (5.83R), TP3 **434** (6.33R). Recommended base-case RR: **5.83R**.

**Why entry:** Hybrid entry uses close 272 and ATR14 46.6: buy zone 254–282. Entry is valid only if price can trade/hold around 282 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 258 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 410 (5.33R), TP2 422 (5.83R), TP3 434 (6.33R). Targets are ATR/structure capped for hold_days=10. ATR14=46.6, resistance_5/10/20/60=410/428/545/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.51% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — position_continual — NO_TRADE

**Score:** 0.349 vs policy min 0.30 · **Close:** 128 · **ATR14:** 22.9 · **Volume ratio 20D:** 0.56 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 120–133, entry trigger **133**, stop **122**, risk 11 points (8.27%).

**Targets:** TP1 **190** (5.18R), TP2 **196** (5.73R), TP3 **202** (6.27R). Recommended base-case RR: **5.73R**.

**Why entry:** Hybrid entry uses close 128 and ATR14 22.9: buy zone 120–133. Entry is valid only if price can trade/hold around 133 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 122 is placed below support structure (123 / 123). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (5.18R), TP2 196 (5.73R), TP3 202 (6.27R). Targets are ATR/structure capped for hold_days=10. ATR14=22.9, resistance_5/10/20/60=190/208/262/306. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%; volume ratio 0.56 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## INET — position_continual — NO_TRADE

**Score:** 0.340 vs policy min 0.30 · **Close:** 157 · **ATR14:** 26.4 · **Volume ratio 20D:** 1.17 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 147–163, entry trigger **163**, stop **149**, risk 14 points (8.59%).

**Targets:** TP1 **244** (5.79R), TP2 **252** (6.36R), TP3 **260** (6.93R). Recommended base-case RR: **6.36R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 26.4: buy zone 147–163. Entry is valid only if price can trade/hold around 163 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 149 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 244 (5.79R), TP2 252 (6.36R), TP3 260 (6.93R). Targets are ATR/structure capped for hold_days=10. ATR14=26.4, resistance_5/10/20/60=244/262/334/382. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.59% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## FUTR — position_continual — NO_TRADE

**Score:** 0.336 vs policy min 0.30 · **Close:** 105 · **ATR14:** 25.0 · **Volume ratio 20D:** 2.03 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 96–110, entry trigger **110**, stop **101**, risk 9 points (8.18%).

**Targets:** TP1 **184** (8.22R), TP2 **189** (8.78R), TP3 **194** (9.33R). Recommended base-case RR: **8.78R**.

**Why entry:** Hybrid entry uses close 105 and ATR14 25.0: buy zone 96–110. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 184 (8.22R), TP2 189 (8.78R), TP3 194 (9.33R). Targets are ATR/structure capped for hold_days=10. ATR14=25.0, resistance_5/10/20/60=184/214/246/330. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DEWA — position_continual — NO_TRADE

**Score:** 0.336 vs policy min 0.30 · **Close:** 250 · **ATR14:** 46.1 · **Volume ratio 20D:** 0.77 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 232–260, entry trigger **260**, stop **238**, risk 22 points (8.46%).

**Targets:** TP1 **352** (4.18R), TP2 **364** (4.73R), TP3 **376** (5.27R). Recommended base-case RR: **4.73R**.

**Why entry:** Hybrid entry uses close 250 and ATR14 46.1: buy zone 232–260. Entry is valid only if price can trade/hold around 260 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 238 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 352 (4.18R), TP2 364 (4.73R), TP3 376 (5.27R). Targets are ATR/structure capped for hold_days=10. ATR14=46.1, resistance_5/10/20/60=352/398/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## IRSX — position_continual — NO_TRADE

**Score:** 0.331 vs policy min 0.30 · **Close:** 242 · **ATR14:** 51.7 · **Volume ratio 20D:** 1.12 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 222–254, entry trigger **254**, stop **232**, risk 22 points (8.66%).

**Targets:** TP1 **386** (6.00R), TP2 **398** (6.55R), TP3 **410** (7.09R). Recommended base-case RR: **6.55R**.

**Why entry:** Hybrid entry uses close 242 and ATR14 51.7: buy zone 222–254. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 232 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 386 (6.00R), TP2 398 (6.55R), TP3 410 (7.09R). Targets are ATR/structure capped for hold_days=10. ATR14=51.7, resistance_5/10/20/60=386/460/480/620. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.66% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GTSI — position_continual — NO_TRADE

**Score:** 0.330 vs policy min 0.30 · **Close:** 101 · **ATR14:** 20.5 · **Volume ratio 20D:** 0.95 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 93–106, entry trigger **106**, stop **97**, risk 9 points (8.49%).

**Targets:** TP1 **158** (5.78R), TP2 **163** (6.33R), TP3 **168** (6.89R). Recommended base-case RR: **6.33R**.

**Why entry:** Hybrid entry uses close 101 and ATR14 20.5: buy zone 93–106. Entry is valid only if price can trade/hold around 106 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 97 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 158 (5.78R), TP2 163 (6.33R), TP3 168 (6.89R). Targets are ATR/structure capped for hold_days=10. ATR14=20.5, resistance_5/10/20/60=158/189/238/332. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.49% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---
