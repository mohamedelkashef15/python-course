######################
# Add and Remove List Items
#   Adding
#     - append()
#     - insert()
#     - extend()
#     - concatenation (+)
#     - * repetation
#   Removing
#     -
######################

names = ["Mohamed", "Ahmed"]

# append()
# ? tell students about warnning
names.append("Tarek")
print(names)

# insert(index, value)
names.insert(1, "Islam")
print(names) # ["Mohamed", "Islam", "Ahmed" "Tarek"]

# extend()
more_names = ["Malak", "Farida"]
names.extend(more_names)
print(names)

# concatenation (+)
all_names = names + ["Sarah", "Farah"]
print(all_names)

# repeatation (*)
numbers = [1, 2, 3] * 3
print(numbers)

#####################################
# Removing from list item
# remove() -> first occurance of a value
fruits = ["apple", "banana", "mango", "banana", "Orange"]
fruits.remove("banana")
print(fruits) # ["apple", "Mango", "banana"]

# pop() -> remove last item
fruits.pop()
print(fruits)