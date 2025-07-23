##########################
# Set Methods
#   - add() => insert a single element
#   - update() => insert a multiple elements at once
#   - remove() => raises KeyError if value doesn’t exist.
#   - discard() => does nothing if value doesn’t exist.
# ? why we use discard
#   - pop() => remove a random element
#   - clear() => clear entire set
##########################

colors = {"red", "green", "blue"}

# add
colors.add("yellow")
print(colors)

# update
colors.update(["purple", "black", "brown"])
print(colors)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
# set3 = set1 + set2
# print(set3) Error

set1.update(set2)
print(set1)

# remove()
numbers = {1, 2, 3, 4, 5}

numbers.remove(3)
print(numbers)

# numbers.remove(10)
# print(numbers) # Error because 10 is not exist

# discard()
numbers.discard(10) # will not show error even if 10 is not exist
print(numbers)

# pop()
popped = colors.pop()
print(colors, popped)

# clear
colors.clear()
print(colors)