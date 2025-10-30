#############################
# Problem 10
# * Problem definition
# Write a Python program that takes a string from the user and counts how many vowels are present in it.
#############################
# Instructions
# 1- Ask the user to enter a string (word or sentence).
# 2- Reverse the order of the characters in the string.
# 3- Display the reversed string.

text = input("Enter a word or sentence: ")
text = text.lower()
count = 0

for char in text:
    if char in "aeiou":
        count += 1

print("Number of vowels:", count)








