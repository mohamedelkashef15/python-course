#########################
# Encapsulation
# => hiding internal data and controlling how it is accessed or modified.

# Types of Attributes
# 1- public
# - Use it when you want it visible and editable.

# 2- protected
# Use it when you want to warn others not to touch it, but still allow subclass access.

# 3- private
# Use it when you must protect the data, and it should not be modified or read from outside class
#########################

class Car:
    def __init__(self, model, year, price):
        self.model = model # public attribute
        self._year = year # protected attribute
        self.__price = price # private attribute

car = Car("Toyota", 2022, 11000000)

# access public attribute
print(car.model)
car.model = "BMW"
print(car.model)

# access protected attribute
print(car._year)
car._year = 2025
print(car._year)

# access private attribute
# print(car.__price)

print(car._Car__price)












