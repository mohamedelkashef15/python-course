#######################
# Variable Scope Part 1
# Variable scope determines where in your code a variable can be accessed and used. Think of it like rooms in a house - variables declared in one room might not be visible in another room.
#######################

# Types of Variable Scope
# 1. Global Scope (Outside All Functions)
# Variables created outside all functions are global and can be accessed anywhere.
company_name = "Vodafone"  # Global variable

def welcome_employee(employee_name):
    print(f"Welcome {employee_name} to {company_name}!")  # ✅ Can read global

welcome_employee("Mohamed")
print(company_name)

# 2. Local Scope (Inside a Function)
# => Variables created inside a function are local to that function.

def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()
# print(local_var)

def calculate_area():
    length = 10 # local variable
    width = 5   # local variable
    area = length * width # local variable
    print(f"Area: {area}")

calculate_area()
#! print(length) Error

def function1():
    x = 10  # Local to function1
    print(f"Function1 x: {x}")

def function2():
    x = 20  # Local to function2 (different variable!)
    print(f"Function2 x: {x}")

function2()
function1()

#! print(x) Error

# Global keyword

counter = 0

def increment():
    # global counter  # ✅ Tell Python we want to use the global counter
    # print(counter)
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment()  # Output: Counter: 1
increment()  # Output: Counter: 2
increment()  # Output: Counter: 3

















