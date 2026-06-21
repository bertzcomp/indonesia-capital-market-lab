# Numeric Trading Desk Report — 2026-05-13

This report is generated from live model scores, selected signal policy, canonical OHLCV, ATR, support/resistance, liquidity, and broker-flow diagnostics. It is not a simple BUY/SELL list; each plan is conditional on execution behaviour.

## Summary

| Plan quality | Count |
|---|---:|
| ACTIONABLE | 3 |
| CONDITIONAL | 20 |
| NO_TRADE | 19 |

## BEEF — momentum_10d_continual_aggressive — ACTIONABLE

**Score:** 0.524 vs policy min 0.30 · **Close:** 157 · **ATR14:** 22.2 · **Volume ratio 20D:** 6.28 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 149–162, entry trigger **162**, stop **150**, risk 12 points (7.41%).

**Targets:** TP1 **212** (4.17R), TP2 **218** (4.67R), TP3 **224** (5.17R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 22.2: buy zone 149–162. Entry is valid only if price can trade/hold around 162 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (4.17R), TP2 218 (4.67R), TP3 224 (5.17R). Targets are ATR/structure capped for hold_days=5. ATR14=22.2, resistance_5/10/20/60=212/302/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BEEF — position_continual — ACTIONABLE

**Score:** 0.379 vs policy min 0.30 · **Close:** 157 · **ATR14:** 22.2 · **Volume ratio 20D:** 6.28 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 149–162, entry trigger **162**, stop **150**, risk 12 points (7.41%).

**Targets:** TP1 **212** (4.17R), TP2 **218** (4.67R), TP3 **224** (5.17R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 22.2: buy zone 149–162. Entry is valid only if price can trade/hold around 162 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (4.17R), TP2 218 (4.67R), TP3 224 (5.17R). Targets are ATR/structure capped for hold_days=10. ATR14=22.2, resistance_5/10/20/60=212/302/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSJA — position_continual — ACTIONABLE

**Score:** 0.322 vs policy min 0.30 · **Close:** 418 · **ATR14:** 40.2 · **Volume ratio 20D:** 1.12 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 402–428, entry trigger **428**, stop **398**, risk 30 points (7.01%).

**Targets:** TP1 **555** (4.23R), TP2 **570** (4.73R), TP3 **585** (5.23R). Recommended base-case RR: **4.73R**.

**Why entry:** Hybrid entry uses close 418 and ATR14 40.2: buy zone 402–428. Entry is valid only if price can trade/hold around 428 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 398 is placed below support structure (400 / 400). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 555 (4.23R), TP2 570 (4.73R), TP3 585 (5.23R). Targets are ATR/structure capped for hold_days=10. ATR14=40.2, resistance_5/10/20/60=555/555/560/560. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** No hard no-trade condition from score, entry distance, risk, or RR filters. Still require intraday confirmation.

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSJA — ara_candidate_continual — CONDITIONAL

**Score:** 0.922 vs policy min 0.50 · **Close:** 418 · **ATR14:** 40.2 · **Volume ratio 20D:** 1.12 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 402–428, entry trigger **428**, stop **398**, risk 30 points (7.01%).

**Targets:** TP1 **458** (1.00R), TP2 **480** (1.73R), TP3 **500** (2.40R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 418 and ATR14 40.2: buy zone 402–428. Entry is valid only if price can trade/hold around 428 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 398 is placed below support structure (400 / 400). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 458 (1.00R), TP2 480 (1.73R), TP3 500 (2.40R). Targets are ATR/structure capped for hold_days=1. ATR14=40.2, resistance_5/10/20/60=555/555/560/560. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — scalping_continual_defensive — CONDITIONAL

**Score:** 0.776 vs policy min 0.05 · **Close:** 850 · **ATR14:** 115.0 · **Volume ratio 20D:** 1.34 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 805–875, entry trigger **875**, stop **820**, risk 55 points (6.29%).

**Targets:** TP1 **935** (1.09R), TP2 **970** (1.73R), TP3 **1,010** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 850 and ATR14 115.0: buy zone 805–875. Entry is valid only if price can trade/hold around 875 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is placed below support structure (825 / 825). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (1.09R), TP2 970 (1.73R), TP3 1,010 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=115.0, resistance_5/10/20/60=1,305/1,515/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.729 vs policy min 0.30 · **Close:** 850 · **ATR14:** 115.0 · **Volume ratio 20D:** 1.34 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 805–875, entry trigger **875**, stop **820**, risk 55 points (6.29%).

**Targets:** TP1 **935** (1.09R), TP2 **970** (1.73R), TP3 **1,305** (7.82R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 850 and ATR14 115.0: buy zone 805–875. Entry is valid only if price can trade/hold around 875 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is placed below support structure (825 / 825). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (1.09R), TP2 970 (1.73R), TP3 1,305 (7.82R). Targets are ATR/structure capped for hold_days=3. ATR14=115.0, resistance_5/10/20/60=1,305/1,515/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — swing_continual_defensive — CONDITIONAL

**Score:** 0.729 vs policy min 0.30 · **Close:** 850 · **ATR14:** 115.0 · **Volume ratio 20D:** 1.34 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 805–875, entry trigger **875**, stop **820**, risk 55 points (6.29%).

**Targets:** TP1 **935** (1.09R), TP2 **970** (1.73R), TP3 **1,010** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 850 and ATR14 115.0: buy zone 805–875. Entry is valid only if price can trade/hold around 875 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is placed below support structure (825 / 825). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (1.09R), TP2 970 (1.73R), TP3 1,010 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=115.0, resistance_5/10/20/60=1,305/1,515/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TIRA — scalping_continual_defensive — CONDITIONAL

**Score:** 0.720 vs policy min 0.05 · **Close:** 640 · **ATR14:** 56.1 · **Volume ratio 20D:** 1.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 620–655, entry trigger **655**, stop **620**, risk 35 points (5.34%).

**Targets:** TP1 **690** (1.00R), TP2 **715** (1.71R), TP3 **740** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 56.1: buy zone 620–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.00R), TP2 715 (1.71R), TP3 740 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=56.1, resistance_5/10/20/60=895/895/1,030/1,290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BEEF — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.681 vs policy min 0.30 · **Close:** 157 · **ATR14:** 22.2 · **Volume ratio 20D:** 6.28 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 149–162, entry trigger **162**, stop **150**, risk 12 points (7.41%).

**Targets:** TP1 **174** (1.00R), TP2 **212** (4.17R), TP3 **218** (4.67R). Recommended base-case RR: **4.17R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 22.2: buy zone 149–162. Entry is valid only if price can trade/hold around 162 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 174 (1.00R), TP2 212 (4.17R), TP3 218 (4.67R). Targets are ATR/structure capped for hold_days=3. ATR14=22.2, resistance_5/10/20/60=212/302/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BEEF — swing_continual_defensive — CONDITIONAL

**Score:** 0.681 vs policy min 0.30 · **Close:** 157 · **ATR14:** 22.2 · **Volume ratio 20D:** 6.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 149–162, entry trigger **162**, stop **150**, risk 12 points (7.41%).

**Targets:** TP1 **174** (1.00R), TP2 **202** (3.33R), TP3 **212** (4.17R). Recommended base-case RR: **3.33R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 22.2: buy zone 149–162. Entry is valid only if price can trade/hold around 162 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 174 (1.00R), TP2 202 (3.33R), TP3 212 (4.17R). Targets are ATR/structure capped for hold_days=1. ATR14=22.2, resistance_5/10/20/60=212/302/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TIRA — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.648 vs policy min 0.30 · **Close:** 640 · **ATR14:** 56.1 · **Volume ratio 20D:** 1.89 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 620–655, entry trigger **655**, stop **620**, risk 35 points (5.34%).

**Targets:** TP1 **690** (1.00R), TP2 **715** (1.71R), TP3 **895** (6.86R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 56.1: buy zone 620–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.00R), TP2 715 (1.71R), TP3 895 (6.86R). Targets are ATR/structure capped for hold_days=3. ATR14=56.1, resistance_5/10/20/60=895/895/1,030/1,290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TIRA — swing_continual_defensive — CONDITIONAL

**Score:** 0.648 vs policy min 0.30 · **Close:** 640 · **ATR14:** 56.1 · **Volume ratio 20D:** 1.89 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 620–655, entry trigger **655**, stop **620**, risk 35 points (5.34%).

**Targets:** TP1 **690** (1.00R), TP2 **715** (1.71R), TP3 **740** (2.43R). Recommended base-case RR: **1.71R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 56.1: buy zone 620–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.00R), TP2 715 (1.71R), TP3 740 (2.43R). Targets are ATR/structure capped for hold_days=1. ATR14=56.1, resistance_5/10/20/60=895/895/1,030/1,290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## GZCO — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.609 vs policy min 0.30 · **Close:** 185 · **ATR14:** 17.4 · **Volume ratio 20D:** 0.28 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 178–189, entry trigger **189**, stop **184**, risk 5 points (2.65%).

**Targets:** TP1 **198** (1.80R), TP2 **232** (8.60R), TP3 **236** (9.40R). Recommended base-case RR: **8.60R**.

**Why entry:** Hybrid entry uses close 185 and ATR14 17.4: buy zone 178–189. Entry is valid only if price can trade/hold around 189 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 184 is placed below support structure (185 / 185). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 198 (1.80R), TP2 232 (8.60R), TP3 236 (9.40R). Targets are ATR/structure capped for hold_days=3. ATR14=17.4, resistance_5/10/20/60=232/252/252/258. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.28 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## GZCO — swing_continual_defensive — CONDITIONAL

**Score:** 0.609 vs policy min 0.30 · **Close:** 185 · **ATR14:** 17.4 · **Volume ratio 20D:** 0.28 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 178–189, entry trigger **189**, stop **184**, risk 5 points (2.65%).

**Targets:** TP1 **198** (1.80R), TP2 **202** (2.60R), TP3 **232** (8.60R). Recommended base-case RR: **2.60R**.

**Why entry:** Hybrid entry uses close 185 and ATR14 17.4: buy zone 178–189. Entry is valid only if price can trade/hold around 189 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 184 is placed below support structure (185 / 185). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 198 (1.80R), TP2 202 (2.60R), TP3 232 (8.60R). Targets are ATR/structure capped for hold_days=1. ATR14=17.4, resistance_5/10/20/60=232/252/252/258. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.28 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.596 vs policy min 0.30 · **Close:** 850 · **ATR14:** 115.0 · **Volume ratio 20D:** 1.34 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 805–875, entry trigger **875**, stop **820**, risk 55 points (6.29%).

**Targets:** TP1 **935** (1.09R), TP2 **1,305** (7.82R), TP3 **1,335** (8.36R). Recommended base-case RR: **7.82R**.

**Why entry:** Hybrid entry uses close 850 and ATR14 115.0: buy zone 805–875. Entry is valid only if price can trade/hold around 875 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is placed below support structure (825 / 825). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (1.09R), TP2 1,305 (7.82R), TP3 1,335 (8.36R). Targets are ATR/structure capped for hold_days=5. ATR14=115.0, resistance_5/10/20/60=1,305/1,515/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRUE — momentum_5d_continual_defensive — CONDITIONAL

**Score:** 0.574 vs policy min 0.30 · **Close:** 137 · **ATR14:** 14.2 · **Volume ratio 20D:** 0.32 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 132–140, entry trigger **140**, stop **135**, risk 5 points (3.57%).

**Targets:** TP1 **148** (1.60R), TP2 **173** (6.60R), TP3 **176** (7.20R). Recommended base-case RR: **6.60R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 14.2: buy zone 132–140. Entry is valid only if price can trade/hold around 140 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 135 is placed below support structure (136 / 136). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 148 (1.60R), TP2 173 (6.60R), TP3 176 (7.20R). Targets are ATR/structure capped for hold_days=3. ATR14=14.2, resistance_5/10/20/60=173/184/220/336. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.32 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## TRUE — swing_continual_defensive — CONDITIONAL

**Score:** 0.574 vs policy min 0.30 · **Close:** 137 · **ATR14:** 14.2 · **Volume ratio 20D:** 0.32 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 132–140, entry trigger **140**, stop **135**, risk 5 points (3.57%).

**Targets:** TP1 **148** (1.60R), TP2 **166** (5.20R), TP3 **173** (6.60R). Recommended base-case RR: **5.20R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 14.2: buy zone 132–140. Entry is valid only if price can trade/hold around 140 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 135 is placed below support structure (136 / 136). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 148 (1.60R), TP2 166 (5.20R), TP3 173 (6.60R). Targets are ATR/structure capped for hold_days=1. ATR14=14.2, resistance_5/10/20/60=173/184/220/336. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.32 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MBMA — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.496 vs policy min 0.30 · **Close:** 585 · **ATR14:** 41.1 · **Volume ratio 20D:** 0.57 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 570–595, entry trigger **595**, stop **580**, risk 15 points (2.52%).

**Targets:** TP1 **690** (6.33R), TP2 **700** (7.00R), TP3 **710** (7.67R). Recommended base-case RR: **7.00R**.

**Why entry:** Hybrid entry uses close 585 and ATR14 41.1: buy zone 570–595. Entry is valid only if price can trade/hold around 595 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 580 is placed below support structure (585 / 585). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (6.33R), TP2 700 (7.00R), TP3 710 (7.67R). Targets are ATR/structure capped for hold_days=5. ATR14=41.1, resistance_5/10/20/60=690/715/775/945. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.57 below required 0.60

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRUE — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.490 vs policy min 0.30 · **Close:** 137 · **ATR14:** 14.2 · **Volume ratio 20D:** 0.32 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 132–140, entry trigger **140**, stop **135**, risk 5 points (3.57%).

**Targets:** TP1 **172** (6.40R), TP2 **173** (6.60R), TP3 **176** (7.20R). Recommended base-case RR: **6.60R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 14.2: buy zone 132–140. Entry is valid only if price can trade/hold around 140 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 135 is placed below support structure (136 / 136). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 172 (6.40R), TP2 173 (6.60R), TP3 176 (7.20R). Targets are ATR/structure capped for hold_days=5. ATR14=14.2, resistance_5/10/20/60=173/184/220/336. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.32 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## BELL — momentum_10d_continual_aggressive — CONDITIONAL

**Score:** 0.489 vs policy min 0.30 · **Close:** 129 · **ATR14:** 14.4 · **Volume ratio 20D:** 0.18 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 123–132, entry trigger **132**, stop **124**, risk 8 points (6.06%).

**Targets:** TP1 **161** (3.62R), TP2 **165** (4.12R), TP3 **169** (4.62R). Recommended base-case RR: **4.12R**.

**Why entry:** Hybrid entry uses close 129 and ATR14 14.4: buy zone 123–132. Entry is valid only if price can trade/hold around 132 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 124 is placed below support structure (125 / 125). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 161 (3.62R), TP2 165 (4.12R), TP3 169 (4.62R). Targets are ATR/structure capped for hold_days=5. ATR14=14.4, resistance_5/10/20/60=161/175/194/270. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.18 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CUAN — position_continual — CONDITIONAL

**Score:** 0.390 vs policy min 0.30 · **Close:** 850 · **ATR14:** 115.0 · **Volume ratio 20D:** 1.34 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 805–875, entry trigger **875**, stop **820**, risk 55 points (6.29%).

**Targets:** TP1 **935** (1.09R), TP2 **1,305** (7.82R), TP3 **1,335** (8.36R). Recommended base-case RR: **7.82R**.

**Why entry:** Hybrid entry uses close 850 and ATR14 115.0: buy zone 805–875. Entry is valid only if price can trade/hold around 875 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is placed below support structure (825 / 825). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (1.09R), TP2 1,305 (7.82R), TP3 1,335 (8.36R). Targets are ATR/structure capped for hold_days=10. ATR14=115.0, resistance_5/10/20/60=1,305/1,515/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## TRUE — position_continual — CONDITIONAL

**Score:** 0.334 vs policy min 0.30 · **Close:** 137 · **ATR14:** 14.2 · **Volume ratio 20D:** 0.32 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 132–140, entry trigger **140**, stop **135**, risk 5 points (3.57%).

**Targets:** TP1 **173** (6.60R), TP2 **176** (7.20R), TP3 **179** (7.80R). Recommended base-case RR: **7.20R**.

**Why entry:** Hybrid entry uses close 137 and ATR14 14.2: buy zone 132–140. Entry is valid only if price can trade/hold around 140 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 135 is placed below support structure (136 / 136). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 173 (6.60R), TP2 176 (7.20R), TP3 179 (7.80R). Targets are ATR/structure capped for hold_days=10. ATR14=14.2, resistance_5/10/20/60=173/184/220/336. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** volume ratio 0.32 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## KOKA — position_continual — CONDITIONAL

**Score:** 0.328 vs policy min 0.30 · **Close:** 148 · **ATR14:** 12.7 · **Volume ratio 20D:** 1.05 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 143–151, entry trigger **151**, stop **143**, risk 8 points (5.30%).

**Targets:** TP1 **185** (4.25R), TP2 **189** (4.75R), TP3 **193** (5.25R). Recommended base-case RR: **4.75R**.

**Why entry:** Hybrid entry uses close 148 and ATR14 12.7: buy zone 143–151. Entry is valid only if price can trade/hold around 151 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 143 is placed below support structure (144 / 144). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 185 (4.25R), TP2 189 (4.75R), TP3 193 (5.25R). Targets are ATR/structure capped for hold_days=10. ATR14=12.7, resistance_5/10/20/60=185/191/226/318. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MSIN — scalping_continual_defensive — NO_TRADE

**Score:** 0.745 vs policy min 0.05 · **Close:** 645 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.16 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 610–665, entry trigger **665**, stop **610**, risk 55 points (8.27%).

**Targets:** TP1 **720** (1.00R), TP2 **760** (1.73R), TP3 **885** (4.00R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 645 and ATR14 86.1: buy zone 610–665. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 610 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.00R), TP2 760 (1.73R), TP3 885 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=86.1, resistance_5/10/20/60=900/935/1,450/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MDIA — scalping_continual_defensive — NO_TRADE

**Score:** 0.720 vs policy min 0.05 · **Close:** 114 · **ATR14:** 33.9 · **Volume ratio 20D:** 0.25 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 102–121, entry trigger **121**, stop **111**, risk 10 points (8.26%).

**Targets:** TP1 **145** (2.40R), TP2 **150** (2.90R), TP3 **155** (3.40R). Recommended base-case RR: **2.90R**.

**Why entry:** Hybrid entry uses close 114 and ATR14 33.9: buy zone 102–121. Entry is valid only if price can trade/hold around 121 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 111 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 145 (2.40R), TP2 150 (2.90R), TP3 155 (3.40R). Targets are ATR/structure capped for hold_days=1. ATR14=33.9, resistance_5/10/20/60=145/162/162/162. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; volume ratio 0.25 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## CYBR — scalping_continual_defensive — NO_TRADE

**Score:** 0.720 vs policy min 0.05 · **Close:** 650 · **ATR14:** 115.7 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **735** (1.09R), TP2 **770** (1.73R), TP3 **810** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 115.7: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.09R), TP2 770 (1.73R), TP3 810 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=115.7, resistance_5/10/20/60=1,330/1,330/1,590/1,710. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.675 vs policy min 0.30 · **Close:** 645 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.16 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 610–665, entry trigger **665**, stop **610**, risk 55 points (8.27%).

**Targets:** TP1 **720** (1.00R), TP2 **900** (4.27R), TP3 **930** (4.82R). Recommended base-case RR: **4.27R**.

**Why entry:** Hybrid entry uses close 645 and ATR14 86.1: buy zone 610–665. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 610 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.00R), TP2 900 (4.27R), TP3 930 (4.82R). Targets are ATR/structure capped for hold_days=3. ATR14=86.1, resistance_5/10/20/60=900/935/1,450/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — swing_continual_defensive — NO_TRADE

**Score:** 0.675 vs policy min 0.30 · **Close:** 645 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.16 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 610–665, entry trigger **665**, stop **610**, risk 55 points (8.27%).

**Targets:** TP1 **720** (1.00R), TP2 **760** (1.73R), TP3 **885** (4.00R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 645 and ATR14 86.1: buy zone 610–665. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 610 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 720 (1.00R), TP2 760 (1.73R), TP3 885 (4.00R). Targets are ATR/structure capped for hold_days=1. ATR14=86.1, resistance_5/10/20/60=900/935/1,450/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CYBR — momentum_5d_continual_defensive — NO_TRADE

**Score:** 0.627 vs policy min 0.30 · **Close:** 650 · **ATR14:** 115.7 · **Volume ratio 20D:** 0.75 · **Hold:** 3 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **735** (1.09R), TP2 **770** (1.73R), TP3 **810** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 115.7: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.09R), TP2 770 (1.73R), TP3 810 (2.45R). Targets are ATR/structure capped for hold_days=3. ATR14=115.7, resistance_5/10/20/60=1,330/1,330/1,590/1,710. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CYBR — swing_continual_defensive — NO_TRADE

**Score:** 0.627 vs policy min 0.30 · **Close:** 650 · **ATR14:** 115.7 · **Volume ratio 20D:** 0.75 · **Hold:** 1 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **735** (1.09R), TP2 **770** (1.73R), TP3 **810** (2.45R). Recommended base-case RR: **1.73R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 115.7: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.09R), TP2 770 (1.73R), TP3 810 (2.45R). Targets are ATR/structure capped for hold_days=1. ATR14=115.7, resistance_5/10/20/60=1,330/1,330/1,590/1,710. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CUAN — momentum_20d_continual_research — NO_TRADE

**Score:** 0.563 vs policy min 0.30 · **Close:** 850 · **ATR14:** 115.0 · **Volume ratio 20D:** 1.34 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 805–875, entry trigger **875**, stop **820**, risk 55 points (6.29%).

**Targets:** TP1 **935** (1.09R), TP2 **1,305** (7.82R), TP3 **1,335** (8.36R). Recommended base-case RR: **7.82R**.

**Why entry:** Hybrid entry uses close 850 and ATR14 115.0: buy zone 805–875. Entry is valid only if price can trade/hold around 875 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 820 is placed below support structure (825 / 825). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 935 (1.09R), TP2 1,305 (7.82R), TP3 1,335 (8.36R). Targets are ATR/structure capped for hold_days=10. ATR14=115.0, resistance_5/10/20/60=1,305/1,515/1,620/1,990. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.524 vs policy min 0.30 · **Close:** 645 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.16 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 610–665, entry trigger **665**, stop **610**, risk 55 points (8.27%).

**Targets:** TP1 **860** (3.55R), TP2 **900** (4.27R), TP3 **930** (4.82R). Recommended base-case RR: **4.27R**.

**Why entry:** Hybrid entry uses close 645 and ATR14 86.1: buy zone 610–665. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 610 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 860 (3.55R), TP2 900 (4.27R), TP3 930 (4.82R). Targets are ATR/structure capped for hold_days=5. ATR14=86.1, resistance_5/10/20/60=900/935/1,450/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BIPI — momentum_10d_continual_aggressive — NO_TRADE

**Score:** 0.496 vs policy min 0.30 · **Close:** 220 · **ATR14:** 22.6 · **Volume ratio 20D:** 1.46 · **Hold:** 5 day(s)

**Execution numbers:** Buy zone 212–226, entry trigger **226**, stop **206**, risk 20 points (8.85%).

**Targets:** TP1 **262** (1.80R), TP2 **272** (2.30R), TP3 **274** (2.40R). Recommended base-case RR: **2.30R**.

**Why entry:** Hybrid entry uses close 220 and ATR14 22.6: buy zone 212–226. Entry is valid only if price can trade/hold around 226 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 206 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 262 (1.80R), TP2 272 (2.30R), TP3 274 (2.40R). Targets are ATR/structure capped for hold_days=5. ATR14=22.6, resistance_5/10/20/60=262/302/304/342. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.85% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## TIRA — momentum_20d_continual_research — NO_TRADE

**Score:** 0.452 vs policy min 0.30 · **Close:** 640 · **ATR14:** 56.1 · **Volume ratio 20D:** 1.89 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 620–655, entry trigger **655**, stop **620**, risk 35 points (5.34%).

**Targets:** TP1 **690** (1.00R), TP2 **895** (6.86R), TP3 **915** (7.43R). Recommended base-case RR: **6.86R**.

**Why entry:** Hybrid entry uses close 640 and ATR14 56.1: buy zone 620–655. Entry is valid only if price can trade/hold around 655 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is placed below support structure (625 / 625). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 690 (1.00R), TP2 895 (6.86R), TP3 915 (7.43R). Targets are ATR/structure capped for hold_days=10. ATR14=56.1, resistance_5/10/20/60=895/895/1,030/1,290. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; TP1 reward/risk 1.00R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CYBR — momentum_20d_continual_research — NO_TRADE

**Score:** 0.440 vs policy min 0.30 · **Close:** 650 · **ATR14:** 115.7 · **Volume ratio 20D:** 0.75 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **735** (1.09R), TP2 **1,330** (11.91R), TP3 **1,360** (12.45R). Recommended base-case RR: **11.91R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 115.7: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.09R), TP2 1,330 (11.91R), TP3 1,360 (12.45R). Targets are ATR/structure capped for hold_days=10. ATR14=115.7, resistance_5/10/20/60=1,330/1,330/1,590/1,710. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BEEF — momentum_20d_continual_research — NO_TRADE

**Score:** 0.396 vs policy min 0.30 · **Close:** 157 · **ATR14:** 22.2 · **Volume ratio 20D:** 6.28 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 149–162, entry trigger **162**, stop **150**, risk 12 points (7.41%).

**Targets:** TP1 **212** (4.17R), TP2 **218** (4.67R), TP3 **224** (5.17R). Recommended base-case RR: **4.67R**.

**Why entry:** Hybrid entry uses close 157 and ATR14 22.2: buy zone 149–162. Entry is valid only if price can trade/hold around 162 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 150 is placed below support structure (151 / 151). A breakdown below this area invalidates the thesis because support/retest behaviour fails. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 212 (4.17R), TP2 218 (4.67R), TP3 224 (5.17R). Targets are ATR/structure capped for hold_days=10. ATR14=22.2, resistance_5/10/20/60=212/302/302/388. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## HBAT — momentum_20d_continual_research — NO_TRADE

**Score:** 0.392 vs policy min 0.30 · **Close:** 394 · **ATR14:** 50.6 · **Volume ratio 20D:** 0.94 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 376–406, entry trigger **406**, stop **372**, risk 34 points (8.37%).

**Targets:** TP1 **545** (4.09R), TP2 **565** (4.68R), TP3 **585** (5.26R). Recommended base-case RR: **4.68R**.

**Why entry:** Hybrid entry uses close 394 and ATR14 50.6: buy zone 376–406. Entry is valid only if price can trade/hold around 406 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 372 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 545 (4.09R), TP2 565 (4.68R), TP3 585 (5.26R). Targets are ATR/structure capped for hold_days=10. ATR14=50.6, resistance_5/10/20/60=545/545/545/545. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** strategy policy has execution_enabled=false; entry-to-stop risk 8.37% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## CYBR — position_continual — NO_TRADE

**Score:** 0.376 vs policy min 0.30 · **Close:** 650 · **ATR14:** 115.7 · **Volume ratio 20D:** 0.75 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 605–675, entry trigger **675**, stop **620**, risk 55 points (8.15%).

**Targets:** TP1 **735** (1.09R), TP2 **1,330** (11.91R), TP3 **1,360** (12.45R). Recommended base-case RR: **11.91R**.

**Why entry:** Hybrid entry uses close 650 and ATR14 115.7: buy zone 605–675. Entry is valid only if price can trade/hold around 675 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 620 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 735 (1.09R), TP2 1,330 (11.91R), TP3 1,360 (12.45R). Targets are ATR/structure capped for hold_days=10. ATR14=115.7, resistance_5/10/20/60=1,330/1,330/1,590/1,710. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.15% exceeds max strategy risk 8.00%; TP1 reward/risk 1.09R is below strategy minimum 1.25R

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## MSIN — position_continual — NO_TRADE

**Score:** 0.365 vs policy min 0.30 · **Close:** 645 · **ATR14:** 86.1 · **Volume ratio 20D:** 1.16 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 610–665, entry trigger **665**, stop **610**, risk 55 points (8.27%).

**Targets:** TP1 **900** (4.27R), TP2 **930** (4.82R), TP3 **960** (5.36R). Recommended base-case RR: **4.82R**.

**Why entry:** Hybrid entry uses close 645 and ATR14 86.1: buy zone 610–665. Entry is valid only if price can trade/hold around 665 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 610 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 900 (4.27R), TP2 930 (4.82R), TP3 960 (5.36R). Targets are ATR/structure capped for hold_days=10. ATR14=86.1, resistance_5/10/20/60=900/935/1,450/1,450. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.27% exceeds max strategy risk 8.00%

**Risk flags:** OK

**Strategy risk note:** Generic strategy rule.

---

## BNBR — position_continual — NO_TRADE

**Score:** 0.349 vs policy min 0.30 · **Close:** 175 · **ATR14:** 19.5 · **Volume ratio 20D:** 1.68 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 168–179, entry trigger **179**, stop **164**, risk 15 points (8.38%).

**Targets:** TP1 **224** (3.00R), TP2 **232** (3.53R), TP3 **240** (4.07R). Recommended base-case RR: **3.53R**.

**Why entry:** Hybrid entry uses close 175 and ATR14 19.5: buy zone 168–179. Entry is valid only if price can trade/hold around 179 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 164 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 224 (3.00R), TP2 232 (3.53R), TP3 240 (4.07R). Targets are ATR/structure capped for hold_days=10. ATR14=19.5, resistance_5/10/20/60=224/228/240/240. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.38% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## MDIA — position_continual — NO_TRADE

**Score:** 0.334 vs policy min 0.30 · **Close:** 114 · **ATR14:** 33.9 · **Volume ratio 20D:** 0.25 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 102–121, entry trigger **121**, stop **111**, risk 10 points (8.26%).

**Targets:** TP1 **145** (2.40R), TP2 **150** (2.90R), TP3 **155** (3.40R). Recommended base-case RR: **2.90R**.

**Why entry:** Hybrid entry uses close 114 and ATR14 33.9: buy zone 102–121. Entry is valid only if price can trade/hold around 121 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 111 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 145 (2.40R), TP2 150 (2.90R), TP3 155 (3.40R). Targets are ATR/structure capped for hold_days=10. ATR14=33.9, resistance_5/10/20/60=145/162/162/162. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.26% exceeds max strategy risk 8.00%; volume ratio 0.25 below required 0.60; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---

## ASPR — position_continual — NO_TRADE

**Score:** 0.309 vs policy min 0.30 · **Close:** 370 · **ATR14:** 40.6 · **Volume ratio 20D:** 3.83 · **Hold:** 10 day(s)

**Execution numbers:** Buy zone 354–380, entry trigger **380**, stop **348**, risk 32 points (8.42%).

**Targets:** TP1 **456** (2.38R), TP2 **472** (2.88R), TP3 **488** (3.38R). Recommended base-case RR: **2.88R**.

**Why entry:** Hybrid entry uses close 370 and ATR14 40.6: buy zone 354–380. Entry is valid only if price can trade/hold around 380 without immediate rejection. If price gaps far above trigger, wait for retest.

**Why stop:** Stop 348 is capped by max risk 8.0% from entry. This prevents a structurally attractive setup from becoming oversized risk. This stop is not a random number; it is the invalidation level for the structure/volatility thesis.

**Why targets:** TP1 456 (2.38R), TP2 472 (2.88R), TP3 488 (3.38R). Targets are ATR/structure capped for hold_days=10. ATR14=40.6, resistance_5/10/20/60=456/456/456/456. TP1 is the realistic execution target, TP2 is stretch target, TP3 is continuation-only and should not be treated as base case.

**No-trade / caution condition:** entry-to-stop risk 8.42% exceeds max strategy risk 8.00%; dominant rank-1 buyer concentration detected; reduce size or wait for cleaner flow

**Risk flags:** DOMINANT_RANK1_BUYER

**Strategy risk note:** Generic strategy rule.

---
