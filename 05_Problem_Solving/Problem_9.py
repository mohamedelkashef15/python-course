#############################
# Problem 9
# * Problem definition
# Write a Python program that takes a string from the user and then reverses it.
#############################

# Instructions
# 1- Ask the user to enter a string (word or sentence).
# 2- Reverse the order of the characters in the string.
# 3- Display the reversed string.

text = input("Enter a word or sentence: ")

reversed_text = text[::-1]
print("Reversed string:", reversed_text)