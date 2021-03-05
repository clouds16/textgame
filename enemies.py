class Enemies:
    def __init__(self, name, ability, feature, health, attack, armor, speed):
        self.name = name
        self.ability = ability
        self.feature = feature
        self.speed = speed
        self.attack = attack
        self.health = health
        self.armor = armor
        self.magic_resist = 0

    def getName(self):
        return self.name

    def getFeature(self):
        return self.feature

    def getAbility(self):
        return self.ability

    def getHealth(self):
        return self.health

    def getSpeed(self):
        return self.speed

    def getAttack(self):
        return self.attack

    def takeDamage(self, damage):
        self.health = self.health - (damage - self.armor)
        return self.health


forestBoss = Enemies("TreeMan ", "Root Slam", "Vines", 100, 30, 10, 5)
desertBoss = Enemies("Giant Lizard", "Tail Whip", "Vanish", 80, 70, 0, 200)
ruinsBoss = Enemies("Stone Golem", "Collosal Slam",
                    "Bullet Punch", 160, 35, 60, 5)


Ganon = Enemies("Ganandorf", "Void Crush", "Slash", 120, 60, 45, 60)
