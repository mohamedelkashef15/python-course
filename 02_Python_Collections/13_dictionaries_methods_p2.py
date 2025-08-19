#########################
# Dictionaries Methods Part 2
#   - pop()
#   - popItem()
#   - setDefult()
#   - fromkeys()
#########################

supermarket = {
    "milk": 2,
    "eggs": 12,
    "bread": 1,
    "chips": 4
}

# pop()
print(f"before {supermarket}")
supermarket.pop("milk")
print(f"after {supermarket}")

# popitem()
supermarket.popitem()
print(supermarket)

# setDefult()
car = {
    "brand": "Hyundai",
    "year": "2026",
}

car.setdefault("model", "Unknown")

print(car)

# fromkeys()
absent_students = ["Mohamed", "Ahmed", "Mostafa", "Gamal", "Maged"]
attendance = dict.fromkeys(absent_students, "absent")

print(attendance)















