##################
# Operator precedence
##################

# Example 1
print(2 + 3 * 4)
# 3 * 4 = 12
# 12 + 2

# Example 2
x = (2 + 3) * 4 #20
print(x)

# Example 3
y = 2 + 3 ** 2
print(y)
# 3 * 3 = 9
# 9 + 2 = 11

# Example 4
z = 10 / 2 + 3
print(z)
# 10/2 = 5
# 5 + 3 = 8

# Example 5
result = 5 + 3 * 2 - 4 / 2 + (2 * 3)
# 2 * 3 = 6
# 3 * 2 = 6
# 4 / 2 = 2
# 5 + 6 - 2 + 6 = 15
print(result)