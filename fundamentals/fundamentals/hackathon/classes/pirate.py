class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 5
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        hitOrMissNumber = random.randint(1,self.speed)
        if(hitOrMissNumber >= self.speed/2):
            ninja.health -= self.strength
            if(ninja.health > 0):
                print(self.name,"says:",pirateAttacksText)
                print(ninja.name,"is down to",ninja.heath," health.")
                print(ninja.name,"cries out:", ninjaWasAttackedText)
            elif(ninja.health <= 0):
                print(self.name,"says triumphantly:",pirateWinsText)
                print(ninja.name,"loses. the victor is", self.name)
                print("With his last breath,",ninja.name,"cries out:",ninjaDefeatedText)
        elif(hitOrMissNumber < self.speed/2):
            print(self.name,"moved too slow! The attack missed!")
        return self

pirateAttacksText = "Avast ye scallywag!"
#how careless!
ninjaWasAttackedText = "うかつ だ な"

pirateWinsText = "Yo ho yo ho! I'll see ye walk the plank"
#you show promise!
ninjaDefeatedText: "可能性"
