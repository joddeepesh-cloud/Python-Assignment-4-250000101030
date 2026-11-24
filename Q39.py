# Question 39: Write a program to modify a global variable inside a function using the global keyword.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
counter = 10

def increment():
    global counter
    counter += 5
    print("Inside function after increment, counter =", counter)

print("Before function call, counter =", counter)
increment()
print("After function call, counter  =", counter)
