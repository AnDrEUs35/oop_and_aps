a = [23, 96, 53, 45, 9, 25, 80, 13, 79, 52]

c = []

b = list(map(lambda x: x**3 if x % 2 == 0 else a.remove(x), a))
print(b)