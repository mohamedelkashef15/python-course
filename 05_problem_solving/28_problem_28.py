#############################
# Problem 28
# * Problem definition
# Write a Python program that takes a dictionary and inverts it, meaning the keys become values and the values become keys.
#############################
# * Problem instruction
# 1- Create empty dictionary "inverted_dictionary"
# 2- Loop through original dict then assign value as a new key, key as a new value
# 3- print "inverted_dictionary"

# * Problem solution
original_dict = {'a': 1, 'b': 2, 'c': 3}

inverted_dictionary = {}

for key, value in original_dict.items():
    print(key, value)
    inverted_dictionary[value] = key

print(inverted_dictionary)









