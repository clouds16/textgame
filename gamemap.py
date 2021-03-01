from enemies import *
from player import *
from textread import *
from fight import *
from items import *
from sounds import *

####################### Main loop to play game ################


def straightMap(player):
    # townSquare(player)
    toDarkForest(player, forestBoss, "Sword of Light")

    toDesert(player, desertBoss, "super potion")
    toRuins(player, ruinsBoss, "Boss Key")
    toCastle(player, Ganon)


def townSquare(player):

    slowText("dialogues/townsquare.txt")
    playsound(songs["townsquare"])


def toDarkForest(player, boss, item):
    paths = {
        "Currently": "Dark Forest"
    }

    slowText("dialogues/darkforest.txt")
    print("You are currently in the {}".format(paths["Currently"]))
    enemyfight = encounterEnemy(player, boss)

    if enemyfight:
        addItemToInvetory(player, item)


def toRuins(player, boss, item):
    paths = {
        "Currently": "Dark Forest"
    }
    print("you are currently in the {} . it looks like we can find the key to the castle here...".format(
        paths["Currently"]))
    slowText("dialogues/ruins.txt")
    enemyfight = encounterEnemy(player, boss)

    if enemyfight:
        addItemToInvetory(player, item)


def toDesert(player, boss, item):
    paths = {
        "Currently": "Dark Forest"
    }

    slowText("dialogues/desert.txt")

    enemyfight = encounterEnemy(player, boss)
    if enemyfight:
        addItemToInvetory(player, item)


# 333
def toCastle(player, boss):
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
            slowText("dialogues/victory.txt")
            slowText("dialogues/endgame.txt")

        else:
            print("Game Over")

    else:
        print("You are not ready to proceed yet")
        time.sleep(3)
