# User is asked to enter two numbers and the output is the first number subtracted from the second
# Author: Andrew Scott

# Converts the user input from string to an int
# Program will return an error if another type such as a float or string is entered by the user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Stores the value of the first number minus the second to a variable
answer = x - y

# Converts the values of each variable to a string so it can be printed as a sentence
print("{} minus {} is equal to {}".format(x, y, answer))