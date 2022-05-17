class Hero():
    """ Class to crreate Hero for oyr game"""
    def __init__(self,name,level,race):
        """Initiate our Hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """print all parametress hero"""
        description = (self.name + " Level is: " + str(self.level) + " Race is" + self.race + "Health is "+str(self.health)).title()
        print(description)

    def level_up(self):
        """Uopgrade level of Hero"""
        self.level += 1

    def move(self):
        """Start moving hero"""
        print("Hero " + self.name + "start moving . . .")


myhero1=Hero("Vurdalac", 5 , "Orc")
myhero2 = Hero("Alecandre",4, "Human")

myhero1.show_hero()
myhero1.move()
myhero2.show_hero()
myhero2.move()



