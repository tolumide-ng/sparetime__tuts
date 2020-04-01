def decorator_func(original_function):
    def wrapper_func():
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function()
    return wrapper_func


# def display():
#     print('display function ran')


# decorated_display = decorator_func(display)

# decorated_display()


@decorator_func
def display():
    print('display function ran')


display()
