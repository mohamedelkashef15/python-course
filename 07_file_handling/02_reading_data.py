############################
# Reading data from files

# r => means read mode
# ? Methods of reading data
#   - read()
#   - readline()
#   - readlines()
############################

file = open("students.txt", "r")

# * Method 1: read()
# data = file.read()
# print(data)
# file.close()

# * Method 2: readline()
# line1 = file.readline()
# line2 = file.readline()
#
# print(line1)
# print(line2)

# * Method 3: readlines()
# lines = file.readlines()
# print(lines)

# * Using loops
for line in file:
    print(line)




