import string
import random
import json

class Pokemon:
    def __init__(self, id, name, lvl):
        self.id = id
        self.lvl = lvl
        # self.id = id if id else self.generateId()
        self.name = name
        with open('pokemon_lvl.json') as f:
            data = json.load(f)
            for pokemon in data["pokemon"]:
                if self.name == pokemon["name"]:
                    for level_info in pokemon["levels"]:
                        if self.lvl == level_info['lvl']:
                            self.health = int(level_info["health"]) *"♥"
                            self.attack = level_info["attack"]
                            self.max_health = level_info["health"]
                            self.membership = level_info["membership"]



    def __repr__(self):
        return f' Id: {self.id}, Name: {self.name}, lvl: {self.lvl}'


    def generateId(self, length= 3):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


    def showPokemon(self):
        print(self)


    def levelUp(self):
        self.lvl += 1
