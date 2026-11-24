# Question 38: Write a program to demonstrate the difference between local and global variables having the same name.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
# Global variable x
x = "GLOBAL value of x"

def test_shadowing():
    # Local variable x shadows global x within this function
    x = "LOCAL value of x"
    print("Inside function, x =", x)

test_shadowing()
print("Outside function, x =", x)
