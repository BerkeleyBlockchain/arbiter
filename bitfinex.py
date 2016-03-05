import requests
from exchange import *
def bitfinex_order_book():
  assocArray = canonicalize(createDictionary("https://api.bitfinex.com/v1/book/BTCUSD"))
  assocArray2 = canonicalize_two(createDictionary("https://api.bitfinex.com/v1/pubticker/btcusd"))
  assocArray.update(assocArray2)

  return assocArray

  ####################################################################################

def canonicalize_two(book):
  return {'last': book['last_price'],
          'volume': book['volume'],
          'low': book['low'],
          'high': book['high']}

def canonicalize(book):
  return {'bids': canon(book['bids']),
          'asks': canon(book['asks'])}

def canon(xs):
  return [[float(x['price']), float(x['amount'])] for x in xs]

def createDictionary(url):
  urlResponse = urllib.request.urlopen(url)
  bitRead = urlResponse.read()
  stringResponse = bitRead.decode("utf-8")

  IOobj = io.StringIO(stringResponse)
  return json.load(IOobj)