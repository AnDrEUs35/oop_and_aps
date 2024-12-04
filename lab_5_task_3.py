a = [23, 96, 53, 45, 9, 25, 80, 13, 79, 52]

c = []
for i in a:
    if i % 2 ==0:
        c.append(i)

b = list(map(lambda i: i**3, c))
print(b)