#############################
# Problem 15
# * Problem definition
# Write a Python program that takes a string from the user and checks whether it starts and ends with specific letter entered by the user.

#############################
# * Problem Instructions
# 1- Ask the user to enter a string.
# 2- Ask the user to enter a starting letter to check.
# 3- Ask the user to enter an ending letter to check.
# 4- Use the string methods startswith() and endswith() to perform the checks.
# 5- Display appropriate messages depending on the result.

# * Problem Solution

text = input("Enter a string: ")


if text[0] == text[-1]:
    print("true")
else:
    print("False")









