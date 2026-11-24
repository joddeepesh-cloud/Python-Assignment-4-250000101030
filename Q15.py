# Question 15: Write a function to check whether a number is even or odd.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

for val in [14, 27, 40]:
    print(f"{val} is {check_even_odd(val)}.")
