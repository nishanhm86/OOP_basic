class calculator:
    def add(self, a=0, b=0, c=0):
        print("Sum =", a + b + c )


calc = calculator()

calc.add(5)
calc.add (5,20)
calc.add(5,20, 55)

class calculator1:
    def add(self, *args):
        print("Sum =", sum(args))

calc = calculator1()

print("\nCalculated Using args\n")
calc.add(5)
calc.add(5,20)
calc.add(5,20, 55)
calc.add(5,20,55,98)

#Operator Polymorphism

# + operator works differently for different types

print("\nOperator Polymorphism(How + work differently for scenario)\n")
print(5+10)
print("Hello " + "AI")
print( [1,2] + [3,4])

#Function Polymorphism

def add (x,y):
    return x + y

print("\nFunction Polymorphism\n")

print(add (5, 10))
print(add("Hello ", "AI"))
print(add([1,2], [3,4]))


#Polymorphism with Classes

class birds:
    def sound(self):
        print("Birds Chirp")

class dog:
    def sound(self):
        print("Dog Bark")

Animal = [birds(), dog()]

print("\nPolymorphism with Classes\n")
for animal in Animal:
    animal.sound() # same method name, different behavior
