import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Input stock symbol and period
symbol = input("Enter stock symbol (e.g., TCS.NS): ")
period = input("Enter period for analysis (e.g., 1y, 6mo): ")

# Fetch historical data
data = yf.download(symbol, period=period)['Adj Close']

# Calculate daily returns
daily_returns = data.pct_change().dropna()

# Calculate metrics
volatility = daily_returns.std() * np.sqrt(252)  # Annualized volatility
sharpe_ratio = (daily_returns.mean() / daily_returns.std()) * np.sqrt(252)  # Annualized Sharpe ratio

print(f"\nStock Risk Metrics for {symbol}:")
print(f"Annualized Volatility: {volatility*100:.2f}%")
print(f"Annualized Sharpe Ratio: {sharpe_ratio:.2f}")

# Plot daily returns and cumulative returns
plt.figure(figsize=(10,6))
plt.plot((1 + daily_returns).cumprod(), label='Cumulative Returns')
plt.title(f"{symbol} - Cumulative Returns Over {period}")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.legend()
plt.show()
