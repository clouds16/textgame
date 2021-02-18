from enemies import *
from player import *
from textread import *
from fight import *
from items import *
from gamemap import *


def main(user):
    slowText("dialogues/intro_dialogue.txt")
    makePlayer()
    townSquare(user)


if __name__ == "__main__":
    main(player)
