############################
# More about Comparison operators
#   and => is a logical operator, and is used to combine conditional statements:
#   or => is a logical operator, and is used to combine conditional statements:
#   Not => is a logical operator, and is used to reverse the result of the conditional statement:
############################

age = 25
has_license = True

if age >= 18 and has_license:
    print("You are legally allowed to drive.")
# Output: You are legally allowed to drive.


is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can sleep in today!")
# Output: You can sleep in today!

is_raining = False

if not is_raining:
    print("The weather is good for a hike.")
# Output: The weather is good for a hike.

age = 70
if (age >= 65) or (age >= 18 and has_license):
    print("You can get a senior discount or drive.")



















