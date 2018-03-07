#!/usr/bin/env ruby

# change base 10 to base 2

# By rliu

base = ARGV[1]

def ten_to_two(num1)
  return [] if num1 <= 0
  first,second=num1.divmod(2)
  ten_to_two(first) << second
end

print ten_to_two(base)