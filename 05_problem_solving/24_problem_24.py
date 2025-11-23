#############################
# Problem 24
# * Problem definition
# Write a Python program that defines a tuple and identifies all elements that appear more than once.
#############################

# * Problem instructions
# 1- Create empty list to add repeated numbers
# 2- loop through tuple then check if number is repeated and is not already added in repeated list, add it
# 3- display result => repeated list

# * Problem solution
numbers = (1, 2, 3, 2, 4, 5, 3, 6)
repeated_list = []

for num in numbers:
    if numbers.count(num) > 1 and num not in repeated_list:
        repeated_list.append(num)


print(repeated_list)

# repeated List = [2, 3]





