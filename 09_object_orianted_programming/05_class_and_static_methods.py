#########################
# * 1- instance Methods:
# - They use self
# - They can access:
# - instance attributes
# - class attributes

# * 2- class Methods
# - work with the class itself, not a specific object
# - Use @classmethod decorator
# - First parameter is cls (the class)
# - access class attributes

# * Why we use class methods
# We need to work with the class itself
# We need to access or modify class attributes

# * 3- static Methods
# - Belongs to the class, but does not access the instance (self) or the class (cls).
# - Is just a utility function related to the class.
# - Is defined with the decorator @staticmethod.
# - Can be called via the class or an instance, but it doesn’t care about any particular object.

# * why we use static methods
# To perform a task that is related to the class, but does not need instance or class attributes.

# * compare between both instance & class & static methods

#########################

class Car:
    count = 0
    def __init__(self, color, price, km, model):
        self.c = color # instance attribute
        self.price = price
        self.km = km
        self.model = model
        Car.count += 1

    # Instance Methods
    def start(self):
        print(f"{self.model} car has started.")
        print(f"{self.model} car color is {self.c}")
        print(f"Car count is: {Car.count}")

    # Class Method
    @classmethod
    def total_cars(cls):
        print(f"Total cars created is: {cls.count}")

    # Static Method
    @staticmethod
    def discount(price, percent):
        result = price - (price * percent/100)
        print(result)

#  100000 - (100000 * 5%)
# 100000 - 5000 = 95000


car1 = Car("Red", "600K", "150K", "Toyota")
car2 = Car("Red", "600K", "150K", "Toyota")
car1.start()

Car.total_cars() # class method called
# car1.total_cars()
# car2.total_cars()

Car.discount(100000, 5) # static method called
car2.discount(100000, 10)
