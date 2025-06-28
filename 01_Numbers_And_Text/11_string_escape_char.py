###################
# escape characters
# \ => escape single/double qoutes
# \\ => escape backslash
# r => raw string
# \n => new line
# \t => tab space
# \b => backspace
# \r => carriage return
###################
# \
message = 'It\'s a sunny day'
welcome_message = "He said \"Hello\""

print(message)
print(welcome_message)

print("It's a sunny day")
print('He said "Hello"')

# \\
path = "C:\\users\\documents\\file.txt"

# r => raw string
path2 = r"C:\users\documents\file.txt"

print(path)
print(path2)

# \n
print("first line\nsecond line")
# print("""first line
# second line""")

# \t
print("Name:\tMohamed\nAge:\t25")

# \b => backspace
print("Hello \bWo\brld")

# \r => carriage return
print("It's Loading... \rDone")

print("""Hello
World
My name is Mohamed \rWelcome to python""")



