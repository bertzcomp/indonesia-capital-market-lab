import argparse, json
from alpha_research.training.registry import build_registry

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--run-id',default='latest'); ap.add_argument('--output',default='configs/model_registry.json')
    a=ap.parse_args(); print(json.dumps(build_registry(a.root,a.run_id,a.output),indent=2,default=str))
if __name__=='__main__': main()
