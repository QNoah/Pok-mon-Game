import json

def buy(balance, id):
    if balance <= 0:
        print("You're broke")
    else:
        with open('store.json') as store:
            storeItems = json.load(store)
            for buyableItems in storeItems:
                print(buyableItems)
