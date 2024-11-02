class Ball:

    def __init__(self):
        self.name = 'Oval' # Публичная переменная
        self._radius = 5 # Приватная переменная
        self.__color = 'red' # Защищённая переменная

    def update_name(self, name):
        self.name = name
        print('new_name = ', self.name)

    def _update_radius(self, radius):
        self._radius = radius
        print('new_radius = ', self._radius)

    def __update_color(self, color):
        self.__color = color
        print('new_color = ', self.__color)

    def default_color(self):
        print('default_color')
        self.__update_color('red')

ball = Ball()
print(ball.name)
print(ball._radius)
#print(ball.__color)

print()

ball.update_name('Happy Oval')
ball._update_radius(5)
#ball.__update_color('blue')

ball._Ball__update_color('blue')

print(dir(ball))