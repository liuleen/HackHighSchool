#!/usr/bin/env python

# a script which finds the sum of all the multiples of 3 or 5 below the
# number given as a command line argument.

# By rliu

import sys

if sys.argv[1] == '':
	exit()
num = sys.argv[1]
num = int(num)

if num < 0:
	num = num * -1
	print sum([i for i in range(num) if not (i % 3 and i % 5)]) * -1
else:
	print sum([i for i in range(num) if not (i % 3 and i % 5)])