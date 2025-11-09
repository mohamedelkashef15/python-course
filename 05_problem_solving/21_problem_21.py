#############################
# Problem 21
# * Problem definition
# Write a Python program that defines a list of numbers and counts how many times a specific element appears in the list USING FOR LOOP
#############################

# * Problem instructions
# 1- Define a list containing several numbers.
# 2- Choose an element to count (for example, 3).
# 3- Use for loop to compare between num and element if they are equals then increase count by 1 if not then do nothing
# 4- display result

# * Problem solution
numbers = [1, 3, 5, 3, 7, 3, 9]
element = 3
count = 0

# Loop through the list and count matches
for num in numbers:
    if num == element:
        count += 1

# Display result
print(f"The number {element} appears {count} times in the list.")