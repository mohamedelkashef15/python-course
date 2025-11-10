#############################
# !Problem 31
# * Problem definition
# Write a Python program that demonstrates how to add new elements to a set and remove existing elements from it using built-in methods.
#############################
# * Problem instruction
# 1- Define a set with some initial elements.
# 2- Use the add() method to insert a single new element.
# 3- Use the update() method to add multiple elements at once.
# 4- Use the remove() or discard() methods to delete elements.
# 5- Print the set after each operation.

# * Problem solution

numbers = {1, 2, 3}
print("Original set:", numbers)

numbers.add(4)
print("After adding 4:", numbers)

numbers.update([5, 6])
print("After adding multiple elements:", numbers)

numbers.remove(2)
print("After removing 2:", numbers)

numbers.discard(10)
print("After discarding 10 (non-existing):", numbers)



