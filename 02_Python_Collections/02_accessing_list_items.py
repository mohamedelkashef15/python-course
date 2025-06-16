#########################
#   Accessing List items
#########################

fruits = ["Orange", "Mango", "Banana", "Apple", "Avocado", "Coconut", "Guava"]

# length
print(len(fruits)) # 7

# access first item
print(fruits[0]) # Orange

# Access third item
print(fruits[2]) # Banana

# access last item in the list
print(fruits[-1]) # Guava

# Slicing lists [End is not included]
print(fruits[2:])
print(fruits[:2])
print(fruits[2:5]) # ["Banana", "Apple", "Avocado"]

# Access nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(nested_list[0])
print(nested_list[0][2]) # 3
print(nested_list[2][0]) # 7












