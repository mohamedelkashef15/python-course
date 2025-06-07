###################
# escape characters
# \'
# \\ => backslash
# r => raw string
# \n
# ? What is the difference between """""" and \n
# \t
# \b => backspace
# ? use case why we use it
# \r => carriage return
# \u => unicode
# \x => hex value
###################
# \'
message = 'It\'s a sunny day'
welcome_message = "He said, \"Hello\""

# quotes inside strings
print(message)
print(welcome_message)
print("It's a sunny day")
print('He said, "Hello"')

# File paths
# C:\Users\Documents\file.txt
path = "C:\\users\\documents\\file.txt"
path2 = r"C:\users\documents\file.txt"
print(path)
print(path2)

# newlines and tabs
print("""first line
second line""")
print("first line\nsecond line")

# Name:   Mohamed
# Age:    25
print("Name:\tMohamed\nAge:\t25")

# backspace & carriage return
print("Hello \bWorld")
print("It's Loading Now ...\rDone")

# Unicode \u => 16 bit \U 8 digit
print("This is a copyright \u00A9 2023")
print("This is a smile \U0001F600")

# => search for unicode table

# hex table
# cat
print("\x43\x41\x54")