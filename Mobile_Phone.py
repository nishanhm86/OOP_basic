class MobilePhone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery = 0

    def show_details(self):
        print(f"Mobile Phone Brand: {self.brand} Model: {self.model} Price: {self.price}")

    def charge(self, amount):
        self.battery += amount
        if self.battery >= 100:
            self.battery = 100
            print("Battery fully charged")
        else:
            print(f"Battery: {self.battery}%")

    def use(self, hours):
        self.battery -= hours * 10
        if self.battery < 0:
            self.battery = 0
        print(f"Battery level is {self.battery}% after using {hours} hours")
                  
    def is_low_battery(self):
        if self.battery < 20:
            print(f"Battery is low {self.battery}%")

        else:
            print("Battery is sufficient")

phone1 = MobilePhone("Samsung", "M02", 10000)
phone1.show_details()
phone1.charge(50)
phone1.use(4)
phone1.is_low_battery()