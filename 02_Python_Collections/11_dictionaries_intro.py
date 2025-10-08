#########################
# Dictionaries Introduction
# Key charcteristics of python
#   - Unordered (Before Python 3.7) / Ordered (Python 3.7+)
#   - No Indexing (Accessed by Keys, Not Positions)
#   - Mutable (Modifiable)
#   - Do not allow duplicates.
#   - Keys Must Be Immutable
#########################
#  Dictionaries Structure
# {
#   Key: value,
# }

student = {
    "id": 1,
    "name": "Ahmed",
    "courses": ["Math", "Accounting", "Information"],
    "Financial hold": False,
    "phone": {
        "phone1": "011132424",
        "phone2": "0100000202"
    }
}

print(student, type(student))

# list_1 = ["apple", "banana"]
# print(list_1[0])

print(student["name"])

student["name"] = "Mohamed"

print(student)

# valid keys
valid_keys = {
    "string": "valid",
    123 : "valid",
    (1, 2, 3): "valid",
}

print(valid_keys)

# invalid keys
invalid_keys = {
    # [1, 2, 3]: "invalid",
    {"a": 1}: "invalid"
}

print(invalid_keys)





