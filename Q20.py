# Question 20: Write a function to reverse a given string.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

sample = "Uttarakhand"
print(f"Original: {sample}")
print(f"Reversed: {reverse_string(sample)}")
