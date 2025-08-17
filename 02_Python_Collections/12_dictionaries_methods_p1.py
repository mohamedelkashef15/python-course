#############################
# Dictionaries Methods Part 1
#   - clear()
#   - copy()
#   - items()
#   - get()
#   - keys()
#   - values()
#############################

# clear()
shopping_cart = {
    "apple": 3,
    "banana": 2,
    "orange": 5
}

print(f"Before {shopping_cart}")
shopping_cart.clear()
print(f"After {shopping_cart}")

# copy()
original_recipe = {
    "floor": "2 cups",
    "suger": "1 cup",
    "eggs": 2
}

copied_recipe = original_recipe.copy()
copied_recipe["suger"] = "3/4 cup"

print(f"Original: {original_recipe}")
print(f"Copied: {copied_recipe}")

# items()
student = {
    "name": "Maged",
    "grade": "A",
    "Attendance": "95%"
}

print(student.items())

# get()
print(student.get("grade"))
print(student.get("age", "Unknown"))

#  keys()
print(student.keys())

# values()
print(student.values())







