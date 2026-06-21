# Narrative Trading Intelligence Report

## Market Context

Signal universe is built from the latest available market panel dated **2026-05-22**. macro risk score: -1.197. 5-day market return proxy: -8.57%. 20-day market volatility proxy: 0.014. FX pressure: 0.00%. Brent move: 0.94%. coal proxy move: 0.93%. Regime label: **risk_off**.

## Operating Principle

This report is not a simple BUY/SELL list. Each signal is interpreted as a conditional trading thesis. Execution is valid only when price structure, liquidity, momentum, and behavioural confirmation remain aligned. If those conditions fail, no-trade or early exit is the correct risk decision.

## Signal Thesis and Execution Plan

### 1. SSMS — scalping_rank_hgb

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_scalp__multi_strategy_time__rank_hgb__scalp` = 0.647570  
**Risk Flags:** OK  

**Trade thesis.** SSMS is selected by the **scalping_rank_hgb** setup (short-time momentum execution). The primary model evidence is `score_scalp__multi_strategy_time__rank_hgb__scalp` at 0.648. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -27.98%; 20-day return is -34.21%; 20-day volatility is 4.84%; volume participation is still thin with volume ratio 0.51. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is CC with streak 1; rank-1 seller is RX; buyer dominance is 30.10%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Needs intraday confirmation; do not enter if opening liquidity fades. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 822 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 2. HRUM — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.662150  
**Risk Flags:** OK  

**Trade thesis.** HRUM is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.662. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -11.73%; 20-day return is -24.04%; 20-day volatility is 4.20%; volume expansion is visible with volume ratio 2.55. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.008; rank-1 buyer is CC with streak 4; rank-1 seller is CC; buyer dominance is 22.27%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 748 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 3. SIMP — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.650567  
**Risk Flags:** OK  

**Trade thesis.** SIMP is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.651. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.18%; 20-day return is -35.26%; 20-day volatility is 4.14%; volume participation is still thin with volume ratio 0.56. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.006; rank-1 buyer is CC with streak 1; rank-1 seller is BQ; buyer dominance is 19.22%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 531 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 4. TOBA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.641704  
**Risk Flags:** OK  

**Trade thesis.** TOBA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.642. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -19.28%; 20-day return is -34.12%; 20-day volatility is 4.91%; volume ratio is neutral at 1.02. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.004; rank-1 buyer is CC with streak 3; rank-1 seller is CC; buyer dominance is 39.81%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 421 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 5. PYFA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.640417  
**Risk Flags:** OK  

**Trade thesis.** PYFA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.640. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -24.38%; 20-day return is -30.06%; 20-day volatility is 8.62%; volume participation is still thin with volume ratio 0.66. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.005; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 21.73%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 223 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 6. KIJA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.638121  
**Risk Flags:** OK  

**Trade thesis.** KIJA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.638. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -30.46%; 20-day return is -35.64%; 20-day volatility is 4.40%; volume expansion is visible with volume ratio 2.37. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.026; rank-1 buyer is CC with streak 1; rank-1 seller is GR; buyer dominance is 18.20%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 114 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 7. CDIA — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.637568  
**Risk Flags:** OK  

**Trade thesis.** CDIA is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.638. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -25.74%; 20-day return is -38.27%; 20-day volatility is 6.92%; volume participation is still thin with volume ratio 0.69. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is AO with streak 1; rank-1 seller is AK; buyer dominance is 15.56%; daily share of the dominant buyer is 0.23%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 690 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 8. INET — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.637457  
**Risk Flags:** OK  

**Trade thesis.** INET is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.637. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -19.01%; 20-day return is -31.14%; 20-day volatility is 5.36%; volume ratio is neutral at 0.81. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 21.63%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 215 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 9. RMKO — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.636244  
**Risk Flags:** OK  

**Trade thesis.** RMKO is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.636. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -23.45%; 20-day return is -44.64%; 20-day volatility is 4.69%; volume ratio is neutral at 1.15. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.000; rank-1 buyer is CC with streak 3; rank-1 seller is XL; buyer dominance is 30.35%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 326 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 10. KRAS — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.633935  
**Risk Flags:** OK  

**Trade thesis.** KRAS is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.634. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -12.12%; 20-day return is -24.68%; 20-day volatility is 3.08%; volume participation is still thin with volume ratio 0.54. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is CC with streak 1; rank-1 seller is XL; buyer dominance is 27.70%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 223 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 11. PSAB — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.631701  
**Risk Flags:** OK  

**Trade thesis.** PSAB is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.632. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.80%; 20-day return is -18.86%; 20-day volatility is 6.61%; volume ratio is neutral at 1.41. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is AK with streak 1; rank-1 seller is AK; buyer dominance is 9.91%; daily share of the dominant buyer is 3.37%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 392 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 12. VKTR — swing_hgb_defensive

**Confidence:** Medium-high  
**Risk Grade:** Controlled  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.628872  
**Risk Flags:** OK  

**Trade thesis.** VKTR is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.629. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.37%; 20-day return is -25.87%; 20-day volatility is 6.04%; volume ratio is neutral at 1.15. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is KI with streak 1; rank-1 seller is KI; buyer dominance is 43.20%; daily share of the dominant buyer is 0.58%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 689 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 13. MBMA — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.560161  
**Risk Flags:** OK  

**Trade thesis.** MBMA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.560. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.61%; 20-day return is -34.86%; 20-day volatility is 5.45%; volume expansion is visible with volume ratio 2.58. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.005; rank-1 buyer is MG with streak 1; rank-1 seller is CC; buyer dominance is 16.64%; daily share of the dominant buyer is 1.74%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 449 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 14. DEWA — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.559974  
**Risk Flags:** OK  

**Trade thesis.** DEWA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.560. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -21.90%; 20-day return is -31.89%; 20-day volatility is 5.76%; volume expansion is visible with volume ratio 1.88. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is AK with streak 1; rank-1 seller is AK; buyer dominance is 12.12%; daily share of the dominant buyer is 3.37%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 351 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 15. BUMI — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.556905  
**Risk Flags:** OK  

**Trade thesis.** BUMI is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.557. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.55%; 20-day return is -26.59%; 20-day volatility is 4.99%; volume expansion is visible with volume ratio 1.77. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is MG with streak 1; rank-1 seller is AK; buyer dominance is 13.06%; daily share of the dominant buyer is 1.74%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 173 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 16. FUTR — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.555299  
**Risk Flags:** OK  

**Trade thesis.** FUTR is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.555. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -16.82%; 20-day return is -36.46%; 20-day volatility is 6.64%; volume ratio is neutral at 1.14. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is AK with streak 1; rank-1 seller is XL; buyer dominance is 15.20%; daily share of the dominant buyer is 3.37%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 168 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 17. NCKL — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.552334  
**Risk Flags:** OK  

**Trade thesis.** NCKL is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.552. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.50%; 20-day return is -25.65%; 20-day volatility is 4.14%; volume ratio is neutral at 1.23. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.009; rank-1 buyer is CC with streak 1; rank-1 seller is PD; buyer dominance is 19.89%; daily share of the dominant buyer is 13.82%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 811 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 18. TRIN — position_xgb

**Confidence:** Medium  
**Risk Grade:** Controlled  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.550094  
**Risk Flags:** OK  

**Trade thesis.** TRIN is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.550. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -17.69%; 20-day return is -41.75%; 20-day volatility is 3.61%; volume ratio is neutral at 1.03. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is KK with streak 1; rank-1 seller is CC; buyer dominance is 28.50%; daily share of the dominant buyer is 1.28%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 476 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 19. FOLK — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.635401  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** FOLK is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.635. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -29.52%; 20-day return is -37.77%; 20-day volatility is 6.01%; volume ratio is neutral at 1.38. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 1; rank-1 seller is YP; buyer dominance is 21.37%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 216 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 20. UNSP — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.634813  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** UNSP is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.635. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -22.01%; 20-day return is -31.49%; 20-day volatility is 6.22%; volume ratio is neutral at 0.76. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 1; rank-1 seller is AI; buyer dominance is 46.91%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 229 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 21. SOCI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.628978  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** SOCI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.629. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -14.16%; 20-day return is -26.10%; 20-day volatility is 5.42%; volume participation is still thin with volume ratio 0.70. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.002; rank-1 buyer is XL with streak 2; rank-1 seller is AK; buyer dominance is 17.20%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 362 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 22. PGLI — swing_hgb_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_swing__multi_strategy_time__hgb__swing` = 0.628782  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** PGLI is selected by the **swing_hgb_defensive** setup (defensive swing continuation). The primary model evidence is `score_swing__multi_strategy_time__hgb__swing` at 0.629. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -20.98%; 20-day return is -17.29%; 20-day volatility is 7.63%; volume expansion is visible with volume ratio 2.18. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 2; rank-1 seller is YP; buyer dominance is 21.56%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer confirmation above prior close or controlled pullback/retest. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 163 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 23. TMPO — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.564074  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** TMPO is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.564. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -12.20%; 20-day return is -20.00%; 20-day volatility is 3.05%; volume expansion is visible with volume ratio 5.22. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.001; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 43.88%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 104 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 24. DIVA — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.563639  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** DIVA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.564. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -13.38%; 20-day return is -20.00%; 20-day volatility is 5.76%; volume ratio is neutral at 0.96. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 45.35%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 126 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 25. BIPI — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.559928  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** BIPI is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.560. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -16.36%; 20-day return is -33.81%; 20-day volatility is 6.26%; volume expansion is visible with volume ratio 2.01. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.007; rank-1 buyer is XL with streak 3; rank-1 seller is XL; buyer dominance is 16.00%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 170 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 26. KOKA — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.559691  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** KOKA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.560. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -19.59%; 20-day return is -39.29%; 20-day volatility is 5.58%; volume expansion is visible with volume ratio 3.32. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 48.40%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 111 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 27. IRSX — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.558329  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** IRSX is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.558. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -29.31%; 20-day return is -31.09%; 20-day volatility is 6.37%; volume expansion is visible with volume ratio 2.40. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.003; rank-1 buyer is XL with streak 2; rank-1 seller is XL; buyer dominance is 21.66%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 302 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 28. SCMA — position_xgb

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_position__multi_strategy_time__xgb__position` = 0.552487  
**Risk Flags:** DOMINANT_RANK1_BUYER  

**Trade thesis.** SCMA is selected by the **position_xgb** setup (position continuation / structural setup). The primary model evidence is `score_position__multi_strategy_time__xgb__position` at 0.552. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -10.57%; 20-day return is -21.99%; 20-day volatility is 3.33%; volume participation is still thin with volume ratio 0.58. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.000; rank-1 buyer is XL with streak 1; rank-1 seller is XL; buyer dominance is 24.59%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer close confirmation and stable liquidity rather than intraday spike. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 211 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 29. PBSA — ara_candidate

**Confidence:** Low-to-medium  
**Risk Grade:** Medium  
**Primary Score:** `score_ara` = 0.356804  
**Risk Flags:** BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** PBSA is selected by the **ara_candidate** setup (tactical event / watchlist). The primary model evidence is `score_ara` at 0.357. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -3.41%; 20-day return is -30.33%; 20-day volatility is 7.71%; volume expansion is visible with volume ratio 2.72. Behavioural context shows that broker flow is relatively balanced with net flow ratio 0.002; rank-1 buyer is AZ with streak 1; rank-1 seller is AZ; buyer dominance is 33.34%; daily share of the dominant buyer is 1.63%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Only after strong opening confirmation; avoid chasing failed gap-up moves. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; as a volatility-adjusted reference, thesis quality weakens materially around 782 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

### 30. SOTS — market_maker_silent_accum_defensive

**Confidence:** Low-to-medium  
**Risk Grade:** High  
**Primary Score:** `score_mm_silent` = 0.492582  
**Risk Flags:** DOMINANT_RANK1_BUYER|BELOW_EXECUTION_THRESHOLD  

**Trade thesis.** SOTS is selected by the **market_maker_silent_accum_defensive** setup (silent accumulation / liquidity behaviour). The primary model evidence is `score_mm_silent` at 0.493. The price/volume context indicates that price is still below the 20-day mean, so the setup needs stronger confirmation before execution; 5-day return is -15.56%; 20-day return is -22.05%; 20-day volatility is 10.53%; volume expansion is visible with volume ratio 1.52. Behavioural context shows that broker flow is relatively balanced with net flow ratio -0.001; rank-1 buyer is XL with streak 3; rank-1 seller is XL; buyer dominance is 47.50%; daily share of the dominant buyer is 35.08%; BDM confirmation is not present, so broker/price behaviour must carry the thesis.

**Execution plan.** Entry should not be treated as automatic at the open. Prefer retest or stable bid support after accumulation confirmation. A valid entry requires price to hold above the immediate support/retest area, liquidity to remain active, and the signal not to deteriorate into a failed breakout or liquidity trap during the first execution window.

**Invalidation / stop logic.** The setup is invalidated by a decisive breakdown below the 20-day mean or failure to reclaim it after a weak open; loss of momentum after entry, especially if price rejects the breakout/retest zone; broker behaviour turning distributive, such as dominant buyer disappearing or net flow flipping negative; excessive dependence on one broker continuing to dominate without broader participation; as a volatility-adjusted reference, thesis quality weakens materially around 699 if structure also breaks. Stop loss should be interpreted as thesis invalidation, not as an arbitrary number.

**Exit / take-profit logic.** Take profit should be based on market behaviour. Partial profit is preferred if the first impulse reaches a structural target but momentum begins to fade. Continuation can be held only if price accepts higher levels with stable liquidity and no abnormal rejection. Early exit is justified if the move becomes exhaustion-driven, volume spikes without continuation, or the probability of follow-through drops after a failed retest.

**No-trade condition.** No-trade is the correct decision if opening movement is purely gap-driven without confirmation, if liquidity disappears after the first move, or if risk flags dominate the setup more than the actual continuation evidence.

---

## Portfolio-Level Notes

Avoid forcing trades simply because a ticker appears in the report. Prioritize candidates whose thesis remains valid after the market opens, avoid concentration in the same dominant broker behaviour, and reduce exposure when multiple names depend on the same liquidity pattern. If market breadth weakens or volatility becomes abnormal, scale down position sizing or move signals to watchlist-only.