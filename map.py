from enemies import *
# from fight import *
# from items import *
from player import *
from createchar import *


def main():
    paths = {
        "Town Square": False,
        "Dark Forest": True,
        "Castle": True,
        "Ruins": True,
        "Desert": True,
        "Currently": "Town Square"
    }
    print("You are Now in the town square, you may go toward the (Dark Forest) (Castle) (Ruins) or (Desert)")
    print("You are currently in the {}".format(paths["Currently"]))
    while True:
        direction = str(input("Where would you like to go? "))
        for items in paths:
            if items == direction:
                routeToNewLocation(direction)
                break
            else:
                print("You cannot go there!")
                showMap()
                break


def toDarkForest():
    paths = {
        "Town Square": True,
        "Dark Forest": False,
        "Castle": False,
        "Ruins": True,
        "Desert": True,
        "Currently": "Dark Forest"
    }
    print("You are currently in the {}".format(paths["Currently"]))
    print("You are Now in the Dark Forest")

    while True:
        direction = str(input("Where would you like to go? "))
        for items in paths:
            if items == direction:
                routeToNewLocation(direction)
                break
            else:
                print("You cannot go there!")
                showMap()


def toCastle(player, boss):
    if player.inventory["Boss Key"]:
        print("You may proceed to the Castle")

        paths = {
            "Town Square": False,
            "Dark Forest": False,
            "Castle": False,
            "Ruins": False,
            "Desert": False,
            "Currently": "Castle"
        }
        print("You are currently in the {}".format(paths["Currently"]))
    else:
        print("You are not ready to proceed yet")
        print("You are currently in the {}".format(paths["Currently"]))
        townSquare()


def toRuins():
    print("Walk to the Temple of Time?")


def toDesert():
    print("Going to desert ")


def showMap():
    locations = ["Town Square", "Dark Forest", "Castle", "Ruins", "Desert"]
    print(locations)


def routeToNewLocation(destination):
    if destination == "Dark Forest":
        toDarkForest()
    elif destination == "Castle":
        toCastle()
    elif destination == "Ruins":
        toRuins()
    elif destination == "Desert":
        toDesert()


main()
