####################
# for loop Break and Continue
#   break => Exit loop when condition is met
#   continue => Skip specific iterations
####################

numbers = [1, 2, 3, 4, 5]

print("Using break on number 3: ")

for num in numbers:
    if num == 3:
        break
    print(num)


# Output
# 1
# 2

print("Using continue on number 3")

for num in numbers:
    if num == 3:
        continue
    print(num)


# Output
# 1
# 2
# 4
# 5







