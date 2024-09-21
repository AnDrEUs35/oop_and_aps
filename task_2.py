import math as m
class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.h = 0 
        self.Sn = []
        for i in range(self.max_h):
            a =(2*self.max_h - (i-1)) * i / 2
            self.Sn.append(a)
    def add_bricks(self, N):
        self.bricks_count += N
        if self.bricks_count >= self.Sn[0]:
            self.h += 1
            self.Sn.remove(self.Sn[0])
        else:
            pass
    def get_height(self):
        print(self.h)
            
    def is_done(self):
        if len(self.Sn) >= 1:
            self.done = self.bricks_count / self.Sn[-1] * 100
            print(self.done)
            return self.done
        



class Builder:
    def __init__(self, bricks):
        self.bricks = bricks
        self.my_pyramid = Pyramid(15)
    def buy_bricks(self, count):
        self.bricks += count
    def build_pyramid(self, n):
        if 1 <= n <= 5:
            if self.bricks >= n:
                self.bricks -= n
                return n
            else:
                self.buy_bricks(n-self.bricks)
                self.bricks -= n
                return n
        else:
            print('Введите другое число')
    def work_day(self):
        N = self.build_pyramid(5)
        self.my_pyramid.add_bricks(N)
        s = self.my_pyramid.is_done()
        if s >= 100:
            exit(0)


p = Pyramid(15)
print(p.Sn[-1])
builder = Builder(13)
while True:
    builder.work_day()