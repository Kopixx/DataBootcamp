#Import required packages
import numpy as np
import matplotlib.pyplot as plt

#Import the speed data
danger_drop = [15, 13, 145, 137, 129, 113, 113, 105, 89, 97, 113, 105, 81]
rail_gun = [121, 113, 97, 105, 97, 73, 89, 81, 64, 64, 56, 56, 48]

#Create the range for x_axis; 120 seconds, measured every 10 seconds
x_axis = np.arange(0, 130, 10)

#Create the data series & plot aesthetics
plt.plot(x_axis, danger_drop, color="red", label="Danger Drop")
plt.plot(x_axis, rail_gun, color="blue", label="Rail Gun")
plt.xlabel("Coaster Runtime")
plt.ylabel("Speed (km/hr)")
plt.title("Coaster Speed Over Time")
plt.grid()
plt.xlim(0, 120)
plt.ylim(0, 150)
plt.legend(loc="best")
plt.savefig("Coaster_Speed_Output.png")
plt.show()