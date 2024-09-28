'''
Пятёрочка.
Есть магазин, у него есть атрибут, обозначающий минимальное кол-во продуктов. Он может продавать случайное кол-во товаров, проверять, хватает ли продуктов,
получать продукты от производителя.

Класс Creator имеет атрибут, обозначающий количество продуктов, которое у него заказали. У может увеличивать количество продуктов у себя,
отправлять продукты.





'''



import random as r


class Creator:
    
    
    def __init__(self, order):
        self.order = order
        self.products = {'Выпечка': 0, 'Молочка': 0, 'Овощи и фрукты': 0, 'Заморозка': 0}
        for i in self.products.keys():
            self.products[i] = r.randint(0, 400)


    def replenishment(self):
        for i in self.products.keys():
            if self.products[i] <= self.order:
                self.products[i] += self.order
        

    def sent(self):
        count = 0
        print(self.products, ' - перед отправкой')
        for i in self.products:
            if self.products[i] >= self.order:
                self.products[i] -= self.order
                count += 1
        if count == len(self.products):
            print(self.products, ' - после отправки')


        
class Shop:
    def __init__(self, min):
        self.products = {'Выпечка': 0, 'Молочка': 0, 'Овощи и фрукты': 0, 'Заморозка': 0}
        self.min = min

    def sell(self):
        print(self.products, ' - до продажи')
        for i in self.products.keys():
            self.products[i] -= r.randint(0, 100)
            if self.products[i] < 0:
                self.products[i] = 0
        print(self.products, ' - после продажи')
    
    def is_products_over(self,):
        for i in self.products.keys():
            if self.products[i] < self.min:
                self.get_products(self.min) 


    def get_products(self, order):
        self.creator = Creator(order)
        self.creator.replenishment()
        self.creator.sent()
        for i in self.products.keys():
            self.products[i] += self.creator.products[i]





if __name__ == '__main__':
    s = Shop(300)
    s.is_products_over()
    s.sell()


