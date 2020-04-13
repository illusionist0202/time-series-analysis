import time
#from datetime import datetime
import pandas as pd


def get_csv(stock_ticker,from_date, to_date):
    
    print('getting data...')
    url_add =f"https://query1.finance.yahoo.com/v7/finance/download/{stock_ticker}?period1={from_date}&period2={to_date}&interval=1d&events=history"
    data = pd.read_csv(url_add)
    print('writing to file...')
    data.to_csv(f"./data/{stock_ticker}.csv", index=False)
    print("Done!!")

get_csv(stock_ticker='TSLA', from_date=1277769600, to_date=int(time.time()))
