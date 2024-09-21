class Ball:
    def __init__(self, radius):
        self.radius = radius
        self.mass = 500
        self.x = 0
        self.y = 0
    def drop(self):
        print('я подбросился')
        self.y += 2
    def kick(self):
        print('я пнулся')
        self.x += 10
    def fall(self):
        print('я сдулся')
        self.mass = 0

ball = Ball(5)
ball.drop()
print(ball.y)
ball.kick()
print('x =', ball.x)
ball.fall()
print(ball.mass)
    
