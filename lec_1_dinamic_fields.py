class Ball:
    def __init__(self, radius):
        self.radius = radius
        self.mass = 500

obj = Ball(5)
print(obj.radius)
obj.radius = 0.5
print(obj.radius)