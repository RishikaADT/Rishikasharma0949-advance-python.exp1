def log_decorator(func):
    def wrapper(a, b):
        print("Adding {a} and {b}")
        result = func(a, b)
        print(f"Result = {result}")
        return result
    return wrapper



@log_decorator
def add(a, b):
    return a + b