# Takes in a number and returns the absolute
# Author: Andrew Scott

# Asks the user to input a number, which is stored in a variable as a float
number = float(input("Enter a number: "))
# Stores the absolute value of the inut number to a new variable and prints it out
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))