# Importing classes
from game import Game
from title import Title
from menu import Menu
from gameplay import Gameplay

# Initializing classes
game = Game("I Wanna Defeat The Microchip", 1000, 700)
# game = Game("I Wanna Defeat The Microchip", 480, 360)
title = Title(game.screen)
menu = Menu(game.screen)
gameplay = Gameplay(game.screen)

# Giving each classes
title.menu = menu
menu.title = title
menu.gameplay = gameplay

# Execute video game
game.run(title)
