class Puppy:
    def __init__(self, states, index):
        self.states = {'1': 'болеет', '2': 'выздоравливает', '3': 'здоров'}
        self.index = index
        self.state = states['1']
    def get_treatment(self):
        if self.state == 'болеет':
            self.state = self.states['2']
        elif self.state == 'выздоравливает':
            self.state = self.states['3']
    def is_healthy(self):
        if self.state == self.states['3']:
            print('щенок здоров')

class Dog:
    def __init__(self, N):
        self.puppies = []

class Vet:
    def __init__(self):
        pass

d = Dog(3)

    
