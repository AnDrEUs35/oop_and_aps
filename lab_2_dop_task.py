# Стратегия, которая изначально должна была быть D&D.
# Пока есть только воины, маги и скелеты, которых эти маги могут создавать. Каждый класс умеет считать количество своих экземпляров,
# которое может изменяться, и уменьшаться в том числе. Каждый класс имеет атрибуты: здоровье и урон. Все классы могут проверять состояние экземпляров: жив или
# нет. Если нет, то уменьшаем количество экземпляров и увеличиваем сумму умерших.
# У каждого класса есть метод, считающий общее количество нанесённого урона. Также у всех классов есть метод атаки, который принимает аргумент, кого бить. У классов есть свои
# особенные атаки. Так, маги могут создавать скелетов, воины могут увеличивать свой урон(для всех воинов сразу), скелеты могут всей толпой напасть на одного врага (всё за одно действие).

# Справка:
# Игрок может создавать сколько угодно юнитов при помощи метода spawn_unit(класс создаваемого юнита) класса Player
# Может управлять этими юнитами с помощью метода atack(кого), который есть в каждом классе.
# Может использовать особые способности классов:
# imporove_damage у воинов
# create_skeleton у магов
# army_atack  у скелетов
# Может получать информацию о том, жив ли юнит с помощью метода sum_of_damage у каждого класса
# Может узнавать, жив ли юнит при помощи is_dead() у каждого класса
# Может получить информацию о конкретном юните через метод info_about_unit(юнит) класса Player
# Может получить информацию о конкретном классе через метод info_about_class(класс) класса Player

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
        print(cls.count_ex, '- количество воинов')
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
        if cls.damage == 100:
            cls.damage = 300
        elif cls.damage == 300:
            cls.damage = 100
    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый воинами урон: {Warrior.sum_damage}')




class Mage:

    count_ex = 0

    def __init__(self):
        self.HP = 300
        self.damage = 200
        Mage.count_ex += 1
        Mage.sum_damage = 0
        Mage.sum_dead = 0


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество магов')
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
        else:
            print('Хватит бить мёртвых')

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
        Skeleton.sum_dead = 0


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество скелетов')
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
            Skeleton.sum_damage += self.damage
            if who.HP <= 0:
                who.is_dead()

    
    def army_atack(self, who):
        for _ in range(Skeleton.count_ex):
            self.atack(who)


    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый скелетами урон: {Skeleton.sum_damage}')


class Player:
    def __init__(self):
        self.Warrior_list = []
        self.Mage_list = []
        self.Skeleton_list = []
    
    def spawn_unit(self, unit_class):
        unit = unit_class()
        if unit_class == Warrior:
            self.Warrior_list.append(unit)
        elif unit_class == Mage:
            self.Mage_list.append(unit)

    def info_about_unit(self, unit):
        print(f'{unit.HP} - здоровье')
        print(f'{unit.damage} - урон')


    def info_about_class(self, cls):
        print(f'{cls.count_ex} - всего юнитов класса {cls}')
        print(f'{cls.sum_damage} - нанесено урона классом {cls}')
        print(f'{cls.sum_dead} - всего умерло из класса {cls}')    
    
player = Player()
for _ in range(5):
    player.spawn_unit(Warrior)
    player.spawn_unit(Mage)
for _ in range(3):
    player.Warrior_list[0].atack(player.Mage_list[0])
player.Warrior_list[0].sum_of_damage

for _ in range(20):
    player.Mage_list[0].create_skeleton(player.Skeleton_list)

Warrior.count()
Mage.count()
Skeleton.count()

Warrior.improve_damage()
player.info_about_unit(player.Warrior_list[0])
Warrior.improve_damage()
player.info_about_unit(player.Warrior_list[0])

player.Skeleton_list[0].army_atack(player.Warrior_list[3])

player.Mage_list[2].atack(player.Skeleton_list[5])

Warrior.count()

player.info_about_unit(player.Mage_list[0])
player.info_about_class(Mage)
