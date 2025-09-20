#########################
# Parameters & Arguments
#########################

# Types of parameters
# Positional parameter
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

greet("Mohamed", "25")
# greet("25", "Mohamed") Wrong
# greet("Mohamed") Error missing 1 required positional argument: 'age'

# Default parameter (Optional)
def greet(age, name = "Deer"):
    print(f"Hello {name}, your age is {age} years old")

greet("20", "Ahmed")
greet("30")

# keywords arguments
def create_user(name, age, email = "test@gmail.com"):
    print(f"Name: {name}, Age: {age}, Email: {email}")

create_user("Tarek", "30", "tarek@gmail.com")
create_user(age = "40", name = "Islam")
create_user("Malak", email="malak@gmail.com", age="30")


