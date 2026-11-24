# Question 08: Write a program to calculate the GCD and LCM of two numbers using mathematical functions.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import math

a = 36
b = 60

gcd_val = math.gcd(a, b)
# LCM formula: lcm(a, b) = (a * b) // gcd(a, b)
lcm_val = (a * b) // gcd_val

print(f"Numbers: {a} and {b}")
print(f"Greatest Common Divisor (GCD): {gcd_val}")
print(f"Least Common Multiple   (LCM): {lcm_val}")
