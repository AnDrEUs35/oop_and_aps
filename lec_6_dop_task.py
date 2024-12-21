
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



def selected_atack(selected_units, selected_enemy):
    try:
        if len(selected_enemy) == len(selected_units):
            for i in range(len(selected_enemy)):
                selected_units[i] - (selected_enemy[i])
        else:
            raise Exception('Количество юнитов не соответстует количеству врагов')
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}')

class Warrior(Unit):

    count_ex = 0
    cost = 500

    def __init__(self):
        Warrior.sum_damage = 0
        self.HP = 1000
        self.damage = 100
        Warrior.count_ex += 1
        Warrior.sum_dead = 0
        self.dead = False


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество воинов всего')
        return cls.count_ex


    def _is_dead(self):
        if self.HP <= 0:
            Warrior.count_ex -= 1
            print('Воин пал.')
            Warrior.sum_dead += 1
            self.dead = True
            who_is_winner()
        else:
            print('Воин пока жив')


    def __sub__(self, who):
        if self.HP > 0:
            if who.HP > 0:
                who.HP -= self.damage
                Warrior.sum_damage += self.damage
                if who.HP <= 0:
                    who._is_dead()
        else:
            print('выбранный юнит мёртв')



    def improve_damage(self):
        if self.damage == 100:
            self.damage = 300
        elif self.damage == 300:
            self.damage = 100




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
        self.dead = False


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество магов всего')
        return cls.count_ex
    

    def _is_dead(self):
        if self.HP <= 0:
            Mage.count_ex -= 1
            print('Маг пал.')
            Mage.sum_dead += 1
            self.dead = True
            who_is_winner()
        else:
            print('Маг пока жив')


    def __sub__(self, who):
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


    def __mul__(self, selected_enemy): # атака метеоритом
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
            print('выбранный юнит мёртв или лишился маны, что одно и то же')


    
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
        self.dead = False


    @classmethod
    def count(cls):
        print(cls.count_ex, '- количество скелетов всего')
        return cls.count_ex


    def _is_dead(self):
        if self.HP <= 0:
            Skeleton.count_ex -= 1
            print('Скелет пал.')
            Skeleton.sum_dead += 1
            self.dead = True
            who_is_winner()
        else:
            print('Скелет пока жив')


    def __sub__(self, who):
        if self.HP > 0:
            if who.HP > 0:
                who.HP -= self.damage
                Skeleton.sum_damage += self.damage
                if who.HP <= 0:
                    who._is_dead()
        else:
            print('выбранный юнит мёртв')


class Player:
    def __init__(self):
        self.gold = 10000
        self.warriors = []
        self.mages = []
        self.skeletons = []

        self.alive_warriors = 0
        self.alive_mages = 0
        self.alive_skeletons = 0
    

    def spawn_unit(self, unit_class, number):
        assert number <= 0 or isinstance(number, int) == False
        if unit_class == Warrior:
            for _ in range(number):
                if self.gold >= unit_class.cost:
                    self.gold -= unit_class.cost
                    unit = unit_class()
                    self.warriors.append(unit)
                else:
                    print('мало золота')
        elif unit_class == Mage:
            for _ in range(number):
                if self.gold >= unit_class.cost:
                    self.gold -= unit_class.cost
                    unit = unit_class()
                    self.mages.append(unit)
                else:
                    print('мало золота')
    
    def desposition(self):
        for i in range(len(self.warriors)):
            if self.warriors[i].dead == False:
                self.alive_warriors += 1
        for i in range(len(self.mages)):
            if self.mages[i].dead == False:
                self.alive_mages += 1
        for i in range(len(self.skeletons)):
            if self.skeletons[i].dead == False:
                self.alive_skeletons += 1
        print(f'{self.alive_warriors} - живых воинов у игрока\n {self.alive_mages} - живых магов у игрока\n {self.alive_skeletons} - живых скелетов у игрока')
    

    def is_winner(self):
        if self == p1:
            winner1 = 0
            for i in range(len(p2.warriors)):
                if p2.warriors[i].dead == False:
                    return
            for i in range(len(p2.mages)):
                if p2.mages[i].dead == False:
                    return
            for i in range(len(p2.skeletons)):
                if p2.skeletons[i].dead == False:
                    return
            self.gold = 10000
            p2.gold = 10000
            print('Победил первый игрок')
            winner1 = 1
            return winner1
    
        elif self == p2:
            winner2 = 0
            for i in range(len(p1.warriors)):
                if p1.warriors[i].dead == False:
                    return
            for i in range(len(p1.mages)):
                if p1.mages[i].dead == False:
                    return
            for i in range(len(p1.skeletons)):
                if p1.skeletons[i].dead == False:
                    return
            self.gold = 10000
            p1.gold = 10000
            print('Победил второй игрок')
            winner2 = 1
            return winner2

def who_is_winner():
        winner1 = p1.is_winner()
        winner2 = p2.is_winner()
        if winner1 == 1 or winner2 == 1:
            p1.mages.clear()
            p1.warriors.clear()
            p1.skeletons.clear()

            p2.mages.clear()
            p2.warriors.clear()
            p2.skeletons.clear()




if __name__ == '__main__':
    p1 = Player()
    p2 = Player()

    p1.spawn_unit(Warrior, 10)
    p1.spawn_unit(Mage, 10)

    for _ in range(20):
        p1.mages[0].create_skeleton(p1.skeletons)


    p2.spawn_unit(Warrior, 10)
    p2.spawn_unit(Mage, 10)

    for _ in range(20):
        p2.mages[0].create_skeleton(p2.skeletons)


    print(p1.gold)

    # p1.warriors[2:3] + p2.warriors[5:7]

    p1.warriors[1] - p2.mages[1]
    p1.warriors[0] - p2.mages[1]
    p1.warriors[0] - p2.mages[1]
    

    p1.warriors[9].improve_damage()
    p1.warriors[9].info_about_unit()
    p1.warriors[9].improve_damage()
    p1.warriors[9].info_about_unit()
    
    p1.warriors[1] - p2.skeletons[1]

    p2.mages[2] - p1.skeletons[5]
    for _ in range(3):
        p1.mages[2] * p2.warriors[1:9]

    Warrior.count()
    p1.warriors[3] - p2.skeletons[2]
    selected_atack(p1.warriors[1:10], p2.skeletons[5:24])
    selected_atack(p2.skeletons[5:8], p1.mages[0:3])

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

    p1.mages[3] * p2.mages[0:10]
    p1.mages[4] * p2.warriors[0:10]
    p1.mages[4] * p2.warriors[0:10]
    p1.mages[5] * p2.skeletons[0:20]

    print(p1.gold, p2.gold)
    
    p1.spawn_unit(Warrior, 10)
    p2.spawn_unit(Mage, 5)

    for _ in range(20):
        p2.mages[0].create_skeleton(p2.skeletons)

    p1.desposition()
    p2.desposition()

    selected_atack(p1.warriors[1:10], p2.skeletons[5:14])
    selected_atack(p1.warriors[1:10], p2.skeletons[5:14])
