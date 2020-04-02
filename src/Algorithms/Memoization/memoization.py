#!/usr/bin/env python3

import timeit
from functools import wraps


"""
Memoization is a specific way of caching used for software optimization technique
"""


def memoize(func):
    cache = dict()

    @wraps(func)
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    # Before caching
    t = timeit.timeit('fibonacci(35)', globals=globals(), number=1)
    print(t)

    # Execute after cachning
    tt = timeit.timeit('fibonacci(35)', globals=globals(), number=1)
    print(tt)
# t = timeit.Timer('fibonacci(35)', globals=globals())
# print(t.timeit(number=1))
