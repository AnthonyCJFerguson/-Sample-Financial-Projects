import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ticker = yf.Ticker("AAPL")
stock_data = ticker.history(period="5y")
stock_data.head()
stock_data['Close'].plot(figsize=(10,5), title="AAPL Stock Price (5 Years)")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.grid()
plt.show()
info = ticker.info

pe_ratio = info['trailingPE']
roe = info.get('returnOnEquity', None)
debt_to_equity = info.get('debtToEquity', None)

print(f"P/E Ratio: {pe_ratio}")
print(f"Return on Equity: {roe}")
print(f"Debt-to-Equity Ratio: {debt_to_equity}")
print("Comparison to Industry:")
print(f"P/E: {'Undervalued' if pe_ratio < 20 else 'Overvalued'}")
print(f"ROE: {'Strong' if roe and roe > 0.15 else 'Weak'}")
print(f"Debt/Equity: {'Low Risk' if debt_to_equity and debt_to_equity < 1.0 else 'High Risk'}")
if pe_ratio < 20 and roe > 0.15 and debt_to_equity < 1.0:
    print("✅ Investment Decision: BUY – Strong fundamentals and good value")
else:
    print("❌ Investment Decision: HOLD/AVOID – Does not meet key metrics")