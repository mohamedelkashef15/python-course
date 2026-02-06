#########################
# Introduction to Object-Oriented Programming
# * What is OOP
# - A paradigm where you organize code into objects that hold both data and functions together.

# Python is a multi paradigm programming language
#   1- Procedural: "Do this step, then that step"
#   2- Functional: "Transform this data without changing it"
#   3- OOP: "Create objects that know how to do things themselves"

# ? Why we use OOP
# Large/complex programs, real-world modeling, web apps, GUIs

#########################
# 1- Procedural paradigm
numbers = [1, 2, 3, 4]

def double_list(data):
    result = []
    for n in data:
        result.append(n * 2)
    return result

print(f"Procedural paradigm: {double_list(numbers)}")


# 2- Functional paradigm
doubled = list(map(lambda x: x * 2, numbers))
print(f"Functional paradigm: {doubled}")

# 3- OOP paradigm
class NumberList:
    def __init__(self, nums):
        self.nums = nums

    def double(self):
        return [n * 2 for n in self.nums]

numbers_obj = NumberList(numbers)

print(f"OOP paradigm: {numbers_obj.double()}")






