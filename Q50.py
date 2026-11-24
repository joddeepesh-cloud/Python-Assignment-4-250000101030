# Question 50: Write a program to create a simple user-defined package containing two modules and import functions from both modules.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import sys, os

# Ensure current directory is in sys.path so 'mypackage' can be imported
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Importing from user-defined package 'mypackage'
from mypackage.math_operations import power, factorial
from mypackage.string_operations import reverse_string, greet_student

print("--- User-Defined Package Demonstration ('mypackage') ---")
print("Module 1 (math_operations):")
print("  power(2, 5)   =", power(2, 5))
print("  factorial(6)  =", factorial(6))

print("\nModule 2 (string_operations):")
print("  reverse_string('Uttarakhand') =", reverse_string("Uttarakhand"))
print(" ", greet_student("DEEPESH JOSHI"))
