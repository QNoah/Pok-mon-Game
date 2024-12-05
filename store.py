import json
import os
import sys
import time
import pokemon

def delay_print(s, delay=0.05):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
class Store:
    def __init__(self, balance, mypokemon):
        self.balance = balance
        self.mypokemon = mypokemon
        with open('store.json') as store_file:
            self.stock = json.load(store_file)
        with open('inventory.json') as inv_file:
            self.inventory = json.load(inv_file)

    def save_inventory(self):
        with open('inventory.json', 'w') as file:
            json.dump(self.inventory, file, indent=4)

    def update_balance(self, amount):
        for item in self.inventory['inventory']:
            if item['id'] == 0:  # Assume id=1 represents money
                item['qty'] += amount
                self.balance = item['qty']

    def buy(self):
        delay_print(f'Your current balance is {self.balance}$\n')
        delay_print('What would you like to buy? \n')

        affordable_items = [
            item for item in self.stock['storeStock']
            if item["cost"] <= self.balance and item["Gym_Membership"] <= self.mypokemon.membership
        ]
        for item in affordable_items:
            delay_print(f'{item["id"]}) {item["name"]} for {item["cost"]}$\n')

        try:
            item_choice = int(input("Enter the item number: "))
            selected_item = next(
                (item for item in affordable_items if item['id'] == item_choice), None
            )
            if selected_item:
                delay_print(f'You bought 1 {selected_item["name"]} for {selected_item["cost"]}$\n')
                self.update_balance(-selected_item['cost'])
                for inv_item in self.inventory['inventory']:
                    if inv_item['name'] == selected_item['name']:
                        inv_item['qty'] += 1
                        break
                self.save_inventory()
            else:
                delay_print("Invalid selection.\n")
        except ValueError:
            delay_print("Please enter a valid number.\n")

    def sell(self):
        delay_print('Your current inventory:\n')
        sellable_items = [
            item for item in self.inventory['inventory'] if item['id'] != 1 and item['qty'] > 0
        ]
        for item in sellable_items:
            store_price = next(
                (stock_item for stock_item in self.stock['storeStock'] if stock_item['name'] == item['name']), None
            )
            if store_price:
                 delay_print(f'{item["id"]}) You can sell {item["qty"]} {item["name"]} for {store_price["cost"]}$\n')

        try:
            item_choice = int(input("Enter the item number to sell: "))
            selected_item = next((item for item in sellable_items if item['id'] == item_choice), None)
            if selected_item:
                store_price = next(
                    (stock_item for stock_item in self.stock['storeStock'] if stock_item['name'] == selected_item['name']), None
                )
                if store_price:
                    delay_print(f'You sold 1 {selected_item["name"]} for {store_price["cost"]}$\n')
                    selected_item['qty'] -= 1
                    self.update_balance(store_price['cost'])
                    self.save_inventory()
                else:
                    delay_print("Cannot sell this item.\n")
            else:
                delay_print("Invalid selection.\n")
        except ValueError:
            delay_print("Please enter a valid number.\n")

    def buy_or_sell(self):
        while True:
            os.system("cls")
            delay_print("Welcome to the Poke Store!\n")
            delay_print("1. Buy\n")
            delay_print("2. Sell\n")
            delay_print("3. Leave\n")

            user_input = input('')
            os.system("cls")
            if user_input == '1':
                if self.balance <= 0:
                    delay_print("You're broke\n")
                    return
                self.buy()
            elif user_input == '2':
                if len(self.inventory['inventory']) == 0:
                    delay_print("You don't have any sellable items in your inventory\n")
                    return
                self.sell()
            elif user_input == '3':
                delay_print("Goodbye! Have a great day! \n")
                return
            else:
                delay_print("Invalid option. Please try again.\n")