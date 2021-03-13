# Plots the function y = x ** 2
# Author: Andrew Scott

import matplotlib.pyplot as plt
import numpy as np

# A variable that will be used to set the calculated values on the x axis to be between 1 and 100
xpoints = np.array(range(1,101))

# A variable that will be used to set the calculated values on the  axis to be the square of the value on the x axis
ypoints = xpoints ** 2

# Creates and then shows the plot
plt.plot(xpoints, ypoints)
plt.show()