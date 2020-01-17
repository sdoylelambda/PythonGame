from player import Player
from room import Room
from item import Item


room = {
    'Canyon passage': Room('Canyon passage', """You have high cliffs all around, you see a passage to the north."""),
}

item = {
    'dagger': Item('dagger', """basic dagger"""),
}

player = Player(input('Enter your name'), room['Canyon passage'])
print(player.name)
print(player.currentLocation)
