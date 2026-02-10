import numpy as np
from sentence_transformers import SentenceTransformer

POS = {"naik","menguat","positif","membaik","borong","akuisisi","katalis"}
NEG = {"turun","melemah","koreksi","jual","tekanan","rugi"}

def lexicon_features(texts):
    feats = []
    for t in texts:
        w = t.lower().split()
        p = sum(x in POS for x in w)
        n = sum(x in NEG for x in w)
        feats.append([(p-n)/max(len(w),1), p, n])
    return np.array(feats)

def indobert_embedding(texts, model_name="indolem/indobert-p2", device="cpu"):
    model = SentenceTransformer(model_name, device=device)
    return model.encode(texts, batch_size=16, show_progress_bar=True)
