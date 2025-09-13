####################
# User Input
#   - allows Python programs to interact with users by accepting data from them.
#   - input() function is used to get user input. It always returns the input as a string.
####################

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# height = input("Enter your height: ")
#
# print(f"{name} is {age} years old and {height}m tall.")
#
# print(f"{name} born in {2027 - age}")

# Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid Operation"

print(f"Result = {result}")



























