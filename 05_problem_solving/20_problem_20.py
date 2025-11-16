#############################
# Problem 20
# * Problem definition
# Write a Python program that defines a list of numbers and counts how many times a specific element appears in the list USING FOR LOOP
#############################

# * Problem instructions
# 1- Create variable count and set it equals 0
# 2- Loop on numbers if element equals value of num then increase count by 1 else do nothing
# 3- Display value of count

# * Problem solution
numbers = [1, 3, 5, 3, 7, 3, 9, 4, 3, 1]
element = 1
count = 0

for num in numbers:
    if num == element:
        count += 1

print(f"The number {element} appears {count} times in the list")









