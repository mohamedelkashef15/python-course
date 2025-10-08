########################
# Membership Operators => are used to test whether a value or variable is found in a sequence
# like (strings, lists, tuples, sets, or dictionaries)

#  in => Returns True if the specified value is present in the sequence.
#  not in => Returns True if the specified value is not present in the sequence.
########################

# strings
text = "Hello, World!"

print('H' in text)        # True
print('hello' in text)    # False (case-sensitive)
print('World' in text)    # True
print('Python' not in text)  # True

# lists
fruits = ['apple', 'banana', 'oranges']

print('banana' in fruits)      # True
print('cherry' in fruits)      # False
print('grape' not in fruits)   # True
print('apple' in fruits)       # True







