' This Program Explains Python Simple I/O '
' Name: Astha Sharma'
' I Tried to use the concept learnt from professors video and minor help from google about how to use the formula in code '
'the output shown on the question is 73.6901 whereas the obtained o/p is 72.6902'

import math

# Entering user input
num_sides = int(input("Enter the number of sides of the polygon: "))
side_length = float(input("Enter the length of each side: "))

# Computing the area using the updated formula
area = ((1/4) * num_sides * side_length**2) / math.tan(math.pi / num_sides)

# Displaying the result
print(f"The area of the regular polygon is: {area:.4f}")






