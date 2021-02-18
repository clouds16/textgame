from player import *
import random
import time


def showItems():
    print(player.inventory)


def useItem():

    print("These are the items currently in your inventory: ",
          player.inventory.keys())
    useanitem = input("which item would you like to use? ")
    found = False

    for items in player.inventory:
        if items == useanitem:
            itemEffects(useanitem)
            found = True
            break

    if found:
        return found
    else:
        print("Item not in your inventory!")


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


def enemyItemDrop():
    randomize = random.randint(1, 10)
    if randomize > 7:
        print("The enemy has dropped an item!")
        randomitem = random.randint(1, len(items))
        itemlist = list(items)
        itempickedup = itemlist[randomitem]

        print(itempickedup)
        return itempickedup

    else:
        print("Looks like The enemy didnt have anything ")


def removeItemFromInventory(item):
    player.inventory.pop(item)
    print("{} has been consumed! ".format(item))


def addItemToInvetory(player, item):
    player.inventory[item] = items[item]

    print("You have added {} to your inventory".format(item))
    print(player.inventory)


items = {
    "small potion": 20,
    "medium potion": 40,
    "super potion": 100,
    "speed potion": 30,
    "Bow": 45,
    "Dagger": 25,
    "Rat on a Stick": 2,
    "Sword of Light": 80,
    "Boots of Swiftness": 50,
    "Boss Key": True
}

#addItemToInvetory(player, "Bow")
