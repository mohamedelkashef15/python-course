#############################
# Problem 16
# * Problem definition
# Write a Python program that takes a string from the user and counts how many letters and digits it contains.

# ? hello123 => 5 letters, 3 digits
#############################
# * Problem Instructions
# 1- Ask user to enter a string
# 2- create 2 variables one to count letters and one for digits
# 3- loop on string then check if character is letter increment letters by 1, if character is digit then increment digit by 1
# 4- display result of number of letters and digits

# * Problem solution
text = input("Enter a string: ")
letters = 0
digits = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

# hello123
print(f"Number of letters: {letters}")
print(f"Number of digits: {digits}")









