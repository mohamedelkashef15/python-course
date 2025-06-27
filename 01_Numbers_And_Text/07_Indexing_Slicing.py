#######################
# Indexing
# Slicing [start: end (end not included): steps]
#######################

# Positive Indexing (Left => Right)
# Indices: 0 1 2 3 4 5
#          P y t h o n

text = "Python"
print(len(text))
print(text[1])
print(text[4])

welcome = "Hello Python developers"

print(welcome[7])

# Negative indexing (Right => Left)
# indices: -6 -5 -4 -3 -2 -1
#           P  y  t  h  o  n

print(text[-1])
print(text[-5])
print(welcome[-12])

# Slicing [start: end (end not included): steps]
s = "Programming"
message = "PythonProgramming"

print(s[3:7]) # gram
print(s[:7]) # Program
print(s[6:])
print(s[:])

# slicing with steps
print(message[2:10:2]) # toPo
print(message[::3]) # PhPgmn

# Negative Index slicing (Right => Left)

skill = "DataScience"

print(skill[-5:])
print(skill[:-3])
print(skill[-8:-3])
print(skill[::-2]) # eniStD










