#############################
# Problem 15
# * Problem definition
# Write a Python program that takes a string and a character from the user, then counts how many times that character appears in the string.
#############################
# * Problem Instructions
# 1- Ask the user to enter a string.
# 2- Ask the user to enter a specific character to count.
# 3- Use the count() method to count occurrences of that character in the string.
# 4- Display the count to the user.

# * Problem Solution
text = input("Enter a string: ")
char = input("Enter a character to count: ")

count = text.count(char)

print(f"The character '{char}' appears {count} time(s) in the string.")


