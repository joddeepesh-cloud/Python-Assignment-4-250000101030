# Question 09: Write a program to calculate the value of sine, cosine and tangent for a given angle.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import math

# Angle in degrees
angle_deg = 45.0
angle_rad = math.radians(angle_deg)

sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

print(f"Angle: {angle_deg}° ({angle_rad:.4f} radians)")
print(f"sin({angle_deg}°) = {sin_val:.4f}")
print(f"cos({angle_deg}°) = {cos_val:.4f}")
print(f"tan({angle_deg}°) = {tan_val:.4f}")
