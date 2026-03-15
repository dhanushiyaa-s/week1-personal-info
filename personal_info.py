# Personal Information Manager
# Author: Dhanushiya S
# Description: A simple Python program that stores and displays personal
# information using variables, user input, validation, and formatted output.

# ---------------------------------------------
# Welcome Message
# ---------------------------------------------
print("=" * 40)
print("      PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

# ---------------------------------------------
# Static Personal Information
# These values are predefined in the program
# ---------------------------------------------

name = "Dhanushiya S"     # string variable for name
age = 20                  # integer variable for age
city = "Bangalore"        # string variable for city
hobby = "Reading books"   # string variable for hobby

# ---------------------------------------------
# Getting User Input
# Asking the user about their preferences
# ---------------------------------------------

print("Please tell me about yourself:")
print("-" * 30)

# Favorite food input with validation
favorite_food = input("What's your favorite food? ").strip()

while favorite_food == "":
    print("Input cannot be empty. Please enter a valid food.")
    favorite_food = input("What's your favorite food? ").strip()

# Favorite color input with validation
favorite_color = input("What's your favorite color? ").strip()

while favorite_color == "":
    print("Input cannot be empty. Please enter a valid color.")
    favorite_color = input("What's your favorite color? ").strip()

# ---------------------------------------------
# Calculating Age in Months
# ---------------------------------------------
age_in_months = age * 12

# ---------------------------------------------
# Displaying All Information
# Using formatted strings
# ---------------------------------------------
print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name: {name.title()}")
print(f"Age: {age} years ({age_in_months} months old)")
print(f"City: {city.title()}")
print(f"Hobby: {hobby.capitalize()}")
print()

print(f"Favorite Food: {favorite_food.capitalize()}")
print(f"Favorite Color: {favorite_color.capitalize()}")
print()

# ---------------------------------------------
# Goodbye Message
# ---------------------------------------------
print("=" * 40)
print("Thank you for using Personal Information Manager!")
print("=" * 40)