# Takes in a number and outputs that number rounded down ie floors that number
# Author: Andrew Scott

# First need to import the math module
import math

# Asks the user to enter a float number and stores it to a variable
numberTofloor = float(input("Enter a float number: "))

# Uses the math method floor to floor the input number and stores it to a new variable which is printed
flooredNumber = math.floor(numberTofloor)
print('{} floored is {}'.format(numberTofloor, flooredNumber))