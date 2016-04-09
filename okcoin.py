import urllib
import http.client
import json

from exchange import *

def okcoin_order_book():
  assocArray = canonicalize(createDictionary("https://www.okcoin.com/api/v1/depth.do"))
  assocArray2 = canonicalize_two(createDictionary("https://www.okcoin.com/api/v1/ticker.do?symbol=ltc_usd"))
  assocArray.update(assocArray2)

  return assocArray

def canonicalize_two(book):
  return {'last': book['ticker']['last'],
          'volume': book['ticker']['vol'],
          'low': book['ticker']['low'],
          'high': book['ticker']['high']}

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

