#############################
# Problem 29 - Sets
# * Problem definition
# Write a Python program that defines two sets and finds their union (all unique elements) and intersection (common elements).
#############################
# * Problem instruction
# 1- Define two sets with some overlapping elements.
# 2- Use the union() method or | operator to find the union.
# 3- Use the intersection() method or & operator to find the intersection.
# 4- Print both results.

# * Problem solution
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Find union and intersection
union_result = set1.union(set2)
intersection_result = set1.intersection(set2)

# Method 2
# union_result = set1 | set2
# intersection_result = set1 & set2

# Display results
print("Union:", union_result)
print("Intersection:", intersection_result)
