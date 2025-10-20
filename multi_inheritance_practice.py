class ElectricCar:
    def __init__(self, make, model, battery_capacity):
        self.make = make
        self.model = model
        self.battery_capacity = battery_capacity

    def start_Engine(self):
        print(f"My car {self.make} {self.model} started silently (Electric)")

    def charge(self):
        print(f"Charging {self.make} {self.model} with {self.battery_capacity} KWh")

class GPS:
    def navigation (self, destination):
        print(f"Car is navigating to {destination}")

class AutoPilot:
    def activate_autopilot(self):
        print("Autopilot activated, Car is driving automatically")

class Smart_Car(ElectricCar,GPS,AutoPilot):
    def display_info(self):
        print(f"My car is {self.make} {self.model} has a battery capacity of {self.battery_capacity} KWh")

my_smart_car = Smart_Car("Tesla", "Model s", 200)
my_smart_car.start_Engine()
my_smart_car.charge()
my_smart_car.activate_autopilot()
my_smart_car.navigation("to Colombo")
my_smart_car.display_info()