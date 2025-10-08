######################
# Type conversion (casting)
#   Manual
#       - String to integer
#       - Float to Integer
#       - Integer to float
#       - Integer to String
#   Automatic
#       - Integer + Float → Float
#       - Integer + Boolean → Integer
######################

# String to integer
age = "25"
age_int = int(age)

print(age, type(age))
print(age_int, type(age_int))

# Float to Integer
grade = 94.6
grade_int = int(grade)

print(grade, type(grade))
print(grade_int, type(grade_int))

# Integer to float
number = 5
number_float = float(number) + 3.2

print(number, type(number))
print(number_float, type(number_float))

# Integer to String
count = 100
count_str = str(count)

print(count, type(count))
print(count_str, type(count_str))

# Automatic
# Integer + Float → Float
num1 = 5
num2 = 3.2
result = num1 + num2

print(result, type(result))

# Integer + Boolean → Integer
a = 3
b = True
result = a + b

print(result, type(result))













