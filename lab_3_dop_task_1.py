class Unit:


    def info_about_unit(self):
        print(f'{self.HP} - здоровье')
        print(f'{self.damage} - урон')


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
    

    def _is_dead(self):
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
                    who._is_dead()
                Mage.sum_damage += self.damage
            else:
                print('Хватит бить мёртвых')
        else:
            print('выбранный юнит мёртв')


    def meteorite_atack(self, selected_enemy):
        if self.HP > 0:
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


    @staticmethod
    def create_skeleton(skeletons):
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
        print(cls.count_ex, '- количество скелетов')
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


if __name__ == '__main__':


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

    for _ in range(20):
        Mage_list[0].create_skeleton(Skeleton_list)

    Warrior.count()
    Mage.count()
    Skeleton.count()

    Warrior.improve_damage()
    Warrior_list[0].info_about_unit()
    Warrior.improve_damage()
    Warrior_list[0].info_about_unit()
    Warrior_list[1].atack(Skeleton_list[1])

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

    Warrior_list[9].atack(Skeleton_list[1])