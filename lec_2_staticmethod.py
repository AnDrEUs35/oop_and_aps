#Статические методы имеют доступ только к атрибутам классов, к ним нельзя обратиться через ​self.
#По сути, статические методы ничего не знают ни о классе, ни об экземпляре, на который вызываются.

class Planet:
    @staticmethod
    def is_big_planet(diameter):
        if diameter > 10000:
            return True
        else:
            return False

print(Planet.is_big_planet(100))






class SummatorClass:
    @staticmethod
    def sum_1(a,b):
        print(a+b)

    def sum_2(self,a,b):
        print(a+b)

    def sum_3(self,a,b):
        return SummatorClass.sum_1(a,b)

SummatorClass.sum_1(5,10)

sum_num = SummatorClass()
sum_num.sum_2(10, 15)
sum_num.sum_1(20, 25)
sum_num.sum_3(30, 35)