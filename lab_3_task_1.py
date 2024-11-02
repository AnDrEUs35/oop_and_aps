class Businessman:
    def __init__(self, name, age, capital):
        def_name = 'Иван'
        def_age = 50
        
        self.name = def_name
        self.age = def_age

        self.name = name
        self.age = age
        self._money = capital
        self.business = 'Нет'
    
    
    def info(self):
        print(f'Имя - {self.name} \n Возраст - {self.old} \n Капитал - {self.capital} \n Бизнес - {self.have_business}')
    
    

class Business:
    pass