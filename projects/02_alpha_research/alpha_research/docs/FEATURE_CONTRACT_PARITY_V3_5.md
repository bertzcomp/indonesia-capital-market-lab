# Feature Contract Parity v3.5

This patch fixes a schema drift found after real macro integration:

- `history`: 115 columns
- `live`: 145 columns

Root causes:

1. The feature store joined `data/raw_canonical/macro.parquet`, so engineered macro features from
   `data/features/macro/macro_features.parquet` were produced but not actually used in the model panel.
2. BDM history vector columns (`hist1`..`hist5`) only appeared when BDM rows existed in the feature date range.
   Because BDM starts in 2026, historical training stores ending in 2025 did not include those columns.

Fixes:

- `features/store.py` now loads engineered macro features first, falling back to raw macro only when needed.
- `features/contract.py` now defines a static, first-class contract for:
  - real macro raw columns
  - macro rolling features
  - macro regime/risk flags
  - full BDM base and history vector fields

After applying, rebuild both history and live feature stores and verify schema parity.
