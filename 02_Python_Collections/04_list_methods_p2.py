######################
# List Methods Part 2
#   - index(element, start, end)
#   - count()
#   - sort()
#   - reverse()
#   - copy()
#   - deepcopy
######################
import copy

fruits = ["apple", "banana", "strawberry", "banana", "orange", "kiwi"]

# index(element, start, end)
print(fruits.index("banana"))
print(fruits.index("banana", 2))
print(fruits.index("banana", 0, 3))

# count()
numbers = [1, 2, 3, 4, 1, 1, 1, 2]

print(numbers.count(1))
print(numbers.count(2))

# sort()
numbers.sort()
print(numbers)

fruits.sort(key=len)
print(fruits)

# reverse()
numbers.reverse()
print(numbers)

# copy()
original = [1, 2, [3, 4]]
copied = original.copy()

print(original)
print(copied)

copied[0] = 99

print(original)
print(copied)

copied[2][0] = 100

print(original)
print(copied)

# deepcopy
original2 = [5, 6, [7, 8]]
copied2 = copy.deepcopy(original2)

print(original2)
print(copied2)

copied2[0] = 99
copied2[2][0] = 100

print(original2)
print(copied2)