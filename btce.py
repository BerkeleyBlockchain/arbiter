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

def btce_load():
  url = "https://btc-e.com/api/3/ticker/btc_usd

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

def btce_last():
  return btce_load()['btc_usd']['last']

def btce_volume():
  return btce_load()['btc_usd']['vol']



