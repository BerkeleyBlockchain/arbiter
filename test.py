from exchange import *
from kraken import kraken_order_book
from bitstamp import bitstamp_order_book
from bitfinex import bitfinex_order_book
from coinbase import coinbase_order_book
from btce     import btce_order_book
from okcoin import okcoin_order_book
from iibit import iibit_order_book

bitstamp = Exchange("Bitstamp", bitstamp_order_book)
bitfinex = Exchange("Bitfinex", bitfinex_order_book)
kraken   = Exchange("Kraken", kraken_order_book)
coinbase = Exchange("Coinbase", coinbase_order_book)
btce     = Exchange("BTC-E", btce_order_book)
okcoin   = Exchange("Okcoin", okcoin_order_book)
iibit    = Exchange("Itbit", iibit_order_book)

exchanges = [bitfinex, coinbase, btce, kraken, okcoin, iibit]
