#!/usr/bin/env pyhton3

# using the lru_cache standard library

import functools


@functools.lru_cache(maxsize=120)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
