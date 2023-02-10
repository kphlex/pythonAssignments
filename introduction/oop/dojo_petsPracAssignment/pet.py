
tricks = ["Sit", "Roll-over", "Speak", "Shake"]
noise = ["Bark", "meow", "Moo", "Some Animal Noise"]

class Pet():
    
    def __init__(self, name, type, tricks, energy=0, health=50):
        super().__init__()
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health
        
    def sleep(self):
        self.energy += 25
        print(f"Gained {self.energy} energy while sleeping!")
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Gained {self.energy} energy and {self.health}health!")
        return self
    
    def play(self):
        self.health += 5
        self.energy -= 10
        print(f"Gained {self.health} health but used {self.energy} energy!")
        return self
    
    def noise(self):
        if self.type == "Dog":
            print(noise[0])
        if self.type == "Cat":
            print(noise[1])
        else:
            print("IDK WHAT PET YOU HAVE")

pet_1 = Pet("Kujo", "Dog", tricks[1])

pet_2 = Pet("SomeCat", "Cat", tricks[2])
