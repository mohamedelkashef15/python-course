#############################
# Problem 32 | remove duplicates using set and list 
# * Problem definition
# Write a Python program that set from a list to remove duplicate elements.
# You are given a list that may contain repeated values — your task is to remove the duplicates.
#############################
# * Problem instruction
# 1- Create a list that contains some duplicate elements.
# 2- Convert the list into a set to automatically remove duplicates.
# 3- (Optional) Convert the set back into a list if you need a list result.
# 4- Print both the original list and the set without duplicates.

# * Problem solution
numbers = [1, 2, 3, 1, 2, 4, 5, 5]

# Convert list to set to remove duplicates
unique_numbers = set(numbers)

print("Original List:", numbers)
print("Set (No Duplicates):", unique_numbers)

# Optional: convert back to list
unique_list = list(unique_numbers)
print("List Without Duplicates:", unique_list)








