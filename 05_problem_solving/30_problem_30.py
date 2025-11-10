#############################
# Problem 30
# * Problem definition
# Write a Python program that checks whether one set is a subset of another — meaning all elements of the first set exist inside the second set.
#############################
# * Problem instruction
# 1- Define two sets.
# 2- Use the issubset() method or the <= operator to check if one set is a subset of another.
# 3- Print whether the first set is a subset of the second.

# * Problem solution
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set1 is subset of set2
is_subset = set1.issubset(set2)

# Display result
print("Set1 is a subset of Set2:", is_subset)















