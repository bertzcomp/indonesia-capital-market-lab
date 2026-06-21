# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-06-08**. macro risk score: -1.305. 5-day market return proxy: -10.42%. 20-day market volatility proxy: 0.018. FX pressure: 0.00%. Brent move: 1.25%. coal proxy move: 1.24%. Regime label: **risk_off**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. ELPI — ara_candidate_continual

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.870403  
**Risk Flags:** OK  

**Trade thesis.** ELPI is selected by the **ara_candidate_continual** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.870. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -45.30%; 20-day return is -46.81%; 20-day volatility is 12.06%; volume ratio is neutral at 0.73. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CC with streak 2; rank-1 seller is MG; buyer dominance is 24.61%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 883 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. COCO — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.572401  
**Risk Flags:** OK  

**Trade thesis.** COCO is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.572. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -36.29%; 20-day return is -49.36%; 20-day volatility is 7.98%; volume participation is still thin with volume ratio 0.51. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.007; rank-1 buyer is CC with streak 3; rank-1 seller is XL; buyer dominance is 31.88%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 145 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. OASA — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.562735  
**Risk Flags:** OK  

**Trade thesis.** OASA is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.563. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -37.50%; 20-day return is -45.00%; 20-day volatility is 7.34%; volume participation is still thin with volume ratio 0.66. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.005; rank-1 buyer is AK with streak 1; rank-1 seller is YB; buyer dominance is 21.64%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 202 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. FUTR — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.561875  
**Risk Flags:** OK  

**Trade thesis.** FUTR is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.562. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -41.34%; 20-day return is -53.54%; 20-day volatility is 6.92%; volume expansion is visible with volume ratio 2.03. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is KK with streak 1; rank-1 seller is YP; buyer dominance is 24.22%; daily share of the dominant buyer is 1.51%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 97 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. PSKT — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.552971  
**Risk Flags:** OK  

**Trade thesis.** PSKT is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.553. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -34.23%; 20-day return is -43.85%; 20-day volatility is 6.47%; volume participation is still thin with volume ratio 0.67. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is CC with streak 2; rank-1 seller is XL; buyer dominance is 28.70%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 134 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. GTSI — momentum_5d_continual_defensive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_5d` = 0.552599  
**Risk Flags:** OK  

**Trade thesis.** GTSI is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.553. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -36.08%; 20-day return is -54.09%; 20-day volatility is 5.69%; volume ratio is neutral at 0.95. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 27.83%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 94 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. INET — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.550138  
**Risk Flags:** OK  

**Trade thesis.** INET is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.550. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -32.33%; 20-day return is -48.01%; 20-day volatility is 5.63%; volume ratio is neutral at 1.17. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is AK with streak 2; rank-1 seller is AK; buyer dominance is 22.18%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 146 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. VKTR — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.548018  
**Risk Flags:** OK  

**Trade thesis.** VKTR is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.548. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.17%; 20-day return is -41.53%; 20-day volatility is 6.48%; volume ratio is neutral at 1.22. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 21.48%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 492 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. BBYB — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.546976  
**Risk Flags:** OK  

**Trade thesis.** BBYB is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.547. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -26.15%; 20-day return is -36.42%; 20-day volatility is 4.41%; volume expansion is visible with volume ratio 1.96. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CC with streak 4; rank-1 seller is YP; buyer dominance is 20.37%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 181 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. DEWA — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.531461  
**Risk Flags:** OK  

**Trade thesis.** DEWA is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.531. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.15%; 20-day return is -49.39%; 20-day volatility is 6.31%; volume ratio is neutral at 0.77. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.018; rank-1 buyer is CC with streak 1; rank-1 seller is AK; buyer dominance is 20.20%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 230 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. COIN — momentum_10d_continual_aggressive

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_momentum_10d` = 0.524457  
**Risk Flags:** OK  

**Trade thesis.** COIN is selected by the **momentum_10d_continual_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d` at 0.524. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -27.16%; 20-day return is -48.47%; 20-day volatility is 4.83%; volume participation is still thin with volume ratio 0.53. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 21.40%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 554 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. UVCR — scalping_continual_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_scalp` = 0.704884  
**Risk Flags:** OK  

**Trade thesis.** UVCR is selected by the **scalping_continual_defensive** setup (short-time momentum execution). The primary model evidence is `score_scalp` at 0.705. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -39.50%; 20-day return is -36.28%; 20-day volatility is 6.15%; volume expansion is visible with volume ratio 1.60. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CP with streak 2; rank-1 seller is OD; buyer dominance is 48.61%; daily share of the dominant buyer is 2.44%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 133 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. BULL — scalping_continual_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_scalp` = 0.700570  
**Risk Flags:** OK  

**Trade thesis.** BULL is selected by the **scalping_continual_defensive** setup (short-time momentum execution). The primary model evidence is `score_scalp` at 0.701. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -29.53%; 20-day return is -46.14%; 20-day volatility is 6.34%; volume ratio is neutral at 0.72. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 24.54%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 250 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. PACK — scalping_continual_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_scalp` = 0.696325  
**Risk Flags:** OK  

**Trade thesis.** PACK is selected by the **scalping_continual_defensive** setup (short-time momentum execution). The primary model evidence is `score_scalp` at 0.696. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -33.12%; 20-day return is -11.97%; 20-day volatility is 7.66%; volume ratio is neutral at 0.89. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 18.00%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 190 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. BIPI — position_continual

**Confidence:** Watchlist only  
**Risk Grade:** Controlled  
**Primary Score:** `score_position` = 0.348794  
**Risk Flags:** OK  

**Trade thesis.** BIPI is selected by the **position_continual** setup (position continuation / structural setup). The primary model evidence is `score_position` at 0.349. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -27.27%; 20-day return is -46.22%; 20-day volatility is 6.66%; volume participation is still thin with volume ratio 0.56. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.005; rank-1 buyer is CC with streak 3; rank-1 seller is XL; buyer dominance is 23.61%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 118 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. IRSX — position_continual

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_position` = 0.330537  
**Risk Flags:** OK  

**Trade thesis.** IRSX is selected by the **position_continual** setup (position continuation / structural setup). The primary model evidence is `score_position` at 0.331. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -35.29%; 20-day return is -45.00%; 20-day volatility is 8.75%; volume ratio is neutral at 1.12. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.003; rank-1 buyer is AK with streak 2; rank-1 seller is XL; buyer dominance is 24.67%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 223 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 17. BUVA — momentum_5d_continual_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_momentum_5d` = 0.573424  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** BUVA is selected by the **momentum_5d_continual_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d` at 0.573. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -27.63%; 20-day return is -48.11%; 20-day volatility is 9.61%; volume ratio is neutral at 0.93. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 19.32%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 506 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 18. GRIA — ara_candidate

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d` = 0.357859  
**Risk Flags:** OK  

**Trade thesis.** GRIA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_momentum_10d` at 0.358. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 21.74%; 20-day return is 68.00%; 20-day volatility is 11.06%; volume expansion is visible with volume ratio 4.96. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is CP with streak 2; rank-1 seller is XL; buyer dominance is 36.10%; daily share of the dominant buyer is 2.44%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 155 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 19. PSAB — ara_candidate

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d` = 0.333853  
**Risk Flags:** OK  

**Trade thesis.** PSAB is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_momentum_10d` at 0.334. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 13.45%; 20-day return is 3.85%; 20-day volatility is 7.77%; volume expansion is visible with volume ratio 2.95. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.009; rank-1 buyer is XL with streak 5; rank-1 seller is XL; buyer dominance is 25.52%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 497 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 20. PSDN — ara_candidate

**Confidence:** Watchlist only  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d` = 0.230509  
**Risk Flags:** OK  

**Trade thesis.** PSDN is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_momentum_10d` at 0.231. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -4.65%; 20-day return is -36.60%; 20-day volatility is 7.48%; volume expansion is visible with volume ratio 4.53. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 52.81%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 113 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 21. MAIN — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.825031  
**Risk Flags:** OK  

**Trade thesis.** MAIN is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.825. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.30%; 20-day return is -28.32%; 20-day volatility is 3.57%; volume ratio is neutral at 1.09. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.004; rank-1 buyer is CC with streak 1; rank-1 seller is CC; buyer dominance is 18.67%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 592 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 22. ARTO — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.820562  
**Risk Flags:** OK  

**Trade thesis.** ARTO is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.821. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -31.78%; 20-day return is -35.60%; 20-day volatility is 4.12%; volume expansion is visible with volume ratio 2.70. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is CC with streak 1; rank-1 seller is ZP; buyer dominance is 24.58%; daily share of the dominant buyer is 15.25%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 764 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 23. SUPA — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.801790  
**Risk Flags:** OK  

**Trade thesis.** SUPA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.802. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -28.57%; 20-day return is -28.99%; 20-day volatility is 4.82%; volume participation is still thin with volume ratio 0.39. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 33.71%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 564 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 24. APLN — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.789860  
**Risk Flags:** OK  

**Trade thesis.** APLN is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.790. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -20.13%; 20-day return is -38.66%; 20-day volatility is 4.52%; volume participation is still thin with volume ratio 0.44. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is AK with streak 3; rank-1 seller is BK; buyer dominance is 26.95%; daily share of the dominant buyer is 5.70%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 112 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 25. NRCA — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.786926  
**Risk Flags:** OK  

**Trade thesis.** NRCA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.787. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -27.76%; 20-day return is -41.00%; 20-day volatility is 5.32%; volume ratio is neutral at 1.47. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 2; rank-1 seller is SQ; buyer dominance is 25.75%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 330 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 26. CBRE — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium-high  
**Primary Score:** `score_ara` = 0.769549  
**Risk Flags:** OK  

**Trade thesis.** CBRE is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.770. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -30.12%; 20-day return is -36.26%; 20-day volatility is 8.90%; volume ratio is neutral at 0.74. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is XL with streak 26; rank-1 seller is XL; buyer dominance is 34.74%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 534 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 27. NSSS — ara_candidate

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_ara` = 0.761060  
**Risk Flags:** OK  

**Trade thesis.** NSSS is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.761. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -18.18%; 20-day return is -53.04%; 20-day volatility is 5.04%; volume participation is still thin with volume ratio 0.56. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is IF with streak 2; rank-1 seller is IF; buyer dominance is 27.51%; daily share of the dominant buyer is 0.93%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 354 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 28. WEHA — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.750049  
**Risk Flags:** OK  

**Trade thesis.** WEHA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.750. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -16.94%; 20-day return is -21.97%; 20-day volatility is 10.19%; volume expansion is visible with volume ratio 1.55. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is YP with streak 1; rank-1 seller is YP; buyer dominance is 55.81%; daily share of the dominant buyer is 5.24%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 95 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 29. CDIA — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.744427  
**Risk Flags:** OK  

**Trade thesis.** CDIA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.744. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -30.59%; 20-day return is -43.81%; 20-day volatility is 7.47%; volume participation is still thin with volume ratio 0.51. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 20.08%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 543 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 30. NZIA — ara_candidate

**Confidence:** High  
**Risk Grade:** Medium-high  
**Primary Score:** `score_ara` = 0.742350  
**Risk Flags:** OK  

**Trade thesis.** NZIA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.742. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 48.48%; 20-day return is 20.99%; 20-day volatility is 15.45%; volume participation is still thin with volume ratio 0.46. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 8; rank-1 seller is XA; buyer dominance is 42.98%; daily share of the dominant buyer is 31.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 180 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.