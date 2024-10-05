import random as r

class Puppy:


    def __init__(self, index):
        self.states = ['болеет', 'выздоравливает', 'здоров']
        self.index = index
        self.state = r.choice(self.states)
    

    def get_treatment(self):
        chance = r.randint(0, 1)
        if self.state == 'болеет' and chance == 1:
            self.state = self.states[1]
        elif self.state == 'выздоравливает' and chance == 1:
            self.state = self.states[2]
    

    def is_healthy(self):
        if self.state == self.states[2]:
            return True
        else:
            return False


class Dog():
    def __init__(self, index, N):
        self.states = ['болеет', 'выздоравливает', 'здоров']
        self.index = index
        self.state = r.choice(self.states)
        self.puppies = []
        for i in range(N+1):
            p = Puppy(i)
            self.puppies.append(p)
    
    def heal_all(self):
        for i in range(len(self.puppies)):
            p = self.puppies[i]
            p.get_treatment()
        print('Щенки подлечились')


    def get_treatment(self):
        if self.state == 'болеет':
            self.state = self.states[1]
        elif self.state == 'выздоравливает':
            self.state = self.states[2]
    
    
    def is_healthy(self):
        if self.state == self.states[2]:
            return True
        else:
            return False
    

    def all_are_healthy(self):
        count = 0
        for i in range(len(self.puppies)):
            p = self.puppies[i]
            result = p.is_healthy()
            if result == True:
                count += 1
        if count == len(self.puppies):
            return True
    
    def give_away_all(self):
        self.puppies.clear()


class Vet:
    def __init__(self, name, obj_N):
        self.name = name
        self.plant = Dog(0, obj_N)
    
    def work(self):
        self.plant.get_treatment()
    
    def care(self):
        healthy = self.plant.all_are_healthy()
        if healthy == True:
            self.plant.give_away_all()
            return True
        else:
            print('Не все щенки здоровы!')
            return False
    
    def knowledge_base(self):
        if self.plant.is_healthy() == True:
            print('Собака здорова')
        else:
            print('Собака пока не здорова')
        if self.plant.all_are_healthy() == True:
            print('Щенки здоровы')
        else:
            print('Щенки еще не здоровы')
        if self.care() == True:
            print('Щенки отданы')
        else:
            print('Щенки пока не отданы')
        

if __name__ == '__main__':
    v = Vet('Andrew', 4)
    while True:
        v.knowledge_base()
        v.plant.heal_all()
        v.work()
        v.care()
        v.knowledge_base()
        if v.plant.is_healthy() == True and v.plant.all_are_healthy() == True:
            break

    
