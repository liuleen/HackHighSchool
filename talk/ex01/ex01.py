#!/usr/bin/env python

# This project creates a short Mad-Libs puzzle

# By rliu

import sys

if sys.argv[1] == '':
	exit()
title = sys.argv[1]

adjective = raw_input("Please input an adjective: ")
if adjective == '':
	print("Error, try again")
	exit()
business = raw_input("Please input a business: ")
if business == '':
	print("Error, try again")
	exit()
animal = raw_input("Please input an animal: ")
if animal == '':
	print("Error, try again")
	exit()
noise = raw_input("Please input a noise: ")
if noise == '':
	print("Error, try again")
	exit()

print("\n" + title.upper())
print(adjective.title() + " Macdonald had a " + business.lower() + ", E-I-E-I-O")
print("And on that " + business.lower() + " he had a " + animal.lower() + ", E-I-E-I-O")
print("With a " + noise.lower() + " " + noise.lower() + " here")
print("And a " + noise.lower() + " " + noise.lower() + " there,")
print("Here a " + noise.lower() + ", there a " + noise.lower() + ",")
print("Everywhere a " + noise.lower() + " " + noise.lower() + ",")
print(adjective.title() + " Macdonald had a " + business.lower() + ", E-I-E-I-O!")
