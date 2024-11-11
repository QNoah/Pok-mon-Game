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
    {"field": 3, "checkpoint": False, "power_up": "level_up", "pokemon": None},
    {"field": 4, "checkpoint": False, "power_up": "merchant", "pokemon": None},
    {"field": 5, "checkpoint": False, "power_up": None, "pokemon": 2},
    {"field": 6, "checkpoint": False, "power_up": "heal", "pokemon": None},
    {"field": 7, "checkpoint": True, "power_up": None, "pokemon": None},
    {"field": 8, "checkpoint": False, "power_up": None, "pokemon": 3},
    {"field": 9, "checkpoint": False, "power_up": "big_dice", "pokemon": None},
    {"field": 10, "checkpoint": False, "power_up": None, "pokemon": None}
]

pygame.mixer.music.set_volume(.1)
# start_theme = pygame.mixer.music.load("./music/start_theme.mp3")
# start_theme.set_volume(.1)
# adventure_theme = pygame.mixer.music.load("./music/adventure_theme.mp3")
# adventure_theme.set_volume(.1)

def playSound(sound):
    effectSound = pygame.mixer.Sound(f"./music/sounds/{sound}.mp3")
    effectSound.play()


def delay_print(s, delay=0.05):
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
        elif field['power_up'] == 'merchant':
            with open('inventory.json') as invi:
                inv = json.load(invi)
            for itemsinInventory in inv["inventory"]:
                if itemsinInventory['id'] == 1:
                    Store(itemsinInventory['qty'], myPokemon)


    if field['pokemon']:
        pygame.mixer.music.pause()
        battle.fight(field['pokemon'], myPokemon)

    if field['checkpoint']:
        message += "This is a checkpoint, your HP has been recovered!"

    return message

pygame.mixer.music.load("./music/start_theme.mp3")
pygame.mixer.music.play(loops= -1)
delay_print("""
Professor Oak: 
Ahhh... the smell of Pokemon, the best there could be!

Professor Oak: 
Welcome to the world of PokePython!

Professor Oak: 
There are lots of People waiting, Pokemon, and other different things for you.
That means there are quite some things to experience!

Professor Oak: There are some things I have to explain, but first choose your Starter Pokemon!
""")
namePokemon = chooseStarter()

delay_print(f"""
Professor Oak:
Are you sure you want to choose {namePokemon}? (y/n)""")
while True:
    pokemon_confirm = input().lower()
    if pokemon_confirm == "y":
        break
    elif pokemon_confirm == "n":
        namePokemon = chooseStarter()
        delay_print(f"""
Professor Oak:
Are you sure you want to choose {namePokemon}? (y/n)""")
        continue
    else:
        delay_print(f"""
Professor Oak:
I understand how most Pokemon behave, but I don't understand their language.
are you sure you want to choose {namePokemon}? (y/n)
""")

delay_print(f"""
Professor Oak:
Make sure to take good care of {namePokemon}, after all your Pokemon and you will be best buddies.
""")

time.sleep(2)
delay_print(""""
Professor Oak: 
But let me tell you a bit about your adventure. You and your Pokemon must get to the end of this region.
But it won't be easy, on the way to the region there are angry Pokemons waiting for you to enter the grass.
Here they will fight you and it is your choice to fight them to level up your Pokemon, or to run away and go back
to your safe spot. (your pokemon would still be hurt if it has taken damage)
""")

input()
delay_print("""
Professor Oak:
There are items you can find or buy at the shop to make bigger steps towards the end or to heal your Pokemon.
It can be hard to go through the first few steps so here take this use these items well..
""")

input()
pygame.mixer.music.pause()
playSound("obtain_item")
print("Professor Oak gave you 5 coins")
input(), print("Professor Oak gave you a healing potion")
playSound("obtain_item")
time.sleep(3)
pygame.mixer.music.unpause()
input()
delay_print("""
Professor Oak:
Alright then... I'll see you at the end..""")
input()

pygame.mixer.music.load("./music/adventure_theme.mp3")
pygame.mixer.music.play(loops= -1)

current_position = 1
current_hp = myPokemon.health
# Dit hieronder veranderen naar een function die de level ophaalt en dan weet wat de max hp is
MAX_HP = 20
# MAX_HP = gethealth()

os.system("cls")
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
        item_not_selected = True
        while item_not_selected:
            with open('inventory.json') as inv:
                items = json.load(inv)
                inventory = list(filter(lambda item: item['qty'] > 0, items['inventory']))
            
            for item in inventory:
                print(f"Option: {item['id']}, you have {item['qty']}x {item['name']}. It gives {item['attribute_value']} {item['attribute']} \n")
            
            wanna_use = input('Would you like to use anything? (Y/N): ')
            
            if wanna_use.lower() == 'n':
                break
            elif wanna_use.lower() == 'y':
                while wanna_use.lower() == 'y':
                    try:
                        item_choice = int(input('Choose your option: '))
                        
                        if any(item_choice == i['id'] for i in inventory):
                            for item in items['inventory']:
                                if item['id'] == item_choice:
                                    if item['attribute'] == "health":  # hp increase
                                        myPokemon.health += item['attribute_value']
                                        delay_print(f'You used a {item["name"]} and increased your health from {(myPokemon.health - item["attribute_value"])} to {myPokemon.health}\n')
                                        item['qty'] -= 1  # Deduct 1 from quantity
                                        print(f'You now have {item["qty"]} left of {item["name"]}')
                                        time.sleep(1)
                                    
                                    else:
                                        if item['name'] == "Coins":
                                            delay_print('You can only use this at the merchant')
                                            time.sleep(1)
                                        else:
                                            delay_print('You can only use this potion in battles')
                                    
                                    with open('inventory.json', 'w') as inv:
                                        json.dump(items, inv, indent=4)
                                    
                                    item_not_selected = False
                                    break
                        
                        else:
                            delay_print('Wrong option\n ')
                    
                    except ValueError:
                        delay_print("Wrong input\n ")
                    
                    item_not_selected = False
                    break
            else:
                delay_print('Wrong Input \n')
                continue

            

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
    elif option == 3:
        current_position += 1

    current_field = board[current_position - 1]

    field_boodschap = check_field(current_field)
    print(field_boodschap)

    if current_field['checkpoint']:
        current_hp = MAX_HP
        print("Your HP has been fully regenerated.")

print(f"Congratulations! You are an official Pokémon Champion.")

