# Question 21: Write a function to calculate the sum of digits of a number.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def sum_of_digits(num):
    total = 0
    num = abs(num)
    while num > 0:
        total += (num % 10)
        num //= 10
    return total

val = 9876
print(f"Sum of digits of {val}: {sum_of_digits(val)}")
