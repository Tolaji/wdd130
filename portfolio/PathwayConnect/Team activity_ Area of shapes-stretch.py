print("\n~~~~~~~~~~~ Areas of Shapes ~~~~~~~~~~~~~\n")
print("Core Requirements:-")
print()

import math

# Calculate the area of a square
square_side_length = float(input("What is the length of a side of the square? "))
area_square = square_side_length * square_side_length
print("The area of the square is: ", area_square)
print()

# Calculate the area of a rectangle
length_rectangle = float(input("What is the length of rectangle? "))
width_rectangle = float(input("What is the width of rectangle? "))
area_rectangle = length_rectangle * width_rectangle
print("The area of the rectangle is: ", area_rectangle)
print()

# Calculate the area of a circle
radius_circle = float(input("What is the radius of the circle? "))
pi = 3.14
area_circle = pi * (radius_circle**2)
print("The area of the circle is: ", area_circle)
print()

print("Stretch Challenge:-")
print()

# Input for length value
length = float(input("Enter a length value in centimeters: "))

# Square area in square centimeters and square meters
square_area_cm2 = length**2
square_area_m2 = square_area_cm2 / 10000

# Circle area in square centimeters and square meters
circle_radius = length / 2
circle_area_cm2 = math.pi * (circle_radius**2)
circle_area_m2 = circle_area_cm2 / 10000

# Cube volume in cubic centimeters and cubic meters
cube_volume_cm3 = length**3
cube_volume_m3 = cube_volume_cm3 / 1000000

# Sphere volume in cubic centimeters and cubic meters
sphere_radius = length / 2
sphere_volume_cm3 = (4 / 3) * math.pi * (sphere_radius**3)
sphere_volume_m3 = sphere_volume_cm3 / 1000000

# Display results
print("Square Area (cm^2):", square_area_cm2)
print("Square Area (m^2):", square_area_m2)
print("Circle Area (cm^2):", circle_area_cm2)
print("Circle Area (m^2):", circle_area_m2)
print("Cube Volume (cm^3):", cube_volume_cm3)
print("Cube Volume (m^3):", cube_volume_m3)
print("Sphere Volume (cm^3):", sphere_volume_cm3)
print("Sphere Volume (m^3):", sphere_volume_m3)
print()
