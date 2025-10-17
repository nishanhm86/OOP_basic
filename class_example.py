class cars:
    def __init__(self, brand, model, YOM, currency, price):

        self.brand = brand
        self.model = model
        self.YOM = YOM
        self.currency = currency
        self.price = price
        self.speed = 0


    def get_car_info(self):
        print(f"My car is a {self.brand} {self.model} made in {self.YOM} and value is {self.currency} {self.price}")

    def car_accelerate(self, value):
        self.speed += value
        print (f"{self.brand} {self.model}, accelerated by {value} current speed: {self.speed} km/h")

    def car_break(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0

        print(f"When {self.brand} {self.model} breaks the speed reduced to {self.speed} km/h in 2 seconds")

c1= cars("Toyota","Yaris", 2024, "LKR", 1100000 )


c1.get_car_info()
c1.car_accelerate(60)
c1.car_break(30)