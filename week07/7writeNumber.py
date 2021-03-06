# Writes a number to a textfile
# Author: Andrew Scott

filename = "count.txt"
def writeNumber(number):
    with open(filename, "wt") as f:
        f.write(str(number))

# Test
writeNumber(5)
