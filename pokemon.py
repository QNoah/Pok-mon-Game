import string
import random
import json

class Pokemon:
    def __init__(self, id, name, lvl):
        self.id = id
        # self.id = id if id else self.generateId()
        self.name = name
        with open('pokemon_lvl.json') as f:
            data = json.load(f)
            for level_info in data["levels"]:
                if level_info["lvl"] == lvl:
                    self.health = level_info["health"]
                    self.attack = level_info["attack"]
                    self.membership = level_info['membership']
        self.lvl = lvl


    def __repr__(self):
        return f' Id: {self.id}, Name: {self.name}, lvl: {self.lvl}'


    def generateId(self, length= 3):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


    def showPokemon(self):
        print(self)


    def levelUp(self):
        self.lvl += 1
