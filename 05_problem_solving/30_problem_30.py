#############################
# Problem 30
# * Problem definition
# Write a Python program that defines a function "max_of_three" to find the maximum of three numbers.
# The function should take three numbers as input and return the largest one.
#############################
# * Problem instruction
# 1- define function called max_of_three that receive 3 numbers
# 2- Compare between 3 numbers to get the largest
# 3- return largest number
# 4- print largest number

# * Problem solution

def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(f"Maximum number is: {max_of_three(10, 25, 15)}")








