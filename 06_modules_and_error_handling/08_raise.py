############################
# Raise keyword
############################

def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old to get driving licence")
    else:
        print("You can have a driving licence")

# check_age(20)
check_age(15)








