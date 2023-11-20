import math

class Area:
    def compute_area_of_square(self):
        square_side_length = float(input("What is the length of a side of the square? "))
        area_square = square_side_length * square_side_length
        return area_square

    def compute_area_of_rectangle(self):
        length_rectangle = float(input("What is the length of rectangle? "))
        width_rectangle = float(input("What is the width of rectangle? "))
        area_rectangle = length_rectangle * width_rectangle
        return area_rectangle

    def compute_area_of_circle(self):
        radius_circle = float(input("What is the radius of the circle? "))
        pi = 3.14
        area_circle = pi * (radius_circle**2)
        return area_circle

# Create an instance of the Area class
area_calculator = Area()

# Call the methods to calculate areas
area_of_square = area_calculator.compute_area_of_square()
area_of_rectangle = area_calculator.compute_area_of_rectangle()
area_of_circle = area_calculator.compute_area_of_circle()

# Print the results
print("The area of the square is:", area_of_square)
print("The area of the rectangle is:", area_of_rectangle)
print("The area of the circle is:", area_of_circle)
