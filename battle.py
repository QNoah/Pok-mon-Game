from pokemon import Pokemon
from encounter import Encounter
import random
import sys
import time
import os

def delay_print(s, delay=0.1):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print() 


myPokemon = Pokemon(name = "Squirtle", lvl = 1)
myPokemon.showPokemon()
encounter = Encounter(1)

turn = "player"
def fight():
    global turn
    while myPokemon.health > 0 and encounter.health > 0:
        if turn == "player":
            print("What is your next move?")
            print("1. Escape (Go back the steps you rolled.)")
            print(f"2. Fight (roll 0 > {myPokemon.attack})")
            print(f"3. Use a item")
            _ = int(input())
            if _ == 1:
                pass
                # lose()
            elif _ == 2:
                damage = random.randint(0, myPokemon.attack)
                if damage == 0:
                    os.system("cls")
                    delay_print(f'{myPokemon.name} missed the attack!')
                    time.sleep(1)
                else:
                    os.system("cls")
                    delay_print(f'{myPokemon.name} did {damage} damage to {encounter.name}')
                    encounter.health -= damage
                    time.sleep(1)
                    if encounter.health <= 0:
                        delay_print(f'{encounter.name} fainted.')
                        delay_print(f'{myPokemon.name} wins!')
                    else:
                        delay_print(f'{encounter.name} is at {encounter.health}HP')
                        time.sleep(1)


                turn = "cpu"
        elif turn == "cpu":
            damage = random.randint(0, encounter.attack)
            if damage == 0:
                os.system("cls")
                delay_print(f'{encounter.name} missed the attack!')
                time.sleep(1)
            else:
                os.system("cls")
                delay_print(f'{encounter.name} did {damage} damage to {myPokemon.name}')
                myPokemon.health -= damage
                time.sleep(3)
                if myPokemon.health <= 0:
                    delay_print(f'{myPokemon.name} fainted.')
                    delay_print(f'{encounter.name} wins!')
                else:
                    delay_print(f'{myPokemon.name} is at {myPokemon.health}HP')
                    time.sleep(1)
            turn = "player"


delay_print(f"A wild {encounter.name} has appeared!")
delay_print(f"You chose {myPokemon.name}")
fight()

# myPokemon.levelUp()
# myPokemon.showPokemon()