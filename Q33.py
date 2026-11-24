# Question 33: Write a function that accepts a list as an argument and returns its largest element.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def get_largest_from_list(numbers):
    if not numbers:
        return None
    return max(numbers)

my_nums = [23, 76, 45, 98, 12, 67]
print("List:", my_nums)
print("Largest element:", get_largest_from_list(my_nums))
