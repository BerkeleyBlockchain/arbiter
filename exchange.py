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


  def __init__(self, name, pull_data_func=None):
    self.name = name
    self.pull_data_func = pull_data_func

    self.load_data()

  def load_data(self):
      self.data = self.pull_data_func()

  # Get the last trade price for the exchange
  def last(self, reloadPrice=False):
      return self.data['last']

  # Returns an associative array that represents the
  # exchange's order book. The two keys are 'bids' and 'asks'
  def order_book(self, reloadData=False):
      return {'bids': self.data['bids'], 'asks': self.data['asks']}

  def bid(self, reloadBook=False):
    return self.data['bids'][0][0]

  def ask(self, reloadBook=False):
    return self.data['asks'][0][0]

  def spread(self, reloadBook=False):
    return self.ask() - self.bid()

  def name(self, reloadBook=False):
    return self.name
  
  def volume(self):
    return self.data['volume']

  def price_history(self):
    return self.data['price_history']
