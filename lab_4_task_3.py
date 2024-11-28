import numpy as np

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __len__(self):
        lenth = np.sqrt(self.x**2 + self.y**2 + self.z**2)
        return lenth

    def __str__(self):
        return f'длина вектора равна {self.__len__()}'
    
    def __repr__(self):
        return self.__len__()
    
    def __add__(self, other):
        V_x = self.x + other.x
        V_y = self.y + other.y
        V_z = self.z + other.z
        V = Vector(V_x, V_y, V_z)
        return(V)

    def __sub__(self, other):
        V_x = self.x - other.x
        V_y = self.y - other.y
        V_z = self.z - other.z
        V = Vector(V_x, V_y, V_z)
        return(V)

    def __mul__(self, other):
        V_x = self.x * other.x
        V_y = self.y * other.y
        V_z = self.z * other.z
        V = Vector(V_x, V_y, V_z)
        return(V)
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False 
        
    def __ne__(self, other):
        if self.x != other.x or self.y != other.y or self.z != other.z:
            return True
        else:
            return False 
        
    def __pow__(self, st):
        vx = self.x ** st
        vy = self.y ** st
        vz = self.z ** st        
        V = Vector(vx, vy, vz)
        return V


a = Vector(3, 4, 5)
b = Vector(2, 2, 2)

a.__len__()
print(a)
a.__repr__() # ????????

v = a + b
v.__len__()
print(v)

v2 = a - b
v2.__len__()
print(v2)

v3 = b * a
v3.__len__()
print(v3)

print(a == b)
print(a != b)

v4 = a**2
print(v4)
