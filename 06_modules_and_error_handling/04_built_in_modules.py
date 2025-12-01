############################
# Useful Modules
#  1- os
#    - Get the current working folder
#    - List files
#    - Work with file paths

#  2- shutil
#    - Copying files
#    - Moving files
#    - Deleting folders
#
#  3- JSON => a way to store and send data.
############################

# os
import os
# current working directory
print(os.getcwd())

print(os.listdir())

# shutil
import shutil
shutil.copy("01_modules_intro.py", "01_modules_intro_copy.py")
shutil.move("01_modules_intro_copy.py", "test.py")

# JSON
import json

data = {"name": "Ali", "age": 20}

# Convert python data into json
json_data = json.dumps(data)

print(json_data)
print(type(data))
print(type(json_data))

# Convert json data to python data
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))

















############################
# Useful Modules
#  1- os
#    - Get the current working folder
#    - List files
#    - Work with file paths

#  2- shutil
#    - Copying files
#    - Moving files
#    - Deleting folders
#
#  3- JSON => a way to store and send data.
############################

# os
import os
# current working directory
print(os.getcwd())

print(os.listdir())

# shutil
import shutil
shutil.copy("01_modules_intro.py", "01_modules_intro_copy.py")
shutil.move("01_modules_intro_copy.py", "test.py")

# JSON
import json

data = {"name": "Ali", "age": 20}

# Convert python data into json
json_data = json.dumps(data)

print(json_data)
print(type(data))
print(type(json_data))

# Convert json data to python data
python_data = json.loads(json_data)
print(python_data)
print(type(python_data))
