# Project Euler Problem #2: Even Fibonacci numbers <http://projecteuler.net/problem=2>

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
# first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.


# fibonacci() is a generator, yields fibonacci sequence
def fibonacci():
    t_1, t_2 = 1, 1
    while True:
        (t_2, t_1) = (t_1 + t_2, t_2)
        yield t_1


# stop_at() takes a stop number, n, and a generator function, f, yielding sequence from f if < n
def stop_at(n, f):
    x = f.next()
    while x < n:
        yield x
        x = f.next()
    else:
        return


# check_even() takes a generator, f, yielding any even numbers from the f sequence
def check_even(f):
    while True:
        x = f.next()
        if x % 2 == 0:
            yield x


print sum(check_even(stop_at(4000000, fibonacci())))
