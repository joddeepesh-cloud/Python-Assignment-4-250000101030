# Question 35: Write a function that returns both the sum and product of two numbers.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def sum_and_product(x, y):
    s = x + y
    p = x * y
    return s, p

a, b = 8, 5
total, product = sum_and_product(a, b)
print(f"Given numbers: {a} and {b}")
print(f"Sum    : {total}")
print(f"Product: {product}")
