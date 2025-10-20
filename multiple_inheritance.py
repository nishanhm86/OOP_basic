#parent 1
class Engine:
    def start_Engine(self):
        print("Engine start")
#parent 2
class GPS:
    def navigation(self, destination):
        print(f"Navigating to {destination}")

#Child class inheritance from both Engine and GPS classes

class car(Engine, GPS):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car is a {self.brand} {self.model}")

car1 = car("Mercedez", "Benz e200")
car1.display_info()
car1.start_Engine()
car1.navigation("to Colombo")