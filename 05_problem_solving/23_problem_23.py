#############################
# Problem 23
# * Problem definition
# Write a Python program that defines a list and checks whether a specific element exists in that list. If it exists, print a message confirming its presence; otherwise, indicate that it is not found.
#############################

# * Problem instructions
# 1- Define the element you want to check.
# 2- Use the in keyword to check if the element is in the list.
# 3- Print an appropriate message based on the result.

# * Problem solution
# Method 1
numbers = [10, 20, 30, 40, 50]

# Define the element to check
element = 30

# Check if element exists
if element in numbers:
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")

# Method 2: Using a for loop (manual check)
numbers = [10, 20, 30, 40, 50]
element = 30
found = False

for num in numbers:
    if num == element:
        found = True
        break

if found:
    print(f"{element} exists in the list.")
else:
    print(f"{element} does not exist in the list.")

