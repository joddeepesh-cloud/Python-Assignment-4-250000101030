# Question 19: Write a function to check whether a string is a palindrome.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def check_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

words = ["radar", "python", "level"]
for w in words:
    print(f"'{w}' is palindrome? {check_palindrome(w)}")
