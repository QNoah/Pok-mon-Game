class trainerProfile:
    def __init__(self, name):
        self.name = name
        self.party = []
        self.gyms = 0
# {"id": 1, "name": "Charmander"}

    def add_party(self, pokemon):
        if len(self.party) != 3:
            self.party.append(pokemon)
        elif len(self.party) == 3:
            print("Sorry, but you're party is full")
            _ = input("Want to release a Pokémon to the wild to have this new one? y/n ").lower()
            while True:
                if _ == "n":
                    confirmation = input("Are you sure? You will lose your caught Pokémon! y/n ")
                    if confirmation == "y":
                        print("You caught a Pokémon and immediatly let it go.")
                        break
                    elif confirmation == "n":
                        break
                elif _ == "y":
                    print("What Pokémon would you like to release?")
                    for pokemons in self.party:
                        print(pokemons)
                        break
                        
                    # confirmation = 