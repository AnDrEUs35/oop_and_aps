def decorator(func):
    def wrapper_function(str):
        func(str)
    return wrapper_function

@decorator
def greet(name):
    print(f'Hello, {name}!')

greet('abc')