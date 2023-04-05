#import required packages
import numpy as np 
import matplotlib.pyplot as plt

#Array of numerical values for months as x axis
x_axis = np.arange(1, 13, 1)

#Data Points Celcius
points_C = [26.1, 25.3, 22.5, 20.6, 17.3, 14.5, 13.5, 15.8, 17.9, 19.2, 20.3, 24.7]

#Data Points Fahrenheit
points_f = []

for i in points_C:
    points_f.append(int(i) * 9/5 + 32)

plt.plot(x_axis, points_C, marker="s", color="red", label="Celsius")
plt.plot(x_axis, points_f, marker="+", color="blue", label="Fahrenheit")
plt.xlabel("Months")
plt.ylabel("Degrees")
plt.legend(loc="lower left")
plt.savefig("Legendary_Temp_Output.png")
plt.show()