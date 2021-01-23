import yfinance as yf
from datetime import datetime, timedelta

today = datetime.today().strftime('%Y-%m-%d')

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
