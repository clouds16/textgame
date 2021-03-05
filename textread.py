import time
import sys
from player import *


def slowText(file):
    dialogue = open(file).read().format(player.getName(),
                                        player.ability, player.item)

    for characters in dialogue:
        print(characters, end='')
        sys.stdout.flush()
        time.sleep(.020)

    time.sleep(2)

# beginJourney()


# player.makePlayer()
# enemies.createBoss()
# slowText("victory.txt")
