#D&D

class Warrior:
    def __init__(self, HP, damage):
        self.HP = HP
        self.damage = damage
        count_ex = 0
        count_ex += 1

    @classmethod
    def count(cls):
        print(cls.count_obj)
        return cls.count_obj


    def atack(self, who):
        who.HP -= self.damage




class Mage:
    def __init__(self, HP, damage, mana):
        self.HP = HP
        self.damage = damage
        self.mana = mana
        count_ex = 0
        count_ex += 1

    @classmethod
    def count(cls):
        print(cls.count_obj)
        return cls.count_obj
    
    def atack(self, who):
        who.HP -= self.damage




class Dragon:
    def __init__(self, HP, damage):
        self.HP = HP
        self.damage = damage
        count_ex = 0
        count_ex += 1

    @classmethod
    def count(cls):
        print(cls.count_obj)
        return cls.count_obj
    
    def atack(self, who):
        who.HP -= self.damage




class skeleton:
    def __init__(self, HP, damage):
        self.HP = HP
        self.damage = damage
        count_ex = 0
        count_ex += 1

    @classmethod
    def count(cls):
        print(cls.count_obj)
        return cls.count_obj
    
    def atack(self, who):
        who.HP -= self.damage


Andre_from_Astora = Warrior(1000, 50)
Logan_big_hat = Mage(230, 200, 5000)

Andre_from_Astora.atack(Logan_big_hat)
