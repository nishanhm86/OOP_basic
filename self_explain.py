class name_list:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")

s1 = name_list("Janethri", 34)
s2 = name_list("Nishan", 30)
s3 = name_list("Methyumi", 3)
s4 = name_list("Mandinu", 5)

s1.display_info()
s2.display_info()
s3.display_info()
s4.display_info()

