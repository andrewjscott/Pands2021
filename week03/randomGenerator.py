# Prints out a random number between one and ten
# Author: Andrew Scott

# The module random has to first be imported to be used
import random

# randint() is a method within the random module that returns a random interger between the specified range, which in this 
# case is between one and ten, and stores that value in a variable named number
number = random.randint(1,10)

# Outputs the number randomly assigned to the variable number
print(number)

# This allows the user to specify their own range for a random number to be selected from and stores their input to variables
x = int(input("Enter the lower value in your range: "))
y = int(input("Enter the higher value in your range: "))

# The numbers entered by the user are now used as the range in the randint() module and stored to a new variable
userNumber = random.randint(x,y)

# Prints out a random number from the range specified by the user
print(userNumber)