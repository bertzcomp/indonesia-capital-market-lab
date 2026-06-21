# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-06-04**. macro risk score: -1.462. 5-day market return proxy: -4.70%. 20-day market volatility proxy: 0.015. FX pressure: -1.79%. Brent move: -2.96%. coal proxy move: -2.94%. Regime label: **risk_off**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. APIC — market_maker_silent_accum_defensive

**Confidence:** Medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.552566  
**Risk Flags:** OK  

**Trade thesis.** APIC is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.553. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -49.37%; 20-day return is -68.73%; 20-day volatility is 10.61%; volume expansion is visible with volume ratio 6.25. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is FS with streak 1; rank-1 seller is AP; buyer dominance is 55.98%; daily share of the dominant buyer is 0.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 557 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. KEEN — scalping_rank_hgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_scalp__multi_strategy_time__rank_hgb__scalp` = 0.658361  
**Risk Flags:** OK  

**Trade thesis.** KEEN is selected by the **scalping_rank_hgb** setup (short-time momentum execution). The primary model evidence is `score_scalp__multi_strategy_time__rank_hgb__scalp` at 0.658. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -10.67%; 20-day return is -18.88%; 20-day volatility is 3.30%; volume ratio is neutral at 1.36. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is LG with streak 23; rank-1 seller is LG; buyer dominance is 83.80%; daily share of the dominant buyer is 0.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 762 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. PSKT — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.771046  
**Risk Flags:** OK  

**Trade thesis.** PSKT is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.771. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.50%; 20-day return is -34.23%; 20-day volatility is 6.12%; volume ratio is neutral at 0.82. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 24.59%; daily share of the dominant buyer is 7.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 158 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. TRIN — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.767348  
**Risk Flags:** OK  

**Trade thesis.** TRIN is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.767. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -29.66%; 20-day return is -53.57%; 20-day volatility is 5.27%; volume expansion is visible with volume ratio 2.77. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is YP with streak 1; rank-1 seller is XL; buyer dominance is 21.95%; daily share of the dominant buyer is 3.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 310 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. HRUM — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.766311  
**Risk Flags:** OK  

**Trade thesis.** HRUM is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.766. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -7.59%; 20-day return is -27.72%; 20-day volatility is 4.36%; volume ratio is neutral at 0.85. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is CC with streak 3; rank-1 seller is YP; buyer dominance is 20.57%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 690 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. SOCI — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.764375  
**Risk Flags:** OK  

**Trade thesis.** SOCI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.764. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.23%; 20-day return is -33.33%; 20-day volatility is 5.38%; volume ratio is neutral at 1.01. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is AK with streak 1; rank-1 seller is AK; buyer dominance is 30.26%; daily share of the dominant buyer is 7.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 306 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. DKFT — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.762942  
**Risk Flags:** OK  

**Trade thesis.** DKFT is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.763. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -12.33%; 20-day return is -23.35%; 20-day volatility is 3.92%; volume ratio is neutral at 1.02. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.006; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 16.31%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 609 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. TOBA — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.762372  
**Risk Flags:** OK  

**Trade thesis.** TOBA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.762. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.49%; 20-day return is -36.55%; 20-day volatility is 4.56%; volume ratio is neutral at 1.38. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is CC with streak 1; rank-1 seller is YP; buyer dominance is 22.87%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 347 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. STAA — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.761438  
**Risk Flags:** OK  

**Trade thesis.** STAA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.761. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -9.95%; 20-day return is -30.38%; 20-day volatility is 2.99%; volume ratio is neutral at 1.11. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is CC with streak 1; rank-1 seller is AT; buyer dominance is 17.25%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 871 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. COCO — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.756647  
**Risk Flags:** OK  

**Trade thesis.** COCO is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.757. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.79%; 20-day return is -44.35%; 20-day volatility is 7.80%; volume participation is still thin with volume ratio 0.69. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 18.05%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 172 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. GTSI — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.754766  
**Risk Flags:** OK  

**Trade thesis.** GTSI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.755. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -32.34%; 20-day return is -50.87%; 20-day volatility is 5.68%; volume ratio is neutral at 1.25. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is AK with streak 2; rank-1 seller is XL; buyer dominance is 34.27%; daily share of the dominant buyer is 7.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 105 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. BBYB — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.750786  
**Risk Flags:** OK  

**Trade thesis.** BBYB is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.751. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -15.94%; 20-day return is -26.58%; 20-day volatility is 3.73%; volume ratio is neutral at 1.46. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is CC with streak 2; rank-1 seller is PD; buyer dominance is 20.67%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 221 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. HOPE — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.749955  
**Risk Flags:** OK  

**Trade thesis.** HOPE is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.750. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.91%; 20-day return is -38.20%; 20-day volatility is 5.24%; volume ratio is neutral at 1.39. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is YP with streak 1; rank-1 seller is XL; buyer dominance is 30.91%; daily share of the dominant buyer is 3.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 103 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. DOOH — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.743766  
**Risk Flags:** OK  

**Trade thesis.** DOOH is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.744. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.86%; 20-day return is -36.46%; 20-day volatility is 5.51%; volume expansion is visible with volume ratio 1.79. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is AK with streak 1; rank-1 seller is YB; buyer dominance is 16.21%; daily share of the dominant buyer is 7.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 107 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. HUMI — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.742961  
**Risk Flags:** OK  

**Trade thesis.** HUMI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.743. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -30.77%; 20-day return is -40.66%; 20-day volatility is 6.32%; volume ratio is neutral at 1.10. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is CC with streak 1; rank-1 seller is XA; buyer dominance is 27.50%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 99 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. ELSA — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.736168  
**Risk Flags:** OK  

**Trade thesis.** ELSA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.736. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -6.92%; 20-day return is -27.11%; 20-day volatility is 3.09%; volume ratio is neutral at 0.84. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is AK with streak 2; rank-1 seller is NI; buyer dominance is 30.21%; daily share of the dominant buyer is 7.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 582 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 17. COIN — swing_hgb_defensive

**Confidence:** High  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.734061  
**Risk Flags:** OK  

**Trade thesis.** COIN is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.734. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.37%; 20-day return is -39.92%; 20-day volatility is 4.26%; volume ratio is neutral at 0.91. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 20.90%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 677 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 18. GOLF — position_xgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.604919  
**Risk Flags:** OK  

**Trade thesis.** GOLF is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.605. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -20.83%; 20-day return is -31.09%; 20-day volatility is 3.20%; volume expansion is visible with volume ratio 3.01. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.021; rank-1 buyer is YP with streak 1; rank-1 seller is YB; buyer dominance is 14.23%; daily share of the dominant buyer is 3.26%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 128 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 19. DGWG — position_xgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.604541  
**Risk Flags:** OK  

**Trade thesis.** DGWG is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.605. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -12.35%; 20-day return is -24.75%; 20-day volatility is 3.47%; volume ratio is neutral at 1.19. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is KI with streak 1; rank-1 seller is LG; buyer dominance is 40.27%; daily share of the dominant buyer is 0.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 285 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 20. DEWA — position_xgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.603177  
**Risk Flags:** OK  

**Trade thesis.** DEWA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.603. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -18.29%; 20-day return is -42.80%; 20-day volatility is 6.21%; volume ratio is neutral at 1.50. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is AK with streak 1; rank-1 seller is CC; buyer dominance is 17.04%; daily share of the dominant buyer is 7.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 264 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 21. AGRO — position_xgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.601599  
**Risk Flags:** OK  

**Trade thesis.** AGRO is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.602. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.17%; 20-day return is -22.04%; 20-day volatility is 3.08%; volume ratio is neutral at 1.29. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is CC with streak 1; rank-1 seller is YP; buyer dominance is 24.68%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 139 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 22. BIPI — position_xgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.601478  
**Risk Flags:** OK  

**Trade thesis.** BIPI is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.601. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -19.55%; 20-day return is -42.86%; 20-day volatility is 6.61%; volume expansion is visible with volume ratio 1.71. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.004; rank-1 buyer is CC with streak 1; rank-1 seller is II; buyer dominance is 20.94%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 132 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 23. TEBE — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.599495  
**Risk Flags:** OK  

**Trade thesis.** TEBE is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.599. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.49%; 20-day return is -28.79%; 20-day volatility is 4.64%; volume expansion is visible with volume ratio 1.74. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CC with streak 2; rank-1 seller is YJ; buyer dominance is 50.32%; daily share of the dominant buyer is 14.34%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 862 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 24. VKTR — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.602980  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** VKTR is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.603. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.19%; 20-day return is -30.94%; 20-day volatility is 6.16%; volume ratio is neutral at 1.32. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is XL with streak 3; rank-1 seller is XL; buyer dominance is 21.95%; daily share of the dominant buyer is 30.54%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 577 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 25. NZIA — ara_candidate

**Confidence:** Low-to-medium  
**Risk Grade:** High  
**Primary Score:** `score_ara` = 0.299572  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** NZIA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.300. The price/volume context indicates that price is trading above the 20-day mean, suggesting structure is still constructive relative to its recent base; 5-day return is 122.41%; 20-day return is 58.28%; 20-day volatility is 14.68%; volume expansion is visible with volume ratio 4.20. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 6; rank-1 seller is XL; buyer dominance is 35.84%; daily share of the dominant buyer is 30.54%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 237 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 26. FUJI — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.507066  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** FUJI is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.507. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -0.71%; 20-day return is -16.77%; 20-day volatility is 3.59%; volume ratio is neutral at 1.33. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CP with streak 1; rank-1 seller is CP; buyer dominance is 95.00%; daily share of the dominant buyer is 2.91%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 266 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 27. BELL — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium-high  
**Primary Score:** `score_mm_silent` = 0.452025  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** BELL is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.452. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -5.17%; 20-day return is -30.38%; 20-day volatility is 6.22%; volume expansion is visible with volume ratio 7.79. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 28; rank-1 seller is XL; buyer dominance is 49.76%; daily share of the dominant buyer is 30.54%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 101 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 28. MSJA — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_mm_silent` = 0.446133  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** MSJA is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.446. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -5.71%; 20-day return is -24.57%; 20-day volatility is 4.44%; volume participation is still thin with volume ratio 0.44. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AZ with streak 2; rank-1 seller is OD; buyer dominance is 55.83%; daily share of the dominant buyer is 1.17%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 374 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 29. IRSX — momentum_5d_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** High  
**Primary Score:** `score_momentum_5d__momentum_ranker__xgb__momentum_5d` = 0.464651  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** IRSX is selected by the **momentum_5d_hgb_defensive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_5d__momentum_ranker__xgb__momentum_5d` at 0.465. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -24.87%; 20-day return is -30.05%; 20-day volatility is 8.68%; volume ratio is neutral at 1.28. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 1; rank-1 seller is YB; buyer dominance is 20.04%; daily share of the dominant buyer is 30.54%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 261 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 30. OASA — momentum_10d_hgb_aggressive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_momentum_10d__momentum_ranker__hgb__momentum_10d` = 0.450169  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** OASA is selected by the **momentum_10d_hgb_aggressive** setup (cross-sectional momentum continuation). The primary model evidence is `score_momentum_10d__momentum_ranker__hgb__momentum_10d` at 0.450. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -28.19%; 20-day return is -31.82%; 20-day volatility is 7.01%; volume ratio is neutral at 0.95. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is MG with streak 1; rank-1 seller is MG; buyer dominance is 18.63%; daily share of the dominant buyer is 1.40%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Enter only if price holds above prior close or reclaims intraday VWAP/support. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 248 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.