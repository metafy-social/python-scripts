import yfinance as yf
from stock import (
    get_df,
    plot,
    user_input,
    stock_visualizer
)

def test_df():
    stock = yf.Ticker("MSFT")
    assert (get_df(stock, "2023-01-01", "2023-02-01") != None)

def test_plot():
    stock = yf.Ticker("MSFT")
    df = get_df(stock, "2023-01-01", "2023-02-01")
    assert(plot(df, stock) != None)


