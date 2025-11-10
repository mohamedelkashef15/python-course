#############################
# Problem 35
# * Problem definition
# Write a Python program that takes a dictionary and inverts it, meaning the keys become values and the values become keys.
# Assume that all original values are unique and hashable so they can be used as dictionary keys.

#############################
# * Problem instruction
# 1- Create a dictionary with unique values.
# 2- Loop through each key-value pair in the dictionary.
# 3- Assign the value as the new key and the key as the new value in a new dictionary.
# 4- Print the inverted dictionary.

# * Problem solution
# Original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Inverted dictionary
inverted_dict = {}

for key, value in original_dict.items():
    inverted_dict[value] = key

print("Original dictionary:", original_dict)
print("Inverted dictionary:", inverted_dict)






