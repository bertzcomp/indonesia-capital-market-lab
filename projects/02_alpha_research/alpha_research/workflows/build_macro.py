import argparse, json
from alpha_research.core.paths import ensure_dirs
from alpha_research.macro.builder import build_macro_features

def main():
    ap = argparse.ArgumentParser(description="Build real macro canonical + macro feature tables")
    ap.add_argument('--root', default='.')
    ap.add_argument('--start-date', required=True)
    ap.add_argument('--end-date', required=True)
    ap.add_argument('--mode', choices=['auto','local','scrape','fallback'], default='auto', help='auto=local then scrape then fallback')
    ap.add_argument('--force', action='store_true')
    ap.add_argument('--bi-rate-path', default=None)
    ap.add_argument('--coal-fill-method', choices=['correlation','ffill'], default='correlation')
    ap.add_argument('--bps-api-key', default=None, help='Optional BPS API key for BI Rate download')
    ap.add_argument('--download-bi-rate', action='store_true', help='Download BI Rate JSON from BPS into data/raw/bps_bi_rate when local cache is missing')
    args = ap.parse_args()
    root = ensure_dirs(args.root)
    meta = build_macro_features(root, args.start_date, args.end_date, mode=args.mode, force=args.force, bi_rate_path=args.bi_rate_path, coal_fill_method=args.coal_fill_method, bps_api_key=args.bps_api_key, download_bps=args.download_bi_rate)
    print(json.dumps(meta, indent=2, default=str))

if __name__ == '__main__':
    main()
