from enemies import *
from player import *
from textread import *
from fight import *
from items import *


def startMap(player):
    destination = townSquare(player)
    
    while True:
        if destination == "Town Square":
            destination = townSquare(player)
        
        if destination == "Dark Forest":
            destination = toDarkForest(player, forestBoss, "Sword of Light")
            
        elif destination == "Castle":
            destination = toCastle(player, Ganon)
            
        elif destination == "Ruins":
            destination = toRuins(player, ruinsBoss, "Boss Key")
        elif destination == "Desert":
            destination = toDesert(player, desertBoss, "super potion")

        


def townSquare(player):
    paths = {
        "Town Square": True,
        "Dark Forest": True,
        "Castle": True,
        "Ruins": True,
        "Desert": True,
        "Currently": "Town Square"
    }
    
    counter = 0
    
    if counter == 0:
        slowText("dialogues/townsquare.txt")
        print("You are Now in the town square, you may go toward the (Dark Forest) (Castle) (Ruins) or (Desert) or (map)")
   # print("You are currently in the {}".format(paths["Currently"]))
    else :
        print("Hello {} good to see you again. You are safe here in the Town Square".format(player.getName()))

    return chooseNewLocation(paths["Currently"])


def toDarkForest(player, boss, item):
    paths = {
        "Town Square": True,
        "Dark Forest": True,
        "Castle": True,
        "Ruins": True,
        "Desert": True,
        "Currently": "Dark Forest"
    }
    slowText("dialogues/darkforest.txt")
    print("You are currently in the {}".format(paths["Currently"]))

    enemyfight = encounterEnemy(player, boss)
    if enemyfight:
 
        addItemToInvetory(player, item)
        print(player.inventory)
        
    return chooseNewLocation(paths["Currently"])
    #routeToNewLocation(chooseNewLocation())


def toRuins(player, boss, item):
    paths = {
            "Town Square": True,
            "Dark Forest": townSquare,
            "Castle": True,
            "Ruins": True,
            "Desert": True,
            "Currently": "Dark Forest"
        }
        
    slowText("dialogues/ruins.txt")
    enemyfight = encounterEnemy(player, boss)

    if enemyfight:
        addItemToInvetory(player, item)
        print(player.inventory)

    return chooseNewLocation(paths["Currently"])
    #routeToNewLocation(chooseNewLocation())


def toDesert(player, boss, item):
    paths = {
            "Town Square": True,
            "Dark Forest": True,
            "Castle": True,
            "Ruins": True,
            "Desert": True,
            "Currently": "Dark Forest"
        }
        
    slowText("dialogues/desert.txt")

    enemyfight = encounterEnemy(player, boss)
    if enemyfight:
        addItemToInvetory(player, item)
        print(player.inventory)
        
    return chooseNewLocation(paths["Currently"])
    #routeToNewLocation(chooseNewLocation())


# 333
def toCastle(player, boss):

    slowText("dialogues/castle.txt")

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
        enemyfight = encounterEnemy(player, boss)

        if enemyfight:
            slowText("dialogues/endgame.txt")
        else:
            print("You have Lost... But you are still alive...")
        if player.getHealth() > 0:
            chooseNewLocation(paths["Currently"])
        else:
            print("Game Over")

    else:
        print("You are not ready to proceed yet")
        time.sleep(3)
        return chooseNewLocation("Castle")


def showMap():
    locations = ["Town Square", "Dark Forest", "Castle", "Ruins", "Desert"]
    print(locations)


def chooseNewLocation(currentlocation):
    map = ["Town Square", "Dark Forest", "Castle", "Ruins", "Desert"]
    counter = 0
    while True:
        if counter != 0:
            print("You cannot go there! Try again!\n")
        
        print("{0} you are currently in {1}".format(player.getName(), currentlocation))

        direction = str(input("Where would you like to go? "))
        for items in map:
            if direction == items:
                return direction
            
            elif direction == "map":
                print(map)
                break


def routeToNewLocation(destination):
    if destination == "Dark Forest":
        toDarkForest(player, forestBoss, "Sword of Light")
    elif destination == "Castle":
        toCastle(player, Ganon)
    elif destination == "Ruins":
        toRuins(player, ruinsBoss, "Boss Key")
    elif destination == "Desert":
        toDesert(player, desertBoss, "super potion")

#townSquare(player)
#startMap(player)