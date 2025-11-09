#############################
# Problem 16
# * Problem definition
# Write a Python program that takes a string from the user and counts how many letters and digits it contains.

#############################
# * Problem Instructions
# 1- Ask the user to enter a string.
# 2- Initialize two counters — one for digits and one for letters.
# 3- Loop through each character in the string.
# 4- Use the isalpha() method to check if a character is a letter.
# 5- Use the isdigit() method to check if a character is a digit.
# 6- Increment the appropriate counter based on the type.
# 7- Print the total number of letters and digits.

# * Problem Solution
text = input("Enter a string: ")

letters = 0
digits = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Number of letters:", letters)
print("Number of digits:", digits)
