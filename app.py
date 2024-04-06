# Importing classes
from game import Game
from title import Title
from menu import Menu

# Initializing classes
game = Game("I Wanna Defeat The Microchip", 1000, 700)
title = Title(game.screen)
menu = Menu(game.screen)

# Giving each classes
title.menu = menu
menu.title = title

# Execute video game
game.run(title)
