import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
API_KEY = os.getenv('COINMARKKETCAP_API_KEY')



crypto_symbol = 'BTC'
convert_symbol = 'USD'

url = f'https://sandbox-api.coinmarketcap.com/v2/tools/price-conversion'
headers = {
'X-CMC_PRO_API_KEY': API_KEY
}
params = {'amount': 100,
          'symbol': crypto_symbol,
          'convert':convert_symbol

          }

response = requests.get(url,headers=headers,params=params)
data = json.loads(response.text)
print(data)
if 'data' in data:
    quote = data['data'][0]['quote'][convert_symbol]
    print(quote['price'])


print(data)
