########################
# Built In function - filter
# filter(function, iterable)
# The filter() function is used to filter elements from an iterable based on a function that returns True or False.
# - Data Filtering - Extract elements that meet certain criteria
########################
# Example 1
# Without Using filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)  # [2, 4, 6, 8, 10]

# Using filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# 1 % 2 = 1
# 2 % 2 = 0
# 3 % 2 = 1
# 4 % 2 = 0
# 5 % 2 = 1
# 6 % 2 = 0


#? What is the difference between map and filter
# Transforms each element |	Filters elements based on condition
# Applies function to each element | Returns only elements where function returns True
# Any value	                       | Must return True/False (or truthy/falsy)


# Example 2
# Without Using filter
names = ["Mohamed", "", "Ahmed", "", "Islam", "", "Mostafa"]
non_empty = []


for name in names:
    if name != "":
        non_empty.append(name)

print(non_empty)

# Using filter
non_empty_filter = list(filter(lambda user: user != "", names))
print(non_empty_filter)
















