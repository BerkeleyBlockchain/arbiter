import urllib
import http.client
import json

from exchange import *

def iibit_order_book():
  assocArray = canonicalize(createDictionary("https://api.itbit.com/v1/markets/XBTUSD/order_book"))
  assocArray2 = canonicalize_two(createDictionary("https://api.itbit.com/v1/markets/XBTUSD/ticker"))
  assocArray.update(assocArray2)
  
  return assocArray

  #################################################################################################

def canonicalize_two(book):
  return {'last': book['lastPrice'],
          'volume': book['volume24h'],
          'low': book['low24h'],
          'high': book['high24h']}

def canonicalize(book):
  return {'bids': to_float_lists(book['bids']),
          'asks': to_float_lists(book['asks'])}

def to_float_list(strs):
  return [float(s) for s in strs]

def to_float_lists(strss):
  return [to_float_list(strs) for strs in strss]

def createDictionary(url):
  headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
  req = urllib.request.Request(url, None, headers)
  urlResponse = urllib.request.urlopen(req)
  bitRead = urlResponse.read()
  stringResponse = bitRead.decode("utf-8")

  IOobj = io.StringIO(stringResponse)
  return json.load(IOobj)

