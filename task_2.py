import math as m
import random as r


class Pyramid:


    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.h = 1
        self.Sn = []

        for i in range(self.max_h+1):
            a =(2*self.max_h - (i-1)) * i / 2
            self.Sn.append(a)


    def add_bricks(self, N):
        self.bricks_count += N

        if self.bricks_count >= self.Sn[0]:
            self.h += 1
            self.Sn.remove(self.Sn[0])
        if self.h > self.max_h:
            print('Пирамида разрушилась')
            exit(0)
        else:
            pass
    
    
    def get_height(self):
        print(self.h, ' высота')
            
    
    def is_done(self):
        if len(self.Sn) >= 1:
            self.done = self.bricks_count / self.Sn[-1] * 100
            print(self.done, ' готовность')
            return self.done
        


class Builder:


    def __init__(self, bricks, height):
        self.bricks = bricks
        self.my_pyramid = Pyramid(height)
        self.day = 0


    def buy_bricks(self):
        self.bricks += 6


    def build_pyramid(self, n):
        if self.bricks >= n:
            self.bricks -= n
            return n
        else:
            self.buy_bricks()
            self.bricks -= n
            return n


    def work_day(self):
        self.day += 1
        b = [1, 2, 3, 4, 5]
        print(self.day, 'день')
        c = r.choice(b)
        self.build_pyramid(c)

        self.my_pyramid.add_bricks(c)
        self.my_pyramid.get_height()

        print(self.bricks, ' кол-во кирпичей')
        
        s = self.my_pyramid.is_done()

        if s == 100:
            exit(0)


if __name__ == '__main__':
    builder = Builder(13, 15)
    while True:
        builder.work_day()