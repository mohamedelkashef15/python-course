#############################
# Problem 22
# * Problem definition
# Write a Python program that defines a list and checks whether a specific element exists in that list. If it exists, print a message confirming its presence; otherwise, indicate that it is not found.
#############################

# * Problem instructions
# 1- Loop on each element inside list then check if element exists inside list then print "element exists" then stop the loop otherwise "element is not exist"

# * Problem solution
numbers = [10, 20, 30, 40, 50]
element = 30
# found = False
#
# for num in numbers:
#     if num == element:
#         found = True
#         break

if element in numbers:
    print(f"{element} is exist in list")
else:
    print(f"{element} is not exist in list")













