def summator(a):
    def decorator(func):
        def sum(b):
            b = func(b)
            return a + b
        return sum
    return decorator

@summator(8)
def func(b):
    return b

print(func(12))