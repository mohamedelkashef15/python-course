#############################
# Problem 33
# * Problem definition
# Write a Python program that takes a list of strings and removes empty strings while also stripping leading and trailing spaces from the remaining ones.

#############################
# * Problem instruction
# 1- Use filter built-in function to remove all empty strings
# 2- Use map built-in function to remove all spaces from each string
# 3- Convert both result into lists then print cleaned list

# * Problem solution
words = ["  apple  ", "", "banana ", "  ", "cherry", "  grape"]

non_empty = list(filter(lambda word: word.strip() != "", words))

# "  apple  " => "apple" => True
# "" => "" => False
# "banana " => "banana" => Ture
# "  " => "" => False
# "cherry" => "cherry" => True
# "  grape" => "grape" => True

print(non_empty)

cleaned_list = list(map(lambda word: word.strip(), non_empty))

print(f"Original list: {words}")
print(f"Cleaned list {cleaned_list}")

# Output ['apple', 'banana', 'cherry', 'grape']












