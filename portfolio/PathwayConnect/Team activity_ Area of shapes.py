print('\n~~~~~~~~~~~ Areas of Shapes ~~~~~~~~~~~~~\n')
print('Core Requirements:-')
print()

#Calculate the area of a square
square_side_length = float(input('What is the length of a side of the square? '))
area_square = square_side_length * square_side_length
print('The area of the square is: ', area_square )
print()

#Calculate the area of a rectangle
length_rectangle = float(input('What is the length of rectangle? '))
width_rectangle = float(input('What is the width of rectangle? '))
area_rectangle = length_rectangle * width_rectangle
print('The area of the rectangle is: ', area_rectangle)
print()
#Calculate the area of a circle
radius_circle = float(input('What is the radius of the circle? '))
pi = 3.14
area_circle = pi * (radius_circle ** 2)
print('The area of the circle is: ', area_circle)
print()

#make the above code 