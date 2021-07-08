class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, animal):
        self.animals.append(animal)
        return self
    def print_all_info(self):
        for animal in self.animals:
            animal.display_info()

class Animal:
    def __init__(self, name):
        self.name = name
    def noise(self):
        print("generic noise")
    def display_info(self):
        print(self.name)

class Mammal(Animal): 
    def __init__(self, name):
        super().__init__(name)
        self.has_hair = True
    def noise(self):
        print("a hairy noise")
    def display_info(self):
        print("A hairy",self.name)

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.has_scales = True
    def noise(self):
        print("sssss")
    def display_info(self):
        self.noise()
        print("A scaly",self.name)

class BigCat(Mammal):
    def __init__(self, name, has_hair= True, lives=9):
        self.name = name
        self.has_hair = True
        self.lives = 9
    def noise(self):
        print("ROAR!")
    def display_info(self):
        self.noise()
        print("A powerful",self.name,"with", self.lives," lives!")

zoo1 = Zoo("John's Zoo")
simba = BigCat("Simba")
nagini = Reptile("Nagini")
zoo1.add_animal(simba)
zoo1.add_animal(nagini)
zoo1.print_all_info()