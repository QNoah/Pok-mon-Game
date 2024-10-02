from pokemon import Pokemon
from encounter import Encounter_Pokemon
import json
import random
import sys
import time
import os

myPokemon = Pokemon(name = "Squirtle", lvl = 1)

def delay_print(s, delay=0.1):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print() 


# myPokemon.showPokemon()
def setEncounter(id):
    encounter = Encounter_Pokemon(id)
    print(encounter)
    return encounter
    

turn = "player"
def fight(id):
    encounter = setEncounter(id)
    global turn
    delay_print(f"A wild {encounter.name} has appeared!")
    delay_print(f"You chose {myPokemon.name}")
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
                        delay_print(f'{myPokemon.name} has leveled up!')
                        myPokemon.levelUp()
                        delay_print(f'{myPokemon.name} is now lvl {myPokemon.lvl}')
                    else:
                        delay_print(f'{encounter.name} is at {encounter.health}HP')
                        time.sleep(1)
            elif _ == 3:
                with open('inventory.json') as inv:
                    items = json.load(inv)
                    for item in items:
                        if item['stock'] != 0:
                            print("You have ")
                    if len(items) == 0:
                        print("You don't have any items in your inventory.")
                    elif True:
                        print("Choose an item: ")
                        with open('inventory.json') as inv:
                            items = json.load(inv)
                            for item in items:
                                print(item)
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


# fight()


# myPokemon.showPokemon()