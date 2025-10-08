######################
# 1- What is variable ?
# 2- Changing variable values
# 3- Multi Words Variable Names
#     - Camel Case
#     - Pascal Case
#     - Snake Case
# 4- Naming Rules
#     - A variable name must start with a letter or the underscore character
#     - A variable name cannot start with a number
#     - A variable name can only contain alphanumeric characters and underscores (A-z, 0-9, and _ )
#     - A variable name cannot be any of the Python keywords.
# 5- Assign Multiple Values
######################
# 1 - What is variable ?
name = "Mohamed"
age = 25

print(name)
print(age)

# 2- Changing variable values
score = 10
print(score)  # 10

score = 20
print(score)  # 20

# 3- Multi Words Variables Names
myName = "Mohamed"
MyName = "Mohamed"
my_name = "Mohamed"

# 4- Naming rules
age = 18
my_age = 19
_age = 20
myAge = 21
MYAGE = 12
myAge2 = 22

# Invalid names:
# 2nd_place = "Islam" # Cannot start with a digit
# my-variable = 10    # Hyphens are not allowed
# def = "keyword"     # Cannot use reserved keywords
# age@2 = "Mohamed"

# help("keywords")

# 5- Assign multiple values at once
name, age, job = "Mohamed", 25, "Teaching Assistant at Misr University"

print(name, age, job)


