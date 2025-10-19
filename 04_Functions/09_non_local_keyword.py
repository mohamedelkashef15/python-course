#######################
# Non Local Keyword
#######################

# Global
x = 10  # Global


def outer():
    def inner():
        # nonlocal x  # ❌ ERROR! x is global, not in outer function
        global x  # ✅ CORRECT
        x = 20

    inner()


outer()
print(x)  # 20


# non local
def outer():
    y = 30  # Outer function variable

    def inner():
        # global y  # ❌ ERROR! y is not global
        nonlocal y  # ✅ CORRECT
        y = 40

    inner()
    print(y)  # 40


outer()