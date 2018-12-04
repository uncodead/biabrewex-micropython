import yaml

def constructor(name):
    def iconstructor(cls):
        yaml.add_constructor(
            name, 
            lambda l, n: cls(**l.construct_mapping(n))
        )
    return iconstructor

@constructor('!Recipe')
class Recipe():
    def __init__(self, name, wort, boil):
        self.name = name
        self.wort = wort
        self.boil = boil

@constructor('!Wort')
class Wort():
    def __init__(self, mashin, steps):
        self.mashin = mashin
        self.steps = steps

@constructor('!Step')
class Step():
    def __init__(self, name, duration, temperature, recirculate):
        self.name = name
        self.duration = duration
        self.temperature = temperature
        self.recirculate = recirculate

@constructor('!Boil')
class Boil():
    def __init__(self, duration, additions):
        self.duration = duration
        self.additions = additions

@constructor('!Addition')
class Addition():
    def __init__(self, name, instant):
        self.name = name
        self.instant = instant

with open('recipe.yaml', 'r') as f:
    recipe = yaml.load(f)
    print(recipe)
