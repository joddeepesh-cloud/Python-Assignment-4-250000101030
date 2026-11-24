# Question 46: Write a program to demonstrate importing a module using an alias.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import math as m

radius = 4.0
area = m.pi * m.pow(radius, 2)

print("Using 'math' with alias 'm':")
print("m.pi:", m.pi)
print(f"Circle Area with radius {radius}: {area:.2f}")
