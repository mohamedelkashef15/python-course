#############################
# Problem 22
# * Problem definition
# Write a Python program that defines a list containing duplicate elements and returns a new list with all duplicates removed, keeping only unique elements.
#############################

# * Problem instructions
# 1- Define a list with some duplicate elements.
# 2- Use either a set or loop logic to remove duplicates.
# 3- Preserve the order of elements if possible.
# 4- Print the final list with duplicates removed.

# * Problem solution
# Using set
numbers = [1, 2, 3, 2, 4, 3, 5]

unique_numbers = list(set(numbers))

print("List after removing duplicates:", unique_numbers)

# using loops
# Remove duplicates manually
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

# Display result
print(f"List after removing duplicates: {unique_numbers}")



