import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_ema(n, data):
    alpha = 2 / (n + 1)
    result = np.nan * np.zeros_like(data)
    result[0] = data[0]

    for i in range(1, len(data)):
        result[i] = (alpha * data[i] + (1 - alpha) * result[i - 1])

    return result

extracted_data = pd.read_csv("data/eth_v_d.csv")

extracted_data["Data"] = pd.to_datetime(extracted_data["Data"])
date = extracted_data["Data"]
close = extracted_data[["Zamkniecie"]]

plt.figure(figsize=(15, 7))
plt.plot(date, close.values, color='b')
plt.ylabel("Price [USD]")
plt.xlabel("Date")
plt.title("Ethereum price over 3 years")
plt.grid(True)
plt.show()

macd = calculate_ema(12, close.to_numpy()) - calculate_ema(26, close.to_numpy())
signal = calculate_ema(9, macd)

plt.figure(figsize=(15, 7))
plt.plot(date, macd, label="MACD", color='b')
plt.plot(date, signal, label="SIGNAL", color='r')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.xlabel("Date")
plt.ylabel("MACD/Signal Value")
plt.title("MACD and Signal Line for ETH")
plt.legend()
plt.grid(True)
plt.show()

buy_values = []
buy_dates = []
sell_values = []
sell_dates = []

for i in range(0, len(macd) - 1):
    if signal[i] > macd[i] and signal[i + 1] < macd[i + 1]:
        buy_values.append(macd[i + 1])
        buy_dates.append(date[i + 1])
    elif signal[i] < macd[i] and signal[i + 1] > macd[i + 1]:
        sell_values.append(macd[i + 1])
        sell_dates.append(date[i + 1])


plt.figure(figsize=(15, 7))
plt.plot(date, macd, label="MACD", color='b')
plt.plot(date, signal, label="Signal", color='orange')
plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
plt.scatter(buy_dates, buy_values, color='green', marker='^', label='BUY', s=75)
plt.scatter(sell_dates, sell_values, color='red', marker='v', label='SELL', s=75)
plt.xlabel("Date")
plt.ylabel("MACD/Signal Value")
plt.title("MACD and Signal Line with Buy/Sell Signals")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(15, 7))
plt.plot(date, close.values, color='b')
plt.scatter(buy_dates, buy_values, color='green', marker='^', label='BUY', s=75)
plt.scatter(sell_dates, sell_values, color='red', marker='v', label='SELL', s=75)
plt.ylabel("Price [USD]")
plt.xlabel("Date")
plt.title("Ethereum price over 3 years")
plt.grid(True)
plt.show()

print(date.head())