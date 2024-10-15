class Planet:
    have_sputnik = True
    count_obj = 0

    def __init__(self, M, R):
        self.G = 6.672 * 10**(-11)
        self.M = M
        self.R = R
        Planet.count_obj += 1
        
    
    @classmethod
    def have_sputnik(cls):
        if cls.have_sputnik == True:
            cls.have_sputnik = False
        else:
            cls.have_sputnik = True
    
    @classmethod
    def count(cls):
        print(cls.count_obj)


    @property
    def calculate_g(self):
        g = self.G * self.M / self.R**2
        print(g)


    @staticmethod
    def is_life(oxigen, temperature, liquid_water):
        if oxigen == 'Есть' and -20 < temperature < 35 and liquid_water == 'Есть':
            print('На планете возможна жизнь')
        else:
            print('На планете невозможна жизнь')
    
pl1 = Planet(200000000, 1500000)
pl2 = Planet(50000000, 20000000)
pl3 = Planet(300000000, 10000)

pl1.calculate_g
pl3.is_life('Есть', 20, 'Есть')
Planet.count()