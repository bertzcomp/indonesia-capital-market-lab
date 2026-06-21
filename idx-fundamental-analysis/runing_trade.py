from providers.stockbit import StockBit
import csv, os
from datetime import datetime

sb = StockBit(stocks=["BBRI"])
trades = sb.get_running_trade_batches(max_scroll=10, delay=0.4, debug=True)

print(f"Collected {len(trades)} trades")

if trades:
    os.makedirs("data/rt", exist_ok=True)
    filename = f"data/rt/running_trade_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(trades[0].keys()))
        writer.writeheader()
        writer.writerows(trades)
    print("Saved to", filename)
else:
    print("No trade data to save.")