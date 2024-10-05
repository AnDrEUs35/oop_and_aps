'''
Пятёрочка.
Есть магазин, у него есть атрибут, обозначающий минимальное кол-во продуктов. Он может продавать случайное кол-во товаров, проверять, хватает ли продуктов,
получать продукты от производителя.

Класс Creator имеет атрибут, обозначающий количество продуктов, которое у него заказали. У может увеличивать количество продуктов у себя,
отправлять продукты.

Класс покупатели имеет атрибут купленные продукты. Покупатели могут покупать товар и выводить информацию о купленных продуктах.
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
        self.shop_products = {'Выпечка': 0, 'Молочка': 0, 'Овощи и фрукты': 0, 'Заморозка': 0}
        self.min = min

    def sell(self):
        print(self.shop_products, ' - до продажи')
        self.buyers = Buyers()
        self.buyers.buy()
        for i in self.shop_products.keys():
            self.shop_products[i] -= self.buyers.purchased_products[i]
        print(self.shop_products, ' - после продажи')
    
    def is_products_over(self):
        for i in self.shop_products.keys():
            if self.shop_products[i] < self.min:
                self.get_products(self.min) 


    def get_products(self, order):
        self.creator = Creator(order)
        self.creator.replenishment()
        for i in self.shop_products.keys():
            self.shop_products[i] += self.creator.products[i]
        self.creator.sent()


class Buyers:
    
    
    def __init__(self):
        self.purchased_products = {'Выпечка': 0, 'Молочка': 0, 'Овощи и фрукты': 0, 'Заморозка': 0}
    
    
    def buy(self):
        for i in self.purchased_products.keys():
            self.purchased_products[i] += r.randint(0, 100)

    
    def analys(self):
        print(self.purchased_products, ' - купленные товары')
        print('Самое большое количество купленного товара - ', max(self.purchased_products.values()))


if __name__ == '__main__':
    s = Shop(300)
    s.is_products_over()
    s.sell()
    s.buyers.analys()


