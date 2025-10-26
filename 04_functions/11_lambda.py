########################
# Lambda Function

# * Key Characteristics
# 1) Anonymous: They don't require a name
# 2) Single expression: Can only contain one expression
# 3) Inline: Typically used where you need a simple function for a short period
# 4) Return value: Automatically returns the result of the expression
########################

# Regular function
def square(num):
    return num * num

print(square(5))

# Using lambda function
square_lambda = lambda num: num * num

print(square_lambda(5))

add = lambda a, b: a + b
print(add(5, 3))

multiply = lambda a, b, c: a * b * c
print(multiply(5, 3, 2))








