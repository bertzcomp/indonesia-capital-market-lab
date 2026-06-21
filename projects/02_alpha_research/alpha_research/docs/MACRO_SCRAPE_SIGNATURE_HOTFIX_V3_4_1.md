# Macro Scrape Signature Hotfix v3.4.1

## Problem

`build_macro_features()` calls:

```python
_scrape_macro(start_date, end_date, coal_fill_method=coal_fill_method, bi_rate_path=bi_rate_path)
```

but `_scrape_macro()` expects:

```python
_scrape_macro(root, start, end, ...)
```

This causes:

```text
TypeError: _scrape_macro() missing 1 required positional argument: 'end'
```

## Fix

The call is changed to:

```python
_scrape_macro(root, start_date, end_date, coal_fill_method=coal_fill_method, bi_rate_path=bi_rate_path)
```

## Apply

From project root:

```bash
python3 tools/fix_macro_scrape_signature_v3_4_1.py --root .
```

Then rerun:

```bash
python3 workflows/build_macro.py \
  --root . \
  --start-date 2015-01-01 \
  --end-date 2026-05-13 \
  --mode scrape \
  --force \
  --download-bi-rate \
  --bps-api-key "$BPS_API_KEY"
```
