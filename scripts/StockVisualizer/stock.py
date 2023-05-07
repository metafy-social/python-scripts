import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = input('Stock Symbol: ')
start_date = input('Start Date (YYYY-MM-DD): ')
end_date = input('End Date (YYYY-MM-DD): ')

stock = yf.Ticker(ticker)
df = stock.history(start=start_date, end=end_date)

plt.figure(figsize=(14, 8))
plt.plot(df['Close'])
plt.title(f'{ticker} Stock Price')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid()
plt.show()

