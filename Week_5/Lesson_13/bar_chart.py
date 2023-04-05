#Import required packages
import numpy as np
import matplotlib.pyplot as plt

#Create an array to align with the given number of users each language has
users = [13000, 26000, 52000, 30000, 9000]
x_axis = np.arange(len(users))

#Create a bar chart; users is y, x_axis is x
plt.bar(x_axis, users, color='red', alpha=0.5, align="center")

#Place x axis labels (ticks and tick locations)
tick_locations = [i for i in x_axis]
plt.xticks(tick_locations, ["Java", "C++", "Python", "Ruby", "Clojure"])

#Set the x and y limits of the chart
plt.xlim(-0.75, len(x_axis)-0.25)
plt.ylim(0, max(users)+5000)

#Give our chart labels & title
plt.title("Popularity of Programming Languages")
plt.xlabel("Programming Language")
plt.ylabel("Number of People Using Programming Languages")

#Save & show our graph
plt.savefig("Bar_Chart_Output.png")
plt.show()