from exchange import *
from kraken import kraken_order_book
from bitstamp import bitstamp_order_book
from cryptsy import cryptsy_order_book

bitstamp = Exchange("Bitstamp", bitstamp_order_book)
cryptsy = Exchange("Cryptsy", cryptsy_order_book)
kraken = Exchange("Kraken", kraken_order_book)

exchanges = [bitstamp, cryptsy, kraken]
