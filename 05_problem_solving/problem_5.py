#############################
# Problem 5
# * Problem definition
# Write a Python program that ask user to enter 2 numbers in Two Variables then Swap variables
# ? hint: if a = 5, b = 10 expected output is b = 5, a = 10
#############################
# * Problem Instructions
# 1- Ask user to enter 2 value inside 2 variables (a, b)
# 2- swap their values
# 3- display result before swapping, after swapping

# * Problem Solution
a = input("Enter first value (a): ")
b = input("Enter second value (b): ")

print("\nBefore swapping")
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a

print("\nAfter swapping")
print(f"a = {a}")
print(f"b = {b}")










