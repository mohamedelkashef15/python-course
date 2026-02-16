#########################
# Getter & Setter
# Methods used to access (get) and update (set) the value of an object's attributes in a controlled way.

# Why Do We Need Getters and Setters

#########################
class Car:
    def __init__(self, price):
        self._price = price # protected attribute

    # get price
    def get_price(self):
        return self._price

    # set price
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

car = Car(10000000)

# print(car._price) # warning

print(car.get_price())

car.set_price(-10)
print(car.get_price())












