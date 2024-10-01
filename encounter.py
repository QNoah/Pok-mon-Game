import json

class Encounter_Pokemon:
    def __init__(self, id):
        self.id = id
        with open('encounters.json') as f:
            data = json.load(f)
            for pokemon_details in data["encounters"]:
                if pokemon_details["id"] == self.id:
                    self.name = pokemon_details['name']
                    self.lvl = pokemon_details['lvl']
                    self.health = pokemon_details['health']
                    self.attack = pokemon_details['attack']
                else:
                    self.name = None
                    self.lvl = None
                    self.health = None
                    self.attack = None