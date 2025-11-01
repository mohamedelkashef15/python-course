#############################
# Problem 16
# * Problem definition
# Write a Python program that takes a string from the user and removes all punctuation marks (like ., ,, !, ?, etc.) from it.
# ? !()-[]{};:'"\,<>./?@#$%^&*_~
#############################

# * Problem Instructions
# 1- Ask the user to enter a sentence.
# 2- Define a set or list of punctuation characters to remove.
# 3- Loop through the string and remove any character that is a punctuation mark.
# 4- Display the cleaned string without punctuation.

# * Problem Solution
text = input("Enter a sentence: ")
# Example: Hello, world! Python is great :)

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

cleaned_text = ""
for char in text:
    if char not in punctuations:
        cleaned_text += char

print("Sentence without punctuation:", cleaned_text)



