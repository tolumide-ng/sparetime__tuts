#!/usr/bin/env python3


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display_info(name, age):
    print(f'display_info ran with arguments ({name} and {age})')


display_info('tolu', '18')
