from enemies import *
from player import *
from textread import *
from fight import *
from items import *
from gamemap import *



def main():
    
    slowText("dialogues/intro_dialogue.txt", player)
    startMap(player)


if __name__ == "__main__":
    main()
