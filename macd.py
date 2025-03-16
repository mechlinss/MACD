import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_ema(N, data):
    alpha = 2/(N + 1)
    factors = (1 - alpha) ** np.arange(N + 1)
    factors = factors[::-1]
    result = np.nan * np.zeros_like(data)
    for i in range(N, len(data)):
        result[i] = np.sum(data[i - N:i + 1] * factors) / factors.sum()
    return result

extracted_data = pd.read_csv("data/eth_v_d.csv")

extracted_data["Data"] = pd.to_datetime(extracted_data["Data"])
date = extracted_data[["Data"]]
close = extracted_data[["Zamkniecie"]]

plt.plot(date, close, color='b')
plt.ylabel("Price [USD]")
plt.xlabel("Date")
plt.title("Ethereum price in 3 years period")
plt.grid(True)
plt.show()

macd = calculate_ema(data['Close'].to_numpy(), 12) - calculate_ema(data['Close'].to_numpy(), 26)
signal = calculate_ema(macd, 9)

data.insert(0, 'MACD', macd, allow_duplicates=True)
data.insert(1, 'Signal', signal, allow_duplicates=True)

# Select last 1000 records
data = data[-1000:]

plt.figure().set_figwidth(15)
plt.plot(data['Date'], data['Close'], label=STOCK_NAME)
plt.xlabel('Data')
plt.ylabel(f'Cena [{STOCK_CURRENCY}]')
plt.title(f'{PLOT_TITLE} od {data.iloc[0]["Date"].date()} do {data.iloc[-1]["Date"].date()}')
plt.legend()
plt.savefig(f'{IMAGES_PATH}part_pln.png', bbox_inches='tight')
plt.show()

print(date.head())