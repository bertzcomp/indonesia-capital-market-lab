# Numeric Trading Desk Report — 2026-06-04

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 6 |
| CONDITIONAL | 8 |
| WATCHLIST_ONLY | 5 |
| NO_TRADE | 37 |

## PSKT — swing_hgb_defensive — ACTIONABLE

**Score:** 0.771 vs policy min 0.50 · **Close:** 171 · **ATR14:** 24.9 · **Volume ratio 20D:** 0.82 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 159–174, entry trigger **174**, stop **168**, risk 6 points (3.45%).

**Targets:** TP1 **187** (2.17R), TP2 **190** (2.67R), TP3 **234** (10.00R). Recommended base-case RR: **2.67R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 171: zone 159–174 uses ATR14 24.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 174 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 168 is placed below support structure (169 / 169). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 187 (2.17R), TP2 190 (2.67R), TP3 234 (10.00R). Targets are ATR/structure capped for hold_days=1. ATR14=24.9, resistance_5/10/20/60=234/240/272/336. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TRIN — swing_hgb_defensive — ACTIONABLE

**Score:** 0.767 vs policy min 0.50 · **Close:** 332 · **ATR14:** 66.3 · **Volume ratio 20D:** 2.77 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 304–340, entry trigger **340**, stop **322**, risk 18 points (5.29%).

**Targets:** TP1 **374** (1.89R), TP2 **384** (2.44R), TP3 **486** (8.11R). Recommended base-case RR: **2.44R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 332: zone 304–340 uses ATR14 66.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 340 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is placed below support structure (324 / 324). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 374 (1.89R), TP2 384 (2.44R), TP3 486 (8.11R). Targets are ATR/structure capped for hold_days=1. ATR14=66.3, resistance_5/10/20/60=486/600/740/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## HUMI — swing_hgb_defensive — ACTIONABLE

**Score:** 0.743 vs policy min 0.50 · **Close:** 108 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.10 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 99–110, entry trigger **110**, stop **103**, risk 7 points (6.36%).

**Targets:** TP1 **120** (1.43R), TP2 **122** (1.71R), TP3 **156** (6.57R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 108: zone 99–110 uses ATR14 18.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is placed below support structure (104 / 104). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 120 (1.43R), TP2 122 (1.71R), TP3 156 (6.57R). Targets are ATR/structure capped for hold_days=1. ATR14=18.1, resistance_5/10/20/60=160/194/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## HUMI — position_xgb — ACTIONABLE

**Score:** 0.608 vs policy min 0.55 · **Close:** 108 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.10 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 99–110, entry trigger **110**, stop **103**, risk 7 points (6.36%).

**Targets:** TP1 **120** (1.43R), TP2 **154** (6.29R), TP3 **160** (7.14R). Recommended base-case RR: **6.29R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 108: zone 99–110 uses ATR14 18.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is placed below support structure (104 / 104). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 120 (1.43R), TP2 154 (6.29R), TP3 160 (7.14R). Targets are ATR/structure capped for hold_days=1. ATR14=18.1, resistance_5/10/20/60=160/194/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DGWG — position_xgb — ACTIONABLE

**Score:** 0.605 vs policy min 0.55 · **Close:** 298 · **ATR14:** 16.6 · **Volume ratio 20D:** 1.19 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 290–300, entry trigger **300**, stop **294**, risk 6 points (2.00%).

**Targets:** TP1 **310** (1.67R), TP2 **340** (6.67R), TP3 **344** (7.33R). Recommended base-case RR: **6.67R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 298: zone 290–300 uses ATR14 16.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 300 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 294 is placed below support structure (296 / 296). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 310 (1.67R), TP2 340 (6.67R), TP3 344 (7.33R). Targets are ATR/structure capped for hold_days=1. ATR14=16.6, resistance_5/10/20/60=344/352/402/500. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## STAA — position_xgb — ACTIONABLE

**Score:** 0.601 vs policy min 0.55 · **Close:** 905 · **ATR14:** 56.1 · **Volume ratio 20D:** 1.11 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 875–915, entry trigger **915**, stop **885**, risk 30 points (3.28%).

**Targets:** TP1 **995** (2.67R), TP2 **1,020** (3.50R), TP3 **1,035** (4.00R). Recommended base-case RR: **3.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 905: zone 875–915 uses ATR14 56.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 915 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 885 is placed below support structure (890 / 890). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 995 (2.67R), TP2 1,020 (3.50R), TP3 1,035 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=56.1, resistance_5/10/20/60=1,020/1,215/1,300/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TOBA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.762 vs policy min 0.50 · **Close:** 368 · **ATR14:** 38.6 · **Volume ratio 20D:** 1.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 350–372, entry trigger **372**, stop **354**, risk 18 points (4.84%).

**Targets:** TP1 **392** (1.11R), TP2 **442** (3.89R), TP3 **462** (5.00R). Recommended base-case RR: **3.89R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 368: zone 350–372 uses ATR14 38.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 372 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is placed below support structure (356 / 356). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 392 (1.11R), TP2 442 (3.89R), TP3 462 (5.00R). Targets are ATR/structure capped for hold_days=1. ATR14=38.6, resistance_5/10/20/60=462/530/650/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## STAA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.761 vs policy min 0.50 · **Close:** 905 · **ATR14:** 56.1 · **Volume ratio 20D:** 1.11 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 875–915, entry trigger **915**, stop **885**, risk 30 points (3.28%).

**Targets:** TP1 **945** (1.00R), TP2 **1,020** (3.50R), TP3 **1,035** (4.00R). Recommended base-case RR: **3.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 905: zone 875–915 uses ATR14 56.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 915 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 885 is placed below support structure (890 / 890). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 945 (1.00R), TP2 1,020 (3.50R), TP3 1,035 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=56.1, resistance_5/10/20/60=1,020/1,215/1,300/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## GOLF — position_xgb — CONDITIONAL

**Score:** 0.605 vs policy min 0.55 · **Close:** 133 · **ATR14:** 14.0 · **Volume ratio 20D:** 3.01 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 126–135, entry trigger **135**, stop **123**, risk 12 points (8.89%).

**Targets:** TP1 **147** (1.00R), TP2 **169** (2.83R), TP3 **170** (2.92R). Recommended base-case RR: **2.83R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 133: zone 126–135 uses ATR14 14.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 135 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 123 is placed below support structure (124 / 124). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 147 (1.00R), TP2 169 (2.83R), TP3 170 (2.92R). Targets are ATR/structure capped for hold_days=1. ATR14=14.0, resistance_5/10/20/60=170/185/198/214. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## VKTR — position_xgb — CONDITIONAL

**Score:** 0.603 vs policy min 0.55 · **Close:** 625 · **ATR14:** 90.4 · **Volume ratio 20D:** 1.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 580–635, entry trigger **635**, stop **580**, risk 55 points (8.66%).

**Targets:** TP1 **690** (1.00R), TP2 **830** (3.55R), TP3 **860** (4.09R). Recommended base-case RR: **3.55R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 625: zone 580–635 uses ATR14 90.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 580 is placed below support structure (585 / 585). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.00R), TP2 830 (3.55R), TP3 860 (4.09R). Targets are ATR/structure capped for hold_days=1. ATR14=90.4, resistance_5/10/20/60=830/885/995/1,090. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DOOH — position_xgb — CONDITIONAL

**Score:** 0.602 vs policy min 0.55 · **Close:** 115 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.79 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 107–117, entry trigger **117**, stop **107**, risk 10 points (8.55%).

**Targets:** TP1 **127** (1.00R), TP2 **150** (3.30R), TP3 **155** (3.80R). Recommended base-case RR: **3.30R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 115: zone 107–117 uses ATR14 17.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 117 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is placed below support structure (108 / 108). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 127 (1.00R), TP2 150 (3.30R), TP3 155 (3.80R). Targets are ATR/structure capped for hold_days=1. ATR14=17.4, resistance_5/10/20/60=150/154/189/197. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## AGRO — position_xgb — CONDITIONAL

**Score:** 0.602 vs policy min 0.55 · **Close:** 145 · **ATR14:** 7.7 · **Volume ratio 20D:** 1.29 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 141–146, entry trigger **146**, stop **141**, risk 5 points (3.42%).

**Targets:** TP1 **151** (1.00R), TP2 **165** (3.80R), TP3 **167** (4.20R). Recommended base-case RR: **3.80R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 145: zone 141–146 uses ATR14 7.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 146 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 141 is placed below support structure (142 / 142). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 151 (1.00R), TP2 165 (3.80R), TP3 167 (4.20R). Targets are ATR/structure capped for hold_days=1. ATR14=7.7, resistance_5/10/20/60=167/179/194/248. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TOBA — position_xgb — CONDITIONAL

**Score:** 0.601 vs policy min 0.55 · **Close:** 368 · **ATR14:** 38.6 · **Volume ratio 20D:** 1.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 350–372, entry trigger **372**, stop **354**, risk 18 points (4.84%).

**Targets:** TP1 **392** (1.11R), TP2 **462** (5.00R), TP3 **472** (5.56R). Recommended base-case RR: **5.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 368: zone 350–372 uses ATR14 38.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 372 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is placed below support structure (356 / 356). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 392 (1.11R), TP2 462 (5.00R), TP3 472 (5.56R). Targets are ATR/structure capped for hold_days=1. ATR14=38.6, resistance_5/10/20/60=462/530/650/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.11R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BBYB — position_xgb — CONDITIONAL

**Score:** 0.600 vs policy min 0.55 · **Close:** 232 · **ATR14:** 17.6 · **Volume ratio 20D:** 1.46 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–234, entry trigger **234**, stop **214**, risk 20 points (8.55%).

**Targets:** TP1 **254** (1.00R), TP2 **278** (2.20R), TP3 **282** (2.40R). Recommended base-case RR: **2.20R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 232: zone 224–234 uses ATR14 17.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 234 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 214 is placed below support structure (216 / 216). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 254 (1.00R), TP2 278 (2.20R), TP3 282 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=17.6, resistance_5/10/20/60=278/294/324/382. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DGWG — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.500 vs policy min 0.55 · **Close:** 298 · **ATR14:** 16.6 · **Volume ratio 20D:** 1.19 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 292–302, entry trigger **302**, stop **294**, risk 8 points (2.65%).

**Targets:** TP1 **312** (1.25R), TP2 **332** (3.75R), TP3 **344** (5.25R). Recommended base-case RR: **3.75R**.

**Why entry:** Hybrid entry uses close 298 and ATR14 16.6: buy zone 292–302. Entry is valid only if price can trade/hold around 302 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 294 is placed below support structure (296 / 296). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 312 (1.25R), TP2 332 (3.75R), TP3 344 (5.25R). Targets are ATR/structure capped for hold_days=1. ATR14=16.6, resistance_5/10/20/60=344/352/402/500. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.500 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## KEEN — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.463 vs policy min 0.55 · **Close:** 795 · **ATR14:** 40.0 · **Volume ratio 20D:** 1.36 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 780–805, entry trigger **805**, stop **780**, risk 25 points (3.11%).

**Targets:** TP1 **830** (1.00R), TP2 **880** (3.00R), TP3 **900** (3.80R). Recommended base-case RR: **3.00R**.

**Why entry:** Hybrid entry uses close 795 and ATR14 40.0: buy zone 780–805. Entry is valid only if price can trade/hold around 805 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 780 is placed below support structure (785 / 785). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 830 (1.00R), TP2 880 (3.00R), TP3 900 (3.80R). Targets are ATR/structure capped for hold_days=1. ATR14=40.0, resistance_5/10/20/60=900/910/995/1,155. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.463 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## MSJA — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.446 vs policy min 0.55 · **Close:** 396 · **ATR14:** 37.3 · **Volume ratio 20D:** 0.44 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 382–404, entry trigger **404**, stop **378**, risk 26 points (6.44%).

**Targets:** TP1 **430** (1.00R), TP2 **450** (1.77R), TP3 **468** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Hybrid entry uses close 396 and ATR14 37.3: buy zone 382–404. Entry is valid only if price can trade/hold around 404 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 378 is placed below support structure (380 / 374). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 430 (1.00R), TP2 450 (1.77R), TP3 468 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=37.3, resistance_5/10/20/60=430/448/555/560. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.446 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.44 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## GULA — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.443 vs policy min 0.60 · **Close:** 505 · **ATR14:** 31.4 · **Volume ratio 20D:** 1.09 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 498–560, entry trigger **560**, stop **515**, risk 45 points (8.04%).

**Targets:** TP1 **605** (1.00R), TP2 **640** (1.78R), TP3 **670** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry trigger 560 is set above recent resistance 555 plus one IDX tick. This requires confirmation instead of buying blindly at close 505. Entry is valid only if price can trade/hold around 560 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 605 (1.00R), TP2 640 (1.78R), TP3 670 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=31.4, resistance_5/10/20/60=555/555/555/555. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.443 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## NZIA — ara_candidate — WATCHLIST_ONLY

**Score:** 0.300 vs policy min 0.50 · **Close:** 258 · **ATR14:** 33.1 · **Volume ratio 20D:** 4.20 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 250–260, entry trigger **260**, stop **234**, risk 26 points (10.00%).

**Targets:** TP1 **286** (1.00R), TP2 **316** (2.15R), TP3 **324** (2.46R). Recommended base-case RR: **2.15R**.

**Why entry:** Entry trigger 260 is set above recent resistance 258 plus one IDX tick. This requires confirmation instead of buying blindly at close 258. Entry is valid only if price can trade/hold around 260 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 234 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 286 (1.00R), TP2 316 (2.15R), TP3 324 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=33.1, resistance_5/10/20/60=258/258/258/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.300 below policy min_score 0.50; TP1 reward/risk 1.00R is below strategy minimum 1.30R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---

## HRUM — swing_hgb_defensive — NO_TRADE

**Score:** 0.766 vs policy min 0.50 · **Close:** 730 · **ATR14:** 68.9 · **Volume ratio 20D:** 0.85 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 695–740, entry trigger **740**, stop **680**, risk 60 points (8.11%).

**Targets:** TP1 **810** (1.17R), TP2 **845** (1.75R), TP3 **885** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 730: zone 695–740 uses ATR14 68.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 740 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 680 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 810 (1.17R), TP2 845 (1.75R), TP3 885 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=68.9, resistance_5/10/20/60=830/835/1,015/1,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.11% exceeds max strategy risk 7.50%; TP1 reward/risk 1.17R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOCI — swing_hgb_defensive — NO_TRADE

**Score:** 0.764 vs policy min 0.50 · **Close:** 328 · **ATR14:** 41.0 · **Volume ratio 20D:** 1.01 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 308–334, entry trigger **334**, stop **308**, risk 26 points (7.78%).

**Targets:** TP1 **360** (1.00R), TP2 **408** (2.85R), TP3 **416** (3.15R). Recommended base-case RR: **2.85R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 328: zone 308–334 uses ATR14 41.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 334 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 308 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 360 (1.00R), TP2 408 (2.85R), TP3 416 (3.15R). Targets are ATR/structure capped for hold_days=1. ATR14=41.0, resistance_5/10/20/60=416/442/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.78% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## DKFT — swing_hgb_defensive — NO_TRADE

**Score:** 0.763 vs policy min 0.50 · **Close:** 640 · **ATR14:** 47.5 · **Volume ratio 20D:** 1.02 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 615–645, entry trigger **645**, stop **595**, risk 50 points (7.75%).

**Targets:** TP1 **695** (1.00R), TP2 **730** (1.70R), TP3 **765** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 640: zone 615–645 uses ATR14 47.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 595 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 695 (1.00R), TP2 730 (1.70R), TP3 765 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=47.5, resistance_5/10/20/60=730/740/845/905. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.75% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## COCO — swing_hgb_defensive — NO_TRADE

**Score:** 0.757 vs policy min 0.50 · **Close:** 187 · **ATR14:** 36.9 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 172–191, entry trigger **191**, stop **176**, risk 15 points (7.85%).

**Targets:** TP1 **210** (1.27R), TP2 **258** (4.47R), TP3 **266** (5.00R). Recommended base-case RR: **4.47R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 187: zone 172–191 uses ATR14 36.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 191 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 176 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 210 (1.27R), TP2 258 (4.47R), TP3 266 (5.00R). Targets are ATR/structure capped for hold_days=1. ATR14=36.9, resistance_5/10/20/60=266/308/402/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.85% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## GTSI — swing_hgb_defensive — NO_TRADE

**Score:** 0.755 vs policy min 0.50 · **Close:** 113 · **ATR14:** 20.1 · **Volume ratio 20D:** 1.25 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 103–116, entry trigger **116**, stop **107**, risk 9 points (7.76%).

**Targets:** TP1 **127** (1.22R), TP2 **132** (1.78R), TP3 **167** (5.67R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 113: zone 103–116 uses ATR14 20.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 116 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 107 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 127 (1.22R), TP2 132 (1.78R), TP3 167 (5.67R). Targets are ATR/structure capped for hold_days=1. ATR14=20.1, resistance_5/10/20/60=173/208/238/334. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.76% exceeds max strategy risk 7.50%; TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## BBYB — swing_hgb_defensive — NO_TRADE

**Score:** 0.751 vs policy min 0.50 · **Close:** 232 · **ATR14:** 17.6 · **Volume ratio 20D:** 1.46 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 224–234, entry trigger **234**, stop **216**, risk 18 points (7.69%).

**Targets:** TP1 **252** (1.00R), TP2 **266** (1.78R), TP3 **278** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 232: zone 224–234 uses ATR14 17.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 234 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 252 (1.00R), TP2 266 (1.78R), TP3 278 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=17.6, resistance_5/10/20/60=278/294/324/382. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## HOPE — swing_hgb_defensive — NO_TRADE

**Score:** 0.750 vs policy min 0.50 · **Close:** 110 · **ATR14:** 15.9 · **Volume ratio 20D:** 1.39 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 102–112, entry trigger **112**, stop **103**, risk 9 points (8.04%).

**Targets:** TP1 **121** (1.00R), TP2 **135** (2.56R), TP3 **140** (3.11R). Recommended base-case RR: **2.56R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 110: zone 102–112 uses ATR14 15.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 112 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 103 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 121 (1.00R), TP2 135 (2.56R), TP3 140 (3.11R). Targets are ATR/structure capped for hold_days=1. ATR14=15.9, resistance_5/10/20/60=135/163/180/372. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.04% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## DOOH — swing_hgb_defensive — NO_TRADE

**Score:** 0.744 vs policy min 0.50 · **Close:** 115 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.79 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 107–117, entry trigger **117**, stop **108**, risk 9 points (7.69%).

**Targets:** TP1 **126** (1.00R), TP2 **149** (3.56R), TP3 **150** (3.67R). Recommended base-case RR: **3.56R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 115: zone 107–117 uses ATR14 17.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 117 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 126 (1.00R), TP2 149 (3.56R), TP3 150 (3.67R). Targets are ATR/structure capped for hold_days=1. ATR14=17.4, resistance_5/10/20/60=150/154/189/197. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## ELSA — swing_hgb_defensive — NO_TRADE

**Score:** 0.736 vs policy min 0.50 · **Close:** 605 · **ATR14:** 44.6 · **Volume ratio 20D:** 0.84 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 580–610, entry trigger **610**, stop **560**, risk 50 points (8.20%).

**Targets:** TP1 **655** (0.90R), TP2 **695** (1.70R), TP3 **730** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 605: zone 580–610 uses ATR14 44.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 610 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 560 is placed below support structure (565 / 565). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 655 (0.90R), TP2 695 (1.70R), TP3 730 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=44.6, resistance_5/10/20/60=670/715/845/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.20% exceeds max strategy risk 7.50%; TP1 reward/risk 0.90R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## COIN — swing_hgb_defensive — NO_TRADE

**Score:** 0.734 vs policy min 0.50 · **Close:** 715 · **ATR14:** 93.2 · **Volume ratio 20D:** 0.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 670–725, entry trigger **725**, stop **670**, risk 55 points (7.59%).

**Targets:** TP1 **780** (1.00R), TP2 **895** (3.09R), TP3 **905** (3.27R). Recommended base-case RR: **3.09R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 715: zone 670–725 uses ATR14 93.2 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 725 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 670 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 780 (1.00R), TP2 895 (3.09R), TP3 905 (3.27R). Targets are ATR/structure capped for hold_days=1. ATR14=93.2, resistance_5/10/20/60=905/980/1,370/1,770. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.59% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KEEN — scalping_rank_hgb — NO_TRADE

**Score:** 0.658 vs policy min 0.60 · **Close:** 795 · **ATR14:** 40.0 · **Volume ratio 20D:** 1.36 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 785–905, entry trigger **905**, stop **865**, risk 40 points (4.42%).

**Targets:** TP1 **935** (0.75R), TP2 **955** (1.25R), TP3 **1,005** (2.50R). Recommended base-case RR: **1.25R**.

**Why entry:** Entry trigger 905 is set above recent resistance 900 plus one IDX tick. This requires confirmation instead of buying blindly at close 795. Entry is valid only if price can trade/hold around 905 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 865 uses 0.90×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (0.75R), TP2 955 (1.25R), TP3 1,005 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=40.0, resistance_5/10/20/60=900/910/995/1,155. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 13.84% > max 5.00%; TP1 reward/risk 0.75R is below strategy minimum 1.10R

**Risk flags:** OK

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## HOPE — position_xgb — NO_TRADE

**Score:** 0.614 vs policy min 0.55 · **Close:** 110 · **ATR14:** 15.9 · **Volume ratio 20D:** 1.39 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 102–112, entry trigger **112**, stop **101**, risk 11 points (9.82%).

**Targets:** TP1 **135** (2.09R), TP2 **141** (2.64R), TP3 **147** (3.18R). Recommended base-case RR: **2.64R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 110: zone 102–112 uses ATR14 15.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 112 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 101 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 135 (2.09R), TP2 141 (2.64R), TP3 147 (3.18R). Targets are ATR/structure capped for hold_days=1. ATR14=15.9, resistance_5/10/20/60=135/163/180/372. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.82% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DEWA — position_xgb — NO_TRADE

**Score:** 0.603 vs policy min 0.55 · **Close:** 286 · **ATR14:** 46.1 · **Volume ratio 20D:** 1.50 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 264–292, entry trigger **292**, stop **264**, risk 28 points (9.59%).

**Targets:** TP1 **358** (2.36R), TP2 **368** (2.71R), TP3 **382** (3.21R). Recommended base-case RR: **2.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 286: zone 264–292 uses ATR14 46.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 292 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 264 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 358 (2.36R), TP2 368 (2.71R), TP3 382 (3.21R). Targets are ATR/structure capped for hold_days=1. ATR14=46.1, resistance_5/10/20/60=368/450/535/595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.59% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DKFT — position_xgb — NO_TRADE

**Score:** 0.602 vs policy min 0.55 · **Close:** 640 · **ATR14:** 47.5 · **Volume ratio 20D:** 1.02 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 615–645, entry trigger **645**, stop **585**, risk 60 points (9.30%).

**Targets:** TP1 **715** (1.17R), TP2 **750** (1.75R), TP3 **790** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 640: zone 615–645 uses ATR14 47.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 645 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 585 is placed below support structure (590 / 590). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 715 (1.17R), TP2 750 (1.75R), TP3 790 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=47.5, resistance_5/10/20/60=730/740/845/905. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.30% exceeds max strategy risk 9.00%; TP1 reward/risk 1.17R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SOCI — position_xgb — NO_TRADE

**Score:** 0.602 vs policy min 0.55 · **Close:** 328 · **ATR14:** 41.0 · **Volume ratio 20D:** 1.01 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 308–334, entry trigger **334**, stop **302**, risk 32 points (9.58%).

**Targets:** TP1 **366** (1.00R), TP2 **416** (2.56R), TP3 **432** (3.06R). Recommended base-case RR: **2.56R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 328: zone 308–334 uses ATR14 41.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 334 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 302 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 366 (1.00R), TP2 416 (2.56R), TP3 432 (3.06R). Targets are ATR/structure capped for hold_days=1. ATR14=41.0, resistance_5/10/20/60=416/442/540/735. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.58% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## BIPI — position_xgb — NO_TRADE

**Score:** 0.601 vs policy min 0.55 · **Close:** 144 · **ATR14:** 23.4 · **Volume ratio 20D:** 1.71 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 133–147, entry trigger **147**, stop **133**, risk 14 points (9.52%).

**Targets:** TP1 **161** (1.00R), TP2 **190** (3.07R), TP3 **197** (3.57R). Recommended base-case RR: **3.07R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 144: zone 133–147 uses ATR14 23.4 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 147 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 133 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 161 (1.00R), TP2 190 (3.07R), TP3 197 (3.57R). Targets are ATR/structure capped for hold_days=1. ATR14=23.4, resistance_5/10/20/60=190/232/262/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.52% exceeds max strategy risk 9.00%; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TEBE — position_xgb — NO_TRADE

**Score:** 0.599 vs policy min 0.55 · **Close:** 915 · **ATR14:** 100.0 · **Volume ratio 20D:** 1.74 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 870–925, entry trigger **925**, stop **840**, risk 85 points (9.19%).

**Targets:** TP1 **1,065** (1.65R), TP2 **1,110** (2.18R), TP3 **1,130** (2.41R). Recommended base-case RR: **2.18R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 915: zone 870–925 uses ATR14 100.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 925 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 840 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,065 (1.65R), TP2 1,110 (2.18R), TP3 1,130 (2.41R). Targets are ATR/structure capped for hold_days=1. ATR14=100.0, resistance_5/10/20/60=1,110/1,140/1,290/1,775. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.19% exceeds max strategy risk 9.00%

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## APIC — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.553 vs policy min 0.55 · **Close:** 605 · **ATR14:** 237.1 · **Volume ratio 20D:** 6.25 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 520–655, entry trigger **655**, stop **605**, risk 50 points (7.63%).

**Targets:** TP1 **775** (2.40R), TP2 **800** (2.90R), TP3 **1,225** (11.40R). Recommended base-case RR: **2.90R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 237.1: buy zone 520–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 605 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 775 (2.40R), TP2 800 (2.90R), TP3 1,225 (11.40R). Targets are ATR/structure capped for hold_days=1. ATR14=237.1, resistance_5/10/20/60=1,225/1,725/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 8.26% > max 8.00%; entry-to-stop risk 7.63% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## FUJI — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.507 vs policy min 0.55 · **Close:** 278 · **ATR14:** 26.3 · **Volume ratio 20D:** 1.33 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 268–284, entry trigger **284**, stop **262**, risk 22 points (7.75%).

**Targets:** TP1 **312** (1.27R), TP2 **324** (1.82R), TP3 **338** (2.45R). Recommended base-case RR: **1.82R**.

**Why entry:** Hybrid entry uses close 278 and ATR14 26.3: buy zone 268–284. Entry is valid only if price can trade/hold around 284 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 262 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 312 (1.27R), TP2 324 (1.82R), TP3 338 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=26.3, resistance_5/10/20/60=324/324/348/460. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.75% exceeds max strategy risk 7.50%; score 0.507 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## TEBE — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.507 vs policy min 0.55 · **Close:** 915 · **ATR14:** 100.0 · **Volume ratio 20D:** 1.74 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 880–935, entry trigger **935**, stop **860**, risk 75 points (8.02%).

**Targets:** TP1 **1,010** (1.00R), TP2 **1,110** (2.33R), TP3 **1,115** (2.40R). Recommended base-case RR: **2.33R**.

**Why entry:** Hybrid entry uses close 915 and ATR14 100.0: buy zone 880–935. Entry is valid only if price can trade/hold around 935 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 860 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,010 (1.00R), TP2 1,110 (2.33R), TP3 1,115 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=100.0, resistance_5/10/20/60=1,110/1,140/1,290/1,775. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.02% exceeds max strategy risk 7.50%; score 0.507 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## HUMI — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.472 vs policy min 0.55 · **Close:** 108 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.10 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 104–195, entry trigger **195**, stop **181**, risk 14 points (7.18%).

**Targets:** TP1 **210** (1.07R), TP2 **220** (1.79R), TP3 **230** (2.50R). Recommended base-case RR: **1.79R**.

**Why entry:** Entry trigger 195 is set above recent resistance 194 plus one IDX tick. This requires confirmation instead of buying blindly at close 108. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 181 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 210 (1.07R), TP2 220 (1.79R), TP3 230 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=18.1, resistance_5/10/20/60=160/194/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 80.56% > max 8.00%; entry-to-stop risk 7.18% exceeds max strategy risk 7.00%; score 0.472 below policy min_score 0.55; TP1 reward/risk 1.07R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## IRSX — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.465 vs policy min 0.55 · **Close:** 284 · **ATR14:** 49.4 · **Volume ratio 20D:** 1.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 274–472, entry trigger **472**, stop **438**, risk 34 points (7.20%).

**Targets:** TP1 **510** (1.12R), TP2 **530** (1.71R), TP3 **555** (2.44R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 472 is set above recent resistance 470 plus one IDX tick. This requires confirmation instead of buying blindly at close 284. Entry is valid only if price can trade/hold around 472 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 438 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 510 (1.12R), TP2 530 (1.71R), TP3 555 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=49.4, resistance_5/10/20/60=386/470/480/675. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 66.20% > max 8.00%; entry-to-stop risk 7.20% exceeds max strategy risk 7.00%; score 0.465 below policy min_score 0.55; TP1 reward/risk 1.12R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## BELL — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.452 vs policy min 0.55 · **Close:** 110 · **ATR14:** 14.3 · **Volume ratio 20D:** 7.79 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 105–113, entry trigger **113**, stop **104**, risk 9 points (7.96%).

**Targets:** TP1 **127** (1.56R), TP2 **129** (1.78R), TP3 **135** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 110 and ATR14 14.3: buy zone 105–113. Entry is valid only if price can trade/hold around 113 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 104 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 127 (1.56R), TP2 129 (1.78R), TP3 135 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=14.3, resistance_5/10/20/60=127/146/161/254. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.96% exceeds max strategy risk 7.50%; score 0.452 below policy min_score 0.55; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## TRIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.452 vs policy min 0.60 · **Close:** 332 · **ATR14:** 66.3 · **Volume ratio 20D:** 2.77 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 318–605, entry trigger **605**, stop **540**, risk 65 points (10.74%).

**Targets:** TP1 **730** (1.92R), TP2 **740** (2.08R), TP3 **765** (2.46R). Recommended base-case RR: **2.08R**.

**Why entry:** Entry trigger 605 is set above recent resistance 600 plus one IDX tick. This requires confirmation instead of buying blindly at close 332. Entry is valid only if price can trade/hold around 605 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 540 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 730 (1.92R), TP2 740 (2.08R), TP3 765 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=66.3, resistance_5/10/20/60=486/600/740/1,120. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 82.23% > max 15.00%; entry-to-stop risk 10.74% exceeds max strategy risk 10.00%; score 0.452 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## OASA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.450 vs policy min 0.60 · **Close:** 270 · **ATR14:** 43.7 · **Volume ratio 20D:** 0.95 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 260–434, entry trigger **434**, stop **390**, risk 44 points (10.14%).

**Targets:** TP1 **478** (1.00R), TP2 **510** (1.73R), TP3 **540** (2.41R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 434 is set above recent resistance 432 plus one IDX tick. This requires confirmation instead of buying blindly at close 270. Entry is valid only if price can trade/hold around 434 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 390 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 478 (1.00R), TP2 510 (1.73R), TP3 540 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=43.7, resistance_5/10/20/60=392/432/466/472. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 60.74% > max 15.00%; entry-to-stop risk 10.14% exceeds max strategy risk 10.00%; score 0.450 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## APIC — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.445 vs policy min 0.60 · **Close:** 605 · **ATR14:** 237.1 · **Volume ratio 20D:** 6.25 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 555–1,730, entry trigger **1,730**, stop **1,555**, risk 175 points (10.12%).

**Targets:** TP1 **1,905** (1.00R), TP2 **2,410** (3.89R), TP3 **2,500** (4.40R). Recommended base-case RR: **3.89R**.

**Why entry:** Entry trigger 1,730 is set above recent resistance 1,725 plus one IDX tick. This requires confirmation instead of buying blindly at close 605. Entry is valid only if price can trade/hold around 1,730 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,555 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,905 (1.00R), TP2 2,410 (3.89R), TP3 2,500 (4.40R). Targets are ATR/structure capped for hold_days=2. ATR14=237.1, resistance_5/10/20/60=1,225/1,725/2,410/2,410. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 185.95% > max 15.00%; entry-to-stop risk 10.12% exceeds max strategy risk 10.00%; score 0.445 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## COCO — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.444 vs policy min 0.60 · **Close:** 187 · **ATR14:** 36.9 · **Volume ratio 20D:** 0.69 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 179–310, entry trigger **310**, stop **278**, risk 32 points (10.32%).

**Targets:** TP1 **342** (1.00R), TP2 **402** (2.88R), TP3 **418** (3.38R). Recommended base-case RR: **2.88R**.

**Why entry:** Entry trigger 310 is set above recent resistance 308 plus one IDX tick. This requires confirmation instead of buying blindly at close 187. Entry is valid only if price can trade/hold around 310 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 278 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 342 (1.00R), TP2 402 (2.88R), TP3 418 (3.38R). Targets are ATR/structure capped for hold_days=2. ATR14=36.9, resistance_5/10/20/60=266/308/402/570. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 65.78% > max 15.00%; entry-to-stop risk 10.32% exceeds max strategy risk 10.00%; score 0.444 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## DOOH — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.442 vs policy min 0.60 · **Close:** 115 · **ATR14:** 17.4 · **Volume ratio 20D:** 1.79 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 111–155, entry trigger **155**, stop **139**, risk 16 points (10.32%).

**Targets:** TP1 **187** (2.00R), TP2 **189** (2.12R), TP3 **194** (2.44R). Recommended base-case RR: **2.12R**.

**Why entry:** Entry trigger 155 is set above recent resistance 154 plus one IDX tick. This requires confirmation instead of buying blindly at close 115. Entry is valid only if price can trade/hold around 155 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 139 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 187 (2.00R), TP2 189 (2.12R), TP3 194 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=17.4, resistance_5/10/20/60=150/154/189/197. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 34.78% > max 15.00%; entry-to-stop risk 10.32% exceeds max strategy risk 10.00%; score 0.442 below policy min_score 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BRMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.440 vs policy min 0.60 · **Close:** 520 · **ATR14:** 72.4 · **Volume ratio 20D:** 1.33 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 505–760, entry trigger **760**, stop **680**, risk 80 points (10.53%).

**Targets:** TP1 **845** (1.06R), TP2 **900** (1.75R), TP3 **955** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 760 is set above recent resistance 755 plus one IDX tick. This requires confirmation instead of buying blindly at close 520. Entry is valid only if price can trade/hold around 760 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 680 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 845 (1.06R), TP2 900 (1.75R), TP3 955 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=72.4, resistance_5/10/20/60=635/755/845/1,045. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 46.15% > max 15.00%; entry-to-stop risk 10.53% exceeds max strategy risk 10.00%; score 0.440 below policy min_score 0.60; TP1 reward/risk 1.06R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## HOPE — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.438 vs policy min 0.60 · **Close:** 110 · **ATR14:** 15.9 · **Volume ratio 20D:** 1.39 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 106–164, entry trigger **164**, stop **147**, risk 17 points (10.37%).

**Targets:** TP1 **181** (1.00R), TP2 **193** (1.71R), TP3 **206** (2.47R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 164 is set above recent resistance 163 plus one IDX tick. This requires confirmation instead of buying blindly at close 110. Entry is valid only if price can trade/hold around 164 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 147 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 181 (1.00R), TP2 193 (1.71R), TP3 206 (2.47R). Targets are ATR/structure capped for hold_days=2. ATR14=15.9, resistance_5/10/20/60=135/163/180/372. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 49.09% > max 15.00%; entry-to-stop risk 10.37% exceeds max strategy risk 10.00%; score 0.438 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## PADA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.438 vs policy min 0.60 · **Close:** 102 · **ATR14:** 19.1 · **Volume ratio 20D:** 1.01 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 98–167, entry trigger **167**, stop **150**, risk 17 points (10.18%).

**Targets:** TP1 **197** (1.76R), TP2 **206** (2.29R), TP3 **208** (2.41R). Recommended base-case RR: **2.29R**.

**Why entry:** Entry trigger 167 is set above recent resistance 166 plus one IDX tick. This requires confirmation instead of buying blindly at close 102. Entry is valid only if price can trade/hold around 167 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 197 (1.76R), TP2 206 (2.29R), TP3 208 (2.41R). Targets are ATR/structure capped for hold_days=2. ATR14=19.1, resistance_5/10/20/60=148/166/197/218. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 63.73% > max 15.00%; entry-to-stop risk 10.18% exceeds max strategy risk 10.00%; score 0.438 below policy min_score 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SSMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.437 vs policy min 0.60 · **Close:** 755 · **ATR14:** 95.4 · **Volume ratio 20D:** 0.98 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 735–1,110, entry trigger **1,110**, stop **995**, risk 115 points (10.36%).

**Targets:** TP1 **1,225** (1.00R), TP2 **1,425** (2.74R), TP3 **1,450** (2.96R). Recommended base-case RR: **2.74R**.

**Why entry:** Entry trigger 1,110 is set above recent resistance 1,105 plus one IDX tick. This requires confirmation instead of buying blindly at close 755. Entry is valid only if price can trade/hold around 1,110 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 995 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,225 (1.00R), TP2 1,425 (2.74R), TP3 1,450 (2.96R). Targets are ATR/structure capped for hold_days=2. ATR14=95.4, resistance_5/10/20/60=825/1,105/1,450/1,770. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 47.02% > max 15.00%; entry-to-stop risk 10.36% exceeds max strategy risk 10.00%; score 0.437 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## VKTR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.435 vs policy min 0.60 · **Close:** 625 · **ATR14:** 90.4 · **Volume ratio 20D:** 1.32 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 605–890, entry trigger **890**, stop **800**, risk 90 points (10.11%).

**Targets:** TP1 **995** (1.17R), TP2 **1,045** (1.72R), TP3 **1,110** (2.44R). Recommended base-case RR: **1.72R**.

**Why entry:** Entry trigger 890 is set above recent resistance 885 plus one IDX tick. This requires confirmation instead of buying blindly at close 625. Entry is valid only if price can trade/hold around 890 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 800 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 995 (1.17R), TP2 1,045 (1.72R), TP3 1,110 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=90.4, resistance_5/10/20/60=830/885/995/1,090. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 42.40% > max 15.00%; entry-to-stop risk 10.11% exceeds max strategy risk 10.00%; score 0.435 below policy min_score 0.60; TP1 reward/risk 1.17R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## PSKT — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.435 vs policy min 0.60 · **Close:** 171 · **ATR14:** 24.9 · **Volume ratio 20D:** 0.82 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 166–242, entry trigger **242**, stop **216**, risk 26 points (10.74%).

**Targets:** TP1 **272** (1.15R), TP2 **288** (1.77R), TP3 **306** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 242 is set above recent resistance 240 plus one IDX tick. This requires confirmation instead of buying blindly at close 171. Entry is valid only if price can trade/hold around 242 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 216 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 272 (1.15R), TP2 288 (1.77R), TP3 306 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=24.9, resistance_5/10/20/60=234/240/272/336. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 41.52% > max 15.00%; entry-to-stop risk 10.74% exceeds max strategy risk 10.00%; score 0.435 below policy min_score 0.60; TP1 reward/risk 1.15R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## HUMI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.434 vs policy min 0.60 · **Close:** 108 · **ATR14:** 18.1 · **Volume ratio 20D:** 1.10 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 104–195, entry trigger **195**, stop **175**, risk 20 points (10.26%).

**Targets:** TP1 **216** (1.05R), TP2 **256** (3.05R), TP3 **260** (3.25R). Recommended base-case RR: **3.05R**.

**Why entry:** Entry trigger 195 is set above recent resistance 194 plus one IDX tick. This requires confirmation instead of buying blindly at close 108. Entry is valid only if price can trade/hold around 195 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 175 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 216 (1.05R), TP2 256 (3.05R), TP3 260 (3.25R). Targets are ATR/structure capped for hold_days=2. ATR14=18.1, resistance_5/10/20/60=160/194/195/260. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 80.56% > max 15.00%; entry-to-stop risk 10.26% exceeds max strategy risk 10.00%; score 0.434 below policy min_score 0.60; TP1 reward/risk 1.05R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## CYBR — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.431 vs policy min 0.60 · **Close:** 560 · **ATR14:** 90.4 · **Volume ratio 20D:** 1.40 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 540–670, entry trigger **670**, stop **600**, risk 70 points (10.45%).

**Targets:** TP1 **740** (1.00R), TP2 **790** (1.71R), TP3 **840** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 670 is set above recent resistance 665 plus one IDX tick. This requires confirmation instead of buying blindly at close 560. Entry is valid only if price can trade/hold around 670 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 600 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 740 (1.00R), TP2 790 (1.71R), TP3 840 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=90.4, resistance_5/10/20/60=620/665/1,330/1,590. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 19.64% > max 15.00%; entry-to-stop risk 10.45% exceeds max strategy risk 10.00%; score 0.431 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## MBMA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.431 vs policy min 0.60 · **Close:** 432 · **ATR14:** 54.7 · **Volume ratio 20D:** 0.77 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 420–555, entry trigger **555**, stop **498**, risk 57 points (10.27%).

**Targets:** TP1 **615** (1.05R), TP2 **690** (2.37R), TP3 **695** (2.46R). Recommended base-case RR: **2.37R**.

**Why entry:** Entry trigger 555 is set above recent resistance 550 plus one IDX tick. This requires confirmation instead of buying blindly at close 432. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 498 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 615 (1.05R), TP2 690 (2.37R), TP3 695 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=54.7, resistance_5/10/20/60=510/550/690/920. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 28.47% > max 15.00%; entry-to-stop risk 10.27% exceeds max strategy risk 10.00%; score 0.431 below policy min_score 0.60; TP1 reward/risk 1.05R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---
