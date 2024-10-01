from pokemon import Pokemon
from encounter import Encounter

myPokemon = Pokemon(name = "Squirtle", lvl = 1)
myPokemon.showPokemon()
encounter = Encounter(1)

def Attack():
    pass
    
    
print(f"A wild {encounter.name} has appeared.")

myPokemon.levelUp()
myPokemon.showPokemon()