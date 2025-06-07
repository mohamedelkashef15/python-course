##################
# Operator precedence
##################
# Example 1
x = (2 + 3) * 4 #20
print(x)

# 3 * 4 = 12
# 12 + 2
print(2 + 3 * 4)

# Example 2
y = 2 + 3 ** 2
print(y) # 11

# Example 3
z = 10 / 2 + 3
# 10/2 = 5
# 5 + 3 = 8
# z = 8
print(z)

# Example 4
result = 5 + 3 * 2 - 4 / 2 + (2 * 3)
# 2 * 3 = 6
# 3 * 2 = 6
# 4 / 2 = 2
# 5 + 6 - 2 + 6 = 15
print(result)