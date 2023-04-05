#Import required packages
import numpy as np
import matplotlib.pyplot as plt

#Set x axis using numpy array
x_axis = np.arange(0, 10, 0.1)

#Set two sets of data; sin and cos
sin = np.sin(x_axis)
cos = np.cos(x_axis)

#Draw a horizontal line at (y = 0, x = (0 to 10)) with 0.25 transparency
plt.hlines(0, 0, 10, alpha=0.25)

#Create the markers; blue circles for sine, red triangles for cosine
sine_handle = plt.plot(x_axis, sin, marker='o', color='blue', label='Sine')
cosine_handle = plt.plot(x_axis, cos, marker='^', color='red', label='Cosine')


#Add a legend in the lower right corner
plt.legend(loc="lower right")

#Show the graph
# plt.show()

#Save an image of the chart
plt.savefig("Configuring_Line_Plots_Out.png")
plt.show()