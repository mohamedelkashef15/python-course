#########################
# Classes and Objects
# * What is class
# A blueprint for creating objects.

# * What is the object
# A real instance of a class.
# instance => a real object created from the blueprint (class).

# * Methods [functions] => actions (behaviors)
# A function that defines behavior

# * Attribute
# Stores data about the object

#########################

class Car:
    # Methods
    def start(self):
        print(f"{self.model} car has started.")
        print(f"{self.model} car color is {self.color} ")

    def drive(self):
        print(f"{self.model} car is driving.")

    def stop(self):
        print(f"{self.model} car has stopped.")

# creating objects
car1 = Car()
car2 = Car()
car3 = Car()

# add attributes
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
car2.start()
# car2.drive()
# car3.stop()



