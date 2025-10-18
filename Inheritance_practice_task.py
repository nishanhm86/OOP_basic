class Animals: #parent/super class
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print("Animals make sounds")

class Mammal(Animals): #child/subclass
    def __init__(self, name, sound, has_feet = True):
        super().__init__(name, sound) # calling the parent constructor
        self.has_feet = has_feet

    def make_sound(self): #overriding parent class method
        print(f"\n{self.name} sounds {self.sound}")
    def check_feet(self): # new method relevant to child class
        if self.has_feet:
            print(f"{self.name} has feet")
        else:
            print(f"{self.name} has no feet")


d1 = Mammal("Cat", "meow meow", True)
d1.make_sound()
d1.check_feet()

d2 = Mammal("Dog", "baw baw", False)
d2.make_sound()
d2.check_feet()
