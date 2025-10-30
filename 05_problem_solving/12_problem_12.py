#############################
# Problem 12
# * Problem definition
# Write a Python program that takes a sentence from the user and counts how many words are in it.
#############################
# * Problem Instructions
# 1- Ask the user to enter a sentence.
# 2- Split the sentence into words using the split() method.
# 3- Count the number of words using the len() function.
# 4- Print the total number of words.

# * Problem Solution
sentence = input("Enter a sentence: ")

words = sentence.split()
count = len(words)

print("Number of words:", count)








