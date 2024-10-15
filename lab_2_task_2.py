def decorator(func):
    def caculator(*args, **kwargs):
        a, b, sign = func(*args, **kwargs)
        if sign == '+':
            result = a + b
        elif sign == '-':
            result = a - b
        elif sign == '*':
            result = a * b
        else:
            result = a / b
        return result
    return caculator
@decorator
def input(a, b, sign):
    return (a, b, sign)

print(input(2, 3, '/'))