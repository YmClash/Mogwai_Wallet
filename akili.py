import requests
from flask import Flask,request,jsonify
from substrateinterface import SubstrateInterface
from dotenv import load_dotenv
from decimal import Decimal,getcontext
from mexc_sdk import Spot
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import pprint


load_dotenv("COINMARKKETCAP_API_KEY")
mexc_client = Spot(api_key=os.getenv('MEXC_ACCESS_KEY'),api_secret=os.getenv('MEXC_SECRET_KEY'))

rpc_url = SubstrateInterface(url="wss://rpc-parachain.bajun.network")

app = Flask(__name__)

# address = "bUMs9SouUoy36GFV4rzrUyVkKG1rTZkGBYrLMhbXUBumuTuck"

# @app.route("/")


def home():
  return "home"


@app.route("/get-balance/<address>")
def get_balance(address):

  url = "https://www.mexc.com/open/api/v2/market/ticker?symbol=BAJU_USDT"
  reponse = requests.get(url)
  data = reponse.json()
  prix_baju = float(data['data'][0]['last'])
  getcontext().prec = 15
  resultat =  rpc_url.query('System','Account',[address])
  balance = Decimal(resultat.value['data']['free']) / Decimal(100 ** 12)
  balance_format = float(format(balance,'.2f'))
  print(address)
  balance_usd = prix_baju * balance_format

  return f"Your Balance  : {balance_format} Bajun  ~ {balance_usd:.2f}$ USD"


if __name__ == '__main__':
  app.run(debug=True)







# url = 'https://polkadot.api.subscan.io/api/scan/metadata'
# parameters = {
#   'start':'1',
#   'limit':'50',
#   'convert':'USD'
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': '42895011-aca1-4898-869c-347ecbd4238d',
# }
# session = Session()
# session.headers.update(headers)
# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
#   pprint(data)
# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   print(e)



