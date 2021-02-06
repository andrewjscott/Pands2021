# Takes in a float and rounds it to the nearest int
# Author: Andrew Scott

# Asks the user to enter a float number and stores it to a variable, and prints the rounded version
numberToRound = float(input("Enter a float number: "))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound,roundedNumber))