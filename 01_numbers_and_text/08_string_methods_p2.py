######################
# String methods part 2
# 1- Searching methods
#    - find(sub, start, end) / rfind()
#    - index()
#
# 2- Validation methods
#    - isalnum()
#    - isalpha()
#    - isdigit()
#    - startswith()
#    - endswith()

# 3- Cleaning methods
#    - strip() / lstrip() / rstrip()
#    - replace(old, new)
######################

# find()
text = "Hello world, welcome to Python world"

print(text.find("world")) # 6
print(text.find("world", 7)) # 31
print(text.find("java"))

# rfind()
text2 = "Hello world, Hello python"
print(text2.rfind("Hello"))

# index()
text3 = "Python Programming"

print(text3.index("Pro"))
# print(text3.index("Java"))

# isalnum() | a-z | A-Z | 0-9

print("Python3".isalnum()) # True
print("Python3 ".isalnum()) # False

# isdigit()
print("123".isdigit()) # True
print("12a".isdigit()) # False

# startswith(prefix, start, end)
filename = "document.pdf"
print(filename.startswith("doc")) # True
print(filename.startswith("pdf", 9)) # True

# endswith(suffix, start, end)
print(filename.endswith(".pdf"))

# strip()
text4 = "    Python is Good    "
print(text4.strip())
print(text4.lstrip())
print(text4.rstrip())

# replace(old, new, count)
text5 = "I like apples, apples are tasty"
print(text5.replace("apples", "oranges"))
print(text5.replace("apples", "oranges", 1))



















