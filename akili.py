from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
url = 'https://polkadot.api.subscan.io/api/scan/metadata'
parameters = {
  'start':'1',
  'limit':'50',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '42895011-aca1-4898-869c-347ecbd4238d',
}
session = Session()
session.headers.update(headers)
try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  pprint(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



