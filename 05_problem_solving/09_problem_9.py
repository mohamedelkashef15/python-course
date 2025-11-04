#############################
# Problem 9
# * Problem definition
# Write a Python program that takes a string from the user and then reverses it.
# ? hello => olleh
#############################
# * Problem Instructions
# 1- Ask user to enter a string (word , sentence)
# 2- Reverse order of characters in the string
# 3- Display result

# * Problem Solution
text = input("Enter a word or sentence: ")

reversed_text = text[::-1]

print(f"Reversed text: {reversed_text}")

