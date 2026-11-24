# Question 36: Write a program to demonstrate the use of local variables inside a function.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def demo_local_variable():
    # local_var is defined inside the function (local scope)
    local_var = "I am a local variable inside demo_local_variable()"
    print("Inside function:", local_var)

demo_local_variable()

# Demonstrating that local_var cannot be accessed outside the function
print("\nAttempting to access local_var outside the function:")
try:
    print(local_var)
except NameError as e:
    print("Caught NameError as expected:", e)
    print("Explanation: Local variables are destroyed once the function execution terminates.")
