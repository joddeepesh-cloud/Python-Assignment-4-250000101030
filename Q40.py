# Question 40: Write a program to demonstrate how local variables behave when two different functions use variables with the same name.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def function_alpha():
    var_name = "Alpha Local Value"
    print("Inside function_alpha:", var_name)

def function_beta():
    var_name = "Beta Local Value"
    print("Inside function_beta :", var_name)

function_alpha()
function_beta()
print("Both functions operate with completely isolated scopes despite having identical variable names.")
