######################
# List Methods Part 1
# Add and Remove List Items
#   Adding
#     - append()
#     - insert()
#     - extend()
#     - concatenation (+)
#     - * repetation
#   Removing
#     - remove() => first occurance of a value
#     - pop() => remove last item
#     - del => remove item or entire list
#     - clear() => removes all elements inside list
######################

names = ["Mohamed", "Ahmed"]

print(names)
# append()
names.append("Tarek")

# names.append(["Malak", "Farida"])
# names.append("abc")
print(names)

# insert(index, value)
names.insert(1, "Islam")
print(names)

# extend()
more_names = ["Malak", "Farida"]

names.extend(more_names)
# names.extend("abc")
print(names)

# concatenation (+)
all_names = names + ["Farah", "Sarah"]

print(all_names)

# * repetation
numbers = [1, 2, 3] * 3
print(numbers)

######################################
languages = ["Python", "Java", "C++", "Ruby", "JavaScript", "Java"]

print(languages)

# remove() => first occurance of a value
languages.remove("Java")
print(languages)

# pop() => remove last item
languages.pop()
print(languages)

# del => remove item or entire list
del languages[1]

# del languages

print(languages)

# clear() => removes all elements inside list
languages.clear()
print(languages)





