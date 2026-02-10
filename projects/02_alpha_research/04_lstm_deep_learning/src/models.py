import torch
import torch.nn as nn

class HybridNet(nn.Module):
    def __init__(self, text_dim, price_dim):
        super().__init__()
        self.text = nn.Linear(text_dim, 256)
        self.price = nn.Linear(price_dim, 64)
        self.fc = nn.Linear(320, 128)
        self.cls = nn.Linear(128, 1)
        self.reg = nn.Linear(128, 3)

    def forward(self, t, p):
        x = torch.relu(self.text(t))
        y = torch.relu(self.price(p))
        z = torch.cat([x,y],1)
        z = torch.relu(self.fc(z))
        return torch.sigmoid(self.cls(z)), self.reg(z)
