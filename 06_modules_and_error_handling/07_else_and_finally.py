############################
# Else and Finally
# Else => The else block runs only if no exception occurs in the try block.
# Finally, => The finally block always runs, whether: An exception happens, No exception happens
############################

# Example 1:
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number")
else:
    if age < 0:
        print("Age cannot be negative")
    else:
        birth_year = 2030 - age
        print(f"You were born {birth_year}")
finally:
    print("Program finished")

# Example 2:
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print(f"10 / {num} = {result}")
finally:
    print("Program finished")












