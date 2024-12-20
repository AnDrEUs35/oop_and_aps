import math as m

def n_factorial(n):
    try:
        if n < 0 or isinstance(n, int) != True:
            raise ValueError
        else:
            return m.factorial(n)
    except ValueError:
        print('Число должно быть целым и неотрицательным')

print(n_factorial(20))