import pygame
import battle
import random
import os
import sys
import time
from pokemon import Pokemon

board = [
    {"field": 1, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 2, "checkpoint": False, "power_up": None, "pokemon": 1},
    {"field": 3, "checkpoint": False, "power_up": "level_up", "pokemon": None},
    {"field": 4, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 5, "checkpoint": False, "power_up": None, "pokemon": 2},
    {"field": 6, "checkpoint": False, "power_up": "heal", "pokemon": None},
    {"field": 7, "checkpoint": True, "power_up": None, "pokemon": None},
    {"field": 8, "checkpoint": False, "power_up": None, "pokemon": 3},
    {"field": 9, "checkpoint": False, "power_up": "big_dice", "pokemon": None},
    {"field": 10, "checkpoint": False, "power_up": None, "pokemon": None}
]
def playSound(sound):
    effectSound = pygame.mixer.Sound(f"./music/sounds/{sound}.mp3")
    effectSound.play()


def delayPrint(s, delay=0.05):
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
    playSound("select")    
    os.system("cls")

def roll_dice(max_value=3):
    return random.randint(1, max_value)


def check_field(field):
    os.system("cls")
    message = f"Je staat op {field['field']}."

    if field['power_up']:
        if field['power_up'] == "heal":
            message += "Je ontvangt hier een heal power-up!"
        elif field['power_up'] == "level_up":
            message += "Je ontvangt hier een level up!"
        elif field['power_up'] == "big_dice":
            message += "Je kan met deze dobbelsteen maximaal 8 gooien in een gevecht!"

    if field['pokemon']:
        battle.fight(field['pokemon'], myPokemon)

    if field['checkpoint']:
        message += "This is a checkpoint, your HP has been recovered!"

    return message


delayPrint("Welcome to the world of Pokemon, choose your pokemon! \n")
chooseStarter()

current_position = 1
current_hp = myPokemon.health
# Dit hieronder veranderen naar een function die de level ophaalt en dan weet wat de max hp is
MAX_HP = 20

while current_position < 10:
    print(f"You are at position {current_position} with {myPokemon.health} HP.")
    print("1. View inventory\n2. Roll")
    while True:
        try:
            option = int(input("Choose an option:"))
            break
        except ValueError:
            print("Not a valid option")
            continue
        
    os.system("cls")
    if option == 1:
        pass
    elif option == 2:
        previous_position = current_position
        dice_roll = roll_dice()
        playSound("dice_roll")
        print(f"You rolled {dice_roll}.")
        time.sleep(1)
        current_position += dice_roll
        if current_position > 10:
            current_position = 10
        elif previous_position < 7 <= current_position:
            current_hp = MAX_HP
            print("You have passed or you are at a checkpoint. Your health has regenerated.")

    current_field = board[current_position - 1]

    field_boodschap = check_field(current_field)
    print(field_boodschap)

    if current_field['checkpoint']:
        current_hp = MAX_HP
        print("Your HP has been fully regenerated.")

print(f"Congratulations! You are an official Pokémon Champion.")

