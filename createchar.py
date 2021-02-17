import enemies
import player
import time
import sys


def beginJourney():

    dialogue = open("intro_dialogue.txt").read()

    for characters in dialogue:
        print(characters, end='')
        sys.stdout.flush()
        time.sleep(.020)

    time.sleep(2)


# beginJourney()

# player.makePlayer()
# enemies.createBoss()
