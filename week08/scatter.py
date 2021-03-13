# Using numpy to create a list of ten random salaries between 20,000 and 80,000,  
# ten ages between 21 and 65, and plotting them on a scatterplot
# Author: Andrew Scott

import matplotlib.pyplot as plt
import numpy as np

# Defining the ranges of the values and size of the randomly generated array
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10
minAge = 21
maxAge = 65

# Ensures that the first set of randomly generated numbers are kept
np.random.seed(1)

# Generates an array of 10 random salaries and ages in the ranegs previously defined
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
print(salaries)
ages = np.random.randint(minAge, maxAge, numberOfEntries)
print(ages)

# Creates then shows a scatterplot of salaries
plt.scatter(salaries, ages)
plt.title("Random plot")
plt.xlabel("Salaries")
plt.ylabel("Age")

# Adds a line of the function of y = x ** 2 for the range 1-100
xpoints = np.array(range(1, 101))
ypoints = xpoints ** 2
plt.plot(xpoints, ypoints, color= 'r', label = "x squared")

plt.show()

plt.savefig('prettier-plot.png')