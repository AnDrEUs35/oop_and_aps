def generator(break_key):
    a = 0

    while a != break_key:
        if a != 1 and (a % 2 != 0 or a == 2) and (a % 3 != 0 or a == 3) and (a % 5 != 0 or a == 5) and (a % 7 != 0 or a == 7):
            yield a**2
        a += 1

    

gen = generator(100)
for i in gen:
    print(i)