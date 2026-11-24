# Question 48: Write a program to use the math module to calculate the value of a mathematical expression.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import math

# Expression: (sqrt(a^2 + b^2) + log10(c)) / (sin(rad) + cos(rad))
a = 3.0
b = 4.0
c = 100.0
deg = 30.0
rad = math.radians(deg)

numerator = math.sqrt(math.pow(a, 2) + math.pow(b, 2)) + math.log10(c)
denominator = math.sin(rad) + math.cos(rad)
result = numerator / denominator

print(f"Expression: (sqrt({a}^2 + {b}^2) + log10({c})) / (sin({deg}°) + cos({deg}°))")
print("Numerator   :", numerator)
print("Denominator :", denominator)
print(f"Final Result: {result:.4f}")
