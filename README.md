# Financial Time Series Analysis with MACD

> This project was created as part of the Numerical Methods course during the 4th semester of the Computer Science engineering program.

This Python project performs technical analysis on various financial instruments using the **MACD (Moving Average Convergence Divergence)** indicator. It generates trading signals, simulates investment performance, and visualizes key metrics using custom and built-in methods for exponential moving averages.

## Features

- Reads historical daily price data from `.csv` files.
- Calculates MACD and signal line using:
  - Custom Exponential Moving Average function
  - Built-in pandas `.ewm()` method
- Detects buy/sell signals based on MACD crossovers.
- Simulates an investor portfolio with initial capital.
- Plots:
  - Asset price chart
  - MACD and signal line
  - Buy/sell points
  - Portfolio value over time
  - Profit/loss per trade
 
## Libraries

- numpy
- pandas
- matplotlib
