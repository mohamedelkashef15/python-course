#########################
# __init__ method
# __init__() is a special method in Python classes. called magic or dunder method
# It is called automatically when you create an object.
# It’s used to initialize attributes of the object.

# * Why we use it
# 1- Automatic initialization
# 2- Avoid editor warnings
# 3- Cleaner code
# 4- Safer objects

#########################

class Car:
    def __init__(self, color, price, km, model):
        self.c = color
        self.price = price
        self.km = km
        self.model = model

    # Methods
    def start(self):
        print(f"{self.model} car has started.")
        print(f"{self.model} car color is {self.c} ")

    def drive(self):
        print(f"{self.model} car is driving.")

    def stop(self):
        print(f"{self.model} car has stopped.")

car1 = Car("Red", "600K", "150K", "Toyota")
car2 = Car("Black", "2.3M", "20K", "Audi")
car3 = Car("White", "1.2M", "200K", "BMW")

car1.start()
car2.drive()
car3.stop()





