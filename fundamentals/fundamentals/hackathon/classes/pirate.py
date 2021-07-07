class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        if(ninja.health > 0):
            print(self.name,"says:",)
        return self

pirateAttacksText = "Avast ye scallywag!"
#how careless!
ninjaWasAttackedText = "うかつ だ な"

pirateWinsText = "Yo ho yo ho! I'll see ye walk the plank"
#you show promise!
ninjaWasDefeatedText: "可能性"
