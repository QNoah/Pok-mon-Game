import string
import random
import json

class Pokemon:
    def __init__(self, name, lvl, id=None):
        self.id = id if id else self.generateId()
        self.name = name
        self.lvl = lvl
        self.attack_damage = self.getAttackDamage(self.lvl)

    
    def __repr__(self):
        return f'Name: {self.name}, lvl: {self.lvl}'


    def generateId(self, length= 3):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    
    
    def getAttackDamage(self, lvl):
        with open('pokemon.json') as f:
            data = json.load(f)
            for level_info in data["levels"]:
                if level_info["level"] == lvl:
                    return level_info["attack"]
            return 0
    
    
    def showPokemon(self):
        print(self)
    
    # def levelUp(self, name, level)