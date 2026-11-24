# Question 22: Write a function to find the largest element in a list.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def find_max_element(lst):
    if not lst:
        return None
    max_el = lst[0]
    for x in lst[1:]:
        if x > max_el:
            max_el = x
    return max_el

data = [35, 12, 89, 44, 95, 62]
print("List:", data)
print("Largest element:", find_max_element(data))
