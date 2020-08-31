import alpaca_trade_api as tradeapi
import requests





key_id = 'PKYO3MW4OLHKIUN5KNG4'
secret_key = 'zZNkwGnK6frktABeNjlrrieqyptawtF92j6AHB8X'
base_url = 'https://paper-api.alpaca.markets'
data_url = 'https://data.alpaca.markets'

api = tradeapi.REST(key_id, secret_key, base_url=base_url, api_version='v1')
account = api.get_account()
api._base_url = data_url

# Get daily price data for AAPL over the last 5 trading days.
barset = api.get_barset('AMZ', 'day', 1000, start='2017-02-15T22:30:00+09:00', end='2020-02-15T05:00:00+09:00')

# twitter time-zone과 맞춤. SEOUL -> UTC+09:00
INX_bars = barset['AMZ']

# See how much AAPL moved in that timeframe.
week_open = INX_bars[0].o
week_close = INX_bars[-1].c
percent_change = (week_close - week_open) / week_open * 100
print('S&P moved {}%  '.format(percent_change))