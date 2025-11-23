#############################
# Problem 36
# * Problem definition
# Write a Python program that merges two dictionaries into a single dictionary. If both dictionaries have the same key, the value from the second dictionary should overwrite the first.
#############################
# * Problem instruction
# 1- Create two dictionaries.
# 2- Use the update() method to merge the second dictionary into the first.
# 3- Print the merged dictionary.
# 4- (Optional) Use dictionary unpacking for a concise one-line solution.

# * Problem solution
# Method 1:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dict2 into dict1
dict1.update(dict2)

print("Merged dictionary:", dict1)

# Method 2:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge using dictionary unpacking
merged_dict = {**dict1, **dict2}

print("Merged dictionary:", merged_dict)



