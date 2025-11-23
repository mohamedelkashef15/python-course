#############################
# Problem 32
# * Problem definition
# Write a Python program that takes a list of words and returns only the words that have more than 3 characters.

#############################
# * Problem instruction
# 1- Use filter built-in function to keep only words which their characters are more than 3
# 2- Convert the result filter to list
# 3- print both original and filtered list

# * Problem solution
words = ["hi", "hello", "sun", "world", "go", "python"]

long_words = list(filter(lambda word: len(word) > 3, words))

print(f"Original list: {words}")
print(f"long words list: {long_words}")












