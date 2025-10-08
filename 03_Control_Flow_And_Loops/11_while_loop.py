#######################
# While Loop

# initialization
# while condition:
#   code to execute
#   increment
#######################

# Count from 1 to 5 using for loop
for count in range(1, 6, 2):
    print(f"Count {count}")

print("Using while loop")

count = 1
while count <= 5:
    print(f"Count {count}")
    count += 2

# Output
# Count 1
# Count 2
# Count 3
# Count 4
# Count 5

# Example
password = ""

while password != "hello123":
    password = input("Enter the password: ")
    if password != "hello123":
        print("Incorrect Password. Try again.")

print("Access granted!")
