class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        print(f"Engine started for {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, year, model, fuel_type):
        super().__init__(brand, year)
        self.model = model
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"{self.brand} is a {self.fuel_type} car manufactured in {self.year}")

class ElectricCar(Car):
    def __init__(self, brand, year, model, battery_capacity):
        super().__init__(brand, year, model, "Electric") # over ridding fuel_type
        self.battery_capacity = battery_capacity
    def charge(self):
        print(f"Charging {self.brand} {self.model} with {self.battery_capacity} KWh")


EV1 = ElectricCar("Nissan", 2022, "Leaf",100)
EV1.start_engine()
EV1.display_info()
EV1.charge()