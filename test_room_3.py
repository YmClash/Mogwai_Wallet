import os
from mexc_sdk import Spot
from dotenv import load_dotenv
import json,pprint
import requests


load_dotenv()

client  = Spot(api_key=os.getenv('MEXC_ACCESS_KEY'), api_secret=os.getenv('MEXC_SECRET_KEY'))


def get_prix():
    url= "https://www.mexc.com/open/api/v2/market/ticker?symbol=BAJU_USDT"
    reponse = requests.get(url)
    data = reponse.json()
    # pprint.pprint(data)
    prix_baju = data['data'][0]['last']
    # print(data['data'][0]['last'])
    print(prix_baju)
    prix = float(prix_baju) * 1000
    print(type(prix))
    print(prix)




get_prix()
#
# exchange = client.ticker_price("BAJU/USD")
# pprint.pprint(exchange)