#############################
# Problem 34
# * Problem definition
# Write a Python program that remove all spaces in each string, remove all names shorter than 4 and make first letter upper case
#############################

# * Problem instruction
# 1- Use map to remove all spaces in each string and convert characters to lower case
# 2- Use filter to remove name that has less than 4 letters
# 3- Use map to set first letter to be capital

# * Problem solution
names = ["   ali", "MOHAMED ", "saRaH   ", "  ahMED"]

cleaned = list(map(lambda name: name.strip().lower(), names))

filtered = list(filter(lambda name: len(name) > 3, cleaned))

final = list(map(lambda name: name.capitalize(), filtered))

print(cleaned)
print(filtered)
print(final)

# Expected Output ["Mohamed", "Sarah", "Ahmed"]
