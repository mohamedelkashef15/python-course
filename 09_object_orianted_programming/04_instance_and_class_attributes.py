#########################
# Instance Attributes VS Class Attributes
#
# 1- Instance Attributes (Unique for Each Car)
#  - Attributes that belong to one specific object
#  - Each car has its own values
#  - Defined using self.attribute
#  - Usually created inside __init__

# 2- Class Attributes (Shared by All Cars)

#########################

class Car:
    # class attribute
    wheels = 4
    def __init__(self, color, price, km, model):
        self.color = color
        self.price = price
        self.km = km
        self.model = model


car1 = Car("Red", "600K", "150K", "Toyota")
car2 = Car("Black", "2.3M", "20K", "Audi")

print(car1.color) # Red
print(car2.color) # Black

print(car1.wheels)
print(car2.wheels)

