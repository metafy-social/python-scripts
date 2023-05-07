import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def get_df(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)  
    return df

def plot(df, ticker):
    plt.figure(figsize=(14, 8))
    plt.plot(df['Close'])
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid()
    plt.show()

def user_input():
    ticker = input('Stock Symbol: ')
    start_date = input('Start Date (YYYY-MM-DD): ')
    end_date = input('End Date (YYYY-MM-DD): ')
    return ticker, start_date, end_date

def stock_visualizer():
    ticker, start_date, end_date = user_input()
    df = get_df(ticker, start_date, end_date)
    plot(df, ticker)





