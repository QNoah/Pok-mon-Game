import battle
import random

from pokemon import Pokemon

board = [
    {"vakje": 1, "checkpoint": False, "power_up": None, "pokemon": None},
    {"vakje": 2, "checkpoint": False, "power_up": None, "pokemon": 1},
    {"vakje": 3, "checkpoint": False, "power_up": "level_up", "pokemon": None},
    {"vakje": 4, "checkpoint": False, "power_up": None, "pokemon": None},
    {"vakje": 5, "checkpoint": False, "power_up": None, "pokemon": 2},
    {"vakje": 6, "checkpoint": False, "power_up": "heal", "pokemon": None},
    {"vakje": 7, "checkpoint": True, "power_up": None, "pokemon": None},
    {"vakje": 8, "checkpoint": False, "power_up": None, "pokemon": 3},
    {"vakje": 9, "checkpoint": False, "power_up": "big_dice", "pokemon": None},
    {"vakje": 10, "checkpoint": False, "power_up": None, "pokemon": None}
]

def roll_dice(max_value=3):
    return random.randint(1, max_value)

def check_vakje(vakje):
    message = f"Je staat op {vakje['vakje']}."

    if vakje['power_up']:
        if vakje['power_up'] == "heal":
            message += " Je ontvangt hier een heal power-up!"
        elif vakje['power_up'] == "level_up":
            message += " Je ontvangt hier een level up!"
        elif vakje['power_up'] == "big_dice":
            message += " Je kan met deze dobbelsteen maximaal 8 gooien in een gevecht!"

    if vakje['pokemon']:
        # battle.setEncounter(vakje['pokemon'])
        print(f"Je staat op pokemon {vakje['pokemon']}")
        battle.fight(vakje['pokemon'])
        
        # pass
        # hier moet de battle komen te staan
        # message += f" Je bent een {vakje['pokemon']} tegengekomen!"

    if vakje['checkpoint']:
        message += " This is a checkpoint, your HP has been recovered!"

    return message

current_position = 1
current_hp = 20
MAX_HP = 20

while current_position < 10:
    print(f"\You are at position{current_position} with {current_hp} HP.")

    input("Press enter to roll...")

    previous_position = current_position

    dice_roll = roll_dice()
    print(f"You rolled {dice_roll}.")

    current_position += dice_roll

    if current_position > 10:
        current_position = 10

    if previous_position < 7 <= current_position:
        current_hp = MAX_HP
        print("You have passed or you are at a checkpoint. Your health has regenerated.")

    current_vakje = board[current_position - 1]

    vakje_boodschap = check_vakje(current_vakje)
    print(vakje_boodschap)

    if current_vakje['checkpoint']:
        current_hp = MAX_HP
        print("Your HP has been fully regenerated.")

print(f"Congratulations! You are an official Pokémon Champion.")
