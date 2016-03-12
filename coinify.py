import urllib
import http.client
import json

from exchange import *
from coinify_api import coinify_api

def coinify_pull_data():
  # Order book URL
  api = CoinifyAPI( apikey, apisecret)
  response = api.buy_orders_list()

  def canonicalize(book):
    return {'bids': to_float_lists(book['bids']),
            'asks': to_float_lists(book['asks'])}

  def to_float_list(strs):
    return [float(s) for s in strs]

  def to_float_lists(strss):
    return [to_float_list(strs) for strs in strss]
    
  return canonicalize(assocArray)

def coinify_load(input):
  headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
  req = urllib.request.Request(input, None, headers)

  # Response object
  urlResponse = urllib.request.urlopen(req)


  # Read response
  bitRead = urlResponse.read()

  # Convert bitstream response to string
  stringResponse = bitRead.decode("utf-8")

  # Load the associative array from the string
  IOobj = io.StringIO(stringResponse)
  assocArray = json.load(IOobj)
  return assocArray

  def canonicalize(book):
    return {'bids': to_float_lists(book['bids']),
            'asks': to_float_lists(book['asks']),
            'last': None,
            'volume': None,
            'price_history', None}

  def to_float_list(strs):
    return [float(s) for s in strs]

  def to_float_lists(strss):
    return [to_float_list(strs) for strs in strss]
    
  return canonicalize(assocArray)
