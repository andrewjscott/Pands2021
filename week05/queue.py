# Creates a queue of 10 random numbers between 1-100, prints the first number and the queue of other numbers,
# removes the first number so the next number heads the que and printing the numbers, repeating until no numbers remain

# Author: Andrew Scott

# Import the random module to generate random numbers
# Variables also created for the list of random numbers, the amount of numbers in the list, and the top range of random numbers
import random
queue = []
amountOfNumbers = 10
rangeTo = 100

# This loop adds a random number to the list and repeats until the list contains 10 random numbers between 1-100
for n in range(0, amountOfNumbers):
    queue.append(random.randint(0, rangeTo))

# Prints the random numbers generated and stored in the list
print("Queue is " + str(queue))

# A loop that says that while the amound of numbers in the list is not equal to zero, the first number of the list is removed and 
# stored in its own variable and is printed along with the remaining list. This is repeated until all numbers have been removed 
# from the list 
while len(queue) != 0:
    topOfQueue = queue.pop(0)
    print("Current number is", str(topOfQueue), "and the queue is " + str(queue))

# The loop ends when the list is empty because the list now equals zero, and a message is printed to confirm this
print("The queue is now empty")