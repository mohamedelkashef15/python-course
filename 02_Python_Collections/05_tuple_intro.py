########################
# Tuple Introduction

# Characteristics of tuples
# 1- Ordered: Elements maintain their position/index in the tuple
# 2- Immutable: Cannot be changed after creation
# 3- Heterogeneous: Can contain elements of different types
# 4- Indexable: Elements can be accessed by their index
# 5- unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
########################


# Difference between mutable vs immutable
# mutable:
#   - Can be changed after creation
#   - Allow modification of contents
#   - Examples: lists, dictionaries, sets

my_list = [1, 2, 3]
print(my_list)

my_list[0] = 99
print(my_list)
my_list.append(4)
print(my_list)


# Immutable
# Cannot be changed after creation
# Any "modification" creates a new object
# Examples: tuples, strings, integers, floats

my_tuple = (1, 2, 3, "hello", 3.14, True)

print(my_tuple, type(my_tuple))
# my_tuple[0] = 99

print(my_tuple)
print(my_tuple[3])

my_string = "python"
# my_string[0] = "y"

print(my_string)

colors = "red", "green", "blue"
print(colors, type(colors))
