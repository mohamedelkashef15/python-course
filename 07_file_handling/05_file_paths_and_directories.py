############################
# File paths and directories
# What is file path
# A file path tells Python where a file or folder is located on your computer.

# Absolute path
# An absolute path gives the full location of a file from the root.

# Relative path
# A relative path gives the location relative to the current working directory.
############################
import os
print(os.getcwd())

print(r"hello\newfile.txt")

absolute_path = "/Users/mohamedelkashef/Programming/Udmey Courses/Python Course/07_file_handling/05_file_paths_and_directories.py"

relative_path = os.path.relpath(absolute_path, os.getcwd())
print(relative_path)

# Working with os module
# * list files and directories
print(os.listdir())

# * create new directory
os.mkdir("files")

# * check if file/directory exists or not
print(os.path.exists("01_file_handling_intro.py"))

# * join paths
print(os.path.join("files", "students.txt"))

# * isfile()/isdir()
print(os.path.isdir("05_file_paths_and_directories.py"))
print(os.path.isdir("files"))

print(os.path.isfile("files"))
print(os.path.isfile("05_file_paths_and_directories.py"))

# * remove directory
os.rmdir("hello")

# * remove file
os.remove("logs.txt")













