from trainer import trainerProfile

def test_party_add():
    player = trainerProfile(name="Quinten")
    player.add_party({"id": 1, "name": "Charmander"})
    print(player.party)


def test_party_add_full():
    player = trainerProfile(name="Quinten")
    player.add_party({"id": 1, "name": "Squirtle"})
    player.add_party({"id": 2, "name": "Dodo"})
    player.add_party({"id": 3, "name": "Pook"})
    player.add_party({"id": 4, "name": "Charmander"})
    print(player.party)

test_party_add_full()