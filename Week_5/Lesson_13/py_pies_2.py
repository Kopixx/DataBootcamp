#Import required packages
import numpy as np
import matplotlib.pyplot as plt

#Import the supplied data
pies = ["Aussie Beef", "Apple", "Chicken", "Lemon Meringue", "Shepherds", "Steak and Kidney", "Curry", "Lamb and Rosemary", "Steak and Mushroom", "Spinach and Feta"]
pie_votes = [47,37,32,27,25,24,24,21,18,16]
colours = ["orange","green","lightblue","yellow","red","purple","pink","yellowgreen","lightskyblue","lightcoral"]

#Explode levels
explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#Creating our pie chart
plt.pie(pie_votes, explode=explode, labels=pies, colors=colours, autopct="%1.1f%%", shadow=True, startangle=140)

#Centre the chart on the page
plt.axis("equal")

#Save and display chart
plt.savefig("Py_Pies_Output.png")
plt.show()