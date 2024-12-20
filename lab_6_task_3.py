import numpy as np
def calculate_area(shape, *args):
    try:
        if shape != 'круг' and shape != 'квадрат' and shape != 'прямоугольник' and shape != 'треугольник':
            raise ValueError

        try:
            for i in args:
                if i < 0:
                    raise ValueError

            try:
                if shape == 'круг' and len(args) == 1:
                    return np.pi * args[0]**2
                
                elif shape == 'квадрат' and len(args) == 1:
                    return args[0]**2

                elif shape == 'прямоугольник' and len(args) == 2:
                    return args[0] * args[1]
                
                elif shape == 'треугольник' and len(args) == 3:
                    return args[0] * args[1] * np.sin(args[2])

                else:
                    raise TypeError
                
            except TypeError:
                print("Неверное количество аргументов")
        
        except ValueError:
            print("Нужны положительные числовые аргументы")
            
    except ValueError:
        print("Неверное название фигуры")


print(calculate_area('треугольник', 5, 5, 2))