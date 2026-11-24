# Question 13: Write a function to calculate the area of a circle.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

r = 7.0
area = calculate_circle_area(r)
print(f"Radius: {r}")
print(f"Area of circle: {area:.2f}")
