#!/usr/bin/env python3
filename= '/etc/protocols'
f=open(filename)
try:
	f.write('shiyanlou')
except:
	print("File Write error")
finally:
	print("HELLO")
	f.close()

