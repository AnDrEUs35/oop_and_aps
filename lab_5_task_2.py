import numpy as np

a = int(input())
l = [0, 100]
b = sum(l) // 2
def rec_func(b):
    if b != a:
        ans = input(f'Ваше число меньше {b}? \n')
        if ans == 'да':
            l[1] = b
            return rec_func(sum(l) // 2)
        if ans == 'нет':
            l[0] = b
            return rec_func(sum(l) // 2)
    return b

if 1 < a < 100:
    c = rec_func(b)
    print(c)
