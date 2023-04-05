#import required packages
import numpy as np
import matplotlib.pyplot as plt

#Generate x values from 0 to 10 increasing by 0.1
x_axis = np.arange(0, 10, 0.1)

#Set two sets of data; sin and cos
sin = np.sin(x_axis)
cos = np.cos(x_axis)

#Add a semi-transparent horizontal line at y = 0
plt.hlines(0, 0, 10, alpha=0.25)

#Use markers but no line for each dataset
sine_handle = plt.plot(x_axis, sin, linewidth = 0, marker='o', color='blue', label='Sine')
cosine_handle = plt.plot(x_axis, cos, linewidth = 0, marker='^', color='red', label='Cosine')

#Add labels & title
plt.title("Juxtaposed Sine and Cosine Curves")
plt.xlabel("Input (Sampled Real Numbers from 0 to 10)")
plt.ylabel("Value of Sine (blue) and Cosine (red)")

#Set x and y limits
plt.xlim(0, 10)
plt.ylim(-1, 1)

#Add a grid to the plot
plt.grid()

#Save the figure
plt.savefig("Aesthetics_Output.png")
plt.show()