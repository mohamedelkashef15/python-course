#########################
# Dictionaries Methods Part 2
#   - pop() => Remove and get a specific item by adding it's key
#   - popItem() => Remove and get the last added item
#   - setDefult() => Get a value or set it if missing
#   - fromkeys() => Create a dictionary with default values
# This method saves you from writing repetitive code when setting up default values!
#########################

# pop()
supermarket = {
    "milk": 2,
    "eggs": 12,
    "bread": 1,
    "Chips": 4,
}

print(f"Before {supermarket}")
supermarket.pop("milk")
print(f"After {supermarket}")

# popItem()
supermarket.popitem()
print(supermarket)

# setDefault()
cars = {
    "brand": "Hyundai",
    "year": "2026",
    # "model": "Elantra",
}

default = cars.setdefault("model", "Unknown")

print(cars)

# fromkeys()
# Example 1
absent_students = ["Mohamed", "Ahmed", "Mostafa", "Islam"]

attendance = dict.fromkeys(absent_students, "absent")

print(attendance)

# Example 2
fruits = {
    "apples",
    "banana",
    "orange",
    "mango"
}

fruits_initial_price = dict.fromkeys(fruits, "0.00")
print(fruits_initial_price)