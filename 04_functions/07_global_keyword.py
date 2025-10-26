########################
# Global Keyword
########################

counter = 0

def increment():
    global counter
    counter += 1

    print(f"inside counter {counter}")

increment()
increment()

print(f"outside counter {counter}")

# counter 0 Global
# counter 1
# counter 2


