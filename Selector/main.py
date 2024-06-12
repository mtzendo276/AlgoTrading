# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np

import yfinance as yf
import mplfinance as mpf
import matplotlib.pyplot as plt
from tradingview_ta import TA_Handler, Interval, Exchange
from datetime import datetime, timedelta

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tickers = ['YPF',
               'BBAR',
               'GGAL',
               'MELI',
               'SUPV',
               'BMA',
               'DESP',
               'LOMA',
               'PAM',
               'CEPU',
               'TGS',
               'TEO',
               'BIOX',
               'CRESY',
               'IRS',
               'EDN']
    tickers_data = []
    # Iterate through each ticker
    for ticker in tickers:
        print(ticker)
        try:
            data = TA_Handler(
                symbol=ticker,
                screener='america',
                exchange='NYSE',
                interval='1d'
            )
            data = data.get_analysis().summary
            tickers_data.append(data)

        except Exception as e:
            # If no data is found for the ticker in NYSE, search in NASDAQ
            print(f"no data found for ticker { ticker } in NYSE. Searching in NASDAQ...")
            data = TA_Handler(
                symbol=ticker,
                screener='america',
                exchange='NASDAQ',
                interval='1d'
            )
            data = data.get_analysis().summary
            tickers_data.append(data)

    print('Data successfully imported')

    recommendations = []
    buys = []
    sells = []
    neutrals = []

    # Iterate through each data in tickers_data
    for data in tickers_data:
        recommendation = data.get('RECOMMENDATION')
        buy = data.get('BUY')
        sell = data.get('SELL')
        neutral = data.get('NEUTRAL')

        recommendations.append(recommendation)
        buys.append(buy)
        sells.append(sell)
        neutrals.append(neutral)

    data = {
        'Ticker': tickers,
        'Recommendations': recommendations,
        'Buys': buys,
        'Sells': sells,
        'Neutrals': neutrals
    }

    df = pd.DataFrame(data)

    # Define the order of categories
    order_categories = {
        'STRONG_BUY': 5,
        'BUY': 4,
        'NEUTRAL': 3,
        'SELL': 2,
        'STRONG-SELL': 1
    }

    #assign a numerical value to each category in a new column "order"
    df['Order'] = df






