from player import *
from enemies import *
from textread import *
from fight import *
from items import *
from gamemap import *
from sounds import *

#################################################################################################################
# Hector Alvarez -


# Run this script


#################################################################################################################


def main():

    playsound(songs["intro"])
    slowText("dialogues/intro_dialogue.txt")
    # startMap(player)
    mainAdventure(player)

    stats = open('dialogues/playerstats.txt').read().format(player.getName(),
                                                            player.getHealth(), player.inventory)
    print(stats)


if __name__ == "__main__":
    main()
