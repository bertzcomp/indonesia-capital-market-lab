# Architecture

The platform normalizes execution into four major graphs:

1. Historical research graph
2. Daily signal graph
3. Continual retraining graph
4. Evaluation/backtest graph

All components must use explicit manifests, registries, and canonical path contracts. Live feature generation never writes to historical feature directories.



## Monthly / quarterly retraining
```
1. update canonical raw
2. rebuild historical/continual feature dataset
3. apply maturity cutoff
4. train challenger model
5. backtest
6. forward test
7. monte carlo
8. promote kalau menang
```


daily inference        = model tetap
periodic retraining    = model baru dilatih ulang dari rolling window
model promotion        = hanya kalau challenger menang
online learning        = belum kita implementasikan, dan belum saya rekomendasikan untuk sekarang