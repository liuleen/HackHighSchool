#!/usr/bin/env ruby

# a program that takes two numbers as command line arguments.  turn them into numbers
# with which you can perform math.

# By rliu

def function_a(v1, v2)
	eq = v1 /v2
	mod = v1 % v2
	puts v1.t_s + " divided by " + v2.to_s + " equals " + eq.to_s + " remainder " + mod.to_s
	function_b
end

def function_b()
	a = 25
	b = 25.25
	c = Complex(2, 5)
	d = 125.divmod(5)
	puts "Variable a contains : " + a.to_s + " which is of type: " + a.class.to_s,
		"Variable a contains : " + b.to_s + " which is of type: " + b.class.to_s,
		"Variable a contains : " + c.to_s + " which is of type: " + c.class.to_s,
		"Variable a contains : " + d.to_s + " which is of type: " + d.class.to_s
end

def main(av)
	v1 = av[0].to_i
	v2 = av[1].to_i
	av.clear
	function_a(v1, v2)
end

main(ARGV)