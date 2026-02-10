import torch
from torch.utils.data import DataLoader
from models_lstm import NewsPriceLSTM
from datasets import NewsPriceDataset

def train_walk_forward(
    splits, device="cpu", epochs=10, lr=1e-3
):
    all_results = []

    for fold, (train_data, test_data) in enumerate(splits):
        model = NewsPriceLSTM().to(device)
        opt = torch.optim.Adam(model.parameters(), lr=lr)

        train_loader = DataLoader(train_data, batch_size=32, shuffle=False)

        for ep in range(epochs):
            model.train()
            for t_emb, p_seq, y_prob, y_reg in train_loader:
                t_emb, p_seq = t_emb.to(device), p_seq.to(device)
                y_prob, y_reg = y_prob.to(device), y_reg.to(device)

                prob_hat, reg_hat = model(t_emb, p_seq)

                loss_prob = torch.nn.functional.binary_cross_entropy(
                    prob_hat.squeeze(), y_prob
                )

                loss_reg = (
                    quantile_loss(reg_hat[:,0], y_reg[:,0], 0.1) +
                    quantile_loss(reg_hat[:,1], y_reg[:,0], 0.5) +
                    quantile_loss(reg_hat[:,2], y_reg[:,0], 0.9)
                )

                loss = loss_prob + loss_reg
                opt.zero_grad()
                loss.backward()
                opt.step()

        model.eval()
        all_results.append(model)

    return all_results
