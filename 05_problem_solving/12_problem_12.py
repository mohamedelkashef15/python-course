#############################
# Problem 12
# * Problem definition
# Write a Python program that takes a sentence from the user and counts how many words are in it.
#############################
# * Problem instructions
# 1- Ask user to enter a sentence
# 2- Split sentence into words using split method
# 3- Count number of words
# 4- display number of words

# * Problem solution
text = input("Enter a sentence: ")
words = text.split()
count = len(words)
print(words)

print(f"Number of words is: {count}")








