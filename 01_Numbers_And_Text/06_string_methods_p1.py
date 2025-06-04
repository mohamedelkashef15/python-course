######################
# String Methods
#     - Length
#     - Concatenation
#     - Repeatation
#     - Indexing
#     - Slicing
######################

# Length
message = "Hello, World"
print(len(message))

# Concatenation
first = "Hello"
second = "World"
combine = first + " " + second
print(combine)

# Repeatation
laugh = "ha"
print(laugh * 3)

# Indexing
# 0 1 2 3 4 5
text = "Python"
print(text)
print(text[0])
print(text[3])

welcome_message = "Welcome to the course"
print(welcome_message[11])

# Slicing [start: end (end not included): steps]
print(text[1:3]) # yt
print(text[:3]) # Pyt
print(text[3:]) # hon

# course
# Welcome
print(welcome_message[:7])
print(welcome_message[0:7])

# to
print(welcome_message[8:10])

# course
print(welcome_message[15:])
print(welcome_message[15: 21])

# Negative indexing
text2 = "programming"
print(text2[-1]) #g
print(text2[-5]) #m
print(text2[-5:-1]) #ytho
print(text2[-5:]) 
