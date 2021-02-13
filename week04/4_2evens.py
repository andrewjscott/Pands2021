# Prints all even numbers between 2 and 100 (inclusive) using a while loop
# Author: Andrew Scott

# Variables that contain the end target of 100 and the start value of 2
numberTo = 100
evenNum = 2

# A loop which prints the value of each even number starting with the initially defined 2 and then adds 2 to the previous 
# number until the number is equal to 100 which will end the loop
while evenNum <= numberTo:
    print(evenNum)
    evenNum += 2