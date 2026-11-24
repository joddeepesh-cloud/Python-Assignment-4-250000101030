# Question 41: Write a Python program to create a user-defined module containing a function to calculate the square of a number and import it into another program.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import sys, os

# Ensure current directory is in search path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Importing user-defined module 'square_module'
import square_module

num = 9
result = square_module.calculate_square(num)

print("Demonstrating user-defined module 'square_module':")
print(f"Number : {num}")
print(f"Square calculated via module: {result}")
