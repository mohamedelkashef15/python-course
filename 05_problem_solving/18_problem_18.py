#############################
# Problem 18
# * Problem definition
# Write a python program that calculates the sum of all its elements using a for loop.
#############################

# * Problem instructions
# 1- Initialize a variable (for example total) to 0.
# 2- Loop through each number in the list.
# 3- Add each number to total.
# 4- Print the final result.

# * Problem solution
numbers = [5, 10, 15, 20, 25]
total = 0

for num in numbers:
    total += num

print(f"The sum of all elements is: {total}")

# Another method
# total = sum(numbers)