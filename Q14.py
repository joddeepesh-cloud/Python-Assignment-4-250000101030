# Question 14: Write a function to find the square and cube of a given number.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def square_and_cube(n):
    sq = n ** 2
    cu = n ** 3
    return sq, cu

num = 5
square, cube = square_and_cube(num)
print(f"Number: {num}")
print(f"Square: {square}")
print(f"Cube  : {cube}")
