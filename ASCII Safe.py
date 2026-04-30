import math

# Reading inputs
ab = float(input())
bc = float(input())

# Calculating the angle
# In a right triangle, the median to the hypotenuse (BM) creates 
# an isosceles triangle MBC, so angle MBC = angle ACB.
angle_rad = math.atan(ab / bc)
angle_deg = math.degrees(angle_rad)

# Rounding to the nearest integer as per constraints
# We use chr(176) for the degree symbol to avoid non-ASCII errors
result = str(int(round(angle_deg))) + chr(176)

print(result)
