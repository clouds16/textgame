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


# def createBoss():
#     print("\n\nA figure approaches you \nYou can tell that it is your old High School Bully!")
#     name = str(input("It's been so long, what was the bullies name again? "))
#     ability = str(input("What was his ability? "))
#     feature = str(input("What was their worst feature? "))

#     boss1 = Enemies(name, ability, feature)
#     print("It looks like  ", boss1.getName(), "has come back from highschool to fight you!",
#           "he looms over you with his ugly ", boss1.getFeature(),
#           " and he threathens you with his ", boss1.getAbility())


forestBoss = Enemies("TreeMan ", "Root Slam", "Vines", 100, 30, 10, 5)
desertBoss = Enemies("Giant Lizard", "Tail Whip", "Vanish", 40, 50, 10, 200)
ruinsBoss = Enemies("Stone Golem", "Collosal Slam",
                    "Bullet Punch", 200, 50, 5, 5)


Ganon = Enemies("Ganandorf", "Void Crush", "Slash", 120, 60, 20, 20)
