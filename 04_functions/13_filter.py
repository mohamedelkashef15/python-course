########################
# Built In function - filter
# filter(function, iterable)
# The filter() function is used to filter elements from an iterable based on a function that returns True or False.
# - Data Filtering - Extract elements that meet certain criteria
########################

#? What is the difference between map and filter
# Transforms each element |	Filters elements based on condition
# Applies function to each element | Returns only elements where function returns True
# Any value	                       | Must return True/False (or truthy/falsy)

# Example 1
names = ["Mohamed", "", "Ahmed", "", "Islam", "", "Mostafa"]
non_empty = []


for name in names:
    if name:
        non_empty.append(name)

print(non_empty)

# Using filter
non_empty_filter = list(filter(lambda user: user != "", names))
print(non_empty_filter)

