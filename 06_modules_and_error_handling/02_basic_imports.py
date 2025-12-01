##########################
# Basic Imports
##########################

# built-in module
import math
import math as m
import random
import tools


# Method 1: Import module_name
print(math.sqrt(25))

# print("Hello".upper())

# Method 2: Import with alias (short name)
print(m.sqrt(16))

# Example 1: using random
random_number = random.randint(1, 100)
print(f"Random Number: {random_number}")

# Example 2: using math
radius = 5
area = m.pi * radius ** 2

print(f"Area of circle = {area}")

# How to know functions inside modules
print(dir(math))
print(dir(tools))













