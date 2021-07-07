class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        if(pirate.health > 0):
            print(self.name,"says:",ninjaAttacksText)
        elif(pirate.health == 0):
            print(self.name,"says triumphantly:",ninjaWinsText)
            print(pirate.name,"loses. the victor is", self.name)
        return self

#This is my full attack!
ninjaAttacksText = "全力攻撃だ"
pirateWasAttackedText = "Shiver me timbers! That hurt me dubloons!"

#You lose. Please do your best next time.
ninjaWinsText = "あなたの負けです。次回はがんばってください"
pirateDefeatedText = "Alas! A captain must go down with his ship..."