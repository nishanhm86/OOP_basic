class cookie_cutter:
    def __init__(self, shape): #method
        self.shape = shape
        self.usage_count = 0

    def describe(self):
        print(f"I am a {self.shape} cookie cutter")

    def make_cookie(self):
        self.usage_count += 1
        print(f"I have made a {self.shape} cookie!")

    def status(self):
        print(f"I have used {self.shape} cutter for {self.usage_count} times!")

    def reset_counter(self):
        self.usage_count = 0
        print(f"\nThe {self.shape} cutter has been reset!")
        print(f"The count of {self.shape} use is {self.usage_count}!")

star_cutter = cookie_cutter("Star")     #Object 1
round_cutter = cookie_cutter("Round")   #Object 2
heart_cutter = cookie_cutter("Heart")   #Object 3


star_cutter.describe()
round_cutter.describe()
heart_cutter.describe()
print("\n")
star_cutter.make_cookie()
star_cutter.make_cookie()
star_cutter.make_cookie()
print("\n")
round_cutter.make_cookie()
round_cutter.make_cookie()
print("\n")
heart_cutter.make_cookie()
print("\n")

star_cutter.status()
round_cutter.status()
heart_cutter.status()

star_cutter.reset_counter()
round_cutter.reset_counter()
heart_cutter.reset_counter()