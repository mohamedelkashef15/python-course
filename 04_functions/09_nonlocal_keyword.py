########################
# Nonlocal Keyword
# Used to modify variables from outer functions
########################

# non-local keyword
def outer():
    y = 20
    def inner():
        nonlocal y
        y = 30
    inner()
    print(y)

outer()

# Global keyword

y = 10
print(f"Y from Global before modification {y}")
def outside():
    y = 20
    def inside():
        global y
        y = 30
    inside()
    print(f"Y from outside function {y}")

outside()
print(f"Y from Global after modification {y}")



