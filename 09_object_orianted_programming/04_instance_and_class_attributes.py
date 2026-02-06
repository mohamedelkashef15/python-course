#########################
# Instance Attributes VS Class Attributes
#
# 1- Instance Attributes (Unique for Each Car)
#  - Attributes that belong to one specific object
#  - Each car has its own values
#  - Defined using self.attribute
#  - Usually created inside __init__

# 2- Class Attributes (Shared by All Cars)

# One-Sentence Rule for Students 🧠
# “If every car has its own value, use an instance attribute.
# If all cars share the same value, use a class attribute.”

#########################

class Car:
    # class attribute
    wheels = 4
    def __init__(self, color, price, km, model):
        self.color = color
        self.price = price
        self.km = km
        self.model = model

#########################
# color
# price
# km
# model
# 👉 These are instance attributes

# 🔹 Why?
# Because:
# Every car can have different color
# Every car can have different price
# Every car can have different km
# Every car can have different model

car1 = Car("Red", "600K", "150K", "Toyota")
car2 = Car("Black", "2.3M", "20K", "Audi")

print(car1.color)  # Red
print(car2.color)  # Black

print(car1.wheels)
print(car2.wheels)

########################





