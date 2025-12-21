############################
# File Errors
# FileNotFoundError
############################
try:
    with open("note.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File Not found!")
else:
    print(data)
finally:
    print("Program finished")

















