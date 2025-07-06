#########################
#   Lists
#     - Accessing List items
#     - Changing List items
#########################

fruits = ["Orange", "Mango", "Banana", "Apple", "Avocado", "Coconut", "Guava"]

# Accessing List items
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[-1])

# Slicing list [End is not included]
print(fruits[2:])
print(fruits[:2])
print(fruits[2:5])

# Acess nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list)
print(nested_list[0])
print(nested_list[0][2])
print(nested_list[2][1])

# Changing List items
colors = ["red", "green", "blue"]

print(colors)
colors[1] = "yellow"

print(colors)

colors[0:2] = ["pink", "purple"]
print(colors)







