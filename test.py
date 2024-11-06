from trainer import trainerProfile

player = trainerProfile(name="Quinten")
print(player.party)
player.add_party({"id": 1, "name": "Charmander"})
print(player.party)
player.add_party({"id": 1, "name": "Charmander"})
print(player.party)
player.add_party({"id": 1, "name": "Charmander"})
print(player.party)
# It will ask here what to do since it is quite full
player.add_party({"id": 1, "name": "Charmander"})
print(player.party)
