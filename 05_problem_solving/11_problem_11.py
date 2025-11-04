#############################
# Problem 11
# * Problem definition
# Write a Python program that takes a string from the user and checks whether it is a palindrome.
# ? A palindrome is a word, phrase, or number that reads the same backward and forward, such as level or racecar.
#############################
# * Problem instructions
# 1- Ask user to enter a string or a word
# 2- convert string to lower case
# 3- reverse string
# 4- compare between original string and reversed string
# 5- if original string equal reversed string => palindrome
# 6- otherwise => not palindrome
# 7- display result

# * Problem solving
text = input("Enter a word or sentence: ")

text = text.lower()
reversed_text = text[::-1]

if text == reversed_text:
    print(f"{text} is palindrome")
else:
    print(f"{text} is not palindrome")








