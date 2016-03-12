import urllib
import http.client
import json

from exchange import *

def bitonic_pull_data():
  # Order book URL

  headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
  req = urllib.request.Request("https://bitonic.nl/api/buy?btc=1", None, headers)
  req2 = urllib.request.Request("https://bitonic.nl/api/sell?btc=1", None, headers)

  # Response object
  urlResponse = urllib.request.urlopen(req)
  urlResponse2 = urllib.request.urlopen(req2)


  # Read response
  bitRead = urlResponse.read()
  bitRead2 = urlResponse2.read()

  # Convert bitstream response to string
  stringResponse = bitRead.decode("utf-8")
  stringResponse2 = bitRead.decode("utf-8")

  # Load the associative array from the string
  IOobj = io.StringIO(stringResponse)
  IOobj2 = io.StringIO(stringResponse2)
  assocArray = json.load(IOobj)
  assocArray2 = json.load(IOobj2)

  def canonicalizeBuy(book):
  	return {'bids': [[book['price']]]}

  def canonicalizeSell(book):
    return {'asks': [[book['price']]]}

  def to_float_list(strs):
    return [float(s) for s in strs]

  def to_float_lists(strss):
    return [to_float_list(strs) for strs in strss]

  d = canonicalizeBuy(assocArray)
  d1 = canonicalizeSell(assocArray2)
  d.update(d1)

  return d


