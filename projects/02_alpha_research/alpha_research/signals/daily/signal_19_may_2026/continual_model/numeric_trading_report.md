# Numeric Trading Desk Report — 2026-05-18

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 5 |
| CONDITIONAL | 15 |
| WATCHLIST_ONLY | 5 |
| NO_TRADE | 17 |

## DSSA — scalping_continual_defensive — ACTIONABLE

**Score:** 0.736 vs policy min 0.05 · **Close:** 880 · **ATR14:** 247.5 · **Volume ratio 20D:** 1.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 790–930, entry trigger **930**, stop **875**, risk 55 points (5.91%).

**Targets:** TP1 **1,055** (2.27R), TP2 **1,085** (2.82R), TP3 **1,115** (3.36R). Recommended base-case RR: **2.82R**.

**Why entry:** Hybrid entry uses close 880 and ATR14 247.5: buy zone 790–930. Entry is valid only if price can trade/hold around 930 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 875 is placed below support structure (880 / 880). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,055 (2.27R), TP2 1,085 (2.82R), TP3 1,115 (3.36R). Targets are ATR/structure capped for hold_days=1. ATR14=247.5, resistance_5/10/20/60=1,700/2,340/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.560 vs policy min 0.30 · **Close:** 880 · **ATR14:** 247.5 · **Volume ratio 20D:** 1.86 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 790–930, entry trigger **930**, stop **875**, risk 55 points (5.91%).

**Targets:** TP1 **1,055** (2.27R), TP2 **1,700** (14.00R), TP3 **1,730** (14.55R). Recommended base-case RR: **14.00R**.

**Why entry:** Hybrid entry uses close 880 and ATR14 247.5: buy zone 790–930. Entry is valid only if price can trade/hold around 930 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 875 is placed below support structure (880 / 880). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,055 (2.27R), TP2 1,700 (14.00R), TP3 1,730 (14.55R). Targets are ATR/structure capped for hold_days=5. ATR14=247.5, resistance_5/10/20/60=1,700/2,340/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_5d_continual_defensive — ACTIONABLE

**Score:** 0.501 vs policy min 0.30 · **Close:** 880 · **ATR14:** 247.5 · **Volume ratio 20D:** 1.86 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 790–930, entry trigger **930**, stop **875**, risk 55 points (5.91%).

**Targets:** TP1 **1,055** (2.27R), TP2 **1,700** (14.00R), TP3 **1,730** (14.55R). Recommended base-case RR: **14.00R**.

**Why entry:** Hybrid entry uses close 880 and ATR14 247.5: buy zone 790–930. Entry is valid only if price can trade/hold around 930 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 875 is placed below support structure (880 / 880). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,055 (2.27R), TP2 1,700 (14.00R), TP3 1,730 (14.55R). Targets are ATR/structure capped for hold_days=3. ATR14=247.5, resistance_5/10/20/60=1,700/2,340/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — swing_continual_defensive — ACTIONABLE

**Score:** 0.501 vs policy min 0.30 · **Close:** 880 · **ATR14:** 247.5 · **Volume ratio 20D:** 1.86 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 790–930, entry trigger **930**, stop **875**, risk 55 points (5.91%).

**Targets:** TP1 **1,055** (2.27R), TP2 **1,085** (2.82R), TP3 **1,115** (3.36R). Recommended base-case RR: **2.82R**.

**Why entry:** Hybrid entry uses close 880 and ATR14 247.5: buy zone 790–930. Entry is valid only if price can trade/hold around 930 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 875 is placed below support structure (880 / 880). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,055 (2.27R), TP2 1,085 (2.82R), TP3 1,115 (3.36R). Targets are ATR/structure capped for hold_days=1. ATR14=247.5, resistance_5/10/20/60=1,700/2,340/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.455 vs policy min 0.30 · **Close:** 288 · **ATR14:** 24.7 · **Volume ratio 20D:** 2.31 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 278–294, entry trigger **294**, stop **286**, risk 8 points (2.72%).

**Targets:** TP1 **308** (1.75R), TP2 **392** (12.25R), TP3 **396** (12.75R). Recommended base-case RR: **12.25R**.

**Why entry:** Hybrid entry uses close 288 and ATR14 24.7: buy zone 278–294. Entry is valid only if price can trade/hold around 294 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 286 is placed below support structure (288 / 288). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 308 (1.75R), TP2 392 (12.25R), TP3 396 (12.75R). Targets are ATR/structure capped for hold_days=5. ATR14=24.7, resistance_5/10/20/60=392/426/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — ara_candidate_continual — CONDITIONAL

**Score:** 0.857 vs policy min 0.50 · **Close:** 750 · **ATR14:** 118.2 · **Volume ratio 20D:** 1.65 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 705–775, entry trigger **775**, stop **720**, risk 55 points (7.10%).

**Targets:** TP1 **835** (1.09R), TP2 **870** (1.73R), TP3 **910** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 118.2: buy zone 705–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is placed below support structure (725 / 725). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.09R), TP2 870 (1.73R), TP3 910 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=118.2, resistance_5/10/20/60=1,305/1,430/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — scalping_continual_defensive — CONDITIONAL

**Score:** 0.745 vs policy min 0.05 · **Close:** 750 · **ATR14:** 118.2 · **Volume ratio 20D:** 1.65 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 705–775, entry trigger **775**, stop **720**, risk 55 points (7.10%).

**Targets:** TP1 **835** (1.09R), TP2 **870** (1.73R), TP3 **910** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 118.2: buy zone 705–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is placed below support structure (725 / 725). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.09R), TP2 870 (1.73R), TP3 910 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=118.2, resistance_5/10/20/60=1,305/1,430/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SIMP — scalping_continual_defensive — CONDITIONAL

**Score:** 0.709 vs policy min 0.05 · **Close:** 600 · **ATR14:** 50.7 · **Volume ratio 20D:** 1.65 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 580–615, entry trigger **615**, stop **585**, risk 30 points (4.88%).

**Targets:** TP1 **645** (1.00R), TP2 **670** (1.83R), TP3 **745** (4.33R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 600 and ATR14 50.7: buy zone 580–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 585 is placed below support structure (590 / 590). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 645 (1.00R), TP2 670 (1.83R), TP3 745 (4.33R). Targets are ATR/structure capped for hold_days=1. ATR14=50.7, resistance_5/10/20/60=770/865/930/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — scalping_continual_defensive — CONDITIONAL

**Score:** 0.681 vs policy min 0.05 · **Close:** 161 · **ATR14:** 19.6 · **Volume ratio 20D:** 0.60 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 154–165, entry trigger **165**, stop **153**, risk 12 points (7.27%).

**Targets:** TP1 **177** (1.00R), TP2 **186** (1.75R), TP3 **214** (4.08R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 161 and ATR14 19.6: buy zone 154–165. Entry is valid only if price can trade/hold around 165 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 153 is placed below support structure (154 / 125). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 177 (1.00R), TP2 186 (1.75R), TP3 214 (4.08R). Targets are ATR/structure capped for hold_days=1. ATR14=19.6, resistance_5/10/20/60=224/228/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.533 vs policy min 0.30 · **Close:** 750 · **ATR14:** 118.2 · **Volume ratio 20D:** 1.65 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 705–775, entry trigger **775**, stop **720**, risk 55 points (7.10%).

**Targets:** TP1 **835** (1.09R), TP2 **870** (1.73R), TP3 **1,290** (9.36R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 118.2: buy zone 705–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is placed below support structure (725 / 725). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.09R), TP2 870 (1.73R), TP3 1,290 (9.36R). Targets are ATR/structure capped for hold_days=3. ATR14=118.2, resistance_5/10/20/60=1,305/1,430/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — swing_continual_defensive — CONDITIONAL

**Score:** 0.533 vs policy min 0.30 · **Close:** 750 · **ATR14:** 118.2 · **Volume ratio 20D:** 1.65 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 705–775, entry trigger **775**, stop **720**, risk 55 points (7.10%).

**Targets:** TP1 **835** (1.09R), TP2 **870** (1.73R), TP3 **910** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 118.2: buy zone 705–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is placed below support structure (725 / 725). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.09R), TP2 870 (1.73R), TP3 910 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=118.2, resistance_5/10/20/60=1,305/1,430/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.525 vs policy min 0.30 · **Close:** 750 · **ATR14:** 118.2 · **Volume ratio 20D:** 1.65 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 705–775, entry trigger **775**, stop **720**, risk 55 points (7.10%).

**Targets:** TP1 **835** (1.09R), TP2 **1,255** (8.73R), TP3 **1,305** (9.64R). Recommended base-case RR: **8.73R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 118.2: buy zone 705–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is placed below support structure (725 / 725). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.09R), TP2 1,255 (8.73R), TP3 1,305 (9.64R). Targets are ATR/structure capped for hold_days=5. ATR14=118.2, resistance_5/10/20/60=1,305/1,430/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SIMP — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.508 vs policy min 0.30 · **Close:** 600 · **ATR14:** 50.7 · **Volume ratio 20D:** 1.65 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 580–615, entry trigger **615**, stop **585**, risk 30 points (4.88%).

**Targets:** TP1 **645** (1.00R), TP2 **770** (5.17R), TP3 **785** (5.67R). Recommended base-case RR: **5.17R**.

**Why entry:** Hybrid entry uses close 600 and ATR14 50.7: buy zone 580–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 585 is placed below support structure (590 / 590). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 645 (1.00R), TP2 770 (5.17R), TP3 785 (5.67R). Targets are ATR/structure capped for hold_days=5. ATR14=50.7, resistance_5/10/20/60=770/865/930/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TIRA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.480 vs policy min 0.30 · **Close:** 610 · **ATR14:** 66.1 · **Volume ratio 20D:** 1.70 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 585–625, entry trigger **625**, stop **575**, risk 50 points (8.00%).

**Targets:** TP1 **675** (1.00R), TP2 **710** (1.70R), TP3 **885** (5.20R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 66.1: buy zone 585–625. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is placed below support structure (580 / 580). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 675 (1.00R), TP2 710 (1.70R), TP3 885 (5.20R). Targets are ATR/structure capped for hold_days=3. ATR14=66.1, resistance_5/10/20/60=885/895/1,030/1,290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TIRA — swing_continual_defensive — CONDITIONAL

**Score:** 0.480 vs policy min 0.30 · **Close:** 610 · **ATR14:** 66.1 · **Volume ratio 20D:** 1.70 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 585–625, entry trigger **625**, stop **575**, risk 50 points (8.00%).

**Targets:** TP1 **675** (1.00R), TP2 **710** (1.70R), TP3 **745** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 66.1: buy zone 585–625. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is placed below support structure (580 / 580). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 675 (1.00R), TP2 710 (1.70R), TP3 745 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=66.1, resistance_5/10/20/60=885/895/1,030/1,290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.480 vs policy min 0.30 · **Close:** 418 · **ATR14:** 61.1 · **Volume ratio 20D:** 2.59 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 396–432, entry trigger **432**, stop **412**, risk 20 points (4.63%).

**Targets:** TP1 **464** (1.60R), TP2 **640** (10.40R), TP3 **650** (10.90R). Recommended base-case RR: **10.40R**.

**Why entry:** Hybrid entry uses close 418 and ATR14 61.1: buy zone 396–432. Entry is valid only if price can trade/hold around 432 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 412 is placed below support structure (414 / 414). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 464 (1.60R), TP2 640 (10.40R), TP3 650 (10.90R). Targets are ATR/structure capped for hold_days=5. ATR14=61.1, resistance_5/10/20/60=640/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## SIMP — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.434 vs policy min 0.30 · **Close:** 600 · **ATR14:** 50.7 · **Volume ratio 20D:** 1.65 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 580–615, entry trigger **615**, stop **585**, risk 30 points (4.88%).

**Targets:** TP1 **645** (1.00R), TP2 **770** (5.17R), TP3 **785** (5.67R). Recommended base-case RR: **5.17R**.

**Why entry:** Hybrid entry uses close 600 and ATR14 50.7: buy zone 580–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 585 is placed below support structure (590 / 590). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 645 (1.00R), TP2 770 (5.17R), TP3 785 (5.67R). Targets are ATR/structure capped for hold_days=3. ATR14=50.7, resistance_5/10/20/60=770/865/930/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SIMP — swing_continual_defensive — CONDITIONAL

**Score:** 0.434 vs policy min 0.30 · **Close:** 600 · **ATR14:** 50.7 · **Volume ratio 20D:** 1.65 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 580–615, entry trigger **615**, stop **585**, risk 30 points (4.88%).

**Targets:** TP1 **645** (1.00R), TP2 **670** (1.83R), TP3 **745** (4.33R). Recommended base-case RR: **1.83R**.

**Why entry:** Hybrid entry uses close 600 and ATR14 50.7: buy zone 580–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 585 is placed below support structure (590 / 590). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 645 (1.00R), TP2 670 (1.83R), TP3 745 (4.33R). Targets are ATR/structure capped for hold_days=1. ATR14=50.7, resistance_5/10/20/60=770/865/930/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BANK — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.421 vs policy min 0.30 · **Close:** 418 · **ATR14:** 61.1 · **Volume ratio 20D:** 2.59 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 396–432, entry trigger **432**, stop **412**, risk 20 points (4.63%).

**Targets:** TP1 **464** (1.60R), TP2 **625** (9.65R), TP3 **640** (10.40R). Recommended base-case RR: **9.65R**.

**Why entry:** Hybrid entry uses close 418 and ATR14 61.1: buy zone 396–432. Entry is valid only if price can trade/hold around 432 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 412 is placed below support structure (414 / 414). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 464 (1.60R), TP2 625 (9.65R), TP3 640 (10.40R). Targets are ATR/structure capped for hold_days=3. ATR14=61.1, resistance_5/10/20/60=640/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BANK — swing_continual_defensive — CONDITIONAL

**Score:** 0.421 vs policy min 0.30 · **Close:** 418 · **ATR14:** 61.1 · **Volume ratio 20D:** 2.59 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 396–432, entry trigger **432**, stop **412**, risk 20 points (4.63%).

**Targets:** TP1 **464** (1.60R), TP2 **466** (1.70R), TP3 **480** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 418 and ATR14 61.1: buy zone 396–432. Entry is valid only if price can trade/hold around 432 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 412 is placed below support structure (414 / 414). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 464 (1.60R), TP2 466 (1.70R), TP3 480 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=61.1, resistance_5/10/20/60=640/640/640/655. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## DSSA — position_continual — WATCHLIST_ONLY

**Score:** 0.290 vs policy min 0.30 · **Close:** 880 · **ATR14:** 247.5 · **Volume ratio 20D:** 1.86 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 790–930, entry trigger **930**, stop **875**, risk 55 points (5.91%).

**Targets:** TP1 **1,700** (14.00R), TP2 **1,730** (14.55R), TP3 **1,760** (15.09R). Recommended base-case RR: **14.55R**.

**Why entry:** Hybrid entry uses close 880 and ATR14 247.5: buy zone 790–930. Entry is valid only if price can trade/hold around 930 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 875 is placed below support structure (880 / 880). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,700 (14.00R), TP2 1,730 (14.55R), TP3 1,760 (15.09R). Targets are ATR/structure capped for hold_days=10. ATR14=247.5, resistance_5/10/20/60=1,700/2,340/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.290 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## PACK — position_continual — WATCHLIST_ONLY

**Score:** 0.286 vs policy min 0.30 · **Close:** 342 · **ATR14:** 30.9 · **Volume ratio 20D:** 0.34 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 330–350, entry trigger **350**, stop **322**, risk 28 points (8.00%).

**Targets:** TP1 **378** (1.00R), TP2 **398** (1.71R), TP3 **418** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 342 and ATR14 30.9: buy zone 330–350. Entry is valid only if price can trade/hold around 350 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 322 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 378 (1.00R), TP2 398 (1.71R), TP3 418 (2.43R). Targets are ATR/structure capped for hold_days=10. ATR14=30.9, resistance_5/10/20/60=342/342/342/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.286 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.34 below required 0.60

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — WATCHLIST_ONLY

**Score:** 0.286 vs policy min 0.30 · **Close:** 750 · **ATR14:** 118.2 · **Volume ratio 20D:** 1.65 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 705–775, entry trigger **775**, stop **720**, risk 55 points (7.10%).

**Targets:** TP1 **835** (1.09R), TP2 **1,305** (9.64R), TP3 **1,335** (10.18R). Recommended base-case RR: **9.64R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 118.2: buy zone 705–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is placed below support structure (725 / 725). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.09R), TP2 1,305 (9.64R), TP3 1,335 (10.18R). Targets are ATR/structure capped for hold_days=10. ATR14=118.2, resistance_5/10/20/60=1,305/1,430/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.286 below policy min_score 0.30; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## UNSP — position_continual — WATCHLIST_ONLY

**Score:** 0.282 vs policy min 0.30 · **Close:** 288 · **ATR14:** 24.7 · **Volume ratio 20D:** 2.31 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 278–294, entry trigger **294**, stop **286**, risk 8 points (2.72%).

**Targets:** TP1 **308** (1.75R), TP2 **392** (12.25R), TP3 **396** (12.75R). Recommended base-case RR: **12.25R**.

**Why entry:** Hybrid entry uses close 288 and ATR14 24.7: buy zone 278–294. Entry is valid only if price can trade/hold around 294 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 286 is placed below support structure (288 / 288). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 308 (1.75R), TP2 392 (12.25R), TP3 396 (12.75R). Targets are ATR/structure capped for hold_days=10. ATR14=24.7, resistance_5/10/20/60=392/426/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.282 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## PBSA — position_continual — WATCHLIST_ONLY

**Score:** 0.271 vs policy min 0.30 · **Close:** 845 · **ATR14:** 65.0 · **Volume ratio 20D:** 0.82 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 820–860, entry trigger **860**, stop **815**, risk 45 points (5.23%).

**Targets:** TP1 **905** (1.00R), TP2 **1,130** (6.00R), TP3 **1,155** (6.56R). Recommended base-case RR: **6.00R**.

**Why entry:** Hybrid entry uses close 845 and ATR14 65.0: buy zone 820–860. Entry is valid only if price can trade/hold around 860 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 815 is placed below support structure (820 / 820). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 905 (1.00R), TP2 1,130 (6.00R), TP3 1,155 (6.56R). Targets are ATR/structure capped for hold_days=10. ATR14=65.0, resistance_5/10/20/60=1,130/1,240/1,270/1,600. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** score 0.271 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## MBMA — scalping_continual_defensive — NO_TRADE

**Score:** 0.702 vs policy min 0.05 · **Close:** 540 · **ATR14:** 44.6 · **Volume ratio 20D:** 1.92 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 520–550, entry trigger **550**, stop **505**, risk 45 points (8.18%).

**Targets:** TP1 **595** (1.00R), TP2 **630** (1.78R), TP3 **665** (2.56R). Recommended base-case RR: **1.78R**.

**Why entry:** Hybrid entry uses close 540 and ATR14 44.6: buy zone 520–550. Entry is valid only if price can trade/hold around 550 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 505 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 595 (1.00R), TP2 630 (1.78R), TP3 665 (2.56R). Targets are ATR/structure capped for hold_days=1. ATR14=44.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## DSSA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.628 vs policy min 0.30 · **Close:** 880 · **ATR14:** 247.5 · **Volume ratio 20D:** 1.86 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 790–930, entry trigger **930**, stop **875**, risk 55 points (5.91%).

**Targets:** TP1 **1,700** (14.00R), TP2 **1,730** (14.55R), TP3 **1,760** (15.09R). Recommended base-case RR: **14.55R**.

**Why entry:** Hybrid entry uses close 880 and ATR14 247.5: buy zone 790–930. Entry is valid only if price can trade/hold around 930 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 875 is placed below support structure (880 / 880). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 1,700 (14.00R), TP2 1,730 (14.55R), TP3 1,760 (15.09R). Targets are ATR/structure capped for hold_days=10. ATR14=247.5, resistance_5/10/20/60=1,700/2,340/3,500/98,000. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.522 vs policy min 0.30 · **Close:** 540 · **ATR14:** 44.6 · **Volume ratio 20D:** 1.92 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 520–550, entry trigger **550**, stop **505**, risk 45 points (8.18%).

**Targets:** TP1 **650** (2.22R), TP2 **680** (2.89R), TP3 **705** (3.44R). Recommended base-case RR: **2.89R**.

**Why entry:** Hybrid entry uses close 540 and ATR14 44.6: buy zone 520–550. Entry is valid only if price can trade/hold around 550 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 505 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 650 (2.22R), TP2 680 (2.89R), TP3 705 (3.44R). Targets are ATR/structure capped for hold_days=5. ATR14=44.6, resistance_5/10/20/60=680/710/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.18% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## NSSS — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.478 vs policy min 0.30 · **Close:** 695 · **ATR14:** 78.2 · **Volume ratio 20D:** 0.41 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 665–715, entry trigger **715**, stop **655**, risk 60 points (8.39%).

**Targets:** TP1 **850** (2.25R), TP2 **880** (2.75R), TP3 **910** (3.25R). Recommended base-case RR: **2.75R**.

**Why entry:** Hybrid entry uses close 695 and ATR14 78.2: buy zone 665–715. Entry is valid only if price can trade/hold around 715 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 655 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 850 (2.25R), TP2 880 (2.75R), TP3 910 (3.25R). Targets are ATR/structure capped for hold_days=5. ATR14=78.2, resistance_5/10/20/60=850/1,060/1,060/1,300. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.39% exceeds max strategy risk 8.00%; volume ratio 0.41 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CYBR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.420 vs policy min 0.30 · **Close:** 635 · **ATR14:** 116.1 · **Volume ratio 20D:** 1.76 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 590–660, entry trigger **660**, stop **605**, risk 55 points (8.33%).

**Targets:** TP1 **720** (1.09R), TP2 **755** (1.73R), TP3 **795** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 635 and ATR14 116.1: buy zone 590–660. Entry is valid only if price can trade/hold around 660 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 605 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.09R), TP2 755 (1.73R), TP3 795 (2.45R). Targets are ATR/structure capped for hold_days=3. ATR14=116.1, resistance_5/10/20/60=1,330/1,330/1,590/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CYBR — swing_continual_defensive — NO_TRADE

**Score:** 0.420 vs policy min 0.30 · **Close:** 635 · **ATR14:** 116.1 · **Volume ratio 20D:** 1.76 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 590–660, entry trigger **660**, stop **605**, risk 55 points (8.33%).

**Targets:** TP1 **720** (1.09R), TP2 **755** (1.73R), TP3 **795** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 635 and ATR14 116.1: buy zone 590–660. Entry is valid only if price can trade/hold around 660 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 605 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.09R), TP2 755 (1.73R), TP3 795 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=116.1, resistance_5/10/20/60=1,330/1,330/1,590/1,695. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.33% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.412 vs policy min 0.30 · **Close:** 630 · **ATR14:** 84.3 · **Volume ratio 20D:** 0.39 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 600–650, entry trigger **650**, stop **595**, risk 55 points (8.46%).

**Targets:** TP1 **800** (2.73R), TP2 **835** (3.36R), TP3 **865** (3.91R). Recommended base-case RR: **3.36R**.

**Why entry:** Hybrid entry uses close 630 and ATR14 84.3: buy zone 600–650. Entry is valid only if price can trade/hold around 650 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 595 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 800 (2.73R), TP2 835 (3.36R), TP3 865 (3.91R). Targets are ATR/structure capped for hold_days=3. ATR14=84.3, resistance_5/10/20/60=835/900/1,450/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%; volume ratio 0.39 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — swing_continual_defensive — NO_TRADE

**Score:** 0.412 vs policy min 0.30 · **Close:** 630 · **ATR14:** 84.3 · **Volume ratio 20D:** 0.39 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 600–650, entry trigger **650**, stop **595**, risk 55 points (8.46%).

**Targets:** TP1 **705** (1.00R), TP2 **805** (2.82R), TP3 **835** (3.36R). Recommended base-case RR: **2.82R**.

**Why entry:** Hybrid entry uses close 630 and ATR14 84.3: buy zone 600–650. Entry is valid only if price can trade/hold around 650 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 595 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 705 (1.00R), TP2 805 (2.82R), TP3 835 (3.36R). Targets are ATR/structure capped for hold_days=1. ATR14=84.3, resistance_5/10/20/60=835/900/1,450/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.46% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R; volume ratio 0.39 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.366 vs policy min 0.30 · **Close:** 750 · **ATR14:** 118.2 · **Volume ratio 20D:** 1.65 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 705–775, entry trigger **775**, stop **720**, risk 55 points (7.10%).

**Targets:** TP1 **835** (1.09R), TP2 **1,305** (9.64R), TP3 **1,335** (10.18R). Recommended base-case RR: **9.64R**.

**Why entry:** Hybrid entry uses close 750 and ATR14 118.2: buy zone 705–775. Entry is valid only if price can trade/hold around 775 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 720 is placed below support structure (725 / 725). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 835 (1.09R), TP2 1,305 (9.64R), TP3 1,335 (10.18R). Targets are ATR/structure capped for hold_days=10. ATR14=118.2, resistance_5/10/20/60=1,305/1,430/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## UNSP — momentum_20d_continual_research — NO_TRADE

**Score:** 0.339 vs policy min 0.30 · **Close:** 288 · **ATR14:** 24.7 · **Volume ratio 20D:** 2.31 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 278–294, entry trigger **294**, stop **286**, risk 8 points (2.72%).

**Targets:** TP1 **308** (1.75R), TP2 **392** (12.25R), TP3 **396** (12.75R). Recommended base-case RR: **12.25R**.

**Why entry:** Hybrid entry uses close 288 and ATR14 24.7: buy zone 278–294. Entry is valid only if price can trade/hold around 294 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 286 is placed below support structure (288 / 288). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 308 (1.75R), TP2 392 (12.25R), TP3 396 (12.75R). Targets are ATR/structure capped for hold_days=10. ATR14=24.7, resistance_5/10/20/60=392/426/450/450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BKDP — position_continual — NO_TRADE

**Score:** 0.323 vs policy min 0.30 · **Close:** 112 · **ATR14:** 9.9 · **Volume ratio 20D:** 4.97 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 108–114, entry trigger **114**, stop **104**, risk 10 points (8.77%).

**Targets:** TP1 **124** (1.00R), TP2 **131** (1.70R), TP3 **138** (2.40R). Recommended base-case RR: **1.70R**.

**Why entry:** Hybrid entry uses close 112 and ATR14 9.9: buy zone 108–114. Entry is valid only if price can trade/hold around 114 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 104 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 124 (1.00R), TP2 131 (1.70R), TP3 138 (2.40R). Targets are ATR/structure capped for hold_days=10. ATR14=9.9, resistance_5/10/20/60=112/112/112/112. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.77% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GPSO — position_continual — NO_TRADE

**Score:** 0.309 vs policy min 0.30 · **Close:** 482 · **ATR14:** 32.3 · **Volume ratio 20D:** 1.09 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 470–490, entry trigger **490**, stop **450**, risk 40 points (8.16%).

**Targets:** TP1 **535** (1.12R), TP2 **560** (1.75R), TP3 **590** (2.50R). Recommended base-case RR: **1.75R**.

**Why entry:** Hybrid entry uses close 482 and ATR14 32.3: buy zone 470–490. Entry is valid only if price can trade/hold around 490 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 450 uses 1.20×ATR14 volatility cap. Thesis invalidates if the move reverses beyond normal volatility. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 535 (1.12R), TP2 560 (1.75R), TP3 590 (2.50R). Targets are ATR/structure capped for hold_days=10. ATR14=32.3, resistance_5/10/20/60=486/486/486/535. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.16% exceeds max strategy risk 8.00%; TP1 reward/risk 1.12R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## SIMP — momentum_20d_continual_research — NO_TRADE

**Score:** 0.305 vs policy min 0.30 · **Close:** 600 · **ATR14:** 50.7 · **Volume ratio 20D:** 1.65 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 580–615, entry trigger **615**, stop **585**, risk 30 points (4.88%).

**Targets:** TP1 **770** (5.17R), TP2 **785** (5.67R), TP3 **800** (6.17R). Recommended base-case RR: **5.67R**.

**Why entry:** Hybrid entry uses close 600 and ATR14 50.7: buy zone 580–615. Entry is valid only if price can trade/hold around 615 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 585 is placed below support structure (590 / 590). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 770 (5.17R), TP2 785 (5.67R), TP3 800 (6.17R). Targets are ATR/structure capped for hold_days=10. ATR14=50.7, resistance_5/10/20/60=770/865/930/930. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TIRA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.289 vs policy min 0.30 · **Close:** 610 · **ATR14:** 66.1 · **Volume ratio 20D:** 1.70 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 585–625, entry trigger **625**, stop **575**, risk 50 points (8.00%).

**Targets:** TP1 **675** (1.00R), TP2 **885** (5.20R), TP3 **910** (5.70R). Recommended base-case RR: **5.20R**.

**Why entry:** Hybrid entry uses close 610 and ATR14 66.1: buy zone 585–625. Entry is valid only if price can trade/hold around 625 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 575 is placed below support structure (580 / 580). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 675 (1.00R), TP2 885 (5.20R), TP3 910 (5.70R). Targets are ATR/structure capped for hold_days=10. ATR14=66.1, resistance_5/10/20/60=885/895/1,030/1,290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; score 0.289 below policy min_score 0.30; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BULL — position_continual — NO_TRADE

**Score:** 0.276 vs policy min 0.30 · **Close:** 438 · **ATR14:** 47.6 · **Volume ratio 20D:** 0.89 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 420–448, entry trigger **448**, stop **412**, risk 36 points (8.04%).

**Targets:** TP1 **545** (2.69R), TP2 **565** (3.25R), TP3 **585** (3.81R). Recommended base-case RR: **3.25R**.

**Why entry:** Hybrid entry uses close 438 and ATR14 47.6: buy zone 420–448. Entry is valid only if price can trade/hold around 448 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 412 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (2.69R), TP2 565 (3.25R), TP3 585 (3.81R). Targets are ATR/structure capped for hold_days=10. ATR14=47.6, resistance_5/10/20/60=545/570/610/610. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.04% exceeds max strategy risk 8.00%; score 0.276 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## BEEF — position_continual — NO_TRADE

**Score:** 0.276 vs policy min 0.30 · **Close:** 168 · **ATR14:** 22.7 · **Volume ratio 20D:** 4.49 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 160–173, entry trigger **173**, stop **159**, risk 14 points (8.09%).

**Targets:** TP1 **210** (2.64R), TP2 **218** (3.21R), TP3 **226** (3.79R). Recommended base-case RR: **3.21R**.

**Why entry:** Hybrid entry uses close 168 and ATR14 22.7: buy zone 160–173. Entry is valid only if price can trade/hold around 173 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 159 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 210 (2.64R), TP2 218 (3.21R), TP3 226 (3.79R). Targets are ATR/structure capped for hold_days=10. ATR14=22.7, resistance_5/10/20/60=210/266/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.09% exceeds max strategy risk 8.00%; score 0.276 below policy min_score 0.30; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---

## TRIN — position_continual — NO_TRADE

**Score:** 0.272 vs policy min 0.30 · **Close:** 570 · **ATR14:** 56.4 · **Volume ratio 20D:** 0.96 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 550–585, entry trigger **585**, stop **535**, risk 50 points (8.55%).

**Targets:** TP1 **715** (2.60R), TP2 **740** (3.10R), TP3 **765** (3.60R). Recommended base-case RR: **3.10R**.

**Why entry:** Hybrid entry uses close 570 and ATR14 56.4: buy zone 550–585. Entry is valid only if price can trade/hold around 585 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 535 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 715 (2.60R), TP2 740 (3.10R), TP3 765 (3.60R). Targets are ATR/structure capped for hold_days=10. ATR14=56.4, resistance_5/10/20/60=715/860/905/1,225. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.55% exceeds max strategy risk 8.00%; score 0.272 below policy min_score 0.30

**Risk flags:** BELOW_EXECUTION_THRESHOLD

**Strategy risk note:** Generic strategy rule.

---
