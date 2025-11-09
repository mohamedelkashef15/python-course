#############################
# Problem 28
# * Problem definition
# Write a Python program that defines multiple tuples and unpacks their elements into separate variables in a single line.
#############################

# * Problem instructions
# 1- Define two or more tuples, each containing a fixed number of elements.
# 2- Unpack each tuple into separate variables using tuple unpacking.
# 3- Print the unpacked variables to verify.

# * Problem solution
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

a, b, c = tuple1
x, y, z = tuple2

print("Tuple1 elements:", a, b, c)
print("Tuple2 elements:", x, y, z)
