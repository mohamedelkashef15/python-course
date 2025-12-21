############################
# The with Statement
#   - Automatically close files
############################

# * Without using with statement
file = open("students.txt", "r")
data = file.read()
print(data)
file.close()

# * Using with statement
# read
with open("students.txt", "r") as file:
    data = file.read()
    print(data)

# write
with open("notes.txt", "w") as file:
    data = file.write("Python is powerful")

# append
with open("logs.txt", "a") as file:
    data = file.write("\nProgram Ended")



