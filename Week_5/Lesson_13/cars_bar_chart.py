#Import the required packages
import numpy as np
import matplotlib.pyplot as plt

#Import the supplied data variables (Cars and Cities)
cities = ["San Francisco", "Omaha", "New Orleans", "Cincinnati", "Pittsburgh"]
cars_in_cities = [214.7, 564.4, 416.5, 466.7, 350.6]

#Create the x axis
x_axis = np.arange(len(cars_in_cities))

#Create the bar plot series & aesthetics
plt.bar(x_axis, cars_in_cities, color="blue", align="center")

#Create the title and axis labels
plt.title("Density of Commuting Cars in Cities")
plt.xlabel("Cities")
plt.ylabel("Commuting Cars Per 1,000 Population Age 16+")

#Add the x axis tickers
tick_locations = [i for i in x_axis]
plt.xticks(tick_locations, cities)

#Save & Display the graph
plt.savefig("Cars_Bar_Chart_Output.png")
plt.show()