############################
# Writing and appending to files
# write
#    - Writes data to a file
#    - Deletes old content if file already exists
#    - Creates a new file if it does not exist

# append
#    - Adds new data at the end of the file
#    - Keeps old content
#    - Creates a new file if it does not exist

############################
# * write
file = open("notes.txt", "w")
file.write("Learning File handling in python is easy")
file.close()

file = open("notes.txt", "w")
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")
file.close()

# * append
# file = open("logs.txt", "a")
# file.write(" Program Started")
# file.close()

file = open("logs.txt", "a")
file.write("\nUser logged")
file.close()





