#############################
# Problem 17
# * Problem definition
# Write a Python program that takes multiple words from the user (separated by spaces) and joins them into a single string where each word is separated by a comma and a space.

# ? apple banana cherry mango
#############################
# * Problem instructions
# 1- Take input from the user as a single string of words separated by spaces.
# 2- Split the string into a list of words.
# 3- Join the words using a comma and a space ", ".
# 4- Print the final formatted string.

# * Problem solution
words = input("Enter words separated by spaces: ")

# Split words into a list
word_list = words.split()

# Join words with commas
result = ", ".join(word_list)

# Display result
print(result)