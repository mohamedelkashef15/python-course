#############################
# Problem 14
# * Problem definition
# Write a Python program that takes a string and a substring from the user, then checks if the substring exists within the main string.
#############################
# * Problem Instructions
# 1- Ask the user to enter a main string.
# 2- Ask the user to enter a substring to search for.
# 3- Use the in operator to check if the substring exists inside the main string.
# 4- Display a message showing whether it was found or not.

# * Problem Solution
main_string = input("Enter the main string: ")
sub_string = input("Enter the substring to search for: ")

if sub_string in main_string:
    print("The substring exists in the main string.")
else:
    print("The substring does not exist in the main string.")