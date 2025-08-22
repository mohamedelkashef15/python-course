###########################
# Handling Multiple Conditions
# elif => (short for "else if") checks another condition if the previous conditions were False.

# if condition1:
#     # Code if condition1 is True
# elif condition2:
#     # Code if condition2 is True
# elif condition3:
#     # Code if condition3 is True
# else:
#     # Code if none of the above are True
###########################

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
