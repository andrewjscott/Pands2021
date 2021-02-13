# Promts the user to guess a number and requests them to keep guessing until they get the correct number
# Author: Andrew Scott

# Defines a variable with a number for the user to guess
numToGuess = 50

# A variable that contains the value entered as the user's guess
guess = int(input("Guess the number: "))

# A loop that tells the user their guess is wrong when their guessed number is not equal to the initial number and continues to
# ask them to guess again
while guess != numToGuess:
    print("Wrong!")
    guess = int(input("Please guess again: "))

# The previous loop ends when the number is correctly guessed and the variable guess is equal to numToGuess which leads to 
# a string being printed that tells the user that they are correct
print("Yes! That is correct! The number is " + str(numToGuess))