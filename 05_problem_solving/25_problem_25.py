#############################
# Problem 25
# * Problem definition
# Write a Python program that defines two sets and (all unique elements) and (common elements).
#############################
# * Problem instruction
# 1- Use union method to get unique elements
# 2- Use intersection method to get common elements

# * Problem solution
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

unique_elements = set1.union(set2)
common_elements = set1.intersection(set2)

print(f"Unique elements: {unique_elements}")
print(f"Common elements: {common_elements}")











