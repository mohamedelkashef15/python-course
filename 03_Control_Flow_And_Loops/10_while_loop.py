####################
# While Loop
#
# initialization
# while condition:
#   code to execute
#   increment


# ? Compare between While and for loop
# While                              | For
# When iterations are unknown        | When iterations are known
# Based on Boolean condition         | Based on sequence/range
# Manual initialization              | Automatic initialization
# Manual increment                   | Automatic increment
# When condition becomes false       | When sequence ends
####################

# count from 1 to 5
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# count = 1
# Output
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5


print("Using for Loop")
# Using for loop
for count in range(1, 5):
    print(f"Count: {count}")


# Example: Remove vowels from a string until only consonant remain
text = "aeioubcdfghjklmnpqrstvwxyz"
vowels = "aeiou"
result = ""

while text[0] in vowels:
    text = text[1:]  # Remove first character
    print(text)

print(f"Final text starts with consonant: {text}")

print(result)

# text = "aeioubcdfghjklmnpqrstvwxyz"

# text[0] = a
# text = "eioubcdfghjklmnpqrstvwxyz"

# text[0] = e
# text = "ioubcdfghjklmnpqrstvwxyz"

# text[0] = i
# text = "oubcdfghjklmnpqrstvwxyz"