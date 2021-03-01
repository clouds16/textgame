from enemies import *
from player import *
from textread import *
from fight import *
from items import *
from gamemap import *
from sounds import *


def main():
    playsound(songs["intro"])
    slowText("dialogues/intro_dialogue.txt")
    # startMap(player)
    straightMap(player)


if __name__ == "__main__":
    main()
