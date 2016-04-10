import requests
from exchange import *

def cexio_order_book():
    depth = 100
    url = "https://cex.io/api/order_book/BTC/USD/?depth=" + str(depth)
    response = requests.post(url)
    response = eval(response.text)
    bids = response['bids']
    asks = response['asks']

    return {"bids": bids,
            "asks": asks}
