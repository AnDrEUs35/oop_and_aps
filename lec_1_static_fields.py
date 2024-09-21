class Ball:
    mass = 500
    color = 'Blue'
    radius = 5
ball1 = Ball()

print(ball1.mass)
print(ball1.radius)

ball1.color = 'White' # изменение экземпляра
Ball.color = 'white' # зменение класса

print(dir(ball1))