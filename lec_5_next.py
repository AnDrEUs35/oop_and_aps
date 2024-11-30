with open('example.txt') as f:
    # print(f.readline(), end='')
    # print(f.readline(), end='')
    # print(f.readline(), end='')

    print(next(f), end='')
    print(next(f), end='')
    # print(next(f), end='')

with open('example_2.txt') as f2:
    for i in f2:
        print(i, end='')
    