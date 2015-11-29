# Arbiter

The exchange class is in exchange.py. To add a new exchange, make an order book function and use it to create and Exchange object. Look at bitstamp.py as an example.

test.py has some code you can use to try out the exchanges.
$ python -i test.py
>>> bitstamp.bid()
363.47
>>> bitstamp.ask()
363.48
>>> bitstamp.name
'Bitstamp'
