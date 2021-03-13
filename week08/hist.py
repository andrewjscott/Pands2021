# Using numpy to create a list of ten random salaries between 20,000 and 80,000, and plotting them on a histogram
# Author: Andrew Scott

import matplotlib.pyplot as plt
import numpy as np

# Defining the ranges of the values and size of the randomly generated array
minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

# Ensures that the first set of randomly generated numbers are kept
np.random.seed(1)

# Generates an array of 10 random salaries in the ranegs previously defined
salaries = np.random.randint(minSalary, maxSalary,numberOfEntries)
print(salaries)

# Creates then shows a histogram of salaries
plt.hist(salaries)
plt.show()
