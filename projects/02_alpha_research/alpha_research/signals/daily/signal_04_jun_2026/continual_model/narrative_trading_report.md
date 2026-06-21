# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-06-03**. macro risk score: -1.161. 5-day market return proxy: -3.00%. 20-day market volatility proxy: 0.015. FX pressure: 0.00%. Brent move: 1.79%. coal proxy move: 1.78%. Regime label: **risk_off**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. DEWA — ara_candidate_continual

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.885507  
**Risk Flags:** OK  

**Trade thesis.** DEWA is selected by the **ara_candidate_continual** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.886. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -22.22%; 20-day return is -41.78%; 20-day volatility is 6.22%; volume ratio is neutral at 1.43. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 21.00%; daily share of the dominant buyer is 10.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 271 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. GTSI — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.593039  
**Risk Flags:** OK  

**Trade thesis.** GTSI is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.593. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -28.07%; 20-day return is -46.52%; 20-day volatility is 5.61%; volume expansion is visible with volume ratio 1.96. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 28.63%; daily share of the dominant buyer is 4.90%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 114 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. RISE — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.582471  
**Risk Flags:** OK  

**Trade thesis.** RISE is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.582. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.75%; 20-day return is -40.42%; 20-day volatility is 4.51%; volume expansion is visible with volume ratio 3.86. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is YJ with streak 1; rank-1 seller is FZ; buyer dominance is 47.29%; daily share of the dominant buyer is 0.35%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 939 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. BULL — momentum_10d_continual_aggressive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.658321  
**Risk Flags:** OK  

**Trade thesis.** BULL is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.658. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -21.74%; 20-day return is -39.44%; 20-day volatility is 5.87%; volume expansion is visible with volume ratio 1.60. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.011; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 19.62%; daily share of the dominant buyer is 4.90%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 300 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. INET — momentum_10d_continual_aggressive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.651906  
**Risk Flags:** OK  

**Trade thesis.** INET is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.652. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.48%; 20-day return is -36.22%; 20-day volatility is 5.33%; volume ratio is neutral at 1.24. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.006; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 20.19%; daily share of the dominant buyer is 4.90%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 186 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. BIPI — momentum_10d_continual_aggressive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.650836  
**Risk Flags:** OK  

**Trade thesis.** BIPI is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.651. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.39%; 20-day return is -38.21%; 20-day volatility is 6.67%; volume ratio is neutral at 1.21. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is MG with streak 1; rank-1 seller is MG; buyer dominance is 21.02%; daily share of the dominant buyer is 1.75%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 140 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. BUMI — momentum_10d_continual_aggressive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.616454  
**Risk Flags:** OK  

**Trade thesis.** BUMI is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.616. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -20.00%; 20-day return is -35.09%; 20-day volatility is 5.10%; volume ratio is neutral at 1.49. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.009; rank-1 buyer is AK with streak 1; rank-1 seller is CC; buyer dominance is 21.80%; daily share of the dominant buyer is 4.90%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 139 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. BRMS — position_continual

**Confidence:** Watchlist only  
**Risk Grade:** Controlled  
**Primary Score:** `score_position` = 0.320803  
**Risk Flags:** OK  

**Trade thesis.** BRMS is selected by the **position_continual** setup (position continuation / structural setup). The primary model evidence is `score_position` at 0.321. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -15.08%; 20-day return is -34.36%; 20-day volatility is 5.56%; volume ratio is neutral at 1.35. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.008; rank-1 buyer is ZP with streak 1; rank-1 seller is ZP; buyer dominance is 25.74%; daily share of the dominant buyer is 2.10%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 498 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. MSIN — position_continual

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_position` = 0.315189  
**Risk Flags:** OK  

**Trade thesis.** MSIN is selected by the **position_continual** setup (position continuation / structural setup). The primary model evidence is `score_position` at 0.315. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -15.19%; 20-day return is -42.75%; 20-day volatility is 8.07%; volume expansion is visible with volume ratio 3.80. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.008; rank-1 buyer is EP with streak 17; rank-1 seller is XL; buyer dominance is 23.28%; daily share of the dominant buyer is 1.17%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 421 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. BNBR — momentum_5d_continual_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_5d` = 0.629105  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** BNBR is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.629. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -23.24%; 20-day return is -48.58%; 20-day volatility is 7.42%; volume ratio is neutral at 1.00. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.005; rank-1 buyer is XL with streak 11; rank-1 seller is XL; buyer dominance is 23.92%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 100 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. HUMI — momentum_5d_continual_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_5d` = 0.626296  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** HUMI is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.626. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -20.00%; 20-day return is -34.07%; 20-day volatility is 6.08%; volume ratio is neutral at 1.02. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 44; rank-1 seller is XL; buyer dominance is 22.66%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 111 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. DEFI — momentum_5d_continual_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_5d` = 0.576158  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** DEFI is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.576. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -22.54%; 20-day return is -43.59%; 20-day volatility is 10.78%; volume participation is still thin with volume ratio 0.23. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 21; rank-1 seller is XL; buyer dominance is 43.38%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 101 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. ASPR — momentum_5d_continual_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_5d` = 0.574752  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** ASPR is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.575. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -36.11%; 20-day return is -20.00%; 20-day volatility is 15.35%; volume participation is still thin with volume ratio 0.56. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 6; rank-1 seller is XL; buyer dominance is 39.42%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 169 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. OASA — momentum_10d_continual_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d` = 0.616131  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** OASA is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.616. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -23.59%; 20-day return is -14.86%; 20-day volatility is 7.49%; volume participation is still thin with volume ratio 0.66. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.009; rank-1 buyer is XL with streak 5; rank-1 seller is XL; buyer dominance is 19.79%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 274 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. COCO — position_continual

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position` = 0.312545  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** COCO is selected by the **position_continual** setup (position continuation / structural setup). The primary model evidence is `score_position` at 0.313. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -18.25%; 20-day return is -40.46%; 20-day volatility is 7.65%; volume participation is still thin with volume ratio 0.57. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 6; rank-1 seller is XL; buyer dominance is 18.62%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 190 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. BUVA — momentum_20d_continual_research

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_20d` = 0.407644  
**Risk Flags:** OK  

**Trade thesis.** BUVA is selected by the **momentum_20d_continual_research** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_20d` at 0.408. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 0.69%; 20-day return is -33.18%; 20-day volatility is 9.27%; volume ratio is neutral at 0.87. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 20.43%; daily share of the dominant buyer is 4.90%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 667 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 17. WEHA — ara_candidate

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d` = 0.368950  
**Risk Flags:** OK  

**Trade thesis.** WEHA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_momentum_10d` at 0.369. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 43.97%; 20-day return is 33.60%; 20-day volatility is 8.27%; volume expansion is visible with volume ratio 7.10. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.007; rank-1 buyer is CP with streak 1; rank-1 seller is CP; buyer dominance is 60.33%; daily share of the dominant buyer is 2.33%; BDM confirmation is present, improving behavioural confidence.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 154 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 18. MMIX — ara_candidate

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d` = 0.394696  
**Risk Flags:** OK  

**Trade thesis.** MMIX is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_momentum_10d` at 0.395. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 80.94%; 20-day return is 116.89%; 20-day volatility is 8.49%; volume expansion is visible with volume ratio 8.39. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AG with streak 4; rank-1 seller is AG; buyer dominance is 34.05%; daily share of the dominant buyer is 0.47%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 603 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 19. NZIA — ara_candidate

**Confidence:** Watchlist only  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_10d` = 0.356767  
**Risk Flags:** OK  

**Trade thesis.** NZIA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_momentum_10d` at 0.357. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 65.81%; 20-day return is 20.50%; 20-day volatility is 12.90%; volume expansion is visible with volume ratio 4.37. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 5; rank-1 seller is XL; buyer dominance is 34.82%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 178 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 20. TRIN — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.873459  
**Risk Flags:** OK  

**Trade thesis.** TRIN is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.873. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -23.69%; 20-day return is -48.99%; 20-day volatility is 4.83%; volume expansion is visible with volume ratio 1.58. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 29.19%; daily share of the dominant buyer is 10.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 357 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 21. APLN — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.865426  
**Risk Flags:** OK  

**Trade thesis.** APLN is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.865. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -16.03%; 20-day return is -29.57%; 20-day volatility is 5.94%; volume participation is still thin with volume ratio 0.27. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.010; rank-1 buyer is CC with streak 2; rank-1 seller is CC; buyer dominance is 18.89%; daily share of the dominant buyer is 10.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 121 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 22. PYFA — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium-high  
**Primary Score:** `score_ara` = 0.862865  
**Risk Flags:** OK  

**Trade thesis.** PYFA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.863. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.88%; 20-day return is -39.41%; 20-day volatility is 8.44%; volume participation is still thin with volume ratio 0.54. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.003; rank-1 buyer is XL with streak 4; rank-1 seller is XL; buyer dominance is 23.17%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 190 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 23. FUTR — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.855907  
**Risk Flags:** OK  

**Trade thesis.** FUTR is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.856. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -19.13%; 20-day return is -36.21%; 20-day volatility is 6.17%; volume ratio is neutral at 1.29. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 23.74%; daily share of the dominant buyer is 10.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 137 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 24. LCKM — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium-high  
**Primary Score:** `score_ara` = 0.854606  
**Risk Flags:** OK  

**Trade thesis.** LCKM is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.855. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -26.24%; 20-day return is -25.71%; 20-day volatility is 13.39%; volume participation is still thin with volume ratio 0.20. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 30; rank-1 seller is XL; buyer dominance is 41.26%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 96 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 25. GZCO — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.854443  
**Risk Flags:** OK  

**Trade thesis.** GZCO is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.854. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -10.90%; 20-day return is -40.09%; 20-day volatility is 4.99%; volume ratio is neutral at 0.75. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 22.67%; daily share of the dominant buyer is 10.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 130 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 26. IRSX — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.850724  
**Risk Flags:** OK  

**Trade thesis.** IRSX is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.851. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 1.22%; 20-day return is -18.63%; 20-day volatility is 8.12%; volume ratio is neutral at 0.99. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is YB with streak 1; rank-1 seller is XL; buyer dominance is 19.40%; daily share of the dominant buyer is 1.17%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 305 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 27. ESIP — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium-high  
**Primary Score:** `score_ara` = 0.845835  
**Risk Flags:** OK  

**Trade thesis.** ESIP is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.846. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.78%; 20-day return is -30.19%; 20-day volatility is 10.68%; volume participation is still thin with volume ratio 0.07. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 42; rank-1 seller is XL; buyer dominance is 39.19%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 102 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 28. CDIA — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.836322  
**Risk Flags:** OK  

**Trade thesis.** CDIA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.836. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is 1.33%; 20-day return is -26.21%; 20-day volatility is 7.40%; volume ratio is neutral at 0.73. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.004; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 19.69%; daily share of the dominant buyer is 4.90%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 699 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 29. TAMA — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.835629  
**Risk Flags:** OK  

**Trade thesis.** TAMA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.836. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.87%; 20-day return is -2.92%; 20-day volatility is 7.77%; volume expansion is visible with volume ratio 3.69. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 4; rank-1 seller is CC; buyer dominance is 26.25%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 153 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 30. VKTR — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.832738  
**Risk Flags:** OK  

**Trade thesis.** VKTR is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.833. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -11.41%; 20-day return is -27.47%; 20-day volatility is 6.10%; volume ratio is neutral at 1.35. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 26.45%; daily share of the dominant buyer is 36.95%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 610 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.