# Numeric Trading Desk Report — 2026-05-22

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| CONDITIONAL | 6 |
| NO_TRADE | 36 |

## KIJA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.694 vs policy min 0.05 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 117–124, entry trigger **124**, stop **118**, risk 6 points (4.84%).

**Targets:** TP1 **130** (1.00R), TP2 **135** (1.83R), TP3 **139** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 10.1: buy zone 117–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 130 (1.00R), TP2 135 (1.83R), TP3 139 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## IRSX — scalping_continual_defensive — CONDITIONAL

**Score:** 0.659 vs policy min 0.05 · **Close:** 328 · **ATR14:** 45.7 · **Volume ratio 20D:** 2.40 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 312–338, entry trigger **338**, stop **316**, risk 22 points (6.51%).

**Targets:** TP1 **362** (1.09R), TP2 **376** (1.73R), TP3 **454** (5.27R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 328 and ATR14 45.7: buy zone 312–338. Entry is valid only if price can trade/hold around 338 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 316 is placed below support structure (318 / 318). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 362 (1.09R), TP2 376 (1.73R), TP3 454 (5.27R). Targets are ATR/structure capped for hold_days=1. ATR14=45.7, resistance_5/10/20/60=472/480/525/685. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.615 vs policy min 0.30 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 117–124, entry trigger **124**, stop **118**, risk 6 points (4.84%).

**Targets:** TP1 **130** (1.00R), TP2 **135** (1.83R), TP3 **174** (8.33R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 10.1: buy zone 117–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 130 (1.00R), TP2 135 (1.83R), TP3 174 (8.33R). Targets are ATR/structure capped for hold_days=5. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.559 vs policy min 0.30 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 117–124, entry trigger **124**, stop **118**, risk 6 points (4.84%).

**Targets:** TP1 **130** (1.00R), TP2 **135** (1.83R), TP3 **168** (7.33R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 10.1: buy zone 117–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 130 (1.00R), TP2 135 (1.83R), TP3 168 (7.33R). Targets are ATR/structure capped for hold_days=3. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — swing_continual_defensive — CONDITIONAL

**Score:** 0.559 vs policy min 0.30 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 117–124, entry trigger **124**, stop **118**, risk 6 points (4.84%).

**Targets:** TP1 **130** (1.00R), TP2 **135** (1.83R), TP3 **139** (2.50R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 10.1: buy zone 117–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 130 (1.00R), TP2 135 (1.83R), TP3 139 (2.50R). Targets are ATR/structure capped for hold_days=1. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## KIJA — position_continual — CONDITIONAL

**Score:** 0.301 vs policy min 0.30 · **Close:** 121 · **ATR14:** 10.1 · **Volume ratio 20D:** 2.37 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 117–124, entry trigger **124**, stop **118**, risk 6 points (4.84%).

**Targets:** TP1 **130** (1.00R), TP2 **174** (8.33R), TP3 **177** (8.83R). Recommended base-case RR: **8.33R**.

**Why entry:** Hybrid entry uses close 121 and ATR14 10.1: buy zone 117–124. Entry is valid only if price can trade/hold around 124 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 118 is placed below support structure (119 / 119). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 130 (1.00R), TP2 174 (8.33R), TP3 177 (8.83R). Targets are ATR/structure capped for hold_days=10. ATR14=10.1, resistance_5/10/20/60=174/189/220/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DIVA — ara_candidate_continual — NO_TRADE

**Score:** 0.876 vs policy min 0.50 · **Close:** 136 · **ATR14:** 26.3 · **Volume ratio 20D:** 0.96 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 126–142, entry trigger **142**, stop **130**, risk 12 points (8.45%).

**Targets:** TP1 **156** (1.17R), TP2 **180** (3.17R), TP3 **186** (3.67R). Recommended base-case RR: **3.17R**.

**Why entry:** Hybrid entry uses close 136 and ATR14 26.3: buy zone 126–142. Entry is valid only if price can trade/hold around 142 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 130 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 156 (1.17R), TP2 180 (3.17R), TP3 186 (3.67R). Targets are ATR/structure capped for hold_days=1. ATR14=26.3, resistance_5/10/20/60=180/198/202/254. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.45% exceeds max strategy risk 8.00%; TP1 reward/risk 1.17R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — scalping_continual_defensive — NO_TRADE

**Score:** 0.699 vs policy min 0.05 · **Close:** 545 · **ATR14:** 184.6 · **Volume ratio 20D:** 3.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 480–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **680** (1.90R), TP2 **920** (6.70R), TP3 **945** (7.20R). Recommended base-case RR: **6.70R**.

**Why entry:** Hybrid entry uses close 545 and ATR14 184.6: buy zone 480–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.90R), TP2 920 (6.70R), TP3 945 (7.20R). Targets are ATR/structure capped for hold_days=1. ATR14=184.6, resistance_5/10/20/60=945/1,720/3,400/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NZIA — scalping_continual_defensive — NO_TRADE

**Score:** 0.689 vs policy min 0.05 · **Close:** 117 · **ATR14:** 16.4 · **Volume ratio 20D:** 0.40 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 111–121, entry trigger **121**, stop **111**, risk 10 points (8.26%).

**Targets:** TP1 **131** (1.00R), TP2 **138** (1.70R), TP3 **160** (3.90R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 117 and ATR14 16.4: buy zone 111–121. Entry is valid only if price can trade/hold around 121 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 111 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 131 (1.00R), TP2 138 (1.70R), TP3 160 (3.90R). Targets are ATR/structure capped for hold_days=1. ATR14=16.4, resistance_5/10/20/60=160/183/214/316. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.40 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## WBSA — scalping_continual_defensive — NO_TRADE

**Score:** 0.658 vs policy min 0.05 · **Close:** 630 · **ATR14:** 679.6 · **Volume ratio 20D:** 2.04 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 392–770, entry trigger **770**, stop **705**, risk 65 points (8.44%).

**Targets:** TP1 **1,325** (8.54R), TP2 **1,360** (9.08R), TP3 **1,395** (9.62R). Recommended base-case RR: **9.08R**.

**Why entry:** Hybrid entry uses close 630 and ATR14 679.6: buy zone 392–770. Entry is valid only if price can trade/hold around 770 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 705 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,325 (8.54R), TP2 1,360 (9.08R), TP3 1,395 (9.62R). Targets are ATR/structure capped for hold_days=1. ATR14=679.6, resistance_5/10/20/60=1,325/1,605/1,605/1,605. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry trigger is too far from latest close: 22.22% > max 8.00%; entry-to-stop risk 8.44% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.600 vs policy min 0.30 · **Close:** 482 · **ATR14:** 54.2 · **Volume ratio 20D:** 2.58 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 462–494, entry trigger **494**, stop **454**, risk 40 points (8.10%).

**Targets:** TP1 **580** (2.15R), TP2 **600** (2.65R), TP3 **620** (3.15R). Recommended base-case RR: **2.65R**.

**Why entry:** Hybrid entry uses close 482 and ATR14 54.2: buy zone 462–494. Entry is valid only if price can trade/hold around 494 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 454 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 580 (2.15R), TP2 600 (2.65R), TP3 620 (3.15R). Targets are ATR/structure capped for hold_days=5. ATR14=54.2, resistance_5/10/20/60=580/690/770/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.10% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.599 vs policy min 0.30 · **Close:** 750 · **ATR14:** 109.3 · **Volume ratio 20D:** 0.69 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 710–775, entry trigger **775**, stop **710**, risk 65 points (8.39%).

**Targets:** TP1 **1,000** (3.46R), TP2 **1,035** (4.00R), TP3 **1,070** (4.54R). Recommended base-case RR: **4.00R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 109.3: buy zone 710–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,000 (3.46R), TP2 1,035 (4.00R), TP3 1,070 (4.54R). Targets are ATR/structure capped for hold_days=5. ATR14=109.3, resistance_5/10/20/60=1,000/1,230/1,255/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.39% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.595 vs policy min 0.30 · **Close:** 545 · **ATR14:** 184.6 · **Volume ratio 20D:** 3.26 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 480–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **945** (7.20R), TP2 **970** (7.70R), TP3 **995** (8.20R). Recommended base-case RR: **7.70R**.

**Why entry:** Hybrid entry uses close 545 and ATR14 184.6: buy zone 480–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 945 (7.20R), TP2 970 (7.70R), TP3 995 (8.20R). Targets are ATR/structure capped for hold_days=5. ATR14=184.6, resistance_5/10/20/60=945/1,720/3,400/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.593 vs policy min 0.30 · **Close:** 515 · **ATR14:** 119.8 · **Volume ratio 20D:** 1.83 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 472–540, entry trigger **540**, stop **496**, risk 44 points (8.15%).

**Targets:** TP1 **810** (6.14R), TP2 **835** (6.70R), TP3 **860** (7.27R). Recommended base-case RR: **6.70R**.

**Why entry:** Hybrid entry uses close 515 and ATR14 119.8: buy zone 472–540. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 496 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 810 (6.14R), TP2 835 (6.70R), TP3 860 (7.27R). Targets are ATR/structure capped for hold_days=5. ATR14=119.8, resistance_5/10/20/60=810/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.592 vs policy min 0.30 · **Close:** 720 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.75 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 680–745, entry trigger **745**, stop **685**, risk 60 points (8.05%).

**Targets:** TP1 **1,000** (4.25R), TP2 **1,020** (4.58R), TP3 **1,050** (5.08R). Recommended base-case RR: **4.58R**.

**Why entry:** Hybrid entry uses close 720 and ATR14 113.9: buy zone 680–745. Entry is valid only if price can trade/hold around 745 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 685 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,000 (4.25R), TP2 1,020 (4.58R), TP3 1,050 (5.08R). Targets are ATR/structure capped for hold_days=5. ATR14=113.9, resistance_5/10/20/60=1,020/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DEWA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.581 vs policy min 0.30 · **Close:** 378 · **ATR14:** 41.5 · **Volume ratio 20D:** 1.88 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 362–388, entry trigger **388**, stop **356**, risk 32 points (8.25%).

**Targets:** TP1 **482** (2.94R), TP2 **498** (3.44R), TP3 **515** (3.97R). Recommended base-case RR: **3.44R**.

**Why entry:** Hybrid entry uses close 378 and ATR14 41.5: buy zone 362–388. Entry is valid only if price can trade/hold around 388 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 356 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 482 (2.94R), TP2 498 (3.44R), TP3 515 (3.97R). Targets are ATR/structure capped for hold_days=5. ATR14=41.5, resistance_5/10/20/60=482/535/575/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.25% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.554 vs policy min 0.30 · **Close:** 720 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.75 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 680–745, entry trigger **745**, stop **685**, risk 60 points (8.05%).

**Targets:** TP1 **805** (1.00R), TP2 **1,020** (4.58R), TP3 **1,050** (5.08R). Recommended base-case RR: **4.58R**.

**Why entry:** Hybrid entry uses close 720 and ATR14 113.9: buy zone 680–745. Entry is valid only if price can trade/hold around 745 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 685 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 805 (1.00R), TP2 1,020 (4.58R), TP3 1,050 (5.08R). Targets are ATR/structure capped for hold_days=3. ATR14=113.9, resistance_5/10/20/60=1,020/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — swing_continual_defensive — NO_TRADE

**Score:** 0.554 vs policy min 0.30 · **Close:** 720 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 680–745, entry trigger **745**, stop **685**, risk 60 points (8.05%).

**Targets:** TP1 **805** (1.00R), TP2 **850** (1.75R), TP3 **1,020** (4.58R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 720 and ATR14 113.9: buy zone 680–745. Entry is valid only if price can trade/hold around 745 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 685 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 805 (1.00R), TP2 850 (1.75R), TP3 1,020 (4.58R). Targets are ATR/structure capped for hold_days=1. ATR14=113.9, resistance_5/10/20/60=1,020/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.540 vs policy min 0.30 · **Close:** 515 · **ATR14:** 119.8 · **Volume ratio 20D:** 1.83 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 472–540, entry trigger **540**, stop **496**, risk 44 points (8.15%).

**Targets:** TP1 **600** (1.36R), TP2 **810** (6.14R), TP3 **835** (6.70R). Recommended base-case RR: **6.14R**.

**Why entry:** Hybrid entry uses close 515 and ATR14 119.8: buy zone 472–540. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 496 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 600 (1.36R), TP2 810 (6.14R), TP3 835 (6.70R). Targets are ATR/structure capped for hold_days=3. ATR14=119.8, resistance_5/10/20/60=810/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — swing_continual_defensive — NO_TRADE

**Score:** 0.540 vs policy min 0.30 · **Close:** 515 · **ATR14:** 119.8 · **Volume ratio 20D:** 1.83 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 472–540, entry trigger **540**, stop **496**, risk 44 points (8.15%).

**Targets:** TP1 **600** (1.36R), TP2 **615** (1.70R), TP3 **810** (6.14R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 515 and ATR14 119.8: buy zone 472–540. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 496 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 600 (1.36R), TP2 615 (1.70R), TP3 810 (6.14R). Targets are ATR/structure capped for hold_days=1. ATR14=119.8, resistance_5/10/20/60=810/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.486 vs policy min 0.30 · **Close:** 545 · **ATR14:** 184.6 · **Volume ratio 20D:** 3.26 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 480–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **905** (6.40R), TP2 **945** (7.20R), TP3 **970** (7.70R). Recommended base-case RR: **7.20R**.

**Why entry:** Hybrid entry uses close 545 and ATR14 184.6: buy zone 480–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 905 (6.40R), TP2 945 (7.20R), TP3 970 (7.70R). Targets are ATR/structure capped for hold_days=3. ATR14=184.6, resistance_5/10/20/60=945/1,720/3,400/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — NO_TRADE

**Score:** 0.486 vs policy min 0.30 · **Close:** 545 · **ATR14:** 184.6 · **Volume ratio 20D:** 3.26 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 480–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **680** (1.90R), TP2 **920** (6.70R), TP3 **945** (7.20R). Recommended base-case RR: **6.70R**.

**Why entry:** Hybrid entry uses close 545 and ATR14 184.6: buy zone 480–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 680 (1.90R), TP2 920 (6.70R), TP3 945 (7.20R). Targets are ATR/structure capped for hold_days=1. ATR14=184.6, resistance_5/10/20/60=945/1,720/3,400/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.479 vs policy min 0.30 · **Close:** 750 · **ATR14:** 109.3 · **Volume ratio 20D:** 0.69 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 710–775, entry trigger **775**, stop **710**, risk 65 points (8.39%).

**Targets:** TP1 **965** (2.92R), TP2 **1,000** (3.46R), TP3 **1,035** (4.00R). Recommended base-case RR: **3.46R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 109.3: buy zone 710–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 965 (2.92R), TP2 1,000 (3.46R), TP3 1,035 (4.00R). Targets are ATR/structure capped for hold_days=3. ATR14=109.3, resistance_5/10/20/60=1,000/1,230/1,255/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.39% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CDIA — swing_continual_defensive — NO_TRADE

**Score:** 0.479 vs policy min 0.30 · **Close:** 750 · **ATR14:** 109.3 · **Volume ratio 20D:** 0.69 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 710–775, entry trigger **775**, stop **710**, risk 65 points (8.39%).

**Targets:** TP1 **840** (1.00R), TP2 **975** (3.08R), TP3 **1,000** (3.46R). Recommended base-case RR: **3.08R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 109.3: buy zone 710–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 840 (1.00R), TP2 975 (3.08R), TP3 1,000 (3.46R). Targets are ATR/structure capped for hold_days=1. ATR14=109.3, resistance_5/10/20/60=1,000/1,230/1,255/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.39% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.468 vs policy min 0.30 · **Close:** 142 · **ATR14:** 20.9 · **Volume ratio 20D:** 1.12 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 134–147, entry trigger **147**, stop **135**, risk 12 points (8.16%).

**Targets:** TP1 **174** (2.25R), TP2 **180** (2.75R), TP3 **186** (3.25R). Recommended base-case RR: **2.75R**.

**Why entry:** Hybrid entry uses close 142 and ATR14 20.9: buy zone 134–147. Entry is valid only if price can trade/hold around 147 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 135 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 174 (2.25R), TP2 180 (2.75R), TP3 186 (3.25R). Targets are ATR/structure capped for hold_days=3. ATR14=20.9, resistance_5/10/20/60=174/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.16% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BNBR — swing_continual_defensive — NO_TRADE

**Score:** 0.468 vs policy min 0.30 · **Close:** 142 · **ATR14:** 20.9 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 134–147, entry trigger **147**, stop **135**, risk 12 points (8.16%).

**Targets:** TP1 **168** (1.75R), TP2 **174** (2.25R), TP3 **176** (2.42R). Recommended base-case RR: **2.25R**.

**Why entry:** Hybrid entry uses close 142 and ATR14 20.9: buy zone 134–147. Entry is valid only if price can trade/hold around 147 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 135 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 168 (1.75R), TP2 174 (2.25R), TP3 176 (2.42R). Targets are ATR/structure capped for hold_days=1. ATR14=20.9, resistance_5/10/20/60=174/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.16% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CDIA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.462 vs policy min 0.30 · **Close:** 750 · **ATR14:** 109.3 · **Volume ratio 20D:** 0.69 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 710–775, entry trigger **775**, stop **710**, risk 65 points (8.39%).

**Targets:** TP1 **1,000** (3.46R), TP2 **1,035** (4.00R), TP3 **1,070** (4.54R). Recommended base-case RR: **4.00R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 109.3: buy zone 710–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,000 (3.46R), TP2 1,035 (4.00R), TP3 1,070 (4.54R). Targets are ATR/structure capped for hold_days=10. ATR14=109.3, resistance_5/10/20/60=1,000/1,230/1,255/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.39% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.459 vs policy min 0.30 · **Close:** 515 · **ATR14:** 119.8 · **Volume ratio 20D:** 1.83 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 472–540, entry trigger **540**, stop **496**, risk 44 points (8.15%).

**Targets:** TP1 **810** (6.14R), TP2 **835** (6.70R), TP3 **860** (7.27R). Recommended base-case RR: **6.70R**.

**Why entry:** Hybrid entry uses close 515 and ATR14 119.8: buy zone 472–540. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 496 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 810 (6.14R), TP2 835 (6.70R), TP3 860 (7.27R). Targets are ATR/structure capped for hold_days=10. ATR14=119.8, resistance_5/10/20/60=810/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.15% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.447 vs policy min 0.30 · **Close:** 184 · **ATR14:** 26.9 · **Volume ratio 20D:** 2.01 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 174–190, entry trigger **190**, stop **174**, risk 16 points (8.42%).

**Targets:** TP1 **234** (2.75R), TP2 **242** (3.25R), TP3 **250** (3.75R). Recommended base-case RR: **3.25R**.

**Why entry:** Hybrid entry uses close 184 and ATR14 26.9: buy zone 174–190. Entry is valid only if price can trade/hold around 190 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 174 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 234 (2.75R), TP2 242 (3.25R), TP3 250 (3.75R). Targets are ATR/structure capped for hold_days=3. ATR14=26.9, resistance_5/10/20/60=234/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.42% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BIPI — swing_continual_defensive — NO_TRADE

**Score:** 0.447 vs policy min 0.30 · **Close:** 184 · **ATR14:** 26.9 · **Volume ratio 20D:** 2.01 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 174–190, entry trigger **190**, stop **174**, risk 16 points (8.42%).

**Targets:** TP1 **206** (1.00R), TP2 **234** (2.75R), TP3 **242** (3.25R). Recommended base-case RR: **2.75R**.

**Why entry:** Hybrid entry uses close 184 and ATR14 26.9: buy zone 174–190. Entry is valid only if price can trade/hold around 190 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 174 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 206 (1.00R), TP2 234 (2.75R), TP3 242 (3.25R). Targets are ATR/structure capped for hold_days=1. ATR14=26.9, resistance_5/10/20/60=234/262/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.42% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BUVA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.420 vs policy min 0.30 · **Close:** 720 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.75 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 680–745, entry trigger **745**, stop **685**, risk 60 points (8.05%).

**Targets:** TP1 **1,020** (4.58R), TP2 **1,050** (5.08R), TP3 **1,080** (5.58R). Recommended base-case RR: **5.08R**.

**Why entry:** Hybrid entry uses close 720 and ATR14 113.9: buy zone 680–745. Entry is valid only if price can trade/hold around 745 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 685 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,020 (4.58R), TP2 1,050 (5.08R), TP3 1,080 (5.58R). Targets are ATR/structure capped for hold_days=10. ATR14=113.9, resistance_5/10/20/60=1,020/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.414 vs policy min 0.30 · **Close:** 545 · **ATR14:** 184.6 · **Volume ratio 20D:** 3.26 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 480–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **945** (7.20R), TP2 **970** (7.70R), TP3 **995** (8.20R). Recommended base-case RR: **7.70R**.

**Why entry:** Hybrid entry uses close 545 and ATR14 184.6: buy zone 480–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 945 (7.20R), TP2 970 (7.70R), TP3 995 (8.20R). Targets are ATR/structure capped for hold_days=10. ATR14=184.6, resistance_5/10/20/60=945/1,720/3,400/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.55% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — momentum_20d_continual_research — NO_TRADE

**Score:** 0.409 vs policy min 0.30 · **Close:** 248 · **ATR14:** 24.7 · **Volume ratio 20D:** 0.76 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 238–254, entry trigger **254**, stop **232**, risk 22 points (8.66%).

**Targets:** TP1 **290** (1.64R), TP2 **292** (1.73R), TP3 **308** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 248 and ATR14 24.7: buy zone 238–254. Entry is valid only if price can trade/hold around 254 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 232 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 290 (1.64R), TP2 292 (1.73R), TP3 308 (2.45R). Targets are ATR/structure capped for hold_days=10. ATR14=24.7, resistance_5/10/20/60=290/392/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.66% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — NO_TRADE

**Score:** 0.311 vs policy min 0.30 · **Close:** 545 · **ATR14:** 184.6 · **Volume ratio 20D:** 3.26 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 480–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **945** (7.20R), TP2 **970** (7.70R), TP3 **995** (8.20R). Recommended base-case RR: **7.70R**.

**Why entry:** Hybrid entry uses close 545 and ATR14 184.6: buy zone 480–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 945 (7.20R), TP2 970 (7.70R), TP3 995 (8.20R). Targets are ATR/structure capped for hold_days=10. ATR14=184.6, resistance_5/10/20/60=945/1,720/3,400/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CDIA — position_continual — NO_TRADE

**Score:** 0.311 vs policy min 0.30 · **Close:** 750 · **ATR14:** 109.3 · **Volume ratio 20D:** 0.69 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 710–775, entry trigger **775**, stop **710**, risk 65 points (8.39%).

**Targets:** TP1 **1,000** (3.46R), TP2 **1,035** (4.00R), TP3 **1,070** (4.54R). Recommended base-case RR: **4.00R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 109.3: buy zone 710–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 710 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,000 (3.46R), TP2 1,035 (4.00R), TP3 1,070 (4.54R). Targets are ATR/structure capped for hold_days=10. ATR14=109.3, resistance_5/10/20/60=1,000/1,230/1,255/1,340. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.39% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BUVA — position_continual — NO_TRADE

**Score:** 0.309 vs policy min 0.30 · **Close:** 720 · **ATR14:** 113.9 · **Volume ratio 20D:** 1.75 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 680–745, entry trigger **745**, stop **685**, risk 60 points (8.05%).

**Targets:** TP1 **1,020** (4.58R), TP2 **1,050** (5.08R), TP3 **1,080** (5.58R). Recommended base-case RR: **5.08R**.

**Why entry:** Hybrid entry uses close 720 and ATR14 113.9: buy zone 680–745. Entry is valid only if price can trade/hold around 745 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 685 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,020 (4.58R), TP2 1,050 (5.08R), TP3 1,080 (5.58R). Targets are ATR/structure capped for hold_days=10. ATR14=113.9, resistance_5/10/20/60=1,020/1,175/1,380/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.05% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — NO_TRADE

**Score:** 0.307 vs policy min 0.30 · **Close:** 515 · **ATR14:** 119.8 · **Volume ratio 20D:** 1.83 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 472–540, entry trigger **540**, stop **496**, risk 44 points (8.15%).

**Targets:** TP1 **810** (6.14R), TP2 **835** (6.70R), TP3 **860** (7.27R). Recommended base-case RR: **6.70R**.

**Why entry:** Hybrid entry uses close 515 and ATR14 119.8: buy zone 472–540. Entry is valid only if price can trade/hold around 540 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 496 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 810 (6.14R), TP2 835 (6.70R), TP3 860 (7.27R). Targets are ATR/structure capped for hold_days=10. ATR14=119.8, resistance_5/10/20/60=810/1,305/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — NO_TRADE

**Score:** 0.306 vs policy min 0.30 · **Close:** 142 · **ATR14:** 20.9 · **Volume ratio 20D:** 1.12 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 134–147, entry trigger **147**, stop **135**, risk 12 points (8.16%).

**Targets:** TP1 **174** (2.25R), TP2 **180** (2.75R), TP3 **186** (3.25R). Recommended base-case RR: **2.75R**.

**Why entry:** Hybrid entry uses close 142 and ATR14 20.9: buy zone 134–147. Entry is valid only if price can trade/hold around 147 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 135 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 174 (2.25R), TP2 180 (2.75R), TP3 186 (3.25R). Targets are ATR/structure capped for hold_days=10. ATR14=20.9, resistance_5/10/20/60=174/224/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.16% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MBMA — position_continual — NO_TRADE

**Score:** 0.303 vs policy min 0.30 · **Close:** 482 · **ATR14:** 54.2 · **Volume ratio 20D:** 2.58 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 462–494, entry trigger **494**, stop **454**, risk 40 points (8.10%).

**Targets:** TP1 **580** (2.15R), TP2 **600** (2.65R), TP3 **620** (3.15R). Recommended base-case RR: **2.65R**.

**Why entry:** Hybrid entry uses close 482 and ATR14 54.2: buy zone 462–494. Entry is valid only if price can trade/hold around 494 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 454 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 580 (2.15R), TP2 600 (2.65R), TP3 620 (3.15R). Targets are ATR/structure capped for hold_days=10. ATR14=54.2, resistance_5/10/20/60=580/690/770/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.10% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRIN — position_continual — NO_TRADE

**Score:** 0.290 vs policy min 0.30 · **Close:** 498 · **ATR14:** 69.6 · **Volume ratio 20D:** 1.03 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 472–515, entry trigger **515**, stop **472**, risk 43 points (8.35%).

**Targets:** TP1 **600** (1.98R), TP2 **625** (2.56R), TP3 **650** (3.14R). Recommended base-case RR: **2.56R**.

**Why entry:** Hybrid entry uses close 498 and ATR14 69.6: buy zone 472–515. Entry is valid only if price can trade/hold around 515 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 472 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 600 (1.98R), TP2 625 (2.56R), TP3 650 (3.14R). Targets are ATR/structure capped for hold_days=10. ATR14=69.6, resistance_5/10/20/60=600/740/870/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.35% exceeds max strategy risk 8.00%; score 0.290 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## NSSS — position_continual — NO_TRADE

**Score:** 0.282 vs policy min 0.30 · **Close:** 472 · **ATR14:** 78.8 · **Volume ratio 20D:** 0.36 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 444–488, entry trigger **488**, stop **448**, risk 40 points (8.20%).

**Targets:** TP1 **740** (6.30R), TP2 **770** (7.05R), TP3 **790** (7.55R). Recommended base-case RR: **7.05R**.

**Why entry:** Hybrid entry uses close 472 and ATR14 78.8: buy zone 444–488. Entry is valid only if price can trade/hold around 488 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 448 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 740 (6.30R), TP2 770 (7.05R), TP3 790 (7.55R). Targets are ATR/structure capped for hold_days=10. ATR14=78.8, resistance_5/10/20/60=770/865/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.20% exceeds max strategy risk 8.00%; score 0.282 below policy min_score 0.30; volume ratio 0.36 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## KOKA — position_continual — NO_TRADE

**Score:** 0.282 vs policy min 0.30 · **Close:** 119 · **ATR14:** 15.6 · **Volume ratio 20D:** 3.32 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 113–123, entry trigger **123**, stop **113**, risk 10 points (8.13%).

**Targets:** TP1 **148** (2.50R), TP2 **153** (3.00R), TP3 **158** (3.50R). Recommended base-case RR: **3.00R**.

**Why entry:** Hybrid entry uses close 119 and ATR14 15.6: buy zone 113–123. Entry is valid only if price can trade/hold around 123 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 113 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 148 (2.50R), TP2 153 (3.00R), TP3 158 (3.50R). Targets are ATR/structure capped for hold_days=10. ATR14=15.6, resistance_5/10/20/60=148/185/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.13% exceeds max strategy risk 8.00%; score 0.282 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
