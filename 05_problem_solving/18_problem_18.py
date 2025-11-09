#############################
# Problem 18
# * Problem definition
# Write a Python program that takes a string from the user and returns a new string with all its characters sorted in alphabetical order.
# ? explain the difference between sort and sorted
#############################
# * Problem instructions
# 1- Take input from the user as a string.
# 2- Convert the string into a list of characters.
# 3- Sort the list alphabetically using the sorted() function.
# 4- Join the sorted characters back into a single string.
# 5- Print the sorted string.

text = input("Enter a string: ")

sorted_text = ''.join(sorted(text))

print(sorted_text)