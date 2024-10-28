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
# imporove_damage() у воинов
# create_skeleton() у магов
# meteorite_atack() у магов
# army_atack()  у скелетов
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
        if self.HP > 0:
            if who.HP > 0:
                who.HP -= Warrior.damage
                Warrior.sum_damage += Warrior.damage
                if who.HP <= 0:
                    who.is_dead()
        else:
            print('выбранный юнит мёртв')
    @staticmethod
    def selected_atack(selected_units, selected_enemy):
        if len(selected_enemy) == len(selected_units):
            for i in range(len(selected_enemy)):
                selected_units[i].atack(selected_enemy[i])
        elif len(selected_enemy) > len(selected_units):
            print('выбрано недостаточно юнитов, один юнит может бить только одного противника')
        else:
            print('Выбрано недостаточно противников, их не хватает, чтобы мог участвовать каждый выбранный юнит')

    @classmethod
    def improve_damage(cls):
        if cls.damage == 100:
            cls.damage = 300
        elif cls.damage == 300:
            cls.damage = 100
    
    
    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый воинами урон: {Warrior.sum_damage}')

    
    def info_about_unit(self):
        print(f'{self.HP} - здоровье')
        print(f'{self.damage} - урон')

    @classmethod
    def info_about_class(cls):
        print(f'{cls.count_ex} - всего юнитов класса {cls}')
        print(f'{cls.sum_damage} - нанесено урона классом {cls}')
        print(f'{cls.sum_dead} - всего умерло из класса {cls}')



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
        if self.HP > 0:
            if who.HP > 0:
                who.HP -= self.damage
                if who.HP <= 0:
                    who.is_dead()
                Mage.sum_damage += self.damage
            else:
                print('Хватит бить мёртвых')
        else:
            print('выбранный юнит мёртв')
    
    @staticmethod
    def selected_atack(selected_units, selected_enemy):
        if len(selected_enemy) == len(selected_units):
            for i in range(len(selected_enemy)):
                selected_units[i].atack(selected_enemy[i])
        elif len(selected_enemy) > len(selected_units):
            print('выбрано недостаточно юнитов, один юнит может бить только одного противника')
        else:
            print('Выбрано недостаточно противников, их не хватает, чтобы мог участвовать каждый выбранный юнит')


    def meteorite_atack(self, selected_enemy):
        if self.HP > 0:
            for i in range(len(selected_enemy)):
                if selected_enemy[i].HP > 0:
                    selected_enemy[i].HP -= 500
                    if selected_enemy[i].HP <= 0:
                        selected_enemy[i].is_dead()
                    Mage.sum_damage += 500
                else:
                    print('Хватит бить мёртвых')
        else:
            print('выбранный юнит мёртв')


    @staticmethod
    def create_skeleton(skeletons):
        skeleton = Skeleton()
        skeletons.append(skeleton)
        return skeletons


    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый магами урон: {Mage.sum_damage}')

    
    def info_about_unit(self):
        print(f'{self.HP} - здоровье')
        print(f'{self.damage} - урон')


    @classmethod
    def info_about_class(cls):
        print(f'{cls.count_ex} - всего юнитов класса {cls}')
        print(f'{cls.sum_damage} - нанесено урона классом {cls}')
        print(f'{cls.sum_dead} - всего умерло из класса {cls}')



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
        if self.HP > 0:
            if who.HP > 0:
                who.HP -= self.damage
                Skeleton.sum_damage += self.damage
                if who.HP <= 0:
                    who.is_dead()
        else:
            print('выбранный юнит мёртв')


    @staticmethod
    def selected_atack(selected_units, selected_enemy):
        if len(selected_enemy) == len(selected_units):
            for i in range(len(selected_enemy)):
                selected_units[i].atack(selected_enemy[i])
        elif len(selected_enemy) > len(selected_units):
            print('выбрано недостаточно юнитов, один юнит может бить только одного противника')
        else:
            print('Выбрано недостаточно противников, их не хватает, чтобы мог участвовать каждый выбранный юнит')
    

    def army_atack(self, who):
        for _ in range(Skeleton.count_ex):
            self.atack(who)


    @property
    def sum_of_damage(self):
        print(f'Общий нанесённый скелетами урон: {Skeleton.sum_damage}')


    def info_about_unit(self):
        print(f'{self.HP} - здоровье')
        print(f'{self.damage} - урон')
    
    
    @classmethod
    def info_about_class(cls):
        print(f'{cls.count_ex} - всего юнитов класса {cls}')
        print(f'{cls.sum_damage} - нанесено урона классом {cls}')
        print(f'{cls.sum_dead} - всего умерло из класса {cls}')



Warrior_list = []
Mage_list = []
Skeleton_list = []
    
def spawn_unit(unit_class, class_list):
    unit = unit_class()
    class_list.append(unit)

for _ in range(10):
    spawn_unit(Warrior, Warrior_list)
    spawn_unit(Mage, Mage_list)

for _ in range(3):
    Warrior_list[0].atack(Mage_list[0])
Warrior_list[0].sum_of_damage

for _ in range(20):
    Mage_list[0].create_skeleton(Skeleton_list)

Warrior.count()
Mage.count()
Skeleton.count()

Warrior.improve_damage()
Warrior_list[0].info_about_unit()
Warrior.improve_damage()
Warrior_list[0].info_about_unit()

Skeleton_list[2].army_atack(Warrior_list[3])

Mage_list[2].atack(Skeleton_list[5])
for _ in range(3):
    Mage_list[1].meteorite_atack(Warrior_list[1:9])

Warrior.count()
Warrior_list[3].atack(Skeleton_list[2])
Warrior.selected_atack(Warrior_list[1:10], Skeleton_list[5:14])
Skeleton.selected_atack(Skeleton_list[5:8], Mage_list[0:3])

Warrior.info_about_class()
Mage.info_about_class()
Skeleton.info_about_class()

for i in range(len(Warrior_list)):
    Warrior_list[i].info_about_unit()
print('')

for i in range(len(Mage_list)):
    Mage_list[i].info_about_unit()
print('')

for i in range(len(Skeleton_list)):
    Skeleton_list[i].info_about_unit()