# Project Euler Problem #3: Largest prime factor <http://projecteuler.net/problem=3>
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

import math


# checks if n is prime
def is_prime(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return False
    return True


# generator function, creates a sequence of prime numbers less than n
def generate_primes(n):
    number = 2
    while number <= n:
        if is_prime(number):
            yield number
        number += 1


# find prime factors of n: check first if n is prime; if not look through sequence of primes for lowest prime divisor;
# when a divisor is found, recursively call the function with the quotient
def find_prime_factors(n):
    prime_factors = []
    if is_prime(n):
        prime_factors += [n]
    else:
        for x in generate_primes(n):
            if n % x == 0:
                prime_factors += [x]
                prime_factors += find_prime_factors(n / x)
                break
    return prime_factors


print max(find_prime_factors(600851475143))
