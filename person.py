class Person:
    def __init__(self, name, age):
        self.name = name #Atribute
        self.age = age #Atribute

person1 = Person("Nishan", 39)
person2 = Person("Mandinu", 5)
person3 = Person("Methyumi", 3)

print(f"My name is {person1.name} and I'm {person1.age} years old.")
print(f"My name is {person2.name} and I'm {person2.age} years old.")
print(f"My name is {person3.name} and I'm {person3.age} years old.")