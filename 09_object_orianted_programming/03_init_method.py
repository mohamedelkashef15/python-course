#########################
# __init__ method
# __init__() is a special method in Python classes. called magic or dunder method
# It is called automatically when you create an object.
# It’s used to initialize attributes of the object.

# * Why we use it
# 1- Automatic initialization
# No need to manually add attributes after creating an object
# 2- Avoid editor warnings
# Attributes exist in the class from the start
# 3- Cleaner code
# You can create objects in one line
# 4- Safer objects
# Every object will always have the required attributes

#########################

class Car:
    # __init__ initializes the object with attributes
    def __init__(self, color, price, km, model):
        self.color = color
        self.price = price
        self.km = km
        self.model = model

    # Methods
    def start(self):
        print(f"{self.model} car has started.")

    def drive(self):
        print(f"{self.model} car is driving.")

    def stop(self):
        print(f"{self.model} car has stopped.")

# Creating Objects
car1 = Car("Red", "600K", "150K", "Toyota")
car2 = Car("Black", "2.3M", "20K", "Audi")
car3 = Car("White", "1.2M", "200K", "BMW")

car1.start()
car2.drive()
car3.stop()

# print(dir(str))
# print(dir(car1))

