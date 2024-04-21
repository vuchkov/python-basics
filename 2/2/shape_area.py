import math
shape = input()

if shape == "square":
    side_of_the_square = float(input())
    square_area = side_of_the_square * side_of_the_square
    print(f"{square_area:.3f}")
elif shape == "rectangle":
    side_a = float(input())
    side_b = float(input())
    rectangle_area = side_a * side_b
    print(f"{rectangle_area:.3f}")
elif shape == "circle":
    radius = float(input())
    pi = math.pi
    circle_area = pi * radius * radius
    print(f"{circle_area:.3f}")
elif shape == "triangle":
    height = float(input())
    side = float(input())
    triangle_area = (side * height) / 2
    print(f"{triangle_area:.3f}")
else:
    print("Please enter correct shape: circle, rectangle, ")