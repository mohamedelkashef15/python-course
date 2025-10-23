#######################
# Function Decorators
# Decorators are functions that modify the behavior of other functions without permanently modifying them. They're a powerful tool for adding functionality to existing code.
# - A decorator takes a function, adds some functionality, and returns it.
#######################

def my_decorator(func):
    def wrapper():
        print("Before Modification")
        func()
        print("After Modification")
    return wrapper

@my_decorator
def say_greetings():
    print("Welcome to the company")

say_greetings()

# Example

# def good_morning(name):
#     print("Function Started...")
#     print(f"Good Morning {name}")
#     print("Function Ended...")
#
# def good_evening(name):
#     print("Function Started...")
#     print(f"Good Evening {name}")
#     print("Function Ended...")
#
# def good_night(name):
#     print("Function Started...")
#     print(f"Good Night {name}")
#     print("Function Ended...")
#
# good_morning("Mohamed")
# print("----------")
# good_evening("Mohamed")
# print("----------")
# good_night("Mohamed")

def my_decorator(func):
    def wrapper(name):
        print("Function Started...")
        func(name)
        print("Function Ended...")
    return wrapper

@my_decorator
def good_morning(name):
    print(f"Good Morning {name}")

@my_decorator
def good_evening(name):
    print(f"Good Evening {name}")

@my_decorator
def good_night(name):
    print(f"Good Night {name}")

good_morning("Mohamed")
print("----------")
good_evening("Mohamed")
print("----------")
good_night("Mohamed")










