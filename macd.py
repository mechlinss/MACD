import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from visualization import *


def calculate_ema(n, data):
    alpha = 2 / (n + 1)
    result = np.zeros_like(close, dtype=float)
    result[0] = data[0]

    for i in range(1, len(data)):
        result[i] = (alpha * data[i] + (1 - alpha) * result[i - 1])

    return result


print("Type 1 for Ethereum")
print("Type 2 for Dogecoin")
choice = int(input("Your choice: "))
if choice == 1:
    extracted_data = pd.read_csv("data/eth_v_d.csv")
    choice = "Etherum"
elif choice == 2:
    extracted_data = pd.read_csv("data/doge_v_d.csv")
    choice = "Dogecoin"
else:
    pass

extracted_data["Data"] = pd.to_datetime(extracted_data["Data"])
date = extracted_data["Data"]
close = extracted_data[["Zamkniecie"]]
close = close.to_numpy()

price_plot(date, close, choice + " price over 3 years")
plt.savefig("plots/" + choice + "price.png")
plt.show()

macd = calculate_ema(12, close) - calculate_ema(26, close)
signal = calculate_ema(9, macd)

macd_plot(date, macd, signal, "MACD and Signal Line for " + choice)
plt.savefig("plots/" + choice + "_macd_signal.png")
plt.show()

buy_values = []
buy_dates = []
sell_values = []
sell_dates = []

for i in range(25, len(macd) - 1):
    if signal[i] > macd[i] and signal[i + 1] < macd[i + 1]:
        buy_values.append(macd[i + 1])
        buy_dates.append(date[i + 1])
    elif signal[i] < macd[i] and signal[i + 1] > macd[i + 1]:
        sell_values.append(macd[i + 1])
        sell_dates.append(date[i + 1])

macd_plot(date, macd, signal, "MACD and Signal Line with Buy/Sell Signals", buy_dates, buy_values, sell_dates,
          sell_values)
plt.savefig("plots/" + choice + "_macd_signal_buy_sell.png")
plt.show()

buy_price = []
sell_price = []

for i in range(len(date)):
    if date[i] in buy_dates:
        buy_price.append(close[i])
    elif date[i] in sell_dates:
        sell_price.append(close[i])

price_plot(date, close, choice + " price over 3 years", buy_dates, buy_price, sell_dates, sell_price)
plt.savefig("plots/" + choice + "_price_buy_sell.png")
plt.show()

cash = 1000 * close[0]
shares = 0
investment_portfolio = np.zeros_like(close, dtype=float)
profit = []
difference = 0
for i in range(len(close)):
    if date[i] in buy_dates:
        difference = investment_portfolio[i - 1]
        shares = shares + cash / close[i]
        cash = 0
    if date[i] in sell_dates:
        cash = cash + shares * close[i]
        shares = 0
        difference = (cash + shares * close[i]) - difference
        profit.append(difference)
    investment_portfolio[i] = cash + (shares * close[i])

portfolio_plot(date, investment_portfolio, "Value of investor's portfolio")
plt.savefig("plots/" + choice + "_portfolio.png")
plt.show()

profit = [p.item() for p in profit]

plt.figure(figsize=(10, 5))
plt.bar(range(1, len(profit) + 1), profit, color=['green' if p >= 0 else 'red' for p in profit])
plt.axhline(0, color='black', linewidth=1)
plt.text(len(profit) - 7, max(profit), f'Sum of transactions: {len(profit)}', fontsize=12)
plt.text(len(profit) - 7, max(profit) * 9 / 10, f'Profit: {len([p for p in profit if p > 0])}', fontsize=12)
plt.text(len(profit) - 7, max(profit) * 8 / 10, f'Loss: {len([p for p in profit if p < 0])}', fontsize=12)
plt.xticks(rotation=45)
plt.xlabel('Number of transaction')
plt.ylabel('USD')
plt.title('Trading Profit/Loss Chart')
plt.savefig("plots/" + choice + "_profit_loss.png")
plt.show()

#MACD with build-in ema
close_series = pd.Series(close.flatten())
ema12 = close_series.ewm(span=12, adjust=False).mean()
ema26 = close_series.ewm(span=26, adjust=False).mean()
macd = ema12 - ema26
signal = macd.ewm(span=9, adjust=False).mean()
macd_plot(date, macd, signal, "MACD and Signal Line from build-in functions")
plt.savefig("plots/" + choice + "_original_macd.png")
plt.show()
