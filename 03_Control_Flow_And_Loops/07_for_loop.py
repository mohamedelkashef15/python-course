##############################
# For loop

# for variable in sequence:
#   code to execute repeatedly
##############################

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

#* Numbers
for i in range(1, 11):
    print(i, i in range(1, 11))

# i = 1
# i = 2
# i = 3
# ...
# i = 10

#* List
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

# fruit = apple
# fruit = banana
# fruit = orange

#* string

name = "Mohamed"

for s in name:
    print(s)

# s = M

#* Example
backpack = ["pencil", "notebook", "eraser", "sharpener"]

for item in backpack:
    if item == "notebook":
        print("Found my notebook")
    else:
        print(f"I have a {item}")


# item = pencil
# item = notebook
# item = eraser
# item = sharpener

# output
# I have a pencil
# Found my notebook
# I have an eraser
# I have a sharpener

