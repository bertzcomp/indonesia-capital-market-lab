# Real Macro Builder v3.3

This patch replaces the market-only fallback default with a first-class macro builder based on the original notebook logic:

- Frankfurter API: `idr_usd`, derived `usd_idr`
- yfinance: WTI `CL=F`, Brent `BZ=F`, Coal proxy `KOL`, IHSG `^JKSE`
- BI rate: local file if provided, otherwise hardcoded historical event table
- Coal gap: correlation-to-Brent fill by default
- Engineered macro features: FX/oil/coal/rate/market regime features

## Commands

Build macro only:

```bash
python3 workflows/build_macro.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13 \
  --mode auto \
  --force
```

Force real scraping and fail if scraping fails:

```bash
python3 workflows/build_macro.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13 \
  --mode scrape \
  --force
```

Build canonical raw including macro:

```bash
python3 workflows/build_canonical_raw.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13 \
  --macro-mode auto \
  --force-macro
```

`auto` means: use valid local macro first, otherwise try scrape, otherwise fallback market-derived macro with `macro_missing_flag=1`.

If you want strict production behavior, use `--macro-mode scrape` so the command fails when external macro cannot be fetched.
