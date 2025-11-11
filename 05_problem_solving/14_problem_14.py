#############################
# Problem 14
# * Problem definition
# Write a Python program that takes a string from the user and removes all punctuation marks (like ., ,, !, ?, etc.) from it.
# ? !()-[]{};:'",<>./?@#$%^&*_~
# Input: Hello, world! Python is great :)
#############################

# * Problem Instructions
# 1- Ask user to enter a sentence
# 2- create variable include all punctuations
# 3- loop through the string and remove any character that is punctuation mark
# 4- display cleaned string without any punctuation

# * Problem Solution
text = input("Enter a sentence: ")

punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
cleaned_string = ""

for char in text:
    if char not in punctuation:
        cleaned_string += char

print(f"cleaned string without punctuation: {cleaned_string}")











