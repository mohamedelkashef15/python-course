#############################
# Problem 33
# * Problem definition
# Write a Python program to find the common characters that appear in all given strings. You will use set operations to find the intersection (common elements) among multiple strings.

#############################
# * Problem instruction
# 1- Create multiple strings.
# 2- Convert each string into a set (since sets only contain unique characters).
# 3- Use the intersection() method to find common characters among all sets.
# 4- Print the common characters.

# * Problem solution

# Define multiple strings
str1 = "python"
str2 = "typhoon"
str3 = "phony"

# Convert strings to sets
set1 = set(str1)
set2 = set(str2)
set3 = set(str3)

# Find common characters using intersection
common_chars = set1.intersection(set2, set3)

print("Common characters:", common_chars)
