# Using numpy to create a list of ten random salaries between 20,000 and 80,000
# Author: Andrew Scott

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

# A demonstration how quick and easy it is to make math changes to numpy arrays 
salariesPlus = salaries + 5000
print(salariesPlus)
salariesMultiplied = salaries * 1.05
print(salariesMultiplied)

# Converts the multiplied salaries from a float to int
newSalaries = salariesMultiplied.astype(int)
print(newSalaries)