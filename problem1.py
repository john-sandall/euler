# Project Euler Problem #1: http://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# sumMultiples() returns the sum of all the multiples of a number less than n. We then add these up for 3 & 5 and
# remove double counting.


def sum_multiples(multiplier, n):
    return sum(range(0, n, multiplier))

print sum_multiples(3, 1000) + sum_multiples(5, 1000) - sum_multiples(15, 1000)
