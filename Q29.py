# Question 29: Write a function to demonstrate positional arguments.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def student_info(name, roll_no, branch):
    print("--- Positional Arguments Demonstration ---")
    print(f"Name   : {name}")
    print(f"Roll No: {roll_no}")
    print(f"Branch : {branch}")

# Passed strictly in positional order
student_info("Deepesh Joshi", 250000101030, "CSE")
