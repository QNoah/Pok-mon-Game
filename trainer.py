import os

class trainerProfile:
    def __init__(self, name):
        self.name = name
        self.party = {"party": []}
        self.gyms = 0
# {"id": 1, "name": "Charmander"}

    def add_party(self, new_pokemon):
        if len(self.party["party"]) != 3:
            self.party["party"].append(new_pokemon)
        elif len(self.party["party"]) == 3:
            while True:
                print("Sorry, but you're party is full")
                _ = input("Want to release a Pokémon to the wild to have this new one? y/n ").lower()
                while True:
                    if _ == "n":
                        confirmation = input("Are you sure? You will lose your caught Pokémon! y/n ")
                        if confirmation == "y":
                            print("You caught a Pokémon and immediatly let it go.")
                            break
                        elif confirmation == "n":
                            os.system("cls")
                            break
                    elif _ == "y":
                        os.system('cls')
                        print("What Pokémon would you like to release?")
                        for pokemon in self.party['party']:
                            print(f"{pokemon['id']}. {pokemon['name']}")
                        print()
                        print("5. Go back")
                        while True:
                            try:
                                _ = int(input().strip())
                                if _ == 1:
                                    print("hello world")
                                elif _ == 2:
                                    print("hello world")
                                elif _ == 3:
                                    print("hello world")
                                elif _ == 5:
                                    os.system("cls")
                                    break
                                else:
                                    print("That is not a valid option!")
                                    continue
                            except ValueError:
                                    print("That is not a valid option!")
                                    continue
                    break
                    # confirmation = 