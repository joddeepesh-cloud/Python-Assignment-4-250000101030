# Question 31: Write a function to demonstrate default arguments.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def greet(name, message="Welcome to Python Programming!"):
    print(f"Hello {name}, {message}")

# Using default value
greet("Deepesh")
# Overriding default value
greet("Deepesh", "Good luck with your semester exams!")
