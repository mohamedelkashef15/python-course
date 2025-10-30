########################
# try and except
# The try and except blocks are used for exception handling - they help your program handle errors instead of crashing.
# try:
#     # Code that might cause an error
# except ExceptionType:
#     # Code to handle the error
########################

# Example 1:
# number = int(input("Enter a number: "))  # User enters "hello"
# print(number)

# try:
#     number = int(input("Enter a number: "))  # User enters "hello"
#     print(number)
# except ValueError:
#     print("Invalid input")

# Example 2:
# try:
#     numerator = float(input("Enter numerator: "))
#     denominator = float(input("Enter denominator: "))
#     result = numerator / denominator
#     print(f"Result: {result}")
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")

# Example 3:
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # This will cause IndexError
    number = int("abc")  # This would cause ValueError
except IndexError:
    print("Error: List index out of range!")

# Example 4
try:
    # We expect these might fail
    result = 10 / int(input("Enter divisor: "))
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    # Catches ANY other unexpected error
    print(f"Unexpected error: {e}")
    # Log the error for debugging


