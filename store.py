import json
import os
import sys
import time

def delayPrint(s, delay=0.05):
    for c in s:
        if c != "":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(delay)
        elif c == '"':
            pass

def Store(balance):
    if balance <= 0:
        delayPrint("You're broke")
    else:
        Stay = True
        while Stay:
            with open('store.json') as store:
                storeItems = json.load(store)
            with open('inventory.json') as inv:
                inventory = json.load(inv)
            delayPrint('I sell the following: ')
            print()
            for buyableItems in storeItems['storeStock']:
                if buyableItems["cost"] <= balance and buyableItems['stock'] > 0:
                    delayPrint(f' {buyableItems["stock"]} {buyableItems["name"]} for {buyableItems["cost"]}$')
                    print()
            Wannabuy = input('Would you like to buy anything? (y/n) ')
            os.system("cls")
            if Wannabuy.lower() == 'y':
                delayPrint('What would you like to buy? ')
                print()
                for items in inventory['inventory']:
                    if items['id'] == 2:
                        delayPrint(f'Your current balance is {items["qty"]}$')
                        print()
                for buyableItems in storeItems['storeStock']:
                    if buyableItems["cost"] <= balance and buyableItems['stock'] > 0:
                        delayPrint(f'{buyableItems["id"]}. {buyableItems["name"]} for {buyableItems["cost"]}$')
                        print()
                try:
                    itemChoice = int(input())
                except ValueError:
                    print("Wrong input")
                for buyableItems in storeItems["storeStock"]:
                    if buyableItems['id'] == itemChoice:
                        delayPrint(f'Successfully added 1 {buyableItems["name"]} to your inventory!')
                        print()
                        with open('inventory.json') as inv:
                            inventory = json.load(inv)
                        for items in inventory['inventory']:
                            if items['name'] == buyableItems['name']:
                                items['qty'] += 1
                                buyableItems['stock'] -= 1
                            if items['id'] == 2:
                                items['qty'] -= buyableItems['cost']
                                delayPrint(f'Your current balance is {items["qty"]}')
                                print()
                

                        
            elif Wannabuy.lower() == 'n':
                delayPrint('Aww, maybe another time? Well i wish you goodluck with your journey! ♥')
            
            wantAgain = input('Would you like to buy something else? (y/n) ')
            if wantAgain.lower() == 'y':
                continue
            else:
                Stay = False




