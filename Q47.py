# Question 47: Write a program to use the random module to generate five random integers.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import random

# Setting seed for reproducible demonstration
random.seed(42)

print("Generating 5 random integers between 10 and 100:")
random_numbers = [random.randint(10, 100) for _ in range(5)]
for i, num in enumerate(random_numbers, 1):
    print(f"Random Integer {i}: {num}")
