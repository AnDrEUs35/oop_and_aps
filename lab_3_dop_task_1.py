class Unit:


    def info_about_unit(self):
        print(f'{self.HP} - здоровье')
        print(f'{self.damage} - урон')
        if isinstance(self, Mage) == True:
            print(f'{self.mana} - мана') 


    @classmethod
    def info_about_class(cls):
        print(f'{cls.count_ex} - всего юнитов класса {cls}')
        print(f'{cls.sum_damage} - нанесено урона классом {cls}')
        print(f'{cls.sum_dead} - всего умерло из класса {cls}')


    @staticmethod
    def selected_atack(selected_units, selected_enemy):
        if len(selected_enemy) == len(selected_units):
            for i in range(len(selected_enemy)):
                selected_units[i].atack(selected_enemy[i])
        elif len(selected_enemy) > len(selected_units):
            print('выбрано недостаточно юнитов, один юнит может бить только одного противника')
        else:
            print('Выбрано недостаточно противников, их не хватает, чтобы мог участвовать каждый выбранный юнит')




class Warrior(Unit):

    count_ex = 0
    cost = 500

    def __init__(self):
        Warrior.sum_damage = 0
        self.HP = 1000
        Warrior.damage = 100
        Warrior.count_ex += 1
        Warrior.sum_dead = 0


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество воинов всего')
        return cls.count_ex


    def _is_dead(self):
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
                    who._is_dead()
        else:
            print('выбранный юнит мёртв')


    @classmethod
    def improve_damage(cls):
        if cls.damage == 100:
            cls.damage = 300
        elif cls.damage == 300:
            cls.damage = 100




class Mage(Unit):

    count_ex = 0
    cost = 700

    def __init__(self):
        self.HP = 300
        self.damage = 200
        Mage.count_ex += 1
        Mage.sum_damage = 0
        Mage.sum_dead = 0
        self.mana = 2000


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество магов всего')
        return cls.count_ex
    

    def _is_dead(self):
        if self.HP <= 0:
            Mage.count_ex -= 1
            print('Маг пал.')
            Mage.sum_dead += 1
        else:
            print('Маг пока жив')


    def atack(self, who):
        if self.HP > 0 and self.mana >= 20:
            if who.HP > 0:
                self.mana -= 20
                who.HP -= self.damage
                if who.HP <= 0:
                    who._is_dead()
                Mage.sum_damage += self.damage
            else:
                print('Хватит бить мёртвых')
        else:
            print('выбранный юнит мёртв или лишился маны, что одно и то же')


    def meteorite_atack(self, selected_enemy):
        if self.HP > 0 and self.mana >= 1000:
            self.mana -= 1000
            for i in range(len(selected_enemy)):
                if selected_enemy[i].HP > 0:
                    selected_enemy[i].HP -= 500
                    if selected_enemy[i].HP <= 0:
                        selected_enemy[i]._is_dead()
                    Mage.sum_damage += 500
                else:
                    print('Хватит бить мёртвых')
        else:
            print('выбранный юнит мёртв')


    
    def create_skeleton(self, skeletons):
        if self.mana >= 100:
            self.mana -= 100
            skeleton = Skeleton()
            skeletons.append(skeleton)
        return skeletons




class Skeleton(Unit):

    count_ex = 0

    def __init__(self):
        self.HP = 200
        self.damage = 50
        Skeleton.count_ex += 1
        Skeleton.sum_damage = 0
        Skeleton.sum_dead = 0


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество скелетов всего')
        return cls.count_ex


    def _is_dead(self):
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
                    who._is_dead()
        else:
            print('выбранный юнит мёртв')
    

    def army_atack(self, who):
        for _ in range(Skeleton.count_ex):
            self.atack(who)


class Player:
    def __init__(self):
        self.gold = 10000
        self.warriors = []
        self.mages = []
        self.skeletons = []
    

    def spawn_unit(self, unit_class, class_list, number):
            for _ in range(number):
                if self.gold >= unit_class.cost:
                    self.gold -= unit_class.cost
                    unit = unit_class()
                    class_list.append(unit)
                else:
                    print('мало золота')


if __name__ == '__main__':
    p1 = Player()
    p2 = Player()

    p1.spawn_unit(Warrior, p1.warriors, 10)
    p1.spawn_unit(Mage, p1.mages, 10)

    for _ in range(20):
        p1.mages[0].create_skeleton(p1.skeletons)


    p2.spawn_unit(Warrior, p2.warriors, 10)
    p2.spawn_unit(Mage, p2.mages, 10)

    for _ in range(20):
        p2.mages[0].create_skeleton(p2.skeletons)


    print(p1.gold)

    p1.warriors[0].atack(p2.mages[0])
    p1.warriors[0].atack(p2.mages[0])
    p1.warriors[0].atack(p2.mages[0])

    Warrior.improve_damage()
    p1.warriors[0].info_about_unit()
    Warrior.improve_damage()
    p1.warriors[0].info_about_unit()
    p1.warriors[1].atack(p2.skeletons[1])

    p2.skeletons[2].army_atack(p1.warriors[3])

    p2.mages[2].atack(p1.skeletons[5])
    for _ in range(3):
        p1.mages[1].meteorite_atack(p2.warriors[1:9])

    Warrior.count()
    p1.warriors[3].atack(p2.skeletons[2])
    Warrior.selected_atack(p1.warriors[1:10], p2.skeletons[5:14])
    Skeleton.selected_atack(p2.skeletons[5:8], p1.mages[0:3])

    Warrior.info_about_class()
    Mage.info_about_class()
    Skeleton.info_about_class()

    for i in range(len(p1.warriors)):
        p1.warriors[i].info_about_unit()
    print('')

    for i in range(len(p2.mages)):
        p2.mages[i].info_about_unit()
    print('')

    for i in range(len(p1.skeletons)):
        p1.skeletons[i].info_about_unit()

    print(p1.gold)

    Warrior.count()
    Mage.count()
    Skeleton.count()
