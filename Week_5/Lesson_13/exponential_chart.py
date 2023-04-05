#Import the required packages; numpy for calculations & matplotlib for charting
import numpy as np
import matplotlib.pyplot as plt

#Create a numpy array from 0 to 5, with each step being 0.1 higher than the last
x_axis = np.arange(0, 5, 0.1)

#Create an exponential series of values to chart, looping through the x_axis array
e_x = [np.exp(x) for x in x_axis]

#Create a graph with the array as x, and the exponential as y
plt.plot(x_axis, e_x)
#plt.show()

#Give the graph axis labels
plt.xlabel("Time With MatPlotLib")
plt.ylabel("How Cool MatPlotLib Seems")

#Display the chart
plt.show()