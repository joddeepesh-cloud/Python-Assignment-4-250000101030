# Question 18: Write a function to check whether a number is prime.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

test_numbers = [2, 17, 21, 29]
for t in test_numbers:
    print(f"Is {t} prime? {is_prime(t)}")
