import torch
import torch.nn as nn

class NewsPriceLSTM(nn.Module):
    def __init__(self, text_dim=768, price_dim=5, lstm_hidden=64):
        super().__init__()

        self.text_proj = nn.Sequential(
            nn.Linear(text_dim, 256),
            nn.ReLU(),
            nn.Dropout(0.2)
        )

        self.lstm = nn.LSTM(
            input_size=price_dim,
            hidden_size=lstm_hidden,
            batch_first=True
        )

        self.fusion = nn.Sequential(
            nn.Linear(256 + lstm_hidden, 256),
            nn.ReLU(),
            nn.Dropout(0.2)
        )

        # heads
        self.prob_head = nn.Linear(256, 1)
        self.reg_head = nn.Linear(256, 9)  
        # (H3 q10,q50,q90 | H5 | H7)

    def forward(self, text_emb, price_seq):
        t = self.text_proj(text_emb)
        _, (h, _) = self.lstm(price_seq)
        p = h[-1]
        x = self.fusion(torch.cat([t, p], dim=1))
        prob = torch.sigmoid(self.prob_head(x))
        reg = self.reg_head(x)
        return prob, reg
