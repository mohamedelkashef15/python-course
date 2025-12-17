############################
# Error types
# - SyntaxError
# - NameError
# - TypeError
# - ValueError
# - IndexError
# - KeyError
# - ZeroDivisionError
############################
# * Syntax error
# try:
#     if True:  # Missing colon - SyntaxError
#         print("Hello"
# except SyntaxError:  # This never runs!
#     print("Caught syntax error")  # ❌ Can't catch SyntaxError like this

# * Name error
# BEFORE (CRASHES):
# message = "Hello"
# print(mesage)  # NameError: name 'mesage' is not defined

# try:
#     message = "Hello"
#     print(mesage)  # Typo!
# except NameError:
#     print("Oops! Variable name is misspelled")
#     print(f"Did you mean 'message'? The value is: {message}")
#



# * Type Error
# BEFORE (CRASHES):
# result = "Hello" + 42  # TypeError: can only concatenate str to str

# AFTER (HANDLED):
# try:
#     name = "Hello"
#     age = 42
#     result = name + age  # Wrong types
# except TypeError:
#     print(f"Cannot add string '{name}' and number {age}")

# * ValueError

# * IndexError
# BEFORE (CRASHES):
# fruits = ["apple", "banana", "cherry"]
# print(fruits[5])  # IndexError: list index out of range

# AFTER (HANDLED):
# try:
#     fruits = ["apple", "banana", "cherry"]
#     index = int(input("Enter fruit position (0-2): "))
#     print(f"Fruit at position {index}: {fruits[index]}")
# except IndexError:
#     print(f"Position {index} doesn't exist!")
#     print(f"Available positions: 0 to {len(fruits)-1}")
#     print(f"Fruits available: {', '.join(fruits)}")

# * KeyError
# person = {"name": "Ahmed", "age": 30}
# print(person["height"])  # KeyError: 'height'

# AFTER (HANDLED):
# try:
#     person = {"name": "Mohamed", "age": 30}
#     key = input("What do you want to know? (name/age): ")
#     print(f"{key}: {person[key]}")
# except KeyError:
#     print(f"'{key}' is not in the person's information")
#     print(f"Available keys: {', '.join(person.keys())}")


# * ZeroDivisionError
# divide = 5 / 0

# try:
#     divide = 5 / 0
#     print(divide)
# except ZeroDivisionError:
#     print("Number can not be divided by zero")





