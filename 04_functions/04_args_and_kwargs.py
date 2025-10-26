#######################
# *args and **kwargs
# args (Arbitrary Positional Arguments)
#   => Collects Any number of positional arguments into a tuple.

# kwargs (Arbitrary Keyword Arguments)
#   => Collects Any number of keyword arguments into a dictionary.
#######################

#* args
def add_numbers(*args):
    # print(args)
    total = 0
    for number in args:
        total += number
    return total

print(f"Total of cart 1: {add_numbers(5, 3, 2)}")
print(f"Total of cart 2: {add_numbers(10, 7, 6, 3)}")
print(f"Total of cart 3: {add_numbers(10, 7)}")

# Output
# number = 5
# total = 0 + 5
# total = total + number = 8
# total = 8 + 2

#* kwargs

my_list = [1, 2, 3, 4]
print(my_list)
# unpacking
num1, num2, num3, num4 = my_list

print(num1)
print(num4)

user = {
    "name": "Mohamed",
    "phone": "0123456"
}

print(user.items())

# for key, value in user.items():
#     print(key)
#     print(value)

#* kwargs
def create_user(**user_info):
    print("-----User profile-----")
    for key, value in user_info.items():
        print(f"{key}: {value}")

create_user(name="Mohamed", age="25", city="Cairo")
create_user(name="Ahmed", city="Alex")
create_user(name="Islam", age="40", phone="1231231", city="Alex")

















