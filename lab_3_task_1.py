class Businessman:
    def_name = 'Иван'
    def_age = 50
    
    def __init__(self, name='Иван', age=50, money=0):

        self.name = name
        self.age = age
        self._money = money
        self._business = 'Нет'
    
    
    def info(self):
        print(f'Имя - {self.name} \nВозраст - {self.age} \nКапитал - {self._money} \nБизнес - {self._business}')
    

    @staticmethod
    def def_info():
        print(Businessman.def_name)
        print(Businessman.def_age)


    def _make_deal(self, obj_business, price):
        self._money -= price
        obj_business.owner = self.name
        self._business = 'Есть'


    def earn_money(self, income):
        self._money += income


    def buy_business(self, obj_business, discount):
        price = obj_business.final_price(discount)
        if self._money >= int(price):
            self._make_deal(obj_business, price)
        else:
            print('На счету недостаточно денег')


class Business:
    def __init__(self, profit, price):
        self._profit = profit
        self._price = price
        self.owner = None

    
    def final_price(self, discount):
        self._price -= discount/100 * self._price
        return self._price



class House(Business):
    def __init__(self, area, price):
        super().__init__(profit=0, price=price)
        self._area = area



class RestourantBusiness(Business):
    def __init__(self, price):
        super().__init__(profit=50000000, price=price)

businessman1 = Businessman('Пётр', 23, 0)
businessman2 = Businessman()

Businessman.def_info()
businessman1.info()

restourant1 = RestourantBusiness(100000000)
house1 = House(120, 10000000)

businessman1.buy_business(restourant1, 10)
businessman1.earn_money(1000000000000)
businessman1.buy_business(house1, 10)
print(f'Владелец - {house1.owner}')

businessman1.info()