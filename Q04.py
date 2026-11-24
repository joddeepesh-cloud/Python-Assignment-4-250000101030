# Question 04: Write a program to demonstrate type conversion using int(), float() and str().
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
num_str = "150"

as_int = int(num_str)
as_float = float(num_str)
as_str = str(as_int * 2)

print(f"num_str : '{num_str}' -> Type: {type(num_str).__name__}")
print(f"as_int  : {as_int} -> Type: {type(as_int).__name__}")
print(f"as_float: {as_float} -> Type: {type(as_float).__name__}")
print(f"as_str  : '{as_str}' -> Type: {type(as_str).__name__}")
