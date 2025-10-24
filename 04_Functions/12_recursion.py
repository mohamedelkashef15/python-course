#######################
# Function recursion
# The Two Essential Parts of Recursion:
# 1) Base Case: The stopping condition that prevents infinite loops
# 2) Recursive Case: The part where the function calls itself
#######################

def countdown(n):
    # Base case - when to stop
    if n <= 0:
        print("Count down finished !!!")
        return
    # Recursive case - call itself
    print(n)
    countdown(n - 1)

countdown(5)











