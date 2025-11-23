#############################
# Problem 27
# * Problem definition
# Write a Python program to detect whether a list contains duplicate elements or not
#############################
# * Problem instruction
# 1- Convert numbers into a set
# 2- Compare between original list and set
# 3- If original list length equals set length then print No duplicate found else duplicate detected

# * Problem solution
numbers = [1, 2, 3, 4, 2, 5, 1]
unique_numbers = set(numbers)

print(numbers)
print(unique_numbers)

if len(numbers) == len(unique_numbers):
    print("No duplicate found")
else:
    print("Duplicate detected")






