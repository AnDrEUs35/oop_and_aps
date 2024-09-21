class Pyramid:
    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
    def add_bricks(self, bricks):
        self.bricks_count += bricks
    def get_height(self):
        pass
    def is_done(self):
        pass

class Builder:
    def __init__(self, bricks):
        self.bricks = bricks
        self.my_piramid = Pyramid(15)
    def buy_bricks(self, count):
        self.bricks += count
    def build_pyramyd(self, n):
        if self.bricks >= n and 1 <= n <= 5:
            self.bricks -= n
        else:
            print('У строителя не хватает кирпичей.')
    def work_day(self):
        self.build_pyramid(5)


builder = Builder(15)
builder