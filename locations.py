class Map:
    def __init__(self, name , enemy , item ):
        self.name = name
        self.enemy = enemy
        self.item = item
        self.timespassed = 0
        
        
    def getName(self):
        return self.name
    
    def getEnemy(self):
        return self.enemy
    
    def getItem(self):
        return self.item
    
    def getTimesPassed(self):
        return self.timespassed
    
    def passTrough(self):
        return self.timespassed  
    

    
        