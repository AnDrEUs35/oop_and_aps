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
    
    def __bool__(self):
        return len(self.planets) > 0
    
    def __str__(self):
        return f'Название системы {self.name}, её планеты {self.planets}'
    
    def __getitem__(self, key):
        return self.planets[key]
    
system = StarSystem(['planet_1', 'planet_2', 'planet_3'], 'StarSystem1')

#len
print(len(system))

#add
system = system + 'planet_4'
print(system.planets)

# radd
system = 'planet_5' + system
print(system.planets)

# iadd
system_1 = StarSystem(['planet_1'], 'System_1')
system_1 += 'planet_2'
print(system_1.planets)


# bool
system_1 = StarSystem(['planet_1', 'planet_2'], 'System_1')
system_2 = StarSystem([], 'System_2')
 
print(bool(system_1))
print(bool(system_2))

# str
system_1 = StarSystem(['planet_1', 'planet_2'], 'System_1')
print(system_1)

# getitem
system_1 = StarSystem(['planet_1', 'planet_2'], 'System_1')
print(system_1[0])
print(system_1[0:2])