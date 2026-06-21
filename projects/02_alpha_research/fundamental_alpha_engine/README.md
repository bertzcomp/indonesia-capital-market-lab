# Fundamental Alpha Engine

Project ini adalah implementasi end-to-end untuk membangun sistem **Fundamental + Keystats + Insider Activity Alpha Engine** untuk saham IDX.

Sistem ini dirancang sebagai **conviction layer** dan **ticker filter**, bukan sebagai model entry intraday. Output utamanya adalah watchlist/ranking ticker dengan family signal seperti:

- `QUALITY_GROWTH`
- `VALUE_RERATING`
- `TURNAROUND_EARLY`
- `INSIDER_ACCUMULATION`
- `DIVIDEND_QUALITY`
- `BALANCE_SHEET_STRENGTH`
- `RED_FLAG_AVOID`

## 1. Struktur project

```text
fundamental_alpha_engine/
├── configs/
│   └── default_config.json
├── data/
│   ├── raw/
│   │   ├── financials/
│   │   ├── keystats_ratios/
│   │   ├── keystats_quarterly/
│   │   ├── keystats_dividends/
│   │   └── insider_activity/
│   ├── interim/
│   ├── features/
│   ├── labels/
│   └── signals/
├── models/
├── reports/
├── src/fae/
└── workflows/
```

## 2. Install environment

```bash
cd fundamental_alpha_engine
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

Atau install editable mode:

```bash
pip install -e .
```

## 3. Letakkan data raw

Masukkan file CSV Anda ke folder berikut:

```text
data/raw/financials/*.csv
data/raw/keystats_ratios/*.csv
data/raw/keystats_quarterly/*.csv
data/raw/keystats_dividends/*.csv
data/raw/insider_activity/*.csv
```

Minimal kolom yang didukung:

### Financials

```text
ticker,report_type_id,report_type_name,statement_type_id,statement_type_name,period_label,period_display,metric_name,metric_level,value_idr,value_usd,value_pct
```

### Keystats ratios

```text
ticker,category,metric_name,metric_id,value
```

### Keystats quarterly

```text
ticker,fitem_name,most_recent_quarter_date,most_recent_quarter_period,year,period,quarter_value,annualised_value,ttm_value,dividend,payout_ratio,dividend_yield
```

### Keystats dividends

```text
ticker,period,dividend,ex_date,payment_date
```

### Insider activity

```text
id,date,ticker,insider_name,action_type,shares_changed,shares_changed_pct,prev_shares,prev_pct,curr_shares,curr_pct,price,broker_code,broker_group,nationality,source_type,source_label
```

## 4. Run pipeline tanpa OHLCV

Mode ini cocok untuk live screener berbasis snapshot financials/keystats/insider.

```bash
python workflows/run_pipeline.py \
  --root . \
  --as-of-date 2026-06-12 \
  --top-n 50 \
  --min-score 55
```

Output utama:

```text
data/interim/*_clean.parquet
data/features/fundamental_signal_panel.parquet
data/features/fundamental_scorecard_panel.parquet
data/signals/fundamental_signals.parquet
data/signals/fundamental_signals.csv
reports/data_quality_report.json
```

## 5. Run pipeline dengan OHLCV

Jika Anda punya OHLCV historical, gunakan ini agar sistem dapat membuat market features, forward labels, dan optional ML model.

OHLCV minimal:

```text
ticker,date,open,high,low,close,volume
```

Command:

```bash
python workflows/run_pipeline.py \
  --root . \
  --as-of-date 2026-06-12 \
  --ohlcv data/raw/ohlcv/ohlcv.parquet \
  --top-n 50 \
  --min-score 55
```

Jika ada sector mapping:

```bash
python workflows/run_pipeline.py \
  --root . \
  --as-of-date 2026-06-12 \
  --ohlcv data/raw/ohlcv/ohlcv.parquet \
  --sector data/raw/sectors/sectors.csv \
  --top-n 50 \
  --min-score 55
```

Sector mapping minimal:

```text
ticker,sector,subsector
```

Sistem juga mendukung nama kolom IDX/listed-company master, baik CSV/parquet maupun JSON dengan root key `data`:

```text
KodeEmiten,Sektor,SubSektor,Industri,SubIndustri,NamaEmiten,PapanPencatatan,TanggalPencatatan
```

Contoh path JSON IDX:

```bash
--sector data/raw/sectors/listed_companies.json
```

## 6. Train optional ML model

Jika OHLCV tersedia dan label sudah bisa dibuat:

```bash
python workflows/run_pipeline.py \
  --root . \
  --as-of-date 2026-06-12 \
  --ohlcv data/raw/ohlcv/ohlcv.parquet \
  --train \
  --target label_outperform_market_60d \
  --top-n 50 \
  --min-score 55
```

Jika menggunakan sector mapping, target yang lebih tepat biasanya:

```bash
--target label_outperform_sector_60d
```

Model tersimpan di:

```text
models/fundamental_model/model.joblib
models/fundamental_model/features.json
models/fundamental_model/training_report.json
```

## 7. Menjalankan workflow satu per satu

### Step 1 - Clean data

```bash
python workflows/01_clean_fundamental_data.py \
  --root . \
  --as-of-date 2026-06-12
```

### Step 2 - Build features

```bash
python workflows/02_build_features.py \
  --root . \
  --ohlcv data/raw/ohlcv/ohlcv.parquet \
  --sector data/raw/sectors/listed_companies.json
```

### Step 3 - Build labels

```bash
python workflows/03_build_labels.py \
  --root . \
  --ohlcv data/raw/ohlcv/ohlcv.parquet \
  --sector data/raw/sectors/listed_companies.json
```


## Step 3 — Build redesigned labels
```bash
python workflows/03_build_labels.py \
  --root . \
  --ohlcv data/raw/ohlcv/ohlcv.parquet \
  --sector data/raw/sectors/listed_companies.json \
  --bad-drawdown-threshold 0.15 \
  --takeprofit-threshold 0.20
```


### Step 4 - Train model

```bash
python workflows/04_train_model.py \
  --root . \
  --target label_outperform_sector_60d
```

## Step 4 — Train redesigned model stack
```bash
python workflows/04_train_model_v2.py \
  --root . \
  --horizon 60 \
  --model-dir models/fundamental_model_v2
```

walk-forward diagnostics:
```bash
python workflows/04_train_model_v2.py \
  --root . \
  --horizon 60 \
  --model-dir models/fundamental_model_v2 \
  --walkforward \
  --purge-days 60
```

## Generate v2 signals

Hybrid:
```bash
python workflows/05_generate_signals_v2.py \
  --root . \
  --as-of-date 2026-06-12 \
  --model-dir models/fundamental_model_v2 \
  --score-mode hybrid \
  --mode research_all \
  --top-n 50 \
  --min-score 55 \
  --save-named-copy
```

Scorecard-only:
```bash
python workflows/05_generate_signals_v2.py \
  --root . \
  --as-of-date 2026-06-12 \
  --model-dir models/fundamental_model_v2 \
  --score-mode scorecard \
  --mode research_all \
  --top-n 50 \
  --min-score 55 \
  --save-named-copy
```

Model-only:
```bash
python workflows/05_generate_signals_v2.py \
  --root . \
  --as-of-date 2026-06-12 \
  --model-dir models/fundamental_model_v2 \
  --score-mode model \
  --mode research_all \
  --top-n 50 \
  --min-score 55 \
  --save-named-copy
```

## Top-k backtest

Scorecard-only:
```bash
python workflows/06_backtest_topk_signals.py \
  --root . \
  --score-col fundamental_score \
  --return-col fwd_excess_sector_60d \
  --mode research_all \
  --top-k 10 20 50 \
  --output reports/topk_scorecard_60d.csv
```

Hybrid:
```bash
python workflows/06_backtest_topk_signals.py \
  --root . \
  --model-dir models/fundamental_model_v2 \
  --score-col final_alpha_score_v2 \
  --return-col fwd_excess_sector_60d \
  --mode tradable \
  --top-k 10 20 50 \
  --output reports/topk_hybrid_tradable_60d.csv
```

Model-only:
```bash
python workflows/06_backtest_topk_signals.py \
  --root . \
  --model-dir models/fundamental_model_v2 \
  --score-col ml_alpha_score \
  --return-col fwd_excess_sector_60d \
  --mode tradable \
  --top-k 10 20 50 \
  --output reports/topk_model_tradable_60d.csv
```

## 8. Output signal

Kolom output utama:

```text
as_of_date
ticker
sector
subsector
final_alpha_score
fundamental_score
quality_score
growth_score
valuation_score
insider_score
balance_sheet_score
dividend_score
risk_penalty
signal_family
conviction
reason_codes
action
```

Contoh interpretasi:

```text
signal_family = VALUE_RERATING;INSIDER_ACCUMULATION
conviction = HIGH
action = ADD_TO_WATCHLIST_AND_WAIT_TECH_CONFIRMATION
```

Artinya ticker tersebut layak masuk watchlist, tetapi entry tetap perlu dikonfirmasi oleh technical/broker-flow/news engine.

## 9. Catatan desain penting

### Point-in-time policy

Financial statement tidak selalu tersedia pada `period_end_date`. Karena sample belum punya `published_date`, sistem memakai conservative lag:

- Quarterly: `period_end_date + 60 days`
- Annual: `period_end_date + 120 days`
- TTM/LTM: `period_end_date + 7 days`

Konfigurasi ini ada di:

```text
configs/default_config.json
```

Jika Anda nanti punya `published_date` atau `filing_date`, sebaiknya parser diubah agar memakai tanggal aktual tersebut.

### Keystats ratios

Jika `keystats_ratios` hanya current snapshot, gunakan untuk inference/live screener. Jangan gunakan untuk backtest historis kecuali Anda punya arsip snapshot historis.

### Insider activity

Action handling awal:

- `BUY` = positive
- `SELL` = negative
- `TRANSFER` = neutral
- `CROSS` = neutral

Fitur insider dibuat dalam window:

```text
7D, 14D, 30D, 60D, 90D, 180D
```

## 10. Cara integrasi dengan sistem alpha lama

Output `data/signals/fundamental_signals.csv` bisa dijoin ke signal lama berdasarkan:

```text
ticker,date/as_of_date
```

Rekomendasi final score gabungan:

```text
final_combined_score =
    0.30 * fundamental_score
  + 0.20 * technical_score
  + 0.20 * broker_flow_score
  + 0.15 * insider_score
  + 0.10 * news_event_score
  + 0.05 * liquidity_score
  - risk_penalty
```

Bobot ini baseline awal dan harus diuji ulang lewat walk-forward validation.

## 11. Batasan versi awal

Versi ini sudah end-to-end, tetapi masih baseline production prototype. Batasan utama:

1. Belum memakai actual `published_date` financial statement.
2. Keystats dianggap snapshot per `--as-of-date`.
3. ML model hanya optional; scorecard adalah baseline utama.
4. Feature alias financials masih berbasis mapping umum dari sample; untuk full dataset perlu audit metric dictionary.
5. Sector-relative scoring akan lebih kuat jika sector mapping tersedia.


....................................................................................................................................................................................

Done. Model stack saved to: models/fundamental_model_v2
Feature count: 161
Keystats included: []
Score components included: ['quality_score', 'growth_score', 'valuation_score', 'insider_score', 'balance_sheet_score', 'dividend_score', 'liquidity_score', 'risk_penalty', 'fundamental_score']
Model diagnostics: {'return_ranker': {'target': 'fwd_risk_adjusted_excess_sector_60d', 'model_type': 'regressor', 'rows': 1843456, 'train_rows': 1474764, 'valid_rows': 368692, 'valid_mae': 0.3322770223244172, 'valid_r2': -0.055379928407098156, 'valid_rank_corr': 0.11026800464934351, 'walkforward': [{'valid_year': 2016, 'train_rows': 96606, 'valid_rows': 120776, 'mae': 0.23623485679375533, 'r2': -0.25066909325823183, 'rank_corr': 0.014391490261558155}, {'valid_year': 2017, 'train_rows': 216716, 'valid_rows': 130266, 'mae': 0.22603315773015334, 'r2': -0.09692229473620517, 'rank_corr': 0.07776387097691552}, {'valid_year': 2018, 'train_rows': 345211, 'valid_rows': 145635, 'mae': 0.20176610534228787, 'r2': 0.007750717500646154, 'rank_corr': 0.12217886570477447}, {'valid_year': 2019, 'train_rows': 488450, 'valid_rows': 157962, 'mae': 0.40068570375586493, 'r2': -0.00306822198310841, 'rank_corr': 0.09905740478938281}, {'valid_year': 2020, 'train_rows': 646114, 'valid_rows': 165807, 'mae': 0.35752286749752177, 'r2': -0.666770214470465, 'rank_corr': 0.09037933201556832}, {'valid_year': 2021, 'train_rows': 808624, 'valid_rows': 180422, 'mae': 0.2909213210101326, 'r2': -0.08658991615529232, 'rank_corr': 0.13622476944438894}, {'valid_year': 2022, 'train_rows': 984782, 'valid_rows': 193293, 'mae': 0.21798854906189538, 'r2': -0.34183291085727086, 'rank_corr': 0.16681253462879017}, {'valid_year': 2023, 'train_rows': 1175372, 'valid_rows': 203360, 'mae': 0.28264443783724413, 'r2': -4.990352474335315, 'rank_corr': 0.11747492253864679}, {'valid_year': 2024, 'train_rows': 1378819, 'valid_rows': 218088, 'mae': 0.2998361473141344, 'r2': -0.049322067826751415, 'rank_corr': 0.08496615437468277}, {'valid_year': 2025, 'train_rows': 1597205, 'valid_rows': 172763, 'mae': 0.3735467235843426, 'r2': -0.038019918227527816, 'rank_corr': 0.14446662460600018}, {'valid_year': 2026, 'train_rows': 1766992, 'valid_rows': 38704, 'mae': 0.24576262797487405, 'r2': -0.09482883129995656, 'rank_corr': 0.2504637648567273}]}, 'outperform_classifier': {'target': 'label_outperform_sector_60d', 'model_type': 'classifier', 'rows': 1950376, 'train_rows': 1560300, 'valid_rows': 390076, 'valid_positive_rate': 0.17930608394261632, 'valid_roc_auc': 0.5466958349914106, 'valid_avg_precision': 0.20446640692072354, 'walkforward': [{'valid_year': 2016, 'train_rows': 96606, 'valid_rows': 120776, 'positive_rate': 0.26731304232629, 'roc_auc': 0.47381430615006936, 'avg_precision': 0.2514391044659008}, {'valid_year': 2017, 'train_rows': 216716, 'valid_rows': 130266, 'positive_rate': 0.24659542781692845, 'roc_auc': 0.5624865164718542, 'avg_precision': 0.29380083243754695}, {'valid_year': 2018, 'train_rows': 345211, 'valid_rows': 145635, 'positive_rate': 0.28216431489683114, 'roc_auc': 0.5636947593217994, 'avg_precision': 0.3274239292889575}, {'valid_year': 2019, 'train_rows': 488450, 'valid_rows': 157962, 'positive_rate': 0.23954495384966004, 'roc_auc': 0.5753754174392999, 'avg_precision': 0.2875088005177153}, {'valid_year': 2020, 'train_rows': 646114, 'valid_rows': 165807, 'positive_rate': 0.3117118095134705, 'roc_auc': 0.5635930284210336, 'avg_precision': 0.3767320841414871}, {'valid_year': 2021, 'train_rows': 808624, 'valid_rows': 180422, 'positive_rate': 0.2481681834809502, 'roc_auc': 0.5631235897019911, 'avg_precision': 0.2693171342081132}, {'valid_year': 2022, 'train_rows': 984782, 'valid_rows': 193293, 'positive_rate': 0.27941001484792516, 'roc_auc': 0.5419974042208189, 'avg_precision': 0.3070667383585689}, {'valid_year': 2023, 'train_rows': 1175372, 'valid_rows': 203360, 'positive_rate': 0.2967053501180173, 'roc_auc': 0.5547046456574336, 'avg_precision': 0.33293475174629816}, {'valid_year': 2024, 'train_rows': 1378819, 'valid_rows': 218088, 'positive_rate': 0.27949268185319687, 'roc_auc': 0.552874998373503, 'avg_precision': 0.3214982251661506}, {'valid_year': 2025, 'train_rows': 1597205, 'valid_rows': 223043, 'positive_rate': 0.1895777944163233, 'roc_auc': 0.5748154297679027, 'avg_precision': 0.23180102387713927}, {'valid_year': 2026, 'train_rows': 1817272, 'valid_rows': 95344, 'positive_rate': 0.13519466353415002, 'roc_auc': 0.3949493431728056, 'avg_precision': 0.10491800167946466}]}, 'downside_risk_classifier': {'target': 'label_bad_drawdown_60d', 'model_type': 'classifier', 'rows': 1960185, 'train_rows': 1568148, 'valid_rows': 392037, 'valid_positive_rate': 0.35998132829299273, 'valid_roc_auc': 0.7475958669770769, 'valid_avg_precision': 0.5953217951855603, 'walkforward': [{'valid_year': 2016, 'train_rows': 96606, 'valid_rows': 120776, 'positive_rate': 0.21920745843545075, 'roc_auc': 0.6367167663219415, 'avg_precision': 0.29852792270393436}, {'valid_year': 2017, 'train_rows': 216716, 'valid_rows': 130266, 'positive_rate': 0.2508712941212596, 'roc_auc': 0.7024980887460506, 'avg_precision': 0.4141951908498915}, {'valid_year': 2018, 'train_rows': 345211, 'valid_rows': 145635, 'positive_rate': 0.296165070209771, 'roc_auc': 0.6888079671488958, 'avg_precision': 0.47308923088746874}, {'valid_year': 2019, 'train_rows': 488450, 'valid_rows': 157962, 'positive_rate': 0.33582127347083474, 'roc_auc': 0.7296329946444056, 'avg_precision': 0.5637899497622558}, {'valid_year': 2020, 'train_rows': 646114, 'valid_rows': 168029, 'positive_rate': 0.3353944854757214, 'roc_auc': 0.7366564277846037, 'avg_precision': 0.5439094195561565}, {'valid_year': 2021, 'train_rows': 810552, 'valid_rows': 181980, 'positive_rate': 0.28578964721397954, 'roc_auc': 0.761105837650321, 'avg_precision': 0.520139614531629}, {'valid_year': 2022, 'train_rows': 988304, 'valid_rows': 194757, 'positive_rate': 0.3101146556991533, 'roc_auc': 0.795425320668878, 'avg_precision': 0.6193698915194713}, {'valid_year': 2023, 'train_rows': 1180358, 'valid_rows': 204593, 'positive_rate': 0.3061834960140376, 'roc_auc': 0.7640826731024832, 'avg_precision': 0.5752851388621714}, {'valid_year': 2024, 'train_rows': 1385101, 'valid_rows': 219067, 'positive_rate': 0.3429087904613657, 'roc_auc': 0.6905209158729015, 'avg_precision': 0.5334220058909285}, {'valid_year': 2025, 'train_rows': 1604483, 'valid_rows': 224901, 'positive_rate': 0.2583492292164108, 'roc_auc': 0.7536813749486986, 'avg_precision': 0.5018102929380819}, {'valid_year': 2026, 'train_rows': 1826086, 'valid_rows': 95839, 'positive_rate': 0.5781884201629817, 'roc_auc': 0.7625631936680874, 'avg_precision': 0.7764283963273059}]}}