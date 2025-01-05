import pandas as pd
import yfinance as yf

def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetches historical stock data from Yahoo Finance.
    
    :param symbol: The stock symbol to fetch data for.
    :param start_date: The start date of the data in 'YYYY-MM-DD' format.
    :param end_date: The end date of the data in 'YYYY-MM-DD' format.
    :return: A pandas DataFrame containing the stock data.
    """
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data
def calculate_portfolio_metrics(df):
    """
    Calculates relevant metrics like daily returns and portfolio balance.
    
    :param df: DataFrame containing stock data.
    :return: Updated DataFrame with new metrics.
    """
    df['Daily Return'] = df['Adj Close'].pct_change()
    return df
import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_trends(df, title):
    """
    Plots stock price trends.
    
    :param df: DataFrame containing stock data.
    :param title: Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df['Adj Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.show()
