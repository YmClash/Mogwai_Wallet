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

@app.route("/")


def home():
  return "home"


@app.route("/get-balance/<address>")
def get_balance(address):


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



