#############################
# Problem 31
# * Problem definition
# Write a Python program that takes a list of strings and returns a new list where all strings are converted to uppercase.

#############################
# * Problem instruction
# 1- Use built-in function map with str.upper() method to convert each string into upper case
# 2- Convert map into list
# 3- print original list and upper case list

# * Problem solution
words = ["hello", "world", "python", "map"]

upper_list = list(map(lambda word: word.upper(), words))

print(f"Original list {words}")
print(f"Upper case list {upper_list}")















