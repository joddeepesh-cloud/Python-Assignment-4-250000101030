# Question 32: Write a function to demonstrate variable-length arguments using *args.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def calculate_sum(*args):
    total = 0
    for val in args:
        total += val
    return total

print("Sum of 2 numbers (10, 20)           :", calculate_sum(10, 20))
print("Sum of 4 numbers (10, 20, 30, 40)   :", calculate_sum(10, 20, 30, 40))
print("Sum of 6 numbers (1, 2, 3, 4, 5, 6) :", calculate_sum(1, 2, 3, 4, 5, 6))
