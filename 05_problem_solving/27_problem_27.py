#############################
# Problem 27
# * Problem definition
# Write a Python program that defines a tuple and identifies all elements that appear more than once.
#############################

# * Problem instructions
# 1- Define a tuple with some repeated elements.
# 2- Create an empty list or set to store repeated elements.
# 3- Loop through the tuple and count occurrences of each element.
# 4- If an element appears more than once and is not already in the repeated list, add it.
# 5- Print the repeated elements.

# * Problem solution
numbers = (1, 2, 3, 2, 4, 5, 3, 6)

# List to store repeated elements
repeated = []

# Loop through the tuple
for num in numbers:
    if numbers.count(num) > 1 and num not in repeated:
        repeated.append(num)

# print(numbers.count(3))
# Display result
print("Repeated elements:", repeated)









