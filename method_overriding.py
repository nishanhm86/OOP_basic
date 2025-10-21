class Animal:
    def speak(self):
        print("Animal make sounds")

class dog(Animal):
    def speak(self):
        print("Dog sounds Woof!")

class cat(Animal):
    def speak(self):
        print("Cat sounds Meow!")

#polymorphism use
for animal in [dog(), cat(), Animal()]:
    animal.speak()