#Import required packages
import numpy as np
import matplotlib.pyplot as plt
import random

#The maximum x value for our chart will be 100
x_limit = 100

#Set the x axis values
x_axis = np.arange(0, x_limit, 1)

#Create a random array of data for our y values
data = [random.random() for value in x_axis]

#Make a scatterplot with the size of each point determined by its x value
plt.scatter(x_axis, data, marker="o", facecolors="red", edgecolors="black", s=x_axis, alpha=0.75)

#Set the x and y limits
plt.ylim(0, 1)
plt.xlim(0, 100)

#Save and display the graph
plt.savefig("Scatterplot_Output.png")
plt.show()
