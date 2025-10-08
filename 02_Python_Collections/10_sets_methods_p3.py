########################
# Sets Methods part 3
#   Updates
#       - intersection_update(&=)
#       - difference_update(-=)
#       - symmetric_difference_update(^=)
#   Relationship Checks
#       - isdisjoint()
#       - issubset()
#       - issuperset()
########################

stand_A = {"apple", "banana", "orange", "kiwi"}
stand_B = {"banana", "kiwi", "grape", "pear"}

#* intersection_update(&=)
# print(stand_A)
# stand_A.intersection_update(stand_B)
# print(stand_A)

#* difference_update(-=)
# print(stand_A)
# stand_A.difference_update(stand_B)
# print(stand_A)

#* symmetric_difference_update(^=)
print(stand_A)
stand_A.symmetric_difference_update(stand_B)
print(stand_A)

# isdisjoint()
print({"apple"}.isdisjoint({"apple"}))
print({"orange"}.isdisjoint({"apple"}))

# issubset()
fruit_A = {"apple", "banana"}
fruit_B = {"apple", "banana", "orange"}

print(fruit_A.issubset(fruit_B))

# issuperset()
print(fruit_B.issuperset(fruit_A))











