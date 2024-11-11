import json
import os
import sys
import time

def delayPrint(s, delay=0.05):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def Store(balance, mypokemon):
    if balance <= 0:
        delayPrint("You're broke")
        return

    Stay = True
    while Stay:
        os.system("cls")

        with open('store.json') as store_file:
            storeItems = json.load(store_file)
        with open('inventory.json') as inv_file:
            inventory = json.load(inv_file)

        delayPrint('I sell the following:\n')
        for buyableItems in storeItems['storeStock']:
            if buyableItems["cost"] <= balance and buyableItems["Gym_Membership"] <= mypokemon.membership:
                delayPrint(f'{buyableItems["id"]}) {buyableItems["name"]} for {buyableItems["cost"]}$\n')


        Wannabuy = input('Would you like to buy anything? (y/n) ')
        
        if Wannabuy.lower() == 'y':
            delayPrint('What would you like to buy? \n')


            current_balance = next(item['qty'] for item in inventory['inventory'] if item['id'] == 1)
            delayPrint(f'Your current balance is {current_balance}$\n')

            for buyableItems in storeItems['storeStock']:
                if buyableItems["cost"] <= balance and buyableItems["Gym_Membership"] <= mypokemon.membership:
                    delayPrint(f'{buyableItems["id"]}) {buyableItems["name"]} for {buyableItems["cost"]}$\n')

            try:
                itemChoice = int(input("Enter the item number: "))
                

                selectedItem = next((item for item in storeItems['storeStock']
                                     if item['id'] == itemChoice and item["cost"] <= balance 
                                     and item["Gym_Membership"] <= mypokemon.membership))
                
                if selectedItem is None:
                    delayPrint("I don't sell that.\n")
                else:
                    delayPrint(f'Successfully added 1 {selectedItem["name"]} to your inventory!\n')
                    
                    for item in inventory['inventory']:
                        if item['name'] == selectedItem['name']:
                            item['qty'] += 1
                        elif item['id'] == 1:
                            item['qty'] -= selectedItem['cost']
                            balance = item['qty']  
                            delayPrint(f'Your current balance is {item["qty"]}$\n')
                    

                    with open('inventory.json', 'w') as inv_file:
                        json.dump(inventory, inv_file, indent=4)

            except ValueError:
                delayPrint("Wrong input\n")

            wantAgain = input('Would you like to buy something else? (y/n) ')
            if wantAgain.lower() != 'y':
                Stay = False
        elif Wannabuy.lower() == 'n':
            delayPrint('Aww, maybe another time? Well, I wish you good luck with your journey! ♥\n')
            Stay = False
        else:
            delayPrint('Invalid input. Please choose "y" or "n".\n')
