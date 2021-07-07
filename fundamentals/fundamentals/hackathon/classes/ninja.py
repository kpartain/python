class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 7
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        hitOrMissNumber = random.randint(1,self.speed)
        if(hitOrMissNumber >= self.speed/2):
            pirate.health -= self.strength
            if(pirate.health > 0):
                print(self.name,"says:",ninjaAttacksText)
                print(pirate.name,"is down to",pirate.heath," health.")
                print(pirate.name,"cries out:", pirateWasAttackedText)
            elif(pirate.health <= 0):
                print(self.name,"says triumphantly:",ninjaWinsText)
                print(pirate.name,"loses. the victor is", self.name)
                print("With his last breath,",pirate.name,"cries out:",pirateDefeatedText)
        elif(hitOrMissNumber < self.speed/2):
            print(self.name,"moved too slow! The attack missed!")
        return self

#This is my full attack!
ninjaAttacksText = "全力攻撃だ"
pirateWasAttackedText = "Shiver me timbers! That hurt me dubloons!"

#You lose. Please do your best next time.
ninjaWinsText = "あなたの負けです。次回はがんばってください"
pirateDefeatedText = "Alas! A captain must go down with his ship..."