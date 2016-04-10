from datetime import datetime

def test():
	f = open("cronjob_test.txt", 'a')
	time = str(datetime.now())
	f.write("Hello World, it is currently: " + time + "\n")
	f.close()

test()