#############################
# Problem 26
# * Problem definition
# Write a Python program to find the common characters that appear in all given strings.
#############################
# * Problem instruction
# 1- Convert 3 strings into 3 sets
# 2- Use intersection method to get the common characters
# 3- print result

# * Problem solution
str1 = "python"
str2 = "typhoon"
str3 = "phony"

set1 = set(str1)
set2 = set(str2)
set3 = set(str3)

common_characters = set1.intersection(set2, set3)

print(f"Common characters {common_characters}")

# [p, y, h, o, n]
















