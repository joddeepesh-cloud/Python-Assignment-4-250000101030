# Question 34: Write a function that accepts a string and returns the number of uppercase and lowercase characters.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

sample = "Deepesh Joshi - CSE Department"
u, l = count_case(sample)
print(f"String: '{sample}'")
print(f"Uppercase characters: {u}")
print(f"Lowercase characters: {l}")
