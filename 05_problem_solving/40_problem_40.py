#############################
# Problem 39
# * Problem definition
# Write a Python program that takes a list of words and returns only the words that have more than 3 characters.
# Use the built-in filter() function to perform the filtering.
#############################
# * Problem instruction
# 1- Create a list of words.
# 2- Use the filter() function with a lambda expression to keep only the words whose length is greater than 3.
# 3- Convert the result from filter into a list using list().
# 4- Print both the original list and the filtered list.

# * Problem solution
words = ["hi", "hello", "sun", "world", "go", "python"]

# Use filter() to get words longer than 3 characters
long_words = list(filter(lambda word: len(word) > 3, words))

print("Original list:", words)
print("Filtered list (more than 3 letters):", long_words)
