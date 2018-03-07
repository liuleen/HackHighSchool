#!/usr/bin/env python

# Take in a set of numbers as command line arguments. Store them as an array and
# print out the min, max, mean, median, mode and range of the set.

# By rliu

import sys
import numpy as np

arr = sys.argv[1].split(' ')

meanNumbers = input("What numbers would you like to use?:")
print (np.average(meanNumbers))

medianNumbers = input("What numbers would like to use?:")
print (np.median(medianNumbers))

modeNumbers = input("What numbers would you like to use?:")
print (np.mode(modeNumbers))
 
rangeNumbers = input("What numbers would you like to use?:")
print (np.arange(rangeNumbers))
  