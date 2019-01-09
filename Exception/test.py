import sys

try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
	print(i)
except OSError as err:
	print("OS Error: {0}".format(err))
except ValueError as err:
	print(err)
	print("Could not convert data to an integer.")
except:
	print("Unexpected error:",sys.exc_info()[0])
	raise