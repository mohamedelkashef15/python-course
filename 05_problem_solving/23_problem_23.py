#############################
# Problem 23
# * Problem definition
# Write a Python program that defines a list of numbers and separates the even and odd numbers into two different lists.
#############################

# * Problem instructions
# 1- Create 2 empty list one for even and other for odd
# 2- Loop numbers list check if num is even then put it in even_number list else put it in odd_numbers list
# 3- Print odd and even lists

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








