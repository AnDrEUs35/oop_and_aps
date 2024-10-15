def summator(a):
    def decorator(func):
        def sum(*args, **kwargs):
            b = func(*args, **kwargs)
            return a + b
        return sum
    return decorator

@summator(8)
def func():
    b = int(input('Введите b: '))
    return b

print(func())