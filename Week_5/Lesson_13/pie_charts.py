#Import the required packages
import numpy as np
import matplotlib.pyplot as plt

#Labels for each section of our pie chart (supplied)
labels = ["Humans", "Smurfs", "Hobbits", "Ninjas"]

#The values for each section of the pie chart (supplied)
sizes = [220, 95, 80, 100]

#List of colours for each pie chart section
colours = ["red", "orange", "lightcoral", "lightskyblue"]

#Explode the 'humans' chart section from the rest
explode = (0.1, 0, 0, 0)

#Create a pie chart 
plt.pie(sizes, explode=explode, labels=labels, colors=colours, autopct="%1.2f%%", shadow=True, startangle=140)
# plt.axis("equal")

#Save and display the pie chart
plt.savefig("Pie_Charts_Output.png")
plt.show()