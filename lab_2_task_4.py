class Planet:
    have_sputnik = True
    count_obj = 0


    def __init__(self, M, R):
        self.G = 6.672 * 10**(-11)
        self.M = M
        self.R = R
        Planet.count_obj += 1
        
    
    @classmethod
    def have_sputnic(cls):
        if cls.have_sputnik == True:
            cls.have_sputnik = False
            print(cls.have_sputnik)
        elif cls.have_sputnik == False:
            cls.have_sputnik = True
            print(cls.have_sputnik)

    @classmethod
    def count(cls):
        print(cls.count_obj)
        return cls.count_obj


    @property
    def g(self):
        g = self.G * self.M / self.R**2
        print(g)


    @staticmethod
    def is_life(oxigen, temperature, liquid_water):
        if oxigen == 'Есть' and -20 < temperature < 35 and liquid_water == 'Есть':
            print('На планете возможна жизнь')
        else:
            print('На планете невозможна жизнь')


    @classmethod
    def gibt_es_viele_von_uns(cls):
        if cls.count_obj > 5:
            print("Es gibt viele von uns")
        else:
            print('Es gibt wenig von uns')
    
pl1 = Planet(200000000, 1500000)
pl2 = Planet(50000000, 20000000)
pl3 = Planet(300000000, 10000)

pl1.g
pl2.is_life('Есть', 20, 'Есть')
Planet.is_life('Есть', 20, 'Нет')
Planet.count()
Planet.have_sputnic()
Planet.gibt_es_viele_von_uns()