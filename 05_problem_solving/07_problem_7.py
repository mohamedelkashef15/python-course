#############################
# Problem 7
# * Problem definition
# Write a Python program that that takes an integer as an input and display it as negative number
#############################
# * Problem Instructions
# 1- Ask user to enter a number
# 2- check if number is positive or negative
# 3- if number is positive => convert to negative
# 4- if number is negative => leave it as it is
# 5- Display result

# * Problem Solution
num = float(input("Enter a number: "))

if num > 0:
    num *= -1

print(f"Negative value = {num}")





