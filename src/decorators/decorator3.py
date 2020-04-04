#!/usr/bin/env python3

import logging
import time


def my_logger(orig_func):
    logging.basicConfig(
        filename=f'{orig_func.__name__}.log', level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args} and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper


@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran with arguments ({name}, {age})')


# display_info = my_logger(my_timer(display_info))

print(display_info.__name__)

display_info('tolu', 18)
