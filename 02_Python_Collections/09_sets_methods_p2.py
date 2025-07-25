#######################
# Sets Methods part 2
#  - union() - (|) => Combines sets into a new set.
#  - intersection() - (&) => Returns new set with common elements.
#  - difference - (-) => Returns a new set containing elements in the first set but not in others.
#  - Symmetric_difference() - (^) => Returns elements in either set but not both.
#######################

stand_A = {"apple", "banana", "orange", "kiwi"}
stand_B = {"banana", "kiwi", "grape", "pear"}
# stand_C = {"strawberry"}

# union()
# all_fruits = stand_A.union(stand_B, stand_C)
all_fruits = stand_A | stand_B

print(all_fruits)

# intersection()
common_fruits = stand_A.intersection(stand_B)
print(common_fruits)

# difference()
only_in_A = stand_A.difference(stand_B)
# stand_A - stand_B

print(only_in_A)

# Symmetric_difference()
unique_to_each = stand_A.symmetric_difference(stand_B)
print(unique_to_each)








