##############################
# Nested for loop
##############################

# Multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Output
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

print("#"*20)

# Multiplication table from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("------")


# i = 10, j = 1

# Output
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# ...
# 1 x 10 = 10
# -------
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ....
# 2 x 10 = 20
# -------
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# ....
# 3 x 10 = 30
# ------
# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# ....
# 10 x 10 = 100
# -----


