#!/usr/bin/python3
import sys
import re

if len(sys.argv) != 2:
	print("usage: " + sys.argv[0] + " <ipv4 addr>")
	exit(1)

mo = re.match(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$', sys.argv[1])
if mo:
	group1 = int(mo.group(1))
	group2 = int(mo.group(2))
	group3 = int(mo.group(3))
	group4 = int(mo.group(4))
	if group1 < 0 or group1 > 255:
		print("not valid IPv4 address")
	elif group2 < 0 or group2 > 255:
		print("not valid IPv4 address")
	elif group3 < 0 or group3 > 255:
		print("not valid IPv4 address")
	elif group4 < 0 or group4 > 255:
		print("not valid IPv4 address")
	else:
		print("valid IPv4 address")
else:
	print("not valid IPv4 address") 
