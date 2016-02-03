import urllib.request
import http.client
import json

from exchange import *

def btce_order_book():
  # Order book URL
  url = "https://btc-e.com/api/2/btc_usd/depth"

  # Response object
  urlResponse = urllib.request.urlopen(url)

  # Read response
  bitRead = urlResponse.read()

  # Convert bitstream response to string
  stringResponse = bitRead.decode("utf-8")

  # Load the associative array from the string
  IOobj = io.StringIO(stringResponse)
  assocArray = json.load(IOobj)

  def canonicalize(book):
    return book
    
  return canonicalize(assocArray)

