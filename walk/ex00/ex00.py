#!/usr/bin/env python

# This project asks for the user's name and only greets you if your name is
# Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen
# Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms,
# Breaker of Chains and Mother of Dragons or "DHTFHNUQARFMQMKGSPRLRSKBCMD"
# for short.

# By rliu

question = raw_input("Who goes there?\n")
name = str("Daenerys of the House Targaryen, the First of Her Name, The Unburnt, Queen of the Andals, the Rhoynar and the First Men, Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons")
namename = str("DHTFHNUQARFMQMKGSPRLRSKBCMD")

if question == name:
	print("Welcome, Daenerys.")
	exit()
if question == namename:
	print("Welcome, Daenerys.")
	exit()
if question == "Dany":
	print("Dany who?")
else:
	print("Move along, now.")
