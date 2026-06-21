import argparse, json
from alpha_research.core.paths import ensure_dirs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--create',action='store_true')
    a=ap.parse_args(); root=ensure_dirs(a.root)
    print(json.dumps({"root":str(root),"created":True},indent=2))
if __name__=='__main__': main()
