class ElectricCar:
    def __init__(self, make, model, battery_capacity):
        self.make = make
        self.model = model
        self.battery_capacity = battery_capacity
        self.battery_level = 100
        self.speed = 0

    def start_Engine(self):
        if self.battery_level == 0:
            print("Battery empty, car cannot be started, plug in to the charger")
        else:
            print(f"{self.make} {self.model} Engine Started Silently")

    def drive(self, speed, duration):
        if self.battery_level <= 0:
            print(f"Car cannot drive. Battery is empty")
            return
        self.speed = speed
        print(f"Car is driving at {self.speed} km/h for {duration} hours")
        self.car_travelled(duration)

    def car_travelled(self, hours):
        self.battery_level = max(0, self.battery_level - hours * 10)
        if self.battery_level > 0:
            print(f"Battery level is {self.battery_level} %")
        else:
            print("Battery depleted!, Charge Battery Immediately")
            self.speed = 0

    def charge(self):
        self.battery_level = 100
        print(f"Battery is fully charged")

class GPS:
    def navigation (self, destination):
        print(f"Navigating to {destination}")

class Autopilot:
    def activate_autopilot (self):
        print("Auto pilot activated")

class Smart_Car(ElectricCar, GPS, Autopilot):
    def display_info(self):
        print(f"My {self.make} {self.model} has a {self.battery_capacity} kWh battery and is {self.battery_level}% charged")


my_smart_car = Smart_Car("Tesla", "Model s", 200)
my_smart_car.start_Engine()
my_smart_car.display_info()
my_smart_car.navigation("to Colombo")
my_smart_car.activate_autopilot()
my_smart_car.drive(100, 2)
my_smart_car.charge()
my_smart_car.display_info()
