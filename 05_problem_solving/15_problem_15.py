#############################
# Problem 15
# * Problem definition
# Write a Python program that takes a string from the user and checks whether it starts and ends with specific letter entered by the user.

#############################
# * Problem Instructions
# 1- Ask user to enter a word or a sentence
# 2- check if word or sentence first letter equals last letter if they are equal then print true else print false
# 3- display result

# * Problem Solution
text = input("Enter a sentence: ")

if text[0] == text[-1]:
    print("True")
else:
    print("false")













