# Question 49: Write a program to create a user-defined module for student marks calculation and use it in another Python program.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Importing user-defined marks_module
import marks_module as mm

student_name = "DEEPESH JOSHI"
roll_no = 250000101030
subject_marks = [95, 92, 88, 96, 94]

total = mm.calculate_total(subject_marks)
percentage = mm.calculate_percentage(subject_marks)
grade = mm.assign_grade(percentage)

print("Student Marks Report using 'marks_module':")
print("Student Name :", student_name)
print("Roll Number  :", roll_no)
print("Marks        :", subject_marks)
print("Total Marks  :", total, "out of 500")
print(f"Percentage   : {percentage:.2f}%")
print("Grade        :", grade)
