#############################
# Problem 35
# * Problem definition
# Write a Python program that remove invalid emails form list and display username of each email
#############################

# * Problem instruction
# 1- Use filter to check if string is a valid email or not
# 2- Use map to display username


# * Problem solution
emails = [
    "mohamed@gmail.com", "invalidemail",
    "sara@hotmail", "ahmed@yahoo.com",
    "@wrong.com", "fatma@outlook.com"
]

# ['mohamed', 'ahmed', 'fatma']

# Step 1: Filter only valid emails
valid = list(filter(lambda e: "@" in e and e.endswith(".com") and e.index("@") > 0, emails))


print(valid)
# Step 2: Extract username before "@"
usernames = list(map(lambda e: e.split("@")[0], valid))

print(usernames)




