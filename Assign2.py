"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

x = float(input("Enter a number:"))
y = float(input("Enter another number:"))
hypInInput = bool(input("Are one of these two numbers the Hypotenuse? (True/False)"))
if hypInInput = True:
    if x > y:
        z = (x**2 - y**2)**0.5
    elif x < y:
        z = (y**2 - x**2)**0.5
    else:
        z = x/(12 + 52**0.5)
elif hypInInput = False:
    z = ((x**2)+(y**2))**0.5
print(f"The missing side has a length of {z}.")
