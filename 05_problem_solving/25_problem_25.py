#############################
# Problem 25
# * Problem definition
# Write a Python program that defines a list of numbers and sorts them in ascending order without using the built-in sort() method.
#############################

# * Problem instructions
# 1- Define a list with numbers.
# 2- Use nested loops to compare each element with the others.
# 3- Swap elements if they are in the wrong order.
# 4- Continue until the list is sorted.
# 5- Print the sorted list.

# * Problem solution

numbers = [5, 2, 9, 1, 5, 6]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(f"Sorted list: {numbers}")

# a, b = 1, 2
# print(a,b)
# b, a = a, b
# print(a, b)

# Output
# i in range(6) => (0, 5)
# j in range(0, 5) => (0, 4) | 6 - 0 - 1 = 5

# 1st round : i = 0 | j => 0, 4
# j=0: Compare 5 and 2 → 5 > 2? YES → Swap → [2, 5, 9, 1, 5, 6]
# j=1: Compare 5 and 9 → 5 > 9? NO → No swap → [2, 5, 9, 1, 5, 6]
# j=2: Compare 9 and 1 → 9 > 1? YES → Swap → [2, 5, 1, 9, 5, 6]
# j=3: Compare 9 and 5 → 9 > 5? YES → Swap → [2, 5, 1, 5, 9, 6]
# j=4: Compare 9 and 6 → 9 > 6? YES → Swap → [2, 5, 1, 5, 6, 9]

# 2nd round: i = 1 | j => 0, 3
# Start: [2, 5, 1, 5, 6, 9]
# j=0: Compare 2 and 5 → NO swap
# j=1: Compare 5 and 1 → YES swap → [2, 1, 5, 5, 6, 9]
# j=2: Compare 5 and 5 → NO swap
# j=3: Compare 5 and 6 → NO swap

# 3rd round i = 2 | j => 0,2
# After Pass 3: [1, 2, 5, 5, 6, 9] - The list is now sorted!








