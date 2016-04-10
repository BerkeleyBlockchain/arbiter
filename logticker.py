from exchange import *
from coinbase import coinbase_order_book
from datetime import datetime

def logticker():
	coinbase = Exchange("coinbase", coinbase_order_book)
	f = open("logticker.txt", 'a')
	time = str(datetime.now())
	f.write("Bid at " + time + " for Coinbase is: " + coinbase.bid() + '\n')
	f.close()

logticker()