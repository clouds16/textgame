
class Player:
    def __init__(self, name, ability,  item):
        self.name = name
        self.ability = ability
        self.item = item
        self.speed = 30
        self.health = 100
        self.attack = 30
        self.armor = 20

        self.inventory = {
            "small potion": 20,
            "medium potion": 40,
            "speed potion": 30,
            "Boss Key": False
        }

    def getName(self):
        return self.name

    def getAbility(self):
        return self.getAbility()

    def getItem(self):
        return self.item

    def getHealth(self):
        return self.health

    def getSpeed(self):
        return self.speed

    def getAttack(self):
        return self.attack

    def setAttack(self, attack):
        self.attack = attack + self.attack

    def setSpeed(self, speed):
        self.speed = speed

    def takeDamage(self, damage):
        self.health = self.health - (damage - self.armor)
        return self.health

    def useHealthPotion(self, item):
        self.health = self.health + item

        if self.health > 100:
            self.health = 100
        return self.health

    def useSpeedPotion(self, item):
        self.speed = self.speed + item
        return self.speed

    def addWeapon(self, weapon):
        self.attack = self.attack + weapon
        return self.attack


def makePlayer():

    player_name = str(input("\n\nWhat is your name? "))
    player_ability = str(input("What kind of abilities do you have? "))
    player_item = str(
        input("What kind of weapon do you use? "))

    player = Player(player_name, player_ability, player_item)

    print("Welcome to the world ", player.name, "may your ",
          player.ability, "and your ", player.item, "help you in your quest")


player = Player("Cloud", "Void", "Sword")
