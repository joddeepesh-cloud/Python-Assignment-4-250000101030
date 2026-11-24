# Question 30: Write a function to demonstrate keyword arguments.
# Student Name: Deepesh Joshi | Roll Number: 250000101030
# Branch: CSE | Faculty of Technology, Dehradun
# University: Veer Madho Singh Bhandari Uttarakhand Technical University

# Solution
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

# Calling with keyword arguments out of order
describe_pet(pet_name="Bruno", animal_type="dog")
describe_pet(animal_type="parrot", pet_name="Mithu")
