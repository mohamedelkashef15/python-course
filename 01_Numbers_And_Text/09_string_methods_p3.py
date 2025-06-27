######################
# String methods part 3
#   1- spliiting/joining
#     - split() / rsplit()
#     - join()
#   2- formatting
#     - zfill
#   3- special transformation
#     - center / ljust(width) / rjust(width)
######################

# split()
# names = ["Mohamed", "Ahmed", "Tarek"]

text = "Python is a good programming langauge"
text2 = "a,b,c"

print(text.split(" "))
print(text.split(","))
print(text2.split(","))
print(text.split(" ", maxsplit=3))

# rsplit()
path = "home/user/documents/file.txt"

print(path.rsplit("/", maxsplit=1))
print(path.split("/", maxsplit=1))

# join()
names = ["Mohamed", "Ahmed", "Tarek"]

print(" ".join(names))

# zfill
print("42".zfill(5))
print("-3.14".zfill(6))
# INV-00002
# INV-00120

# center
name = "soha"

print(name.center(10))
print(name.center(10, "*"))

# ljust(width)
print(name.ljust(10, "*"))

# rjust(width)
print(name.rjust(10, "*"))



