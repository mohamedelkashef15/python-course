#############################
# Problem 37
# * Problem definition
# Write a Python program that defines a function to find the maximum of three numbers.
# The function should take three numbers as input and return the largest one.
#############################
# * Problem instruction
# 1- Define a function that accepts three numbers as parameters.
# 2- Compare the numbers using conditional statements (if, elif, else).
# 3- Return the largest number.
# 4- Test the function with sample values and print the result.

# * Problem solution

# Define the function
def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Test the function
num1 = 10
num2 = 25
num3 = 15

print("Maximum number:", max_of_three(num1, num2, num3))

# Method 2:
def max_of_three(a, b, c):
    return max(a, b, c)

# Test the function
print("Maximum number:", max_of_three(10, 25, 15))







