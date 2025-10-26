#############################
# Problem 5
# * Problem definition
# Write a Python program that Swap Two Variables
#############################
# * Swap variables
# Instructions
# 1- Ask the user to enter two variables (e.g., a and b).
# 2- Swap their values without using a third variable.
# 3- Display the values before and after swapping.

# * Problem Solution
a = input("Enter first value (a): ")
b = input("Enter second value (b): ")

# Step 2: Display before swapping
print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Step 3: Swap without using a third variable
a, b = b, a

# Step 4: Display after swapping
print("\nAfter swapping:")
print("a =", a)
print("b =", b)