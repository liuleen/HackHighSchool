#!/usr/bin/env python

# Create a script which takes a sentence worth of command-line arguments,
# splits them into an array, and then prints them each out on a different line along
# with the corresponding index of the array

# By rliu

def function_a(av)
	i = 0
	while i < av.size
		puts "Argv of " + i.to_s + " is " + av[i]
		i += 1
	end
	pa = av.sort_by { |x| x.length }
	av.clear
	i = pa.size - 1
	while i >= 0
		puts pa[i]
		i -= 1
	end
end

function_a(ARGV)