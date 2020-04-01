#!/usr/bin/env python3


def outer_func(msg):
    def inner_func():
        print(msg)
    return inner_func


hi = outer_func('Hi')
hello = outer_func('Hello')

hi()
hello()
