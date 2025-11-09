#############################
# Problem 26
# * Problem definition
# Write a Python program that defines a tuple and finds the index of a specific element in that tuple. If the element does not exist, handle it gracefully.
#############################

# * Problem instructions
# 1- Define the element whose index you want to find.
# 2- Use the index() method to find the position of the element.
# 3- Print the index or a message if the element is not found.

# * Problem solution
# Define the tuple
numbers = (10, 20, 30, 40, 50)

# Define the element to find
element = 10

if element in numbers:
    index = numbers.index(element)
    print(f"The element {element} is at index {index}.")
else:
    print(f"The element {element} is not in the tuple.")



