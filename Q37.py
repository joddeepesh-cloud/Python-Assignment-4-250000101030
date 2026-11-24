# Question 37: Write a program to demonstrate the use of global variables inside a function.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Global variable
global_counter = 100

def show_global():
    # Reading global variable directly
    print("Reading global_counter inside function:", global_counter)

show_global()
print("Reading global_counter outside function:", global_counter)
