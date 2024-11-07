from trainer import trainerProfile

player = trainerProfile(name="Quinten")
player.add_party({"id": 1, "name": "Charmander"})
player.add_party({"id": 2, "name": "Squirtle"})
player.add_party({"id": 3, "name": "Pook"})
# It will ask here what to do since it is quite full
player.add_party({"id": 1, "name": "Charmander"})
