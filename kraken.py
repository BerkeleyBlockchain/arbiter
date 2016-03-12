import requests
from exchange import *

def kraken_order_book():
  url = "https://api.kraken.com/0/public/Depth"
  response = requests.post(url, data={"pair": "XBTUSD"})
  response = eval(response.text)
  response = response['result']

  key = list(response.keys())[0]
  unprocessed_book = response[key]

  def canonicalize(book_list):
    canonical = []

    for entry in book_list:
      canonical.append([float(entry[0]), float(entry[1])])

    return canonical

  order_book = {'bids': canonicalize(unprocessed_book['bids']),
                'asks': canonicalize(unprocessed_book['asks'])}

  return order_book

def kraken_pull_data():
    url = "https://api.kraken.com/0/public/Ticker"
    response = requests.post(url, data={"pair": "XBTUSD"})
    response = eval(response.text)
    response = response['result']

    # Currently evaluates to 'XXBTZUSD'
    key = list(response.keys())[0]

    unprocessed_data = response[key]
    last = unprocessed_data['c'][0]
    volume = unprocessed_data['v'][1]

    ob = kraken_order_book()

    return {'bids': ob['bids'],
            'asks': ob['asks'], 
            'last': last,
            'volume': volume,
            'price_history': None}
