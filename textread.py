from player import *
import time
import sys


def slowText(file, player):
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
