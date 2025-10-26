#######################
# return values and multiple return
#######################

# Single value return
def square(number):
    return number * number

print(square(4))

# Multiple return values (as tuple)
def calculate(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

print(calculate(10, 2))

# Unpacking multiple returns
addition, subtraction, multiplication = calculate(10, 2)

print(addition)
print(subtraction)
print(multiplication)














