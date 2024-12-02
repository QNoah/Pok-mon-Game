from pokemon import Pokemon
from encounter import Encounter_Pokemon
import pygame 
import json
import random
import sys
import time
import os

pygame.mixer.init()
# test
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
    while myPokemon.health > 0 and enemy.health > 0:
        if turn == "player":
            damage_multiplier = 1
            enemy_damage_multiplier = 1
            catch_luck_factor = 1
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

                turn = "cpu"
                pass
            elif _ == 2:
                damage = random.randint(0, myPokemon.attack) * damage_multiplier
                damage_multiplier = 1
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
                turn = "cpu"
            elif _ == 3:
                os.system("cls")
                bulk_use = ''
                item_not_selected = True
                while item_not_selected:
                    with open('inventory.json') as inv:
                        items = json.load(inv)
                        for item in items['inventory']:
                            if item['id'] == item_choice and item['qty'] > 0 and item['name'] != 'coins':
                                print(f"Option: {item['id']}, item: {item['name']}, qty: {item['qty']}, | {item['attribute_calc']} {item['attribute_value']} {item['attribute']}")
                        time.sleep(1)
                        delay_print('Choose your item:')
                        try:
                            item_choice = int(input())
                        except ValueError:
                            print("Wrong input")
                    for item in items['inventory']:
                        if item['id'] == item_choice and item['qty'] > 0 and item['name'] != 'coins':
                            item['qty'] -= 1
                            if item['attribute'] == "health": #hp increase
                                if item['attribute_value'] == 'MAX':
                                    with open('pokemon_lvl.json', 'r') as pokelvls:
                                        lvls = json.load(pokelvls)
                                        myPokemon.health = next(lvl['health'] for lvl in lvls['levels'] if lvl == myPokemon.lvl)
                                        print(myPokemon.health)
                                else:
                                    myPokemon.health += item['attribute_value']
                                delay_print(f'You used a {item["name"]} and increased your health from {(myPokemon.health - item["attribute_value"])} to {myPokemon.health}')
                            elif item['attribute'] == 'shield': #incoming damage decrease for a turn
                                enemy_damage_multiplier = 1
                                enemy_damage_multiplier *= item['attribute_value']
                                delay_print(f'You used a {item["name"]} and decreased enemy damage by {item["attribute_value"] * 100}%')
                            elif item['attribute'] == 'luck': #catching pokemon luck
                                catch_luck_factor = 1
                                catch_luck_factor *= item['attribute_value']
                                delay_print(f'You used a {item["name"]} and increased the chance of catching {enemy.name} by {item["attribute_value"] * 100}%')
                            elif item['attribute'] == 'damage': #increased damage for a turn
                                damage_multiplier = 1
                                damage_multiplier *= item["attribute_value"]
                                delay_print(f'You used a {item["name"]} and increased your damage for the next turn by {item["attribute_value"] * 100}%')
                            elif item['attribute'] == 'damage': #increased damage for a turn
                                damage_multiplier = 1
                                damage_multiplier *= item["attribute_value"]
                                delay_print(f'You used a {item["name"]} and increased your damage for the next turn by {item["attribute_value"] * 100}%')

                    while bulk_use not in ['Y', 'N']:
                        bulk_use = input('Do you want to use another item? (Y/N) ')
                        if bulk_use.upper() == 'Y':
                            continue
                        elif bulk_use.upper() == 'N':
                            item_not_selected == False

                            
                        
                    
            turn = "cpu"
        elif turn == "cpu":
            damage = random.randint(0, enemy.attack) * enemy_damage_multiplier
            enemy_damage_multiplier = 1
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
            turn = "player"

# fight(2, myPokemon = Pokemon(id = 1,name = "Charmander", lvl = 1))

# keyboard.add_hotkey('1')