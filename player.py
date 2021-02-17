
class Player:
    def __init__(self, name, feature,  item):
        self.name = name
        self.feature = feature
        self.item = item
        self.speed = 30
        self.health = 100
        self.attack = 30
        self.armor = 20

        self.inventory = {
            "small potion": 20,
            "medium potion": 40,
            "speed potion": 30,
            "Boss Key": True

        }

    def getName(self):
        return self.name

    def getAbility(self):
        return self.feature

    def getItem(self):
        return self.item

    def getFeature(self):
        return self.feature

    def getHealth(self):
        return self.health

    def getSpeed(self):
        return self.speed

    def getAttack(self):
        return self.attack

    def setAttack(self, attack):
        self.attack = attack

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
    player_feature = str(input("What is your best feature? "))
    player_item = str(
        input("You wake up, look around you, the first thing you see is: "))

    player = Player(player_name, player_feature, player_item)

    print("Welcome to the world ", player.name, "may your ",
          player.feature, "and your ", player.item, "help you in your quest")


player = Player("Cloud", "Stamina", "Sword")
