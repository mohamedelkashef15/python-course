########################
# Global Keyword
########################


# Global keyword

counter = 0

def increment():
    # global counter  # ✅ Tell Python we want to use the global counter
    # print(counter)
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment()  # Output: Counter: 1
increment()  # Output: Counter: 2
increment()  # Output: Counter: 3
