# Question 23: Write a function to calculate the average of a list of numbers.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def calculate_average(nums):
    if not nums:
        return 0.0
    return sum(nums) / len(nums)

marks = [85, 90, 78, 92, 88]
print("Numbers:", marks)
print(f"Average: {calculate_average(marks):.2f}")
