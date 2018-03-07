#!/usr/bin/env python

# Create a script that prints the prime factors, in increasing order, of the
# number given as an argument.

# By rliu

import sys
import math

if sys.argv[1] == '':
	exit()
num = sys.argv[1]
num = int(num)
 
def primeFactors(n):
     
    while n % 2 == 0:
        print 2,
        n = n / 2

    for i in range(3,int(math.sqrt(n))+1,2):
         
        while n % i== 0:
            print i,
            n = n / i
             
    if n > 2:
        print n

print primeFactors(num)