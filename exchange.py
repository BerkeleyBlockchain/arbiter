import urllib.request
import requests
from urllib.error import HTTPError
import http.client
import json
import io

class Exchange:
  # Features to implement, in rough order of importance
    # [x] Name
    # [x] Bid
    # [x] Ask
    # [x] Spread
    # [ ] Last
    # [ ] 24H high
    # [ ] 24H low
    # [ ] 24H volume
    # [x] Order book
    # [ ] Price over time
    # [ ] Transaction list

    # [ ] Add try/catch error statements

  def __init__(self, name, order_book_func):
    self.name = name
    self.order_book_func = order_book_func

  # Opens this exchange for reading. Will throw an error 
  # if opening fails
  def open():
    raise NotImplementedError("Need to implement open()")

  # Returns an associative array that represents the
  # exchange's order book. The two keys are 'bids' and 'asks'
  def order_book(self):
    return self.order_book_func()

  def bid(self):
    ob = self.order_book()
    return float(ob['bids'][0][0])

  def ask(self):
    ob = self.order_book()
    return float(ob['asks'][0][0])

  def spread(self):
    ob = self.order_book()
    return float(ob['asks'][0][0]) - float(ob['bids'][0][0])

  def name(self):
    return self.name
