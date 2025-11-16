#############################
# Problem 21
# * Problem definition
# Write a Python program that defines a list containing duplicate elements and returns a new list with all duplicates removed, keeping only unique elements.
#############################

# * Problem instructions
# 1- Use loops or set to remove duplicates
# 2- display results
# * Problem solution
numbers = [1, 2, 3, 2, 4, 3, 5]

# Using loop
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(f"List after removing duplicates: {unique_numbers}")

# Using set
# unique_numbers = list(set(numbers))
# print(f"List after removing duplicates: {unique_numbers}")











