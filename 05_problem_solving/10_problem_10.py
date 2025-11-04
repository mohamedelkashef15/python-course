# Problem 10
# * Problem definition
# Write a Python program that takes a string from the user and counts how many vowels are present in it.

# ?vowels: aeiou
# hello => 2
#############################
# * Problem instructions
# 1- Ask user to enter a word or a sentence
# 2- convert text to lower case to handle both upper and lower letters
# 3- Check if each character is a vowel or not
# 4- Count how many vowels found
# 5- Display number of vowels

# * Problem Solution
text = input("Enter a sentence or a word: ")
text = text.lower()
count = 0

for char in text:
    if char in "aeiou":
        count += 1

print(f"Number of vowels is: {count}")

# Hello => hello







