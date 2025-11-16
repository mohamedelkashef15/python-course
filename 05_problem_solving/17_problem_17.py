#############################
# Problem 17
# * Problem definition
# Write a Python program that takes multiple words from the user (separated by spaces) and joins them into a single string where each word is separated by a comma and a space.

# ? apple banana cherry mango
#############################
# * Problem Instructions
# 1- Ask user to enter a multiple words
# 2- Split the string into list of words then join the words with comma and spaces
# 3- display result

# * Problem Solution
text = input("Enter multiple words: ")

word_split = text.split()
print(word_split)

result = ", ".join(word_split)

print(result)









