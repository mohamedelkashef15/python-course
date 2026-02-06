#########################
# Classes and Objects
# ? What is class
# A blueprint for creating objects.
# Defines what the object will have (attributes) and what it can do (methods).
# PascalCase[UpperCamelCase]

# Example blueprint of car

# ? What is the object
# A real instance of a class.
# instance => a real object created from the blueprint (class).
# Each object has its own copy of attributes.
# Example actual car

# Attributes [data] with examples

# * Methods [functions] with examples => actions (behaviors)
# A function that defines behavior
# drive()
# start()
# stop()

# * Attribute
# Stores data about the object
# brand,

#########################
# self means “this object”.
# self.attribute



class Car:
    # model = None
    # Methods
    def start(self):
        print(f"{self.model} car has started.")

    def drive(self):
        print(f"{self.model} car is driving.")

    def stop(self):
        print(f"{self.model} car has stopped.")
        print(f"{self.model} car color is {self.color}")

# Create 3 Objects
car1 = Car()
car2 = Car()
car3 = Car()

# add attributes to each object
car1.color = "Red"
car1.price = "600K"
car1.km = "150K"
car1.model = "Toyota"

car2.color = "Black"
car2.price = "2.3M"
car2.km = "20K"
car2.model = "Audi"

car3.color = "White"
car3.price = "1.2M"
car3.km = "200K"
car3.model = "BMW"

car1.start()
car2.drive()
car3.stop()