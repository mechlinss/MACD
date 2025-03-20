from matplotlib import pyplot as plt


def price_plot(dates, values, title, buy_dates=None, buy_price=None, sell_dates=None, sell_price=None):
    plt.figure(figsize=(15, 7))
    plt.plot(dates, values, label="Price", color='b')
    if buy_price is not None and buy_dates is not None:
        plt.scatter(buy_dates, buy_price, color='green', marker='^', label='BUY', s=75, edgecolors='black', zorder=2)
    if sell_price is not None and sell_dates is not None:
        plt.scatter(sell_dates, sell_price, color='red', marker='v', label='SELL', s=75, edgecolors='black', zorder=2)
    plt.ylabel("Price [USD]")
    plt.xlabel("Date")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def macd_plot(dates, macd_values, signal_values, title, buy_dates=None, buy_price=None, sell_dates=None,
              sell_price=None):
    plt.figure(figsize=(15, 7))
    plt.plot(dates, macd_values, label="MACD", color='b')
    plt.plot(dates, signal_values, label="Signal", color='red')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
    if buy_price is not None and buy_dates is not None:
        plt.scatter(buy_dates, buy_price, color='green', marker='^', label='BUY', s=75, edgecolors='black', zorder=2)
    if sell_price is not None and sell_dates is not None:
        plt.scatter(sell_dates, sell_price, color='red', marker='v', label='SELL', s=75, edgecolors='black', zorder=2)
    plt.xlabel("Date")
    plt.ylabel("MACD/Signal Value")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def portfolio_plot(dates, values, title):
    plt.figure(figsize=(15, 7))
    plt.plot(dates, values, label="", color='green')
    plt.xlabel("Date")
    plt.ylabel("USD")
    plt.title(title)
    plt.grid(True)
    plt.show()
