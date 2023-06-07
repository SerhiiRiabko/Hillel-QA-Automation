def print_function_intended(func):
    def wrapper(*args, **kwargs):
        print("Function called:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@print_function_intended
def sum_func(a, b):
    result = a + b
    return result


@print_function_intended
def multiplication(a, b):
    result = a * b
    return result


print(sum_func(2, 3))
print(multiplication(4, 5))
