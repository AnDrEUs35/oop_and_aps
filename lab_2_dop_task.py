# Стратегия, которая изначально должна была быть D&D.
# Пока есть только воины, маги и скелеты, которых эти маги могут создавать. Каждый класс умеет считать количество своих экземпляров,
# которое может изменяться, и уменьшаться в том числе. Каждый класс имеет атрибуты: здоровье и урон, а маги ещё и ману. Все классы могут проверять состояние экземпляров: жив или
# нет. Если нет, то уменьшаем количество экземпляров и увеличиваем сумму умерших.
# У каждого класса есть метод, считающий общее количество нанесённого урона. Также у всех классов есть метод атаки, который принимает аргумент, кого бить. У классов есть свои
# особенные атаки. Так, маги могут создавать скелетов, воины могут увеличивать свой урон(для всех воинов сразу), скелеты могут всей толпой напасть на одного врага (всё за одно действие).

class Warrior:

    count_ex = 0

    def __init__(self):
        Warrior.sum_damage = 0
        self.HP = 1000
        Warrior.damage = 100
        Warrior.count_ex += 1
        Warrior.sum_dead = 0


    @classmethod
    def count(cls):
        print(cls.count_ex)
        return cls.count_ex
    
    def is_dead(self):
        if self.HP <= 0:
            Warrior.count_ex -= 1
            print('Воин пал.')
            Warrior.sum_dead += 1
        else:
            print('Воин пока жив')

    def atack(self, who):
        if who.HP > 0:
            who.HP -= Warrior.damage
            Warrior.sum_damage += Warrior.damage
            if who.HP <= 0:
                who.is_dead()

    @classmethod
    def improve_damage(cls):
        cls.damage = 300

    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый воинами урон: {Warrior.sum_damage}')




class Mage:

    count_ex = 0

    def __init__(self):
        self.HP = 300
        self.damage = 200
        self.mana = 3000
        Mage.count_ex += 1
        Mage.sum_damage = 0
        Mage.sum_dead = 0


    @classmethod
    def count(cls):
        print(cls.count_ex)
        return cls.count_ex
    

    def is_dead(self):
        if self.HP <= 0:
            Mage.count_ex -= 1
            print('Маг пал.')
            Mage.sum_dead += 1
        else:
            print('Маг пока жив')


    def atack(self, who):
        if who.HP > 0:
            who.HP -= self.damage
            if who.HP <= 0:
                who.is_dead()
            Mage.sum_damage += self.damage


    @staticmethod
    def create_skeleton(skeletons):
        skeleton = Skeleton()
        skeletons.append(skeleton)
        return skeletons


    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый магами урон: {Mage.sum_damage}')



class Skeleton:
    count_ex = 0
    def __init__(self):
        self.HP = 200
        self.damage = 50
        Skeleton.count_ex += 1
        Skeleton.sum_damage = 0


    @classmethod
    def count(cls):
        print(cls.count_ex)
        return cls.count_ex


    def is_dead(self):
        if self.HP <= 0:
            Skeleton.count_ex -= 1
            print('Скелет пал.')
            Skeleton.sum_dead += 1
        else:
            print('Скелет пока жив')


    def atack(self, who):
        if who.HP > 0:
            who.HP -= self.damage
            if who.HP <= 0:
                who.is_dead()
            Skeleton.sum_damage += self.damage

    
    def army_atack(self, who):
        for _ in range(Skeleton.count_ex):
            self.atack(who)


    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый скелетами урон: {Skeleton.sum_damage}')


Andre_from_Astora = Warrior()
Logan_big_hat = Mage()
mage2 = Mage() 

Logan_big_hat.atack(mage2)
Logan_big_hat.atack(mage2)


print(Andre_from_Astora.damage)
Andre_from_Astora.improve_damage()
print(Andre_from_Astora.damage)


mage2.sum_of_damage


skeletons = []
for _ in range(20):
    skeletons = Logan_big_hat.create_skeleton(skeletons)

skeletons[2].atack(Andre_from_Astora)


skeletons[2].army_atack(Andre_from_Astora)
Skeleton.count()
skeletons[3].sum_of_damage