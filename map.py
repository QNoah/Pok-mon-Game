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

start_theme = pygame.mixer.Sound("./music/start_theme.mp3")
start_theme.set_volume(.1)

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
    print("""
    Choose your pokemon:
    1. Charmander
    2. Squirtle
    3. Bulbasaur
    """)

    while True:
        try:
            starter = int(input())
            break
        except ValueError:
            print("That is not a valid option")
    
    if starter == 1:
        myPokemon = Pokemon(id = 1,name = "Charmander", lvl = 1)
        return myPokemon.name
    elif starter == 2:
        myPokemon = Pokemon(id = 2, name = "Squirtle", lvl = 1)
        return myPokemon.name        
    elif starter == 3:
        myPokemon = Pokemon(id = 3,name = "Bulbasaur", lvl = 1)
        return myPokemon.name
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

start_theme.play(loops=-1)
delayPrint("""
Professor Oak: Ahhh... the smell of Pokemon, the best there could be!
Professor Oak: Welcome to the world of PokePython!
Professor Oak: There are waiting a lot of People, Pokemon, and lots of
                other different things for you. That means there are quite some things to experience!
Professor Oak: There are some things I have to explain, but first choose your Starter Pokemon!
""")
namePokemon = chooseStarter()
delayPrint(f"""
Professor Oak: Are you sure you want to choose {namePokemon} (y/n)""")
while True:
    pokemon_confirm = input().lower()
    if pokemon_confirm == "y":
        break
    elif pokemon_confirm == "n":
        namePokemon = chooseStarter()
        delayPrint(f"""
Professor Oak: Are you sure you want to choose {namePokemon} (y/n)""")
        continue
    else:
        delayPrint("""
Professor Oak: I don't understand Pokemon language, but are you sure? (y/n)
""")


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

