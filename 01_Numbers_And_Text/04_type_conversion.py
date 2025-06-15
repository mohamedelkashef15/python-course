######################
    # Manual
    #     - String to integer
    #     - Float to Integer
    #     - Integer to float
    #     - Integer to String
    #*    - convert to boolean Explained in lec.10
    # Automatic
    #     - Integer + Float → Float
    #     - Integer + Boolean → Integer
    #
    # Search for why we use it ?
######################
# String to integer
age = "25"
age_int = int(age) # converts "25" to => 25

print(age, type(age))
print(age_int, type(age_int))

# Float to Integer
grade = 94.6
grade_int = int(grade)

print(grade, type(grade))
print(grade_int, type(grade_int))

# Float to Integer
number = 5
number_float = float(number) + 3.2

print(number, type(number))
print(number_float, type(number_float))

# Integer to String
count = 100
count_str = str(count)

print(count, type(count))
print(count_str, type(count_str))

# Integer + Float => Float
x = 5
y = 3.2
result = x + y
print(result, type(result))

# Integer + Boolean → Integer
a = 3
b = True # 1
result = a + b
print(result, type(result))
















