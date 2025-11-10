#############################
# Problem 38
# * Problem definition
# Write a Python program that takes a list of strings and returns a new list where all strings are converted to uppercase.
# Use the built-in map() function to achieve this transformation.
#############################
# * Problem instruction
# 1- Create a list containing multiple strings.
# 2- Use the map() function with the built-in str.upper method to convert each string to uppercase.
# 3- Convert the result from map into a list using list().
# 4- Print both the original list and the new uppercase list.

# * Problem solution
words = ["hello", "world", "python", "map"]

# Use map() to convert all strings to uppercase
uppercase_words = list(map(lambda word: word.upper(), words))

print("Original list:", words)
print("Uppercase list:", uppercase_words)





