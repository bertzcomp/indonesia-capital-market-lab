# Numeric Trading Desk Report — 2026-06-02

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 3 |
| CONDITIONAL | 6 |
| WATCHLIST_ONLY | 10 |
| NO_TRADE | 37 |

## TPMA — position_xgb — ACTIONABLE

**Score:** 0.569 vs policy min 0.55 · **Close:** 438 · **ATR14:** 20.3 · **Volume ratio 20D:** 1.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 428–442, entry trigger **442**, stop **434**, risk 8 points (1.81%).

**Targets:** TP1 **454** (1.50R), TP2 **492** (6.25R), TP3 **510** (8.50R). Recommended base-case RR: **6.25R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 438: zone 428–442 uses ATR14 20.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 442 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 434 is placed below support structure (436 / 436). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 454 (1.50R), TP2 492 (6.25R), TP3 510 (8.50R). Targets are ATR/structure capped for hold_days=1. ATR14=20.3, resistance_5/10/20/60=510/550/585/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## OMED — position_xgb — ACTIONABLE

**Score:** 0.557 vs policy min 0.55 · **Close:** 206 · **ATR14:** 22.0 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 196–210, entry trigger **210**, stop **200**, risk 10 points (4.76%).

**Targets:** TP1 **242** (3.20R), TP2 **250** (4.00R), TP3 **256** (4.60R). Recommended base-case RR: **4.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 206: zone 196–210 uses ATR14 22.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 210 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 200 is placed below support structure (202 / 202). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 242 (3.20R), TP2 250 (4.00R), TP3 256 (4.60R). Targets are ATR/structure capped for hold_days=1. ATR14=22.0, resistance_5/10/20/60=250/252/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## RALS — position_xgb — ACTIONABLE

**Score:** 0.551 vs policy min 0.55 · **Close:** 378 · **ATR14:** 12.6 · **Volume ratio 20D:** 0.63 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 372–380, entry trigger **380**, stop **372**, risk 8 points (2.11%).

**Targets:** TP1 **398** (2.25R), TP2 **402** (2.75R), TP3 **406** (3.25R). Recommended base-case RR: **2.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 378: zone 372–380 uses ATR14 12.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 380 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 372 is placed below support structure (374 / 374). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 398 (2.25R), TP2 402 (2.75R), TP3 406 (3.25R). Targets are ATR/structure capped for hold_days=1. ATR14=12.6, resistance_5/10/20/60=402/464/466/530. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## STAA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.634 vs policy min 0.50 · **Close:** 980 · **ATR14:** 52.9 · **Volume ratio 20D:** 2.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 955–990, entry trigger **990**, stop **945**, risk 45 points (4.55%).

**Targets:** TP1 **1,045** (1.22R), TP2 **1,070** (1.78R), TP3 **1,100** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 980: zone 955–990 uses ATR14 52.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 990 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 945 is placed below support structure (950 / 950). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,045 (1.22R), TP2 1,070 (1.78R), TP3 1,100 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=52.9, resistance_5/10/20/60=1,045/1,240/1,320/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.22R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## OMED — swing_hgb_defensive — CONDITIONAL

**Score:** 0.627 vs policy min 0.50 · **Close:** 206 · **ATR14:** 22.0 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 196–210, entry trigger **210**, stop **200**, risk 10 points (4.76%).

**Targets:** TP1 **222** (1.20R), TP2 **250** (4.00R), TP3 **256** (4.60R). Recommended base-case RR: **4.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 206: zone 196–210 uses ATR14 22.0 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 210 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 200 is placed below support structure (202 / 202). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 222 (1.20R), TP2 250 (4.00R), TP3 256 (4.60R). Targets are ATR/structure capped for hold_days=1. ATR14=22.0, resistance_5/10/20/60=250/252/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.20R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## ELSA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.626 vs policy min 0.50 · **Close:** 630 · **ATR14:** 42.5 · **Volume ratio 20D:** 0.58 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 610–635, entry trigger **635**, stop **590**, risk 45 points (7.09%).

**Targets:** TP1 **680** (1.00R), TP2 **715** (1.78R), TP3 **745** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 630: zone 610–635 uses ATR14 42.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 635 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 590 is placed below support structure (595 / 595). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.00R), TP2 715 (1.78R), TP3 745 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=42.5, resistance_5/10/20/60=670/715/845/1,050. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.58 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## KIJA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.624 vs policy min 0.50 · **Close:** 122 · **ATR14:** 9.3 · **Volume ratio 20D:** 0.41 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 117–123, entry trigger **123**, stop **117**, risk 6 points (4.88%).

**Targets:** TP1 **133** (1.67R), TP2 **134** (1.83R), TP3 **138** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 122: zone 117–123 uses ATR14 9.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.67R), TP2 134 (1.83R), TP3 138 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=9.3, resistance_5/10/20/60=133/174/190/230. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.41 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## ESSA — swing_hgb_defensive — CONDITIONAL

**Score:** 0.617 vs policy min 0.50 · **Close:** 665 · **ATR14:** 59.3 · **Volume ratio 20D:** 0.55 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 635–675, entry trigger **675**, stop **640**, risk 35 points (5.19%).

**Targets:** TP1 **720** (1.29R), TP2 **735** (1.71R), TP3 **760** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 665: zone 635–675 uses ATR14 59.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 640 is placed below support structure (645 / 645). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.29R), TP2 735 (1.71R), TP3 760 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=59.3, resistance_5/10/20/60=720/825/995/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.55 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## GTSI — position_xgb — CONDITIONAL

**Score:** 0.561 vs policy min 0.55 · **Close:** 140 · **ATR14:** 19.6 · **Volume ratio 20D:** 2.48 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 131–142, entry trigger **142**, stop **138**, risk 4 points (2.82%).

**Targets:** TP1 **152** (2.50R), TP2 **180** (9.50R), TP3 **182** (10.00R). Recommended base-case RR: **9.50R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 140: zone 131–142 uses ATR14 19.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 142 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 138 is placed below support structure (139 / 139). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 152 (2.50R), TP2 180 (9.50R), TP3 182 (10.00R). Targets are ATR/structure capped for hold_days=1. ATR14=19.6, resistance_5/10/20/60=180/222/240/348. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## STAA — position_xgb — WATCHLIST_ONLY

**Score:** 0.548 vs policy min 0.55 · **Close:** 980 · **ATR14:** 52.9 · **Volume ratio 20D:** 2.91 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 955–990, entry trigger **990**, stop **945**, risk 45 points (4.55%).

**Targets:** TP1 **1,045** (1.22R), TP2 **1,070** (1.78R), TP3 **1,100** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 980: zone 955–990 uses ATR14 52.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 990 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 945 is placed below support structure (950 / 950). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,045 (1.22R), TP2 1,070 (1.78R), TP3 1,100 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=52.9, resistance_5/10/20/60=1,045/1,240/1,320/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.548 below policy min_score 0.55; TP1 reward/risk 1.22R is below strategy minimum 1.35R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## DGWG — position_xgb — WATCHLIST_ONLY

**Score:** 0.548 vs policy min 0.55 · **Close:** 306 · **ATR14:** 16.6 · **Volume ratio 20D:** 1.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 298–308, entry trigger **308**, stop **304**, risk 4 points (1.30%).

**Targets:** TP1 **332** (6.00R), TP2 **344** (9.00R), TP3 **346** (9.50R). Recommended base-case RR: **9.00R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 306: zone 298–308 uses ATR14 16.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 308 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 304 is placed below support structure (306 / 306). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 332 (6.00R), TP2 344 (9.00R), TP3 346 (9.50R). Targets are ATR/structure capped for hold_days=1. ATR14=16.6, resistance_5/10/20/60=344/374/402/510. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.548 below policy min_score 0.55

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## KIJA — position_xgb — WATCHLIST_ONLY

**Score:** 0.540 vs policy min 0.55 · **Close:** 122 · **ATR14:** 9.3 · **Volume ratio 20D:** 0.41 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 117–123, entry trigger **123**, stop **117**, risk 6 points (4.88%).

**Targets:** TP1 **133** (1.67R), TP2 **134** (1.83R), TP3 **138** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 122: zone 117–123 uses ATR14 9.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 117 is placed below support structure (118 / 118). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 133 (1.67R), TP2 134 (1.83R), TP3 138 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=9.3, resistance_5/10/20/60=133/174/190/230. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.540 below policy min_score 0.55; volume ratio 0.41 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## GULA — position_xgb — WATCHLIST_ONLY

**Score:** 0.538 vs policy min 0.55 · **Close:** 545 · **ATR14:** 29.3 · **Volume ratio 20D:** 1.07 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 530–550, entry trigger **550**, stop **505**, risk 45 points (8.18%).

**Targets:** TP1 **595** (1.00R), TP2 **625** (1.67R), TP3 **660** (2.44R). Recommended base-case RR: **1.67R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 545: zone 530–550 uses ATR14 29.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 550 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 505 uses 1.40×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 595 (1.00R), TP2 625 (1.67R), TP3 660 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=29.3, resistance_5/10/20/60=550/550/550/550. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.538 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## GPSO — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.417 vs policy min 0.60 · **Close:** 515 · **ATR14:** 23.0 · **Volume ratio 20D:** 0.85 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 510–525, entry trigger **525**, stop **494**, risk 31 points (5.90%).

**Targets:** TP1 **560** (1.13R), TP2 **580** (1.77R), TP3 **600** (2.42R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 525 is set above recent resistance 520 plus one IDX tick. This requires confirmation instead of buying blindly at close 515. Entry is valid only if price can trade/hold around 525 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 494 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 560 (1.13R), TP2 580 (1.77R), TP3 600 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=23.0, resistance_5/10/20/60=520/520/520/520. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.417 below policy min_score 0.60; TP1 reward/risk 1.13R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GULA — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.416 vs policy min 0.60 · **Close:** 545 · **ATR14:** 29.3 · **Volume ratio 20D:** 1.07 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 535–555, entry trigger **555**, stop **515**, risk 40 points (7.21%).

**Targets:** TP1 **595** (1.00R), TP2 **625** (1.75R), TP3 **655** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 555 is set above recent resistance 550 plus one IDX tick. This requires confirmation instead of buying blindly at close 545. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 595 (1.00R), TP2 625 (1.75R), TP3 655 (2.50R). Targets are ATR/structure capped for hold_days=2. ATR14=29.3, resistance_5/10/20/60=550/550/550/550. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.416 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## ESSA — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.410 vs policy min 0.55 · **Close:** 665 · **ATR14:** 59.3 · **Volume ratio 20D:** 0.55 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 640–680, entry trigger **680**, stop **640**, risk 40 points (5.88%).

**Targets:** TP1 **720** (1.00R), TP2 **750** (1.75R), TP3 **780** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 665 and ATR14 59.3: buy zone 640–680. Entry is valid only if price can trade/hold around 680 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 640 is placed below support structure (645 / 645). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.00R), TP2 750 (1.75R), TP3 780 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=59.3, resistance_5/10/20/60=720/825/995/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.410 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.55 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## OMED — market_maker_silent_accum_defensive — WATCHLIST_ONLY

**Score:** 0.388 vs policy min 0.55 · **Close:** 206 · **ATR14:** 22.0 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 198–212, entry trigger **212**, stop **200**, risk 12 points (5.66%).

**Targets:** TP1 **224** (1.00R), TP2 **250** (3.17R), TP3 **256** (3.67R). Recommended base-case RR: **3.17R**.

**Why entry:** Hybrid entry uses close 206 and ATR14 22.0: buy zone 198–212. Entry is valid only if price can trade/hold around 212 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 200 is placed below support structure (202 / 202). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (1.00R), TP2 250 (3.17R), TP3 256 (3.67R). Targets are ATR/structure capped for hold_days=1. ATR14=22.0, resistance_5/10/20/60=250/252/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.388 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## HATM — momentum_10d_hgb_aggressive — WATCHLIST_ONLY

**Score:** 0.381 vs policy min 0.60 · **Close:** 382 · **ATR14:** 21.0 · **Volume ratio 20D:** 3.09 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 376–388, entry trigger **388**, stop **360**, risk 28 points (7.22%).

**Targets:** TP1 **416** (1.00R), TP2 **436** (1.71R), TP3 **456** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 388 is set above recent resistance 386 plus one IDX tick. This requires confirmation instead of buying blindly at close 382. Entry is valid only if price can trade/hold around 388 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 360 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 416 (1.00R), TP2 436 (1.71R), TP3 456 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=21.0, resistance_5/10/20/60=386/386/386/386. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.381 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BEER — ara_candidate — WATCHLIST_ONLY

**Score:** 0.281 vs policy min 0.50 · **Close:** 112 · **ATR14:** 14.1 · **Volume ratio 20D:** 8.85 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 109–120, entry trigger **120**, stop **108**, risk 12 points (10.00%).

**Targets:** TP1 **132** (1.00R), TP2 **144** (2.00R), TP3 **149** (2.42R). Recommended base-case RR: **2.00R**.

**Why entry:** Entry trigger 120 is set above recent resistance 119 plus one IDX tick. This requires confirmation instead of buying blindly at close 112. Entry is valid only if price can trade/hold around 120 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 108 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 132 (1.00R), TP2 144 (2.00R), TP3 149 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=14.1, resistance_5/10/20/60=112/119/144/212. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.281 below policy min_score 0.50; TP1 reward/risk 1.00R is below strategy minimum 1.30R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** High drawdown tactical setup. Use as execution only if confirmation is strong and liquidity is clean.

---

## COIN — swing_hgb_defensive — NO_TRADE

**Score:** 0.645 vs policy min 0.50 · **Close:** 825 · **ATR14:** 92.5 · **Volume ratio 20D:** 0.83 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 780–835, entry trigger **835**, stop **770**, risk 65 points (7.78%).

**Targets:** TP1 **905** (1.08R), TP2 **950** (1.77R), TP3 **995** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 825: zone 780–835 uses ATR14 92.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 835 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 770 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 905 (1.08R), TP2 950 (1.77R), TP3 995 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=92.5, resistance_5/10/20/60=905/1,050/1,370/1,895. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.78% exceeds max strategy risk 7.50%; TP1 reward/risk 1.08R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SIMP — swing_hgb_defensive — NO_TRADE

**Score:** 0.640 vs policy min 0.50 · **Close:** 565 · **ATR14:** 41.1 · **Volume ratio 20D:** 0.49 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 545–570, entry trigger **570**, stop **525**, risk 45 points (7.89%).

**Targets:** TP1 **615** (1.00R), TP2 **645** (1.67R), TP3 **680** (2.44R). Recommended base-case RR: **1.67R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 565: zone 545–570 uses ATR14 41.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 570 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 525 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 615 (1.00R), TP2 645 (1.67R), TP3 680 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=41.1, resistance_5/10/20/60=585/660/855/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.89% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.49 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## TOBA — swing_hgb_defensive — NO_TRADE

**Score:** 0.639 vs policy min 0.50 · **Close:** 432 · **ATR14:** 37.5 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 414–436, entry trigger **436**, stop **402**, risk 34 points (7.80%).

**Targets:** TP1 **470** (1.00R), TP2 **494** (1.71R), TP3 **520** (2.47R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 432: zone 414–436 uses ATR14 37.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 436 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 402 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 470 (1.00R), TP2 494 (1.71R), TP3 520 (2.47R). Targets are ATR/structure capped for hold_days=1. ATR14=37.5, resistance_5/10/20/60=462/575/650/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.80% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## MSJA — swing_hgb_defensive — NO_TRADE

**Score:** 0.638 vs policy min 0.50 · **Close:** 408 · **ATR14:** 38.5 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 390–412, entry trigger **412**, stop **380**, risk 32 points (7.77%).

**Targets:** TP1 **444** (1.00R), TP2 **468** (1.75R), TP3 **490** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 408: zone 390–412 uses ATR14 38.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 412 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 380 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 444 (1.00R), TP2 468 (1.75R), TP3 490 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=38.5, resistance_5/10/20/60=436/456/555/560. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.77% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## GZCO — swing_hgb_defensive — NO_TRADE

**Score:** 0.632 vs policy min 0.50 · **Close:** 154 · **ATR14:** 15.8 · **Volume ratio 20D:** 0.65 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 146–156, entry trigger **156**, stop **144**, risk 12 points (7.69%).

**Targets:** TP1 **168** (1.00R), TP2 **177** (1.75R), TP3 **185** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 154: zone 146–156 uses ATR14 15.8 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 156 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 144 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 168 (1.00R), TP2 177 (1.75R), TP3 185 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=15.8, resistance_5/10/20/60=166/195/236/252. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## OMED — scalping_rank_hgb — NO_TRADE

**Score:** 0.632 vs policy min 0.60 · **Close:** 206 · **ATR14:** 22.0 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 200–252, entry trigger **252**, stop **240**, risk 12 points (4.76%).

**Targets:** TP1 **264** (1.00R), TP2 **274** (1.83R), TP3 **282** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Entry trigger 252 is set above recent resistance 250 plus one IDX tick. This requires confirmation instead of buying blindly at close 206. Entry is valid only if price can trade/hold around 252 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 240 is capped by max risk 4.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 264 (1.00R), TP2 274 (1.83R), TP3 282 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=22.0, resistance_5/10/20/60=250/252/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 22.33% > max 5.00%; entry-to-stop risk 4.76% exceeds max strategy risk 4.50%; TP1 reward/risk 1.00R is below strategy minimum 1.10R

**Risk flags:** OK

**Strategy risk note:** Top-1 short-horizon scalp; invalidation must be quick.

---

## HRUM — swing_hgb_defensive — NO_TRADE

**Score:** 0.630 vs policy min 0.50 · **Close:** 805 · **ATR14:** 62.9 · **Volume ratio 20D:** 0.38 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 775–815, entry trigger **815**, stop **750**, risk 65 points (7.98%).

**Targets:** TP1 **880** (1.00R), TP2 **930** (1.77R), TP3 **975** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 805: zone 775–815 uses ATR14 62.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 815 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 750 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 880 (1.00R), TP2 930 (1.77R), TP3 975 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=62.9, resistance_5/10/20/60=830/920/1,020/1,270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.98% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.38 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SSMS — swing_hgb_defensive — NO_TRADE

**Score:** 0.630 vs policy min 0.50 · **Close:** 815 · **ATR14:** 89.3 · **Volume ratio 20D:** 1.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 770–825, entry trigger **825**, stop **760**, risk 65 points (7.88%).

**Targets:** TP1 **910** (1.31R), TP2 **940** (1.77R), TP3 **985** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 815: zone 770–825 uses ATR14 89.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 825 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 760 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 910 (1.31R), TP2 940 (1.77R), TP3 985 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=89.3, resistance_5/10/20/60=910/1,310/1,460/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.88% exceeds max strategy risk 7.50%

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## SOCI — swing_hgb_defensive — NO_TRADE

**Score:** 0.622 vs policy min 0.50 · **Close:** 386 · **ATR14:** 36.9 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 368–390, entry trigger **390**, stop **360**, risk 30 points (7.69%).

**Targets:** TP1 **420** (1.00R), TP2 **442** (1.73R), TP3 **462** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 386: zone 368–390 uses ATR14 36.9 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 390 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 360 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 420 (1.00R), TP2 442 (1.73R), TP3 462 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=36.9, resistance_5/10/20/60=416/480/540/780. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## NCKL — swing_hgb_defensive — NO_TRADE

**Score:** 0.620 vs policy min 0.50 · **Close:** 885 · **ATR14:** 72.1 · **Volume ratio 20D:** 0.83 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 850–895, entry trigger **895**, stop **825**, risk 70 points (7.82%).

**Targets:** TP1 **965** (1.00R), TP2 **1,015** (1.71R), TP3 **1,065** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 885: zone 850–895 uses ATR14 72.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 895 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 825 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 965 (1.00R), TP2 1,015 (1.71R), TP3 1,065 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=72.1, resistance_5/10/20/60=925/1,035/1,150/1,595. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.82% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## APEX — swing_hgb_defensive — NO_TRADE

**Score:** 0.615 vs policy min 0.50 · **Close:** 141 · **ATR14:** 11.7 · **Volume ratio 20D:** 1.19 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 135–143, entry trigger **143**, stop **132**, risk 11 points (7.69%).

**Targets:** TP1 **154** (1.00R), TP2 **162** (1.73R), TP3 **170** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 141: zone 135–143 uses ATR14 11.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 143 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 132 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 154 (1.00R), TP2 162 (1.73R), TP3 170 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=11.7, resistance_5/10/20/60=153/177/218/270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.69% exceeds max strategy risk 7.50%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Core defensive swing. Buy zone should avoid chasing far above close.

---

## APEX — position_xgb — NO_TRADE

**Score:** 0.547 vs policy min 0.55 · **Close:** 141 · **ATR14:** 11.7 · **Volume ratio 20D:** 1.19 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 135–143, entry trigger **143**, stop **130**, risk 13 points (9.09%).

**Targets:** TP1 **156** (1.00R), TP2 **166** (1.77R), TP3 **175** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 141: zone 135–143 uses ATR14 11.7 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 143 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 130 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 156 (1.00R), TP2 166 (1.77R), TP3 175 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=11.7, resistance_5/10/20/60=153/177/218/270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; score 0.547 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## COIN — position_xgb — NO_TRADE

**Score:** 0.542 vs policy min 0.55 · **Close:** 825 · **ATR14:** 92.5 · **Volume ratio 20D:** 0.83 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 780–835, entry trigger **835**, stop **755**, risk 80 points (9.58%).

**Targets:** TP1 **915** (1.00R), TP2 **975** (1.75R), TP3 **1,030** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 825: zone 780–835 uses ATR14 92.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 835 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 755 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 915 (1.00R), TP2 975 (1.75R), TP3 1,030 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=92.5, resistance_5/10/20/60=905/1,050/1,370/1,895. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.58% exceeds max strategy risk 9.00%; score 0.542 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## TOBA — position_xgb — NO_TRADE

**Score:** 0.540 vs policy min 0.55 · **Close:** 432 · **ATR14:** 37.5 · **Volume ratio 20D:** 0.61 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 414–436, entry trigger **436**, stop **396**, risk 40 points (9.17%).

**Targets:** TP1 **476** (1.00R), TP2 **505** (1.73R), TP3 **535** (2.48R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 432: zone 414–436 uses ATR14 37.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 436 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 396 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 476 (1.00R), TP2 505 (1.73R), TP3 535 (2.48R). Targets are ATR/structure capped for hold_days=1. ATR14=37.5, resistance_5/10/20/60=462/575/650/815. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.17% exceeds max strategy risk 9.00%; score 0.540 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.35R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SSMS — position_xgb — NO_TRADE

**Score:** 0.537 vs policy min 0.55 · **Close:** 815 · **ATR14:** 89.3 · **Volume ratio 20D:** 1.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 770–825, entry trigger **825**, stop **750**, risk 75 points (9.09%).

**Targets:** TP1 **910** (1.13R), TP2 **955** (1.73R), TP3 **1,005** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 815: zone 770–825 uses ATR14 89.3 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 825 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 750 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 910 (1.13R), TP2 955 (1.73R), TP3 1,005 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=89.3, resistance_5/10/20/60=910/1,310/1,460/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.09% exceeds max strategy risk 9.00%; score 0.537 below policy min_score 0.55; TP1 reward/risk 1.13R is below strategy minimum 1.35R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## MSJA — position_xgb — NO_TRADE

**Score:** 0.536 vs policy min 0.55 · **Close:** 408 · **ATR14:** 38.5 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 390–412, entry trigger **412**, stop **374**, risk 38 points (9.22%).

**Targets:** TP1 **450** (1.00R), TP2 **478** (1.74R), TP3 **505** (2.45R). Recommended base-case RR: **1.74R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 408: zone 390–412 uses ATR14 38.5 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 412 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 374 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 450 (1.00R), TP2 478 (1.74R), TP3 505 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=38.5, resistance_5/10/20/60=436/456/555/560. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.22% exceeds max strategy risk 9.00%; score 0.536 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.35R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## SIMP — position_xgb — NO_TRADE

**Score:** 0.535 vs policy min 0.55 · **Close:** 565 · **ATR14:** 41.1 · **Volume ratio 20D:** 0.49 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 545–570, entry trigger **570**, stop **515**, risk 55 points (9.65%).

**Targets:** TP1 **625** (1.00R), TP2 **665** (1.73R), TP3 **705** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 565: zone 545–570 uses ATR14 41.1 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 570 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 515 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 625 (1.00R), TP2 665 (1.73R), TP3 705 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=41.1, resistance_5/10/20/60=585/660/855/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.65% exceeds max strategy risk 9.00%; score 0.535 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.35R; volume ratio 0.49 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## MBMA — position_xgb — NO_TRADE

**Score:** 0.534 vs policy min 0.55 · **Close:** 474 · **ATR14:** 54.6 · **Volume ratio 20D:** 0.45 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 448–480, entry trigger **480**, stop **436**, risk 44 points (9.17%).

**Targets:** TP1 **525** (1.02R), TP2 **555** (1.70R), TP3 **590** (2.50R). Recommended base-case RR: **1.70R**.

**Why entry:** Entry is a controlled pullback/retest plan around close 474: zone 448–480 uses ATR14 54.6 so the trade avoids chasing a far breakout. Entry is valid only if price can trade/hold around 480 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 436 is capped by max risk 9.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 525 (1.02R), TP2 555 (1.70R), TP3 590 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=54.6, resistance_5/10/20/60=510/615/710/920. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 9.17% exceeds max strategy risk 9.00%; score 0.534 below policy min_score 0.55; TP1 reward/risk 1.02R is below strategy minimum 1.35R; volume ratio 0.45 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Moderate position sleeve; targets can be wider but remain staged.

---

## NICL — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.421 vs policy min 0.55 · **Close:** 605 · **ATR14:** 60.7 · **Volume ratio 20D:** 0.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 580–620, entry trigger **620**, stop **570**, risk 50 points (8.06%).

**Targets:** TP1 **670** (1.00R), TP2 **705** (1.70R), TP3 **775** (3.10R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 605 and ATR14 60.7: buy zone 580–620. Entry is valid only if price can trade/hold around 620 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 570 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 670 (1.00R), TP2 705 (1.70R), TP3 775 (3.10R). Targets are ATR/structure capped for hold_days=1. ATR14=60.7, resistance_5/10/20/60=615/785/925/1,215. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.06% exceeds max strategy risk 7.50%; score 0.421 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.26 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## IRSX — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.411 vs policy min 0.55 · **Close:** 374 · **ATR14:** 45.3 · **Volume ratio 20D:** 0.65 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 358–384, entry trigger **384**, stop **354**, risk 30 points (7.81%).

**Targets:** TP1 **414** (1.00R), TP2 **436** (1.73R), TP3 **456** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 374 and ATR14 45.3: buy zone 358–384. Entry is valid only if price can trade/hold around 384 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 354 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 414 (1.00R), TP2 436 (1.73R), TP3 456 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=45.3, resistance_5/10/20/60=406/480/480/685. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.81% exceeds max strategy risk 7.50%; score 0.411 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## OMED — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.409 vs policy min 0.55 · **Close:** 206 · **ATR14:** 22.0 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 200–254, entry trigger **254**, stop **236**, risk 18 points (7.09%).

**Targets:** TP1 **272** (1.00R), TP2 **286** (1.78R), TP3 **310** (3.11R). Recommended base-case RR: **1.78R**.

**Why entry:** Entry trigger 254 is set above recent resistance 252 plus one IDX tick. This requires confirmation instead of buying blindly at close 206. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 236 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 272 (1.00R), TP2 286 (1.78R), TP3 310 (3.11R). Targets are ATR/structure capped for hold_days=1. ATR14=22.0, resistance_5/10/20/60=250/252/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 23.30% > max 8.00%; entry-to-stop risk 7.09% exceeds max strategy risk 7.00%; score 0.409 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## FUJI — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.408 vs policy min 0.55 · **Close:** 288 · **ATR14:** 25.9 · **Volume ratio 20D:** 1.83 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 278–294, entry trigger **294**, stop **270**, risk 24 points (8.16%).

**Targets:** TP1 **320** (1.08R), TP2 **336** (1.75R), TP3 **352** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 288 and ATR14 25.9: buy zone 278–294. Entry is valid only if price can trade/hold around 294 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 270 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 320 (1.08R), TP2 336 (1.75R), TP3 352 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=25.9, resistance_5/10/20/60=324/336/348/474. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.16% exceeds max strategy risk 7.50%; score 0.408 below policy min_score 0.55; TP1 reward/risk 1.08R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## CUAN — momentum_5d_hgb_defensive — NO_TRADE

**Score:** 0.407 vs policy min 0.55 · **Close:** 785 · **ATR14:** 110.0 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 760–890, entry trigger **890**, stop **825**, risk 65 points (7.30%).

**Targets:** TP1 **955** (1.00R), TP2 **1,005** (1.77R), TP3 **1,050** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 890 is set above recent resistance 885 plus one IDX tick. This requires confirmation instead of buying blindly at close 785. Entry is valid only if price can trade/hold around 890 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 825 is capped by max risk 7.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 955 (1.00R), TP2 1,005 (1.77R), TP3 1,050 (2.46R). Targets are ATR/structure capped for hold_days=1. ATR14=110.0, resistance_5/10/20/60=785/885/1,340/1,850. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 13.38% > max 8.00%; entry-to-stop risk 7.30% exceeds max strategy risk 7.00%; score 0.407 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Selective high-liquidity 5D momentum sleeve.

---

## BEER — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.406 vs policy min 0.55 · **Close:** 112 · **ATR14:** 14.1 · **Volume ratio 20D:** 8.85 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 107–115, entry trigger **115**, stop **106**, risk 9 points (7.83%).

**Targets:** TP1 **124** (1.00R), TP2 **131** (1.78R), TP3 **137** (2.44R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 112 and ATR14 14.1: buy zone 107–115. Entry is valid only if price can trade/hold around 115 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 106 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 124 (1.00R), TP2 131 (1.78R), TP3 137 (2.44R). Targets are ATR/structure capped for hold_days=1. ATR14=14.1, resistance_5/10/20/60=112/119/144/212. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.83% exceeds max strategy risk 7.50%; score 0.406 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## MBMA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.392 vs policy min 0.60 · **Close:** 474 · **ATR14:** 54.6 · **Volume ratio 20D:** 0.45 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 462–620, entry trigger **620**, stop **555**, risk 65 points (10.48%).

**Targets:** TP1 **710** (1.38R), TP2 **735** (1.77R), TP3 **780** (2.46R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 620 is set above recent resistance 615 plus one IDX tick. This requires confirmation instead of buying blindly at close 474. Entry is valid only if price can trade/hold around 620 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 555 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 710 (1.38R), TP2 735 (1.77R), TP3 780 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=54.6, resistance_5/10/20/60=510/615/710/920. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 30.80% > max 15.00%; entry-to-stop risk 10.48% exceeds max strategy risk 10.00%; score 0.392 below policy min_score 0.60; TP1 reward/risk 1.38R is below strategy minimum 1.40R; volume ratio 0.45 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## OMED — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.387 vs policy min 0.60 · **Close:** 206 · **ATR14:** 22.0 · **Volume ratio 20D:** 1.12 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 200–254, entry trigger **254**, stop **228**, risk 26 points (10.24%).

**Targets:** TP1 **280** (1.00R), TP2 **310** (2.15R), TP3 **318** (2.46R). Recommended base-case RR: **2.15R**.

**Why entry:** Entry trigger 254 is set above recent resistance 252 plus one IDX tick. This requires confirmation instead of buying blindly at close 206. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 228 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 280 (1.00R), TP2 310 (2.15R), TP3 318 (2.46R). Targets are ATR/structure capped for hold_days=2. ATR14=22.0, resistance_5/10/20/60=250/252/310/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 23.30% > max 15.00%; entry-to-stop risk 10.24% exceeds max strategy risk 10.00%; score 0.387 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## ALII — market_maker_silent_accum_defensive — NO_TRADE

**Score:** 0.385 vs policy min 0.55 · **Close:** 890 · **ATR14:** 74.3 · **Volume ratio 20D:** 1.98 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 860–905, entry trigger **905**, stop **835**, risk 70 points (7.73%).

**Targets:** TP1 **975** (1.00R), TP2 **1,025** (1.71R), TP3 **1,075** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 890 and ATR14 74.3: buy zone 860–905. Entry is valid only if price can trade/hold around 905 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 835 is capped by max risk 7.5% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 975 (1.00R), TP2 1,025 (1.71R), TP3 1,075 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=74.3, resistance_5/10/20/60=915/950/1,025/1,130. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 7.73% exceeds max strategy risk 7.50%; score 0.385 below policy min_score 0.55; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Defensive accumulation. Prefer retest and clean broker flow.

---

## SSMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.385 vs policy min 0.60 · **Close:** 815 · **ATR14:** 89.3 · **Volume ratio 20D:** 1.59 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 795–1,315, entry trigger **1,315**, stop **1,195**, risk 120 points (9.13%).

**Targets:** TP1 **1,460** (1.21R), TP2 **1,520** (1.71R), TP3 **1,605** (2.42R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 1,315 is set above recent resistance 1,310 plus one IDX tick. This requires confirmation instead of buying blindly at close 815. Entry is valid only if price can trade/hold around 1,315 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,195 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,460 (1.21R), TP2 1,520 (1.71R), TP3 1,605 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=89.3, resistance_5/10/20/60=910/1,310/1,460/1,800. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 61.35% > max 15.00%; score 0.385 below policy min_score 0.60; TP1 reward/risk 1.21R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## BRMS — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.382 vs policy min 0.60 · **Close:** 580 · **ATR14:** 69.6 · **Volume ratio 20D:** 1.08 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 565–790, entry trigger **790**, stop **710**, risk 80 points (10.13%).

**Targets:** TP1 **870** (1.00R), TP2 **930** (1.75R), TP3 **985** (2.44R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 790 is set above recent resistance 785 plus one IDX tick. This requires confirmation instead of buying blindly at close 580. Entry is valid only if price can trade/hold around 790 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 870 (1.00R), TP2 930 (1.75R), TP3 985 (2.44R). Targets are ATR/structure capped for hold_days=2. ATR14=69.6, resistance_5/10/20/60=640/785/845/1,095. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 36.21% > max 15.00%; entry-to-stop risk 10.13% exceeds max strategy risk 10.00%; score 0.382 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## EMTK — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.378 vs policy min 0.60 · **Close:** 605 · **ATR14:** 42.9 · **Volume ratio 20D:** 0.94 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 595–765, entry trigger **765**, stop **705**, risk 60 points (7.84%).

**Targets:** TP1 **845** (1.33R), TP2 **870** (1.75R), TP3 **910** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 765 is set above recent resistance 760 plus one IDX tick. This requires confirmation instead of buying blindly at close 605. Entry is valid only if price can trade/hold around 765 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 705 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 845 (1.33R), TP2 870 (1.75R), TP3 910 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=42.9, resistance_5/10/20/60=675/760/850/995. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 26.45% > max 15.00%; score 0.378 below policy min_score 0.60; TP1 reward/risk 1.33R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## STAA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.376 vs policy min 0.60 · **Close:** 980 · **ATR14:** 52.9 · **Volume ratio 20D:** 2.91 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 965–1,245, entry trigger **1,245**, stop **1,175**, risk 70 points (5.62%).

**Targets:** TP1 **1,320** (1.07R), TP2 **1,365** (1.71R), TP3 **1,415** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Entry trigger 1,245 is set above recent resistance 1,240 plus one IDX tick. This requires confirmation instead of buying blindly at close 980. Entry is valid only if price can trade/hold around 1,245 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 1,175 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,320 (1.07R), TP2 1,365 (1.71R), TP3 1,415 (2.43R). Targets are ATR/structure capped for hold_days=2. ATR14=52.9, resistance_5/10/20/60=1,045/1,240/1,320/1,385. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 27.04% > max 15.00%; score 0.376 below policy min_score 0.60; TP1 reward/risk 1.07R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## MSIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.374 vs policy min 0.60 · **Close:** 370 · **ATR14:** 79.5 · **Volume ratio 20D:** 1.91 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 354–685, entry trigger **685**, stop **615**, risk 70 points (10.22%).

**Targets:** TP1 **755** (1.00R), TP2 **900** (3.07R), TP3 **935** (3.57R). Recommended base-case RR: **3.07R**.

**Why entry:** Entry trigger 685 is set above recent resistance 680 plus one IDX tick. This requires confirmation instead of buying blindly at close 370. Entry is valid only if price can trade/hold around 685 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 615 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 755 (1.00R), TP2 900 (3.07R), TP3 935 (3.57R). Targets are ATR/structure capped for hold_days=2. ATR14=79.5, resistance_5/10/20/60=555/680/900/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 85.14% > max 15.00%; entry-to-stop risk 10.22% exceeds max strategy risk 10.00%; score 0.374 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## KIJA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.374 vs policy min 0.60 · **Close:** 122 · **ATR14:** 9.3 · **Volume ratio 20D:** 0.41 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 120–175, entry trigger **175**, stop **162**, risk 13 points (7.43%).

**Targets:** TP1 **190** (1.15R), TP2 **198** (1.77R), TP3 **208** (2.54R). Recommended base-case RR: **1.77R**.

**Why entry:** Entry trigger 175 is set above recent resistance 174 plus one IDX tick. This requires confirmation instead of buying blindly at close 122. Entry is valid only if price can trade/hold around 175 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 162 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 190 (1.15R), TP2 198 (1.77R), TP3 208 (2.54R). Targets are ATR/structure capped for hold_days=2. ATR14=9.3, resistance_5/10/20/60=133/174/190/230. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 43.44% > max 15.00%; score 0.374 below policy min_score 0.60; TP1 reward/risk 1.15R is below strategy minimum 1.40R; volume ratio 0.41 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## SIMP — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.374 vs policy min 0.60 · **Close:** 565 · **ATR14:** 41.1 · **Volume ratio 20D:** 0.49 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 555–665, entry trigger **665**, stop **610**, risk 55 points (8.27%).

**Targets:** TP1 **720** (1.00R), TP2 **760** (1.73R), TP3 **855** (3.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Entry trigger 665 is set above recent resistance 660 plus one IDX tick. This requires confirmation instead of buying blindly at close 565. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 610 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.00R), TP2 760 (1.73R), TP3 855 (3.45R). Targets are ATR/structure capped for hold_days=2. ATR14=41.1, resistance_5/10/20/60=585/660/855/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 17.70% > max 15.00%; score 0.374 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; volume ratio 0.49 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## COIN — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.372 vs policy min 0.60 · **Close:** 825 · **ATR14:** 92.5 · **Volume ratio 20D:** 0.83 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 805–1,055, entry trigger **1,055**, stop **945**, risk 110 points (10.43%).

**Targets:** TP1 **1,165** (1.00R), TP2 **1,360** (2.77R), TP3 **1,370** (2.86R). Recommended base-case RR: **2.77R**.

**Why entry:** Entry trigger 1,055 is set above recent resistance 1,050 plus one IDX tick. This requires confirmation instead of buying blindly at close 825. Entry is valid only if price can trade/hold around 1,055 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 945 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,165 (1.00R), TP2 1,360 (2.77R), TP3 1,370 (2.86R). Targets are ATR/structure capped for hold_days=2. ATR14=92.5, resistance_5/10/20/60=905/1,050/1,370/1,895. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 27.88% > max 15.00%; entry-to-stop risk 10.43% exceeds max strategy risk 10.00%; score 0.372 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## TPMA — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.371 vs policy min 0.60 · **Close:** 438 · **ATR14:** 20.3 · **Volume ratio 20D:** 1.32 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 432–555, entry trigger **555**, stop **525**, risk 30 points (5.41%).

**Targets:** TP1 **585** (1.00R), TP2 **610** (1.83R), TP3 **630** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Entry trigger 555 is set above recent resistance 550 plus one IDX tick. This requires confirmation instead of buying blindly at close 438. Entry is valid only if price can trade/hold around 555 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 525 uses 1.30×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 585 (1.00R), TP2 610 (1.83R), TP3 630 (2.50R). Targets are ATR/structure capped for hold_days=2. ATR14=20.3, resistance_5/10/20/60=510/550/585/630. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 26.71% > max 15.00%; score 0.371 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---

## GTSI — momentum_10d_hgb_aggressive — NO_TRADE

**Score:** 0.368 vs policy min 0.60 · **Close:** 140 · **ATR14:** 19.6 · **Volume ratio 20D:** 2.48 · **Hold:** 2 day(s)

**Execution numbers:** Buy zone 136–224, entry trigger **224**, stop **200**, risk 24 points (10.71%).

**Targets:** TP1 **248** (1.00R), TP2 **266** (1.75R), TP3 **282** (2.42R). Recommended base-case RR: **1.75R**.

**Why entry:** Entry trigger 224 is set above recent resistance 222 plus one IDX tick. This requires confirmation instead of buying blindly at close 140. Entry is valid only if price can trade/hold around 224 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 200 is capped by max risk 10.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 248 (1.00R), TP2 266 (1.75R), TP3 282 (2.42R). Targets are ATR/structure capped for hold_days=2. ATR14=19.6, resistance_5/10/20/60=180/222/240/348. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 60.00% > max 15.00%; entry-to-stop risk 10.71% exceeds max strategy risk 10.00%; score 0.368 below policy min_score 0.60; TP1 reward/risk 1.00R is below strategy minimum 1.40R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Aggressive momentum. Avoid chasing triggers that are too extended.

---
