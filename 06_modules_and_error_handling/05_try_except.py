############################
# Try and except
############################
# Basic structure
# try:
#     # Try to do this risky thing
#     risky_operation()
# except:
#     # If it fails, do this instead
#     handle_the_problem()

# print(20/0)
# print("Hello Mohamed")

# * Without Using error handling
# age = int(input("How old are you? "))
# print(age)

# * Using error handling
try:
    age = int(input("How old are you? "))
    print(age)
except ValueError:
    print("Please type a number like 25")

print("Hello Mohamed")




