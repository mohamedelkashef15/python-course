###########################
# If Statement and Indentation
# if condition:
#   code runs if condition is true

# indentation => (the spaces at the beginning of a line) is crucial for defining blocks of code.
# elif => (short for "else if") checks another condition if the previous conditions were False.
# else runs code when all previous conditions are False.
###########################

age = 21

if age >= 18:
    print("You are an adult")
    print("You can vote")


print("Hello world")
print(age)

# Using elif
grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Failed")















