from exchange import *
from coinbase import coinbase_order_book
from cexio import cexio_order_book
from datetime import datetime

def logticker():
	coinbase = Exchange("coinbase", coinbase_order_book)
	cexio = Exchange("cexio", cexio_order_book)
	f = open("logticker.txt", 'a')
	time = str(datetime.now())
	f.write(time + "\n")
	f.write("Coinbase - Bid: " + coinbase.bid() + " Ask: " + coinbase.ask() + "\n")
	f.write("Cexio - Bid: " + str(cexio.bid()) + " Ask: " + str(cexio.ask()) + "\n\n")
	f.close()

logticker()