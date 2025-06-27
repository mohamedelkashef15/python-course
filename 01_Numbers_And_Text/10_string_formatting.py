#######################
    # String Formatting
#######################

name = "Mohamed"
age = "25"
job = "Teaching Assistant"
text = "My name is " + name + ". I'm " + age + " years old. " + "I work as a " + job + " at Misr University"
text2 = f"My name is {name}. I'm {age} years old. I work as a {job} at Misr University"
print(text)
print(text2)

num1 = 10
num2 = 5
result = f"Sum = {num1 + num2}"
print(result)

price = 50.74123123123
print(f"product price = {price:.1f}")

# Concatenation
first = "Hello"
second = "World"
combine = first + " " + second
print(combine)