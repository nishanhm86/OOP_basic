class Vehicles:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} Engine started")

class Cars(Vehicles):
    def __init__(self, brand, model):
        super().__init__(brand) # Inherit 'brand' from Vehicle
        self.model = model

    def display_info(self):
            print(f"Car {self.brand} {self.model}")

#Creating objects

c1 = Cars("Mercedez", "Benz E 200")
c1.start_engine()   #Inherited method
c1.display_info()   #Child method