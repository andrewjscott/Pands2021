# Counts how many times a program has been run
# Author: Andrew Scott

# Reads in a number from a text file
filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

# Writes a number to a textfile
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

# Main program
num = readNumber()
num += 1
if num == 1:
    print("This program has been run {} time".format(num))
else:
    print("This program has been run {} times".format(num))
writeNumber(num)