#############################
# Problem 17
# * Problem definition
# Write a Python program that takes a string from the user and checks whether it starts and ends with specific letters entered by the user.

#############################
# * Problem Instructions
# 1- Ask the user to enter a string.
# 2- Ask the user to enter a starting letter to check.
# 3- Ask the user to enter an ending letter to check.
# 4- Use the string methods startswith() and endswith() to perform the checks.
# 5- Display appropriate messages depending on the result.

# * Problem Solution

text = input("Enter a string: ")
start = input("Enter the starting letter to check: ")
end = input("Enter the ending letter to check: ")

starts_with = text.startswith(start)
ends_with = text.endswith(end)

if starts_with and ends_with:
    print(f"The string starts with '{start}' and ends with '{end}'.")
elif starts_with:
    print(f"The string starts with '{start}' but does not end with '{end}'.")
elif ends_with:
    print(f"The string ends with '{end}' but does not start with '{start}'.")
else:
    print(f"The string neither starts with '{start}' nor ends with '{end}'.")










