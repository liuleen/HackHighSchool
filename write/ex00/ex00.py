#!/usr/bin/env python

# Progam which performs three tasks in a row on the phrase given as a command
# line argument.

# By rliu

import sys
import re

if sys.argv[1] == '':
	exit()
title = sys.argv[1]

def capitalize(s):
    ret = ""
    i = True  # capitalize
    for char in s:
        if i:
            ret += char.upper()
        else:
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret

print capitalize(title)

print re.sub(r'[A-Z]', '*', capitalize(title))

def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0

count = matched(title)
if count == 0:
	print "Balanced? False"
else:
	print "Balanced? True"