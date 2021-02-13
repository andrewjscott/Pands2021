# Generates 10 random numbers between 0 and 100 and then shows the three highest numbers
# Author: Andrew Scott

import random

# Defines variables for the parameters of the program
howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

# creates a list for the randomly generated numbers to be stored 
numbers = []

# Generates a random number to be added to the previously created list, and this is repeated 10 times
for i in range (0,10):
    numbers.append(random.randint(rangeFrom,rangeTo))
    print ("{} random numbers\t {}".format(howMany,numbers))

# Sorts the numbers in decending order and slices the list to isolate the top 3 highest numbers
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {} are \t\t {} ".format(topHowMany,topOnes[0:topHowMany]))