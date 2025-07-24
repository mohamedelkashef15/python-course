##########################
# Set Methods part 1
#   - add() => insert a single element
#   - update() => insert a multiple elements at once
#   - copy() => return a copy from set
#   - remove() => raises KeyError if value doesn’t exist.
#   - discard() => does nothing if value doesn’t exist.
#   - pop() => remove a random element
#   - clear() => clear entire set
##########################

colors = {"red", "green", "blue"}

# add()
colors.add("yellow")
print(colors)

# update()
colors.update(["purple", "black", "brown"])
print(colors)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
# set3 = set1 + set2
# print(set3) Error

set1.update(set2)
print(set1)

# copy()
set3 = set1.copy()

print(set3)

# remove()
numbers = {1, 2, 3, 4, 5}
print(numbers)
numbers.remove(3)

print(numbers)

# numbers.remove(10)
# print(numbers)

# discard
numbers.discard(2)
print(numbers)

numbers.discard(10)
print(numbers)

# pop()
print(colors)
popped = colors.pop()

print(colors, popped)

# clear()
colors.clear()
print(colors)



