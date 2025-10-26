#######################
# Tuple and methods
#   - Indexing & Slicing
#   - Adding/Removing Items to tuple
#   - del tuple
#   - len()
#   - count()
#   - index()
#   - unpacking tuple
#######################

numbers = (10, 20, 30, 40, 50, 60, 60)

# Indexing & Slicing
print(numbers[0])
print(numbers[2])

print(numbers[-1])
print(numbers[-3])

print(numbers[1:4])
print(numbers[::2])

# Adding/Removing Items to tuple
# Method 1: convert tuple into list
names_t = ("Mohamed", "Ahmed", "Mahmoud")
names_l = list(names_t)

print(names_t)
print(names_l)

names_l.append("Malak")
print(names_l)

names_l.remove("Ahmed")
print(names_l)

names_t = tuple(names_l)
print(names_t)

# Method 2: add two tuples togther
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5)

tuple_1 += tuple_2
# tuple_1 = tuple_1 + tuple_2
print(tuple_1)

# del tuple
del tuple_1

# print(tuple_1)

# len()
print(len(numbers))

# count()
print(numbers.count(60))

# index()
print(numbers.index(20))
# print(numbers[1])

# unpacking tuple
rank = (120, 2, 3, 30, 40, 50, 60, 70, 80, 90, 100)
(first, second, third, forth, *rest) = rank

print(f"first {first}")
print(f"second {second}")
print(f"third {third}")
print(f"forth {forth}")
print(rest)

