import argparse, json
from alpha_research.features.store import build_feature_store
from alpha_research.labels.builder import build_training_dataset
from alpha_research.validation.folds import build_folds
from alpha_research.training.trainer import train_models
from alpha_research.training.registry import build_registry

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',default='.'); ap.add_argument('--start-date',required=True); ap.add_argument('--end-date',required=True); ap.add_argument('--fold-set',default='yearly'); ap.add_argument('--families',default='sm_tracker,ara_predictor,multi_strategy_time'); ap.add_argument('--algos',default='hgb,rank_hgb,regime_hgb')
    a=ap.parse_args();
    out={}
    out['features']=build_feature_store(a.root,a.start_date,a.end_date,'history')
    out['dataset']=build_training_dataset(a.root,'history',a.start_date,a.end_date)
    out['folds']=build_folds(a.root,'year',a.fold_set,2018,int(a.end_date[:4]))
    out['training']=train_models(a.root,a.fold_set,a.families.split(','),a.algos.split(','))
    out['registry']=build_registry(a.root,out['training']['run_id'],'configs/model_registry.json')
    print(json.dumps(out,indent=2,default=str))
if __name__=='__main__': main()
