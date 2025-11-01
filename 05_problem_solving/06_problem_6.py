#############################
# Problem 6
# * Problem definition
# Write a Python program that that takes an integer as input and display "Even" for even numbers or "Odd" for odd numbers.
#############################
# * Problem Instructions
# 1- Ask from user to enter integer number
# 2- Check weather the number even or odd
# 3- display result

# * Problem Solution
num = int(input("Enter an integer number: "))

if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")


# 10 % 2 == 0
# 2 * 5 = 10
# Reminder = 0

# 9 % 2
# 2 * 4 = 8
# Reminder = 1




