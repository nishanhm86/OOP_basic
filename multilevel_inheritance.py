class Animals:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sounds(self):
        print(f"Animal make sounds")

class Mammal(Animals):
    def __init__(self, name, sound, has_feet = True):
        super().__init__(name, sound)
        self.has_feet = has_feet
    def check_feet(self):
        if self.has_feet:
            print(f"The {self.name} has feet")
        else:
            print(f"The {self.name} has no feet")

class Dog(Mammal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed

    def display_info(self):
        print(f"Animal {self.name} sounds {self.sound} is a {self.breed}")

dog = Dog("Jojo", "baw baw", "Dobaman")
dog.check_feet()
dog.display_info()
dog.make_sounds()
