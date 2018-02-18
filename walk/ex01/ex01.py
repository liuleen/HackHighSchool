#!/usr/bin/env python

# This project creates a program that contains a secret five letter word
# that the user has 10 tries to guess. Use loops to received user and
# respond with different responses depending on answer you get from user

# By rliu

secretWord = str("fives")

print("The secret word begins with an f.")
i = 0

while i < 10:
	guess = raw_input("GUESS: ")
	if len(guess) > 5:
		print("0, 1, 2, 3, 4 that's how we count to five!")
	elif guess == "":
		print("You wasted a guess!")
	elif guess[0] != 'f':
		print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	elif guess == "fives":
		print("Good Job! You are one with the Source.")
		exit()
	else:
		print("You have " + str(9 - i) + " guesses left!")
	i += 1
exit()
