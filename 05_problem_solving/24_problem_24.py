#############################
# Problem 24
# * Problem definition
# Write a Python program that defines a list of numbers and separates the even and odd numbers into two different lists.
#############################

# * Problem instructions
# 1- Define the element you want to check.
# 2- Use the in keyword to check if the element is in the list.
# 3- Print an appropriate message based on the result.

# * Problem solution
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")