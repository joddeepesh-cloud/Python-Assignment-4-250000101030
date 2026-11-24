# Question 28: Write a function to calculate simple interest using arguments and a return statement.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def calculate_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100.0
    return si

p, r, t = 15000, 6.5, 2
si = calculate_simple_interest(p, r, t)
print(f"Principal = {p}, Rate = {r}%, Time = {t} years")
print(f"Calculated Simple Interest = {si}")
