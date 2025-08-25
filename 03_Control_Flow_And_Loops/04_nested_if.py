#############################
# Nested If
#############################

# Example 1
age = 17
has_id = True

if age >= 18:
    print("You can vote!")
    if has_id:
        print("Remember to bring your ID to the polling station.")
else:
    print("You are too young to vote.")

# Example 2
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful!")
    else:
        print("Wrong password!")
else:
    print("User not found!")












