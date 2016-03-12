import urllib.request
import http.client
import json

from exchange import *
from coinbase.wallet.client import Client

client = Client(api_key, api_secret)

def coinbase_order_book():
  buy = client.get_buy_price()
  sell = client.get_sell_price()


  def canonicalize(book):
    return {'bids': [buy]],
            'asks': [sell]}

  def to_float_list(strs):
    return [float(s) for s in strs]

  def to_float_lists(strss):
    return [to_float_list(strs) for strs in strss]
    
  return canonicalize(assocArray)
