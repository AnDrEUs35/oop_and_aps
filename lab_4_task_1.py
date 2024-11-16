class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name

    
    def __len__(self):
        return len(self.planets) # будет выводить кол-во планет при обращении к экземпляру класса
    
    def __add__(self, other):
        planets_1 = self.planets[:]
        planets_1.append(other)
        return StarSystem(planets_1, self.name)
    
    def __radd__(self, other):
        planets_1 = self.planets[:]
        planets_1.insert(0, other)
        return StarSystem(planets_1, self.name)
    
    def __iadd__(self, other):
        self.planets.append(other)
        return self
    
    
    def __sub__(self, other):
        planets_1 = self.planets[:]
        planets_1.remove(other)
        return StarSystem(planets_1, self.name)
    
    def __rsub__(self, other):
        pass
    
    def __isub__():
        return
    
    
system = StarSystem(['planet_1', 'planet_2', 'planet_3'], 'StarSystem1')

#add
system = system + 'planet_4'
print(system.planets)

# radd
system = 'planet_5' + system
print(system.planets)

# iadd
system += 'planet_6'
print(system.planets)


system = system - 'planet_2'
print(system.planets)

