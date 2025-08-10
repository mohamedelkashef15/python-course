#############################
# Dictionaries Methods Part 1
#   - clear()
#   - copy()
#   - items() => Returns a list containing a tuple for each key value pair
# Display or export complete records
#   - get() => Returns the value of the specified key
#   Safe data retrieval from APIs/databases

#   - keys()
#   - values()
#############################

# clear()
shopping_cart = {
    "apple": 3,
    "banana": 4,
    "orange": 2
}
print(f"before {shopping_cart}")
shopping_cart.clear()

print(f"after {shopping_cart}")

# copy()
original_recipe = {
    "flour": "2 cups",
    "suger": "1 cup",
    "eggs": 2
}

bakery_copy = original_recipe.copy()
bakery_copy["suger"] = "3/4 cup"

print(f"Original: {original_recipe}")
print(f"Modified: {bakery_copy}")

# items()
student = {
    "name": "Maged",
    "grade": "A",
    "attendance": "95%"
}
print(student.items())

# get()
print(student.get("name", "Unknown"))
print(student.get("age", "Unknown"))

# keys()
print(student.keys())

# values()
print(student.values())





