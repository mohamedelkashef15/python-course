############################
# Function Introduction
#? What are Functions and Why Use Them?

# Function Structure
# def function_name(parameters):
#     """
#     Docstring - describes what the function does
#     """
#     # Function body - code that executes
#     return result  # Optional - sends data back
############################

# Example: Calculate area of multiple rectangles

length1 = 5
width1 = 2
area1 = length1 * width1
print(f"Area of rectangle 1 is {area1}")

length2 = 20
width2 = 5
area2 = length2 * width2
print(f"Area of rectangle 2 is {area2}")

length3 = 15
width3 = 3
area3 = length3 * width3
print(f"Area of rectangle 3 is {area3}")

length4 = 8
width4 = 5
area4 = length4 * width4
print(f"Area of rectangle 4 is {area4}")

length5 = 12
width5 = 4
area5 = length5 * width5
print(f"Area of rectangle 5 is {area5}")

print("Using function")

def calculate_area(length, width):
    """Calculate area of rectangle"""
    area = length * width
    return area


print(f"Area of rectangle 1 is {calculate_area(5, 2)}")
print(f"Area of rectangle 2 is {calculate_area(20, 5)}")
print(f"Area of rectangle 3 is {calculate_area(15, 3)}")
print(f"Area of rectangle 5 is {calculate_area(8, 5)}")
print(f"Area of rectangle 4 is {calculate_area(12, 4)}")










