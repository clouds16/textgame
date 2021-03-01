from items import *
from enemies import *
from textread import *
from fight import *
from player import *


class Map:
    def __init__(self, name, enemy, item, textfile):
        self.name = name
        self.enemy = enemy
        self.item = item
        self.round = 0
        self.textfile = textfile

    def getName(self):
        return self.name

    def getEnemy(self):
        return self.enemy

    def getItem(self):
        return self.item

    def getRound(self):
        return self.round

    def updateRound(self):
        self.round += 1
        return self.round

    def getText(self, script):
        return self.textfile[script]


town = Map("Town Square", "npc", "none", [
           "dialogues/townsquare.txt", "dialogues/returntotown.txt"])
castle = Map("Castle", "Ganon", "Dagger", [
             "dialogues/endgame.txt", "dialogues/victory.txt"])
darkforest = Map("Dark Forest", "forestBoss",
                 "Sword of Light", "dialogues/darkforest.txt")
ruins = Map("Ruins", "Stone Golem", "Boss Key", "dialogues/ruins.txt")
desert = Map("Desert", "Giant Lizard", "super potion", "dialogues/desert.txt")


def startTownSquare(player, place):
    if place.getRound() == 0:
        slowText(place.getText(0))
        place.updateRound()

    else:
        slowText(place.getText(1))
        place.updateRound()

    print("You encounter a merchant that wants to talk to you... ")
    npcdialogue = str(input("Would you like to find out more about he world?"))

    if npcdialogue == "yes" or npcdialogue == "y":

        print("This world has different areas you can explore :")
        showMap()
        worldinfo = str(
            input("Which location would you like no know more about ? (e) to exit"))

        if worldinfo == "Dark Forest" or worldinfo == "dark forest":
            print("Legend has it... there is a magical sword in the forest...")
        elif worldinfo == "Ruins" or worldinfo == "ruins":
            print("Many believe that Ganon hid something very important in the ruins.. perhaps something to get into the castle")
        elif worldinfo == "Desert" or worldinfo == "desert":
            print(
                "I have heard tales of a magical healing potion long forgotten in the desert")
        else:
            print("That is not a place on this world")
    else:
        print("On your way then Hero")

    return chooseNewLocation(place.getName())


def mapEvents(player, enemy, place):
    slowText(place.getText(0))
    enemyFight = encounterEnemy(player, enemy)
    if enemyFight:
        addItemToInvetory(player, place.getItem())
    return chooseNewLocation(place.getName())


def routeToNewLocation(destination):
    if destination == "Dark Forest":
        toDarkForest(player, forestBoss, "Sword of Light")
    elif destination == "Castle":
        toCastle(player, Ganon)
    elif destination == "Ruins":
        toRuins(player, ruinsBoss, "Boss Key")
    elif destination == "Desert":
        toDesert(player, desertBoss, "super potion")


def showMap():
    locations = ["Town Square", "Dark Forest", "Castle", "Ruins", "Desert"]
    print(locations)


def chooseNewLocation(currentlocation):
    map = ["Town Square", "Dark Forest", "Castle", "Ruins", "Desert"]
    counter = 0
    while True:
        if counter != 0:
            print("You cannot go there! Try again!\n")

        print("{0} you are currently in {1}".format(
            player.getName(), currentlocation))

        direction = str(input("Where would you like to go? "))
        for items in map:
            if direction == items:
                return direction

            elif direction == "map":
                print(map)
                break


def startEvents(player):
    destination = startTownSquare(player, town)

    while True:

        if destination == "Town Square":
            destination = startTownSquare(player, town)

        elif destination == "Dark Forest":
            destination = mapEvents(player, forestBoss, darkforest)

        elif destination == "Castle":
            destination = mapEvents(player, Ganon, castle)

        elif destination == "Ruins":
            destination = mapEvents(player, ruinsBoss, ruins)
        elif destination == "Desert":
            destination = mapEvents(player, desertBoss, desert)


startEvents(player)
