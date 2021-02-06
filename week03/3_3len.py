# Reads in a string and outputs that string's length
# Author: Andrew Scott

# Asks the user to input a string which is then stored to a variable
inputString = input('Enter a string: ')

# len is a python inbuilt function that counts the characters of the string which is then stored to a new variable
lenghtOfString = len(inputString)

# Prints out the length of the string, which is formatted to allow numbers to be conjoined to a string
print('The lenghth of \"{}\" is {}.'.format(inputString, lenghtOfString))