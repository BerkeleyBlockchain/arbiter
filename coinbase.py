import requests
from exchange import *

def coinbase_order_book():
  url="https://api.exchange.coinbase.com/products/BTC-USD/book?level=2"
  urlResponse = urllib.request.urlopen(url)
  bitRead = urlResponse.read()
  stringResponse = bitRead.decode("utf-8")  

  IOobj = io.StringIO(stringResponse)
  assocArray = json.load(IOobj)

  def canonicalize(book):
    return {'bids': canon(book['bids']),
            'asks': canon(book['asks'])}

  def canon(xs):
    return [x[:2] for x in xs]

  return canonicalize(assocArray)
