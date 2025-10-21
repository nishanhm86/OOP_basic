import math
class Shapes:
    def area(self):
        print("The area is not defined")

class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(f"The radius of the circle is: {math.pi * self.radius**2:.2f}")

class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"The area of the rectangle is: {self.width * self.height}")

#list to store shapes
shape_list = []

#ask user how many shapes to be inserted
num_shapes = int(input(f"How many shapes do you want? \n"))

for i in range(num_shapes):
    shape_type = input(f"\nEnter the shape {i+1} type (Circle/Rectangle): ").strip().lower()
    if shape_type == "circle":
        radius = float(input("Enter the radius of the circle "))
        shape_list.append(Circle(radius))
    elif shape_type == "rectangle":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        shape_list.append(Rectangle(width, height))
    else:
        print("Invalid input")


#Display Area
print("\nCalculating Area")
for shape in shape_list:
    shape.area()

