# Importing classes
from game import Game
from title import Title

# Initializing classes
game = Game("I Wanna Defeat The Microchip", 1000, 700)
title = Title(game.screen)

# Execute video game
game.run(title)
