import requests
from exchange import *
def bitfinex_order_book():
  url = "https://api.bitfinex.com/v1/book/BTCUSD"
  urlResponse = urllib.request.urlopen(url)
  bitRead = urlResponse.read()
  stringResponse = bitRead.decode("utf-8")

  IOobj = io.StringIO(stringResponse)
  assocArray = json.load(IOobj)

  def canonicalize(book):
    return {'bids': canon(book['bids']),
            'asks': canon(book['asks'])}

  def canon(xs):
    return [[float(x['price']), float(x['amount'])] for x in xs]

  return canonicalize(assocArray)
