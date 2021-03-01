from player import *
import random
import time
from sounds import *


def showItems():
    print(player.inventory)

# Main logic for items ################################333


def useItem():

    print("These are the items currently in your inventory: ",
          player.inventory.keys())
    useanitem = input("which item would you like to use? ")
    found = False

    for items in player.inventory:
        if items == useanitem:
            itemEffects(useanitem)
            playsound(songs["get-item"])
            return True
    print("item not found in inventory")

############################## secondary item usage logic  #############################


def itemEffects(itempicked):
    if itempicked == "small potion" or itempicked == "medium potion" or itempicked == "super potion":
        player.useHealthPotion(player.inventory[itempicked])
        print("You have restored {} HP, your health is now {}".format(
            player.inventory[itempicked], player.getHealth()))
        removeItemFromInventory(itempicked)

    elif itempicked == "speed potion":
        player.useSpeedPotion(player.inventory[itempicked])
        print("You have increased {} Speed, your speed is now {}".format(
            player.inventory[itempicked], player.getSpeed()))
        removeItemFromInventory(itempicked)

    elif itempicked == "Bow" or itempicked == "Sword of Light":
        player.setAttack(player.inventory[itempicked])
        print("You have now equipped {} , your attack is now {}".format(
            player.inventory[itempicked], player.getAttack()))
        removeItemFromInventory(itempicked)


def removeItemFromInventory(item):
    player.inventory.pop(item)
    print("{} has been consumed! ".format(item))


def addItemToInvetory(player, item):
    player.inventory[item] = items[item]
    print("You have added {} to your inventory".format(item))
    print(player.inventory)
    playsound(songs["get-item"])


items = {
    "small potion": 20,
    "medium potion": 40,
    "super potion": 100,
    "speed potion": 30,
    "Bow": 45,
    "Dagger": 25,
    "Sword of Light": 80,
    "Boots of Swiftness": 50,
    "Boss Key": True
}

#addItemToInvetory(player, "Bow")
