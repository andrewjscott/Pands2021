# Reads in a number from a text file
# Author: Andrew Scott

# Checks the contents of count.txt and returns the contents as an integer
filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number
# Tests the function to ensure it's working correctly
num = readNumber()
print(num)