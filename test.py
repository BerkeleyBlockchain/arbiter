from exchange import *
from kraken import kraken_order_book
from bitstamp import bitstamp_order_book
from bitfinex import bitfinex_order_book
from coinbase import coinbase_order_book
from btce     import btce_order_book
from okcoin   import okcoin_order_book
from bitonic  import bitonic_order_book
from iibit    import iibit_order_book
from localbitcoins import localbitcoins_order_book
from shapeshift import shapeshift_order_book

bitstamp = Exchange("Bitstamp", bitstamp_order_book)
bitfinex = Exchange("Bitfinex", bitfinex_order_book)
kraken = Exchange("Kraken", kraken_order_book)
coinbase = Exchange("Coinbase", coinbase_order_book)
btce = Exchange("BTC-E", btce_order_book)
bitonic = Exchange("bitonic", bitonic_order_book)
localbitcoins = Exchange("localbitcoins", localbitcoins_order_book)
shapeshift = Exchange("shapeshift", shapeshift_order_book)

btce     = Exchange("BTC-E", btce_order_book)
okcoin   = Exchange("Okcoin", okcoin_order_book)
iibit    = Exchange("Itbit", iibit_order_book)

exchanges = [bitstamp, shapeshift, bitfinex, coinbase, btce, kraken, okcoin, bitonic, btcchina, iibit, localbitcoins]
