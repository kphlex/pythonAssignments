import pet

treats = ["bits", "bacon", "wishbone", "milkbone", "salmon", "tuna","dubia"]
pet_food = ["diamond", "purina", "blue", "greens", "pedigree"]

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
        
    def __repr__(self):
        ninja_info = (f"First Name:{self.first_name}\nLast Name:{self.last_name}\nPet:{self.pet}")
        return ninja_info
    
    def walk(self):
        print(f"Come on {self.pet}, let's go for a walk")
        return self
    
    def feed(self):
        print(f"Come get your {self.pet_food}")
        return self
    
    def bathe(self):
        print(f"Time to give the {self.pet} a bath")
        return self


green_ninja = Ninja("First", "One", pet.pet_1.name, treats[1], pet_food[0])

print(green_ninja)
print(green_ninja.pet_food)

green_ninja.walk().bathe().feed()