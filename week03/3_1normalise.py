# Reads in a string and strips any leading or trailing spaces, converts the string to lower case.
# Also outputs the number of characters of both the original and the new string
# Author: Andrew Scott

# Asks the user to enetr a string and stores it to a variable
rawString = input("Please enter a string: ")
# Uses python methods to remove any leading and trailing spaces, coverts all characters to lower case, and stores the 
# result to a new variable
normalisedString = rawString.strip().lower()

# Counts the number of characters for each string respectively
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

# Outputs the normalised string and the number of characters in the original and normalised strings
print("That String normalised is: {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lenghtOfRawString, lenghtOfNormalised))