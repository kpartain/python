class Ninja:
    def __init__(self, first_name, last_name, pet, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        if type(treats) is str: 
            self.treats = []
            self.treats.append(treats)
        self.treats = treats
    def walk(self):
        #walks the ninja's pet invoking the pet play() method
        self.pet.play()
        return self
    def feed(self, treat_fed):
        #feeds the ninja's pet invoking the pet eat() method
        self.treats.remove(treat_fed)
        self.pet.eat()
        return self
    def bathe(self):
        #cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()
        return self

class Pet:
    def __init__(self, pet_name, pet_type, tricks, health, energy):
        self.pet_name = pet_name
        self.pet_type = pet_type
        if type(tricks) is str:
            self.tricks = []
            self.tricks.append(tricks)
        self.tricks = tricks
        if health is None:
            self.health = 80
        self.health = health
        if energy is None:
            self.energy = 80
        self.energy = energy
    def sleep(self):
        #increase energy by 25
        self.energy += 25
        return self
    def eat(self):
        #increase energy 5, health 10
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        # increase health 5
        self.health += 5
        return self
    def noise(self):
        #print out pet sound
        if(self.pet_type == 'dog'):
            print("woof")
        elif(self.pet_type == 'cat'):
            print("meow")
        else:
            print("*low rumble*")

testNinja = Ninja('Nin', 'Ja', Pet('Bowser', 'dog', ['sit', 'hex'], 85, 60), ['acorn', 'potato'])
testNinja.feed('acorn').walk().bathe()