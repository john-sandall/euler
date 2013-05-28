# Project Euler Problem #4: Largest palindrome product <http://projecteuler.net/problem=4>

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 99. Find the largest palindrome made from the product of two 3-digit numbers.


# Checks if n is a palindromic number.
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


# Digits allows easy manipulation of the problem, e.g. solve example above by setting digits = 2.
digits = 3
# Range to iterate over, equals range(999,99,-1) for digits = 3.
values = range(10 ** digits - 1, 10 ** (digits-1) - 1, -1)
# Somewhere to store our "winning" combination
largest = [0, 0, 0]


# Iterate over range, break if its impossible to beat our winning combination, and update if new winner found.
for i, j in ((i, j) for i in values for j in values):
    if i ** 2 < largest[2]:
        break
    if is_palindrome(i * j) and (i * j > largest[2]):
        largest = [i, j, i * j]


print "%d x %d = %d" % (largest[0], largest[1], largest[2])
