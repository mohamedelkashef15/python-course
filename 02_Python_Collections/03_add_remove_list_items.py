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
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
languages.remove("Java")
print(languages) # ['Python', 'C++', 'JavaScript', 'Ruby']

# pop() -> remove last item
languages.pop()
print(languages)

# del - remove item or entire list
del languages[0]
print(languages)

languages.clear()
print(languages)