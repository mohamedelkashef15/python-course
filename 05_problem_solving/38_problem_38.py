#############################
# Problem 40
# * Problem definition
# Write a Python program that takes a list of strings and removes empty strings while also stripping leading and trailing spaces from the remaining ones.
# Use the built-in filter() function to remove empty strings and the map() function to strip spaces.
#############################
# * Problem instruction
# 1- Create a list containing strings, some of which may be empty or have extra spaces.
# 2- Use the filter() function to remove all empty strings ("").
# 3- Use the map() function with str.strip (or a lambda) to remove spaces from each string.
# 4- Convert both results to lists and print the cleaned list.

# * Problem solution
# Define a list of strings
words = ["  apple  ", "", "banana ", "  ", "cherry", "  grape"]

# Step 1: Remove empty strings (including spaces-only strings)
non_empty = list(filter(lambda word: word.strip() != "", words))

# Step 2: Strip spaces from remaining strings
cleaned_words = list(map(lambda word: word.strip(), non_empty))

print("Original list:", words)
print("Cleaned list:", cleaned_words)





