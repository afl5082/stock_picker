import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd

today = datetime.today().strftime('%Y-%m-%d')


def stock_growth(symbol, purchase_date):

    purchase_date_date = datetime.strptime(purchase_date, '%m/%d/%y')
    purchase_date_rf = purchase_date_date - timedelta(days=1)

    #should be user input

    #get data on ticker
    tickerData = yf.Ticker(symbol)
    tickerDF = tickerData.history(period='1d',
                                  start=purchase_date_rf,
                                  end=today)

    purchase_price = tickerDF.iloc[0]['Close']
    price_today = tickerDF.iloc[-1]['Close']

    price_list = []
    price_list.append(purchase_price)
    price_list.append(price_today)

    return price_list


def stock_recs():
    symbols = {
        'TSLA': ['Tesla'],
        'ZM': ['Zoom'],
        'SE': ['Sea Limited'],
        'NIO': ['NIO Limited'],
        'MRNA': ['Moderna, Inc.']
    }

    for key, value in symbols.items():
        tickerData = yf.Ticker(key)
        tickerDF = tickerData.history(period='1d', start='2019-1-1', end=today)

        purchase_price = tickerDF.iloc[0]['Close']
        today_price = tickerDF.iloc[-1]['Close']

        units_bought = 10000 / float(purchase_price)
        growth = round((units_bought * float(today_price)) - 10000, 0)

        value.append(int(growth))

    return symbols