#########################
# Property Decorator
# @property lets you access a method like an attribute.
#########################

class Car:
    def __init__(self, price, km):
        self.km = km
        self.__price = price # private attribute

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value

car = Car(10000000, "150K")

print(car.km)

print(car.price)
car.price = 20000000
print(car.price)




