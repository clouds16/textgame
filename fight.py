from player import *
from enemies import *
from items import *
import random as r
import time
import os
from sounds import *


def encounterEnemy(player, enemy):

    print("You have encountered a ", enemy.getName(),
          "Enemy. Your current HP is :", player.getHealth(), "\nEnemy HP is: ", enemy.getHealth())
    player_choice = input(
        "\nFight (f) or use item (i):")
    counter = 0

    while True:
        if counter >= 1:
            player_choice = input(
                "\nKeep fighting (f)  or use item(i) ? ")

        # if player_choice == "run" or player_choice == "r":
        #     runroll = runAway(player)
        #     if runroll:
        #         break

        # PLayer chooses to fight
        if player_choice == "fight" or player_choice == "f":
            time.sleep(1)
            fightEnemy(player, enemy)
            # Player Death
            if player.getHealth() <= 0:
                playsound(songs["player-defeated"])
                print("You have been defeated")
                exit()
            # Enemy Defeated
            elif enemy.getHealth() <= 0:
                print("you have defeated the boss!")
                playsound(songs["defeat-enemy"])
                return True

        elif player_choice == "i":
            useItem()

        else:
            print("you cannot do that right now!")

        counter += 1


def runAway(player):

    while True:
        rand = r.randint(1, 10)

        if rand > 6:
            time.sleep(1)
            print("You have successfully run away")
            return True

        else:
            time.sleep(1)
            print("You cannot run!, you took some damage while trying to run away")
            print("Your health is now at {}".format(player.getHealth()))
            player.takeDamage(30)
            return False


# Turn Based fighting logic
def fightEnemy(player, enemy):
    if player.getSpeed() > enemy.getSpeed():
        time.sleep(.20)

        if checkHealth(player):
            enemy.takeDamage(player.getAttack())
            print("{} uses {}".format(player.name,
                                      player.getItem()))
            print("{} hits {} first! {} is now at {} HP".format(
                player.getName(), enemy.getName(), enemy.getName(), enemy.getHealth()))

            if checkHealth(enemy):
                player.takeDamage(enemy.getAttack())
                print("{} uses {}".format(enemy.getName(), enemy.getAbility()))
                print("{} Hits You Back, your health is now {}\n".format(
                    enemy.getName(), player.getHealth()))

    else:
        if checkHealth(enemy):
            time.sleep(.20)
            player.takeDamage(enemy.getAttack())
            print("{} uses {}".format(player.name,
                                      enemy.getName(), player.getItem()))

            print("{} Hits You first, your health  {}".format(
                enemy.getName(), player.getHealth()))

            if checkHealth(player):
                enemy.takeDamage(player.getAttack())
                print("{} uses {}".format(enemy.getName(), enemy.getAbility()))
                print("{} hits {} f, {} is now at {} HP\n".format(
                    player.getName(), enemy.getName(), enemy.getName(), enemy.getHealth()))


def checkHealth(person):
    personhealth = person.getHealth()

    if personhealth > 0:
        return True


# Test Loop
#encounterEnemy(player, forestBoss)
# encounterEnemy(player, speeder)
