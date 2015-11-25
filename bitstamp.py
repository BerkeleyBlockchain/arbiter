import urllib.request
import http.client
import json

from exchange import *

def bitstamp_order_book():
  # Order book URL
  url = "https://www.bitstamp.net/api/order_book/"

  # Response object
  urlResponse = urllib.request.urlopen(url)

  # Read response
  bitRead = urlResponse.read()

  # Convert bitstream response to string
  stringResponse = bitRead.decode("utf-8")

  # Load the associative array from the string
  IOobj = io.StringIO(stringResponse)
  assocArray = json.load(IOobj)

  return assocArray

