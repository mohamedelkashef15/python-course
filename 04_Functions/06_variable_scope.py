########################
# Variable Scope
########################

# Types of Variable Scope
# 1. Global Scope (Outside All Functions)
company_name = "Vodafone"

def welcome_company(employee_name):
    print(f"Welcome {employee_name} to {company_name}")

welcome_company("Mohamed")
print(company_name)

# 2. Local Scope (Inside a Function)

name = "Ahmed from Global"

def my_function():
    local_var = "I'm local"
    name = "Mohamed from local"
    print(local_var)
    print(name)


my_function()
# print(local_var)
print(name)

x = 10

def function1():
    name = "Ahmed"
    x = 20
    print(f"Function 1 x = {x}, name = {name}")

def function2():
    x = 30
    print(f"Function 2 x = {x}, name = {name}")


function2()
function1()
print(x)










