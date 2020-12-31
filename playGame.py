# default to hunter hero
# make selection by choosing hero respectively

import Game, sys
import Hunter, DemonHunter, Priest

# 0 Hunter
# 1 Demon Hunter
# 2 Priest



choice = 2
try:
    input = sys.argv
    choice = int(input[1])
except:
    pass
Game.Game().runGame(choice)
