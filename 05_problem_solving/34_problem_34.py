#############################
# Problem 34
# * Problem definition
# Write a Python program to detect whether a list contains duplicate elements or not. You will use a set to help identify duplicates efficiently.

#############################
# * Problem instruction
# 1- Create a list with some elements.
# 2- Convert the list into a set.
# 3- Compare the length of the list and the set.
# 4- If they differ, it means duplicates exist.
# 5- Print whether duplicates are found or not.

# * Problem solution
numbers = [1, 2, 3, 4, 2, 5, 1]

# Convert list to set
unique_numbers = set(numbers)

# Compare lengths
if len(numbers) != len(unique_numbers):
    print("Duplicates detected!")
else:
    print("No duplicates found.")

