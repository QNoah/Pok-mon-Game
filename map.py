import battle
import random
import sys
import os
import time
from pokemon import Pokemon

board = [
    {"vakje": 1, "checkpoint": False, "power_up": None, "pokemon": None},
    {"vakje": 2, "checkpoint": False, "power_up": None, "pokemon": 1},
    {"vakje": 3, "checkpoint": False, "power_up": "level_up", "pokemon": None},
    {"vakje": 4, "checkpoint": False, "power_up": None, "pokemon": None},
    {"vakje": 5, "checkpoint": False, "power_up": None, "pokemon": 2},
    {"vakje": 6, "checkpoint": False, "power_up": "heal", "pokemon": None},
    {"vakje": 7, "checkpoint": True, "power_up": None, "pokemon": None},
    {"vakje": 8, "checkpoint": False, "power_up": None, "pokemon": 3},
    {"vakje": 9, "checkpoint": False, "power_up": "big_dice", "pokemon": None},
    {"vakje": 10, "checkpoint": False, "power_up": None, "pokemon": None}
]

def delayPrint(s, delay=0.1):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


def chooseStarter():
    global myPokemon
    print("1. Charmander")
    print("2. Squirtle")
    print("3. Bulbasaur")

    while True:
        try:
            starter = int(input())
            break
        except ValueError:
            print("That is not a valid option")
    
    if starter == 1:
        myPokemon = Pokemon(id = 1,name = "Charmander", lvl = 1)
    elif starter == 2:
        myPokemon = Pokemon(id = 2, name = "Squirtle", lvl = 1)
    elif starter == 3:
        myPokemon = Pokemon(id = 3,name = "Bulbasaur", lvl = 1)
    else:
        os.system("cls")
        print("As far as I know there is no other pokemon here.")
        chooseStarter()

def roll_dice(max_value=3):
    return random.randint(1, max_value)

def check_vakje(vakje):
    message = f"Je staat op {vakje['vakje']}."

    if vakje['power_up']:
        if vakje['power_up'] == "heal":
            message += "Je ontvangt hier een heal power-up!"
        elif vakje['power_up'] == "level_up":
            message += "Je ontvangt hier een level up!"
        elif vakje['power_up'] == "big_dice":
            message += "Je kan met deze dobbelsteen maximaal 8 gooien in een gevecht!"

    if vakje['pokemon']:
        battle.fight(vakje['pokemon'], myPokemon)

    if vakje['checkpoint']:
        message += " This is a checkpoint, your HP has been recovered!"

    return message

current_position = 1
current_hp = 20
MAX_HP = 20

delayPrint("Welcome to the world of Pokemon, choose your pokemon! \n")
chooseStarter()

while current_position < 10:
    print(f"You are at position {current_position} with {myPokemon.health} HP.")

    input("Press enter to roll...")
    os.system("cls")

    previous_position = current_position

    dice_roll = roll_dice()
    print(f"You rolled {dice_roll}.")

    current_position += dice_roll

    if current_position > 10:
        current_position = 10

    if previous_position < 7 <= current_position:
        current_hp = MAX_HP
        print("You have passed or you are at a checkpoint. Your health has regenerated.")

    current_vakje = board[current_position - 1]

    vakje_boodschap = check_vakje(current_vakje)
    print(vakje_boodschap)

    if current_vakje['checkpoint']:
        current_hp = MAX_HP
        print("Your HP has been fully regenerated.")

print(f"Congratulations! You are an official Pokémon Champion.")

