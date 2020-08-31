import alpaca_trade_api as tradeapi
import requests

base_url = 'https://paper-api.alpaca.markets'
data_url = 'https://data.alpaca.markets/v1/bars/day'

headers = { 
    'APCA-API-KEY-ID': 'PKYO3MW4OLHKIUN5KNG4',
    'APCA-API-SECRET-KEY': 'zZNkwGnK6frktABeNjlrrieqyptawtF92j6AHB8X'
    
 }

payload = {'symbols' :'AMZ, AAPL', 'limit': 1000}


response = requests.get(data_url, headers=headers,params=payload)

print(response.text)




