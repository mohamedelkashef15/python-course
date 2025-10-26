########################
# Built In function - map
# map(function, iterable)
########################

# Example 1
# without using map
numbers = [1, 2, 3, 4, 5]
square_list = []

for num in numbers:
    square_list.append(num ** 2)

print(square_list)

# Using map and lambda
# square_map = list(map(lambda x: x ** 2, numbers))
# print(square_map)

# Using map and Regular function
def square_fun(x):
    return x ** 2

square_map = list(map(square_fun, numbers))
print(square_map)

# Example 2
names = ["Mohamed", "Ahmed", "Mostafa", "Islam"]
names_upper = []

for name in names:
    names_upper.append(name.upper())

print(names_upper)

names_upper_map = list(map(lambda user: user.upper(), names))
print(names_upper_map)









