import numpy as np
import torch
from torch.utils.data import Dataset

class NewsPriceDataset(Dataset):
    def __init__(self, text_emb, price_seq, y_prob, y_reg):
        self.text_emb = torch.tensor(text_emb, dtype=torch.float32)
        self.price_seq = torch.tensor(price_seq, dtype=torch.float32)
        self.y_prob = torch.tensor(y_prob, dtype=torch.float32)
        self.y_reg = torch.tensor(y_reg, dtype=torch.float32)

    def __len__(self):
        return len(self.text_emb)

    def __getitem__(self, idx):
        return (
            self.text_emb[idx],
            self.price_seq[idx],
            self.y_prob[idx],
            self.y_reg[idx],
        )
