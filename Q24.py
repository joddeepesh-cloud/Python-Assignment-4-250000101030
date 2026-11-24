# Question 24: Write a function to count vowels in a given string.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

text = "Veer Madho Singh Bhandari Technical University"
print(f"Text: '{text}'")
print(f"Vowel count: {count_vowels(text)}")
