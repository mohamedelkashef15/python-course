#############################
# Problem 11
# * Problem definition
# Write a Python program that takes a string from the user and checks whether it is a palindrome.
# A palindrome is a word, phrase, or number that reads the same backward and forward, such as madam or racecar.
#############################
# Instructions
# 1- Ask the user to enter a string.
# 2- Convert the string to lowercase to make the check case-insensitive.
# 3- Reverse the string using Python slicing.
# 4- Compare the original and reversed strings.
# 5- If they are the same → it’s a palindrome.
# 6- Otherwise → it’s not a palindrome.
# 7- Display the result.


# Step 1: Input a string
text = input("Enter a word or sentence: ")

# Step 2: Convert to lowercase
text = text.lower()

# Step 3: Reverse the string
reversed_text = text[::-1]

# Step 4: Check if palindrome
if text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")




