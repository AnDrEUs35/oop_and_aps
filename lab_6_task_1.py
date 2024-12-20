def square_root(x):
    try:
        if x < 0:
            raise ValueError
        else:
            return x**0.5
    except ValueError:
        print('Не смей извлекать корень квадратный из отрицательного числа')

print(square_root(-2))