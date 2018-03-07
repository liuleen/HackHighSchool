#!/usr/bin/env python

# Write a program which tests boolean logic by combining one element from each array
# into an equation and printing the full equation with its result. You can either use the
# arrays as given or have your program randomize them.

# By rliu

def decide

	a = [false,true,true,nil,true,nil,nil,false,false,nil,true,false]
	b = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"]
	c = [false,false,nil,nil,true,true,false,true,nil,false,true,nil]

	i = 0
	while i < a2.size
		if a[i] == nil
			a[i] = "nil"
		end
		if c[i] == nil
			c[i] = "nil"
		end
		print a[i].to_s + " " + b[i] + " " + c[i].to_s + " => "
		if b[i] == "or"
			puts (a[i] or c[i]).to_s
		elsif b[i] == "=="
			puts (a[i] == c[i]).to_s
		elsif b[i] == "!="
			puts (a[i] != c[i]).to_s
		elsif b[i] == "and"
			puts (a[i] and c[i]).to_s
		end
		i += 1
	end
end


def main
decide
end

main