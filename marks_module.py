# User-Defined Module: marks_module.py
# Module for student marks calculation

def calculate_total(marks_list):
    """Returns the total sum of subject marks."""
    return sum(marks_list)

def calculate_percentage(marks_list, max_per_subject=100):
    """Calculates the percentage based on maximum marks per subject."""
    if not marks_list:
        return 0.0
    total = sum(marks_list)
    return (total / (len(marks_list) * max_per_subject)) * 100

def assign_grade(percentage):
    """Assigns an academic letter grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"
