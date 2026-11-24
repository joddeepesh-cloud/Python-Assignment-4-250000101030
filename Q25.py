# Question 25: Write a function to find the length of a string without using the len() function.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

phrase = "Computer Science"
print(f"String: '{phrase}'")
print(f"Length without len(): {string_length(phrase)}")
