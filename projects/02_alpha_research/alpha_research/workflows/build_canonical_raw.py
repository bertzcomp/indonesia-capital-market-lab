import argparse, json
from alpha_research.core.paths import ensure_dirs
from alpha_research.core.io import write_json
from alpha_research.canonical.builders import build_all_canonical
from alpha_research.macro.builder import build_macro_features

def main():
    ap = argparse.ArgumentParser(description="Build canonical raw tables, including real macro builder")
    ap.add_argument('--root', default='.')
    ap.add_argument('--start-date', required=True)
    ap.add_argument('--end-date', required=True)
    ap.add_argument('--skip-tradebook', action='store_true')
    ap.add_argument('--skip-macro', action='store_true')
    ap.add_argument('--macro-mode', choices=['auto','local','scrape','fallback'], default='auto')
    ap.add_argument('--force-macro', action='store_true')
    ap.add_argument('--bi-rate-path', default=None)
    ap.add_argument('--coal-fill-method', choices=['correlation','ffill'], default='correlation')
    ap.add_argument('--bps-api-key', default=None, help='Optional BPS API key for BI Rate download')
    ap.add_argument('--download-bi-rate', action='store_true', help='Download BI Rate JSON from BPS into data/raw/bps_bi_rate when local cache is missing')
    args = ap.parse_args()
    root = ensure_dirs(args.root)

    # Build all non-macro canonical tables first. Macro fallback can use canonical OHLCV if real macro fails.
    manifest = build_all_canonical(root, args.start_date, args.end_date, include_tradebook=not args.skip_tradebook, build_macro=False)
    if not args.skip_macro:
        macro_meta = build_macro_features(root, args.start_date, args.end_date, mode=args.macro_mode, force=args.force_macro, bi_rate_path=args.bi_rate_path, coal_fill_method=args.coal_fill_method, bps_api_key=args.bps_api_key, download_bps=args.download_bi_rate)
        manifest.setdefault('steps', []).append(macro_meta)
        manifest['macro_mode'] = args.macro_mode
        write_json(root/'data/raw_canonical/canonical_manifest.json', manifest)
    print(json.dumps(manifest, indent=2, default=str))

if __name__ == '__main__':
    main()