from pokemon import Pokemon
from encounter import Encounter_Pokemon
import pygame 
import json
import random
import sys
import time
import os

pygame.mixer.init()
# tes
battleSong = pygame.mixer.Sound("./music/battle_theme.mp3")
victorySong = pygame.mixer.Sound("./music/Victory_Theme.mp3")
battleSong.set_volume(.3)

def playSound(sound, vol):
    effectSound = pygame.mixer.Sound(f"./music/battle_sounds/{sound}.mp3")
    effectSound.set_volume(vol)
    effectSound.play()


def delay_print(s, delay=0.08):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def fight(id, myPokemon):
    battleSong.play(loops=-1)
    os.system("cls")
    turn = "player"
    enemy = Encounter_Pokemon(id)
    delay_print(f"A wild {enemy.name} has appeared!")
    playSound("Pokemon Out", 0.3)
    delay_print(f"You chose {myPokemon.name}")
    damage_multiplier = 1
    enemy_damage_multiplier = 1
    while myPokemon.health > 0 and enemy.health > 0:
        if turn == "player":
            print("What is your next move?")
            print("1. Escape (Go back the steps you rolled.)")
            print(f"2. Fight (roll 0 > {myPokemon.attack})")
            print(f"3. Use a item (work in project)")
            while True:
                try:
                    _ = int(input())
                    break
                except ValueError:
                    print("Not a valid option")
                    continue
            playSound("select", 1)
            if _ == 1:
                pass
                # lose()
            elif _ == 2:
                damage = random.randint(0, myPokemon.attack) * damage_multiplier
                print(f"[DEBUG] Damage Multiplier: {damage_multiplier}, Calculated Damage: {damage}")
                if damage == 0:
                    os.system("cls")
                    time.sleep(1)
                    playSound("dodge", 1)
                    delay_print(f'{myPokemon.name} used tackle but missed the attack!')
                    time.sleep(1)
                else:
                    time.sleep(1)
                    playSound("tackle", 1)
                    time.sleep(2)
                    playSound("Hit Normal Damage", 1)
                    os.system("cls")
                    delay_print(f'{myPokemon.name} did {damage} damage to {enemy.name}')
                    enemy.health -= damage
                    time.sleep(1)
                    if enemy.health <= 0:
                        playSound("In-Battle Faint No Health", 1)
                        delay_print(f'{enemy.name} fainted.')
                        time.sleep(1)
                        delay_print(f'{myPokemon.name} has leveled up!')
                        myPokemon.levelUp()
                        time.sleep(1)
                        delay_print(f'{myPokemon.name} is now lvl {myPokemon.lvl}')
                        # playSound()
                        time.sleep(1)
                        battleSong.stop(), victorySong.play()
                        delay_print(f'{myPokemon.name} wins!')
                        while True:
                            _ = input("Continue? (y/n)").lower()
                            if _ == "y":
                                playSound("select", 1)
                                victorySong.stop()
                                break
                            elif _ == "n":
                                playSound("select", 1)
                                continue
                            else:
                                continue
                    else:
                        delay_print(f'{enemy.name} is at {enemy.health}HP')
                        time.sleep(1)
            elif _ == 3:
                os.system("cls")
                item_not_selected = True
                while item_not_selected:
                    with open('C:/Users/nitro/PokePython-1/inventory.json', 'r') as inv:
                        items = json.load(inv)
                        available_items = [
                            item for item in items['inventory']
                            if item['qty'] > 0 and item['id'] != 1
                        ]
                        if available_items:
                            print("Available Items:")
                            for item in available_items:
                                print(f"Option: {item['id']}, Item: {item['name']}, Qty: {item['qty']}, "
                                    f"Effect: {item['attribute_calc']} {item['attribute_value']} {item['attribute']}")
                        else:
                            delay_print("No usable items in your inventory!")
                            break

                    time.sleep(1)
                    delay_print("Choose your item (Enter the Option ID):")

                    try:
                        item_choice = int(input())
                    except ValueError:
                        print("Invalid input. Please enter a valid Option ID.")
                        continue

                    selected_item = next((item for item in available_items if item['id'] == item_choice), None)
                    if not selected_item:
                        print("Invalid choice or item not available.")
                        continue

                    selected_item['qty'] -= 1
                    if selected_item['attribute'] == "health": 
                        if selected_item['attribute_value'] == 'MAX':
                            with open('pokemon_lvl.json', 'r') as pokelvls:
                                lvls = json.load(pokelvls)
                                max_health = next(
                                    lvl['health'] for lvl in lvls['levels']
                                    if lvl['level'] == myPokemon.lvl
                                )
                                myPokemon.health = max_health
                        else:
                            myPokemon.health = min(
                                myPokemon.health + selected_item['attribute_value'],
                                myPokemon.max_health
                            )
                        delay_print(f"You used a {selected_item['name']}. {myPokemon.name}'s health is now {myPokemon.health}.")

                    elif selected_item['attribute'] == "shield":
                        enemy_damage_multiplier = selected_item['attribute_value']
                        delay_print(f"You used a {selected_item['name']}! Enemy damage reduced by {enemy_damage_multiplier * 100}% for the next turn.")

                    elif selected_item['attribute'] == "luck":
                        catch_luck_factor = selected_item['attribute_value']
                        delay_print(f"You used a {selected_item['name']}! Catch rate increased by {catch_luck_factor * 100}%.")

                    elif selected_item['attribute'] == "damage":
                        damage_multiplier = selected_item['attribute_value']
                        delay_print(f"You used a {selected_item['name']}! Damage boosted by {damage_multiplier * 100}% for the next turn.")

                    with open('C:/Users/nitro/PokePython-1/inventory.json', 'w') as inv:
                        json.dump(items, inv, indent=4)

                    while True:
                        bulk_use = input("Do you want to use another item? (Y/N): ").upper()
                        if bulk_use == 'Y':
                            break
                        elif bulk_use == 'N':
                            item_not_selected = False
                            break
                        else:
                            print("Invalid input. Please enter 'Y' or 'N'.")
                    
            enemy_damage_multiplier = 1
            turn = "player"
        elif turn == "cpu":
            damage = random.randint(0, enemy.attack) * enemy_damage_multiplier
            print(f"[DEBUG] Enemy Damage Multiplier: {enemy_damage_multiplier}, Calculated Damage: {damage}")
            if damage == 0:
                time.sleep(1)
                os.system("cls")
                playSound("dodge", 1)
                delay_print(f'{enemy.name} used tackle but missed the attack!')
                time.sleep(1)
            else:
                time.sleep(1)
                playSound("tackle", 1)
                time.sleep(2)
                playSound("Hit Normal Damage", 1)
                os.system("cls")
                delay_print(f'{enemy.name} did {damage} damage to {myPokemon.name}')
                myPokemon.health -= damage
                time.sleep(3)
                if myPokemon.health <= 0:
                    playSound("In-Battle Faint No Health", 1)
                    delay_print(f'{myPokemon.name} fainted.')
                    delay_print(f'{enemy.name} wins!')
                else:
                    delay_print(f'{myPokemon.name} is at {myPokemon.health}HP')
                    time.sleep(1)
            enemy_damage_multiplier = 1
            turn = "player"

# fight(2, myPokemon = Pokemon(id = 1,name = "Charmander", lvl = 1))

# keyboard.add_hotkey('1')