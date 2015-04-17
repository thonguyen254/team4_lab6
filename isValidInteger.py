#!/usr/bin/python3
import re
import sys

# Syntax check
if len(sys.argv) != 2:
	print("usage: " + sys.argv[0] + "<number>")
	exit(1)

# Determine if valid integer
mo = re.match('^[+-]?[0-9]+$', sys.argv[1])
if mo:
	print("is valid integer")
else:
	print("not valid integer")

