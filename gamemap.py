from enemies import *
from player import *
from textread import *
from fight import *
from items import *
from sounds import *

####################### Main loop to play game ################


def mainAdventure(player):

    townSquare(player)

    toLocation("Dark Forest", "dialogues/darkforest.txt",
               "sounds/darkforest.mp3", player, forestBoss, "Sword of Light")

    toLocation("Desert", "dialogues/desert.txt",
               "sounds/darkforest.mp3", player, desertBoss, "super potion")

    toLocation("Ruins", "dialogues/ruins.txt",
               "sounds/darkforest.mp3", player, ruinsBoss, "Boss Key")

    toCastle(player, Ganon, "Crown of the Conqueror")


def toLocation(maplocation, readfile, soundfile, player, boss, item):

    slowText(readfile)
    playsound(soundfile)
    print("You are currently in the {}".format(maplocation))
    enemyfight = encounterEnemy(player, boss)

    if enemyfight:
        addItemToInvetory(player, item)


def townSquare(player):

    slowText("dialogues/townsquare.txt")
    playsound(songs["townsquare"])


# 333
def toCastle(player, boss, item):
    playsound(songs["castle"])
    slowText("dialogues/castle.txt")

    if player.inventory["Boss Key"]:
        print("You may proceed to the Castle")

        paths = {

            "Currently": "Castle"
        }
        print("You are currently in the {}".format(paths["Currently"]))
        enemyfight = encounterEnemy(player, boss)

        if enemyfight:
            addItemToInvetory(player, item)

            slowText("dialogues/victory.txt")
            slowText("dialogues/endgame.txt")

        else:
            print("Game Over")

    # This function was a remnant of when the player could choose where to go to first.. player could not proceed without the key from the right
    # previous boss
    else:
        print("You are not ready to proceed yet")
        time.sleep(3)
