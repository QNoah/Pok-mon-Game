import pygame
import battle
import random
import os
import sys
import time
import json
from pokemon import Pokemon
from store import Store


board = [
    {"field": 1, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 2, "checkpoint": False, "power_up": None, "pokemon": 1},
    {"field": 3, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 4, "checkpoint": False, "power_up": "Merchant", "pokemon": None},
    #shop
    {"field": 5, "checkpoint": False, "power_up": None, "pokemon": 2},
    {"field": 6, "checkpoint": False, "power_up": "Health Potion", "pokemon": None},
    #healt 50% HP 
    {"field": 7, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 8, "checkpoint": False, "power_up": None, "pokemon": 3},
    {"field": 9, "checkpoint": False, "power_up": " Big_dice", "pokemon": None},
    #dobbelsteen met 8 of 9 ogen
    {"field": 10, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 11, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 12, "checkpoint": False, "power_up": None, "pokemon": 4},
    {"field": 13, "checkpoint": False, "power_up": "Damage potion", "pokemon": None},
    #multiplied damage 2x voor 1
    {"field": 14, "checkpoint": False, "power_up": "Merchant", "pokemon": None},
    #shop
    {"field": 15, "checkpoint": False, "power_up": None, "pokemon": 5},
    {"field": 16, "checkpoint": False, "power_up": "HyperPotion", "pokemon": None},
    #Healt 75% HP
    {"field": 17, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 18, "checkpoint": False, "power_up": None, "pokemon": 6},
    {"field": 19, "checkpoint": False, "power_up": "Mini-Shield", "pokemon": None},
    #blokkeert 25 damage 
    {"field": 20, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 21, "checkpoint": False, "power_up": "Amulet Coin", "pokemon": None},
    #verdubbelt aantal coins na 1 gevecht
    {"field": 22, "checkpoint": False, "power_up": None, "pokemon": 7},
    {"field": 23, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 24, "checkpoint": False, "power_up": "Merchant", "pokemon": None},
    #Shop
    {"field": 25, "checkpoint": False, "power_up": None, "pokemon": 8},
    {"field": 26, "checkpoint": False, "power_up": "HyperPotion", "pokemon": None},
    #healt 75% HP
    {"field": 27, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 28, "checkpoint": False, "power_up": None, "pokemon": 9},
    {"field": 29, "checkpoint": False, "power_up": "big_dice", "pokemon": None},
    #dobbelsteen met 8 of 9 ogen
    {"field": 30, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 31, "checkpoint": False, "power_up": "Max Potion", "pokemon": None},
    #restored alle HP
    {"field": 32, "checkpoint": False, "power_up": None, "pokemon": 10},
    {"field": 33, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 34, "checkpoint": False, "power_up": "Merchant", "pokemon": None},
    #shop
    {"field": 35, "checkpoint": False, "power_up": None, "pokemon": 11},
    {"field": 36, "checkpoint": False, "power_up": "Big Shield", "pokemon": None},
    #blokeert 50 damage
    {"field": 37, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 38, "checkpoint": False, "power_up": None, "pokemon": 12},
    {"field": 39, "checkpoint": False, "power_up": "Amulet Coin", "pokemon": None},
    #verdubbelt Coins na gevecht
    {"field": 40, "checkpoint": False, "power_up": None, "pokemon": 13},
    {"field": 41, "checkpoint": False, "power_up": "Damage Potion", "pokemon": None},
    #verdubbelt damage voor 1 attack
    {"field": 42, "checkpoint": False, "power_up": None, "pokemon": 14},
    {"field": 43, "checkpoint": False, "power_up": "Paralyze Potion", "pokemon": None},
    #als je Paralyze potion op enemy gooit kan hij 1 keer geen attack gooien
    {"field": 44, "checkpoint": False, "power_up": "Merchant", "pokemon": None},
    {"field": 45, "checkpoint": False, "power_up": None, "pokemon": 15},
    {"field": 46, "checkpoint": False, "power_up": "HyperPotion", "pokemon": None},
    #restored 75% HP
    {"field": 47, "checkpoint": False, "power_up": None, "pokemon": None},
    {"field": 48, "checkpoint": False, "power_up": None, "pokemon": 16},
    {"field": 49, "checkpoint": False, "power_up": "Max Potion", "pokemon": None},
    #restored alle HP
    {"field": 50, "checkpoint": False, "power_up": None, "pokemon": None}
]

pygame.mixer.music.set_volume(.1)
# start_theme = pygame.mixer.music.load("./music/start_theme.mp3")
# start_theme.set_volume(.1)
# adventure_theme = pygame.mixer.music.load("./music/adventure_theme.mp3")
# adventure_theme.set_volume(.1)

def playSound(sound):
    effectSound = pygame.mixer.Sound(f"./music/sounds/{sound}.mp3")
    effectSound.play()


def delayPrint(s, delay=0.05):
    for c in s:
        if c != "":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        elif c == '"':
            pass


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
        except ValueError:
            print("That is not a valid option")

        if starter == 1:
            myPokemon = Pokemon(id = 1,name = "Charmander", lvl = 1)
            playSound("select")
            return myPokemon.name
        elif starter == 2:
            myPokemon = Pokemon(id = 2, name = "Squirtle", lvl = 1)
            playSound("select")
            return myPokemon.name        
        elif starter == 3:
            myPokemon = Pokemon(id = 3,name = "Bulbasaur", lvl = 1)
            playSound("select")
            return myPokemon.name
        else:
            print("As far as I know there is no other pokemon here.")
            # chooseStarter()
        

def roll_dice(max_value=5):
    return random.randint(1, max_value)


def check_field(field):
    os.system("cls")
    message = f"Je staat op {field['field']}."

    if field['power_up']:
        if field['power_up'] == "Health Potion":
            message += "Je ontvangt hier een Health Potion power-up!"
        elif field['power_up'] == "Amulet Coin":
            message += "Je ontvangt hier een Amulet coin!"
        elif field['power_up'] == "Damage Potion":
            message += "Je ontvangt hier Damage Potion!"
        elif field['power_up'] == "HyperPotion":
            message += "Je ontvangt hier een HyperPotion!"
        elif field['power_up'] == "Max Potion":
            message += "Je ontvangt hier een Max Potion!"
        elif field['power_up'] == "big_dice":
            message += "Je kan met deze dobbelsteen maximaal 9 gooien in een gevecht!"
        elif field['power_up'] == "Paralyze Potion":
            message += "Je ontvangt hier een Paralyze Potion!"
        elif field['power_up'] == 'Merchant':
            with open('inventory.json') as invi:
                inv = json.load(invi)
            for itemsinInventory in inv["inventory"]:
                if itemsinInventory['id'] == 2:
                    Store(itemsinInventory['qty'])


    if field['pokemon']:
        pygame.mixer.music.pause()
        if battle.fight(field['pokemon'], myPokemon) == "lost":
            current_position = 5
            with open('pokemon_lvl.json') as f:
                data = json.load(f)
                for level_info in data["pokemons"]:
                    if level_info["lvl"] == myPokemon.lvl:
                        myPokemon.health = level_info["health"]
            return current_position

    if field['checkpoint']:
        message += "This is a checkpoint, your HP has been recovered!"
    return message

pygame.mixer.music.load("./music/start_theme.mp3")
pygame.mixer.music.play(loops= -1)
chooseStarter()
# delayPrint("""
# Professor Oak: 
# Ahhh... the smell of Pokemon, the best there could be!

# Professor Oak: 
# Welcome to the world of PokePython!

# Professor Oak: 
# There are lots of People waiting, Pokemon, and other different things for you.
# That means there are quite some things to experience!

# Professor Oak: There are some things I have to explain, but first choose your Starter Pokemon!
# """)
# namePokemon = chooseStarter()

# delayPrint(f"""
# Professor Oak:
# Are you sure you want to choose {namePokemon}? (y/n)""")
# while True:
#     pokemon_confirm = input().lower()
#     if pokemon_confirm == "y":
#         break
#     elif pokemon_confirm == "n":
#         namePokemon = chooseStarter()
#         delayPrint(f"""
# Professor Oak:
# Are you sure you want to choose {namePokemon}? (y/n)""")
#         continue
#     else:
#         delayPrint(f"""
# Professor Oak:
# I understand how most Pokemon behave, but I don't understand their language.
# are you sure you want to choose {namePokemon}? (y/n)
# """)

# delayPrint(f"""
# Professor Oak:
# Make sure to take good care of {namePokemon}, after all your Pokemon and you will be best buddies.
# """)

# time.sleep(2)
# delayPrint(""""
# Professor Oak: 
# But let me tell you a bit about your adventure. You and your Pokemon must get to the end of this region.
# But it won't be easy, on the way to the region there are angry Pokemons waiting for you to enter the grass.
# Here they will fight you and it is your choice to fight them to level up your Pokemon, or to run away and go back
# to your safe spot. (your pokemon would still be hurt if it has taken damage)
# """)

# input()
# delayPrint("""
# Professor Oak:
# There are items you can find or buy at the shop to make bigger steps towards the end or to heal your Pokemon.
# It can be hard to go through the first few steps so here take this use these items well..
# """)

# input()
# pygame.mixer.music.pause()
# playSound("obtain_item")
# print("Professor Oak gave you 5 coins")
# input(), print("Professor Oak gave you a healing potion")
# playSound("obtain_item")
# time.sleep(3)
# pygame.mixer.music.unpause()
# input()
# delayPrint("""
# Professor Oak:
# Alright then... I'll see you at the end..""")
# input()

pygame.mixer.music.load("./music/adventure_theme.mp3")
pygame.mixer.music.play(loops= -1)
# Dit hieronder veranderen naar een function die de level ophaalt en dan weet wat de max hp is
# MAX_HP = gethealth()
current_position = 1
current_hp = myPokemon.health

os.system("cls")
while current_position < 50:
    os.system('cls')
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
            # current_hp = MAX_HP
            print("You have passed or you are at a checkpoint. Your health has regenerated.")
    elif option == 3:
        current_position += 3

    current_field = board[current_position - 1]

    field_boodschap = check_field(current_field)
    print(field_boodschap)

    if current_field['checkpoint']:
        # current_hp = MAX_HP
        print("Your HP has been fully regenerated.")

print(f"Congratulations! You are an official Pokémon Champion.")

