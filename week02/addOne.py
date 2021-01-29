# This program asks a user to enter a number and outputs a value that adds 1 to that number
# Author: Andrew Scott

# Asks the user to enter a number, and stores it in a variable called number
number = input("Please enter a number: ")

# Adds one to the number given by the user, adds 1 to it, and stores it in a new variable
# int added to ensure that python is not trying to add a string and an integer
numberPlusOne = int(number) + 1

# Outputs the number the user entered and adds 1 to it
# str used to convert any integers to strings to allow python to print the output
print(str(number) + " + 1 = " + str(numberPlusOne))