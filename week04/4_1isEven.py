# Program that asks a user to enter a numbber and determines if the number is even or odd
# Author: Andrew Scott

# Stores the user input integer to a variable
number = int(input("Enter an integer: "))

# As all even numbers are divisable by two without leaving a remainder, the first command divides 
# the input number by 2 and if the remainder is equal to 0, the first print command (even) is used and the program ends 
# but if the remainder is not equal to zero the programs continues to print the second print command (odd) instead 
if (number % 2) == 0:
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))