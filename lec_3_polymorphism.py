class MyVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, item):
        print('v1(', self.x, self.y, self.z, ')', end=' ')
        print('+ v2(', item.x, item.y, item.z, ')')
        return MyVector(
            self.x + item.x,
            self.x + item.x,
            self.x + item.x)
    def __str__(self):
        return f'MyVector: {self.x} {self.y} {self.z}'
    

v1 = MyVector(3, 4, 5)
v2 = MyVector(7, -3, 5)

# '+' - это неявный вызов __add__
v = v1 + v2
# print неявно вызывает __str__
print(v)


a = 'Good'
a.__str__()

a = 7
c = a.__add__(3)
print(c)