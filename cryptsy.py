import urllib.request
import http.client
import json

from exchange import *

def cryptsy_order_book():
  def canonicalize(dictionary):
    canonical = []

    for entry in dictionary:
      canonical.append([entry['price'], entry['quantity']])

    return canonical

  url = "http://pubapi.cryptsy.com/api.php?method=singleorderdata&marketid=2"

  success = False
  while not success:
    try:
      urlResponse = urllib.request.urlopen(url)
      bitRead = urlResponse.read()
      success = True
    except HTTPError:
      success = False

  stringResponse = bitRead.decode("utf-8")
  IOobj = io.StringIO(stringResponse)
  full_dict = json.load(IOobj)

  # Prune some stuff from the full dictionary
  full_dict = full_dict['return']['BTC']
  buys = full_dict['buyorders']
  sells = full_dict['sellorders']

  bids = canonicalize(buys)
  asks = canonicalize(sells)

  order_book = {'bids': bids, 'asks': asks}

  return order_book


